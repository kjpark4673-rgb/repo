#!/usr/bin/env python3
"""공개 저장소에 학생 개인정보가 올라가지 않게 막는 자물쇠.

"학생 실명·드라이브 문서 식별자를 적지 않는다"는 글로 된 규칙을, 커밋·푸시 직전에
실제로 막는 장치로 바꾼 것이다. 새로 들어가는 줄만 본다(이미 있는 줄은 보지 않는다).

쓰는 법
  python3 classroom/tools/privacy_check.py            # 지금 커밋될 수 있는 변경을 점검
  python3 classroom/tools/privacy_check.py --push     # 아직 원격에 없는 커밋을 점검
  python3 classroom/tools/privacy_check.py --all      # 저장소 전체 파일을 점검
  python3 classroom/tools/privacy_check.py --hook     # Claude Code 훅(.claude/settings.json)이 부름

훅으로 걸릴 때: Bash 명령에 `git commit`이 있으면 커밋될 수 있는 변경을,
`git push`가 있으면 아직 원격에 없는 커밋을 점검하고, 걸리면 그 명령을 막는다(종료 코드 2).

찾는 것
  - 휴대전화 번호, 주민등록번호 모양, 이메일 주소
  - 구글 문서·드라이브·시트 링크(문서 식별자가 들어 있음)
  - 학생 원자료 파일(.xlsx .xls .hwp .hwpx)과 .private/ 폴더 안의 파일
  - 학생 실명: 이름 목록 파일이 있을 때만. 목록은 .private/names.txt (한 줄에 한 이름,
    #으로 시작하는 줄은 무시)에 둔다. .private/는 .gitignore에 있어 저장소에 올라가지 않는다.
    다른 곳에 두려면 환경 변수 CLASSROOM_NAMES_FILE에 경로를 적는다.

일부러 넣은 예시(가짜 번호 등)는 그 줄에 `privacy-ok`를 적으면 넘어간다.
010-0000-0000, 010-1234-5678, example.com 같은 자리표시자는 처음부터 넘어간다.
결과에는 찾은 값을 가려서(앞 몇 글자만) 보여 준다.
"""
import json
import os
import re
import subprocess
import sys

RISKY_EXT = ('.xlsx', '.xls', '.hwp', '.hwpx')
PRIVATE_DIR = '.private/'
SKIP_MARK = 'privacy-ok'
MAX_BYTES = 2_000_000

PATTERNS = [
    ('휴대전화 번호', re.compile(r'(?<![0-9])01[016789][-. ]?[0-9]{3,4}[-. ]?[0-9]{4}(?![0-9])')),
    ('주민등록번호 모양', re.compile(r'(?<![0-9])[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12][0-9]|3[01])[- ][1-4][0-9]{6}(?![0-9])')),
    ('이메일 주소', re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}')),
    ('구글 문서·드라이브 링크', re.compile(r'(?:docs|drive|sheets)\.google\.com/[^\s"\'<>)\]]+')),
]
PLACEHOLDERS = re.compile(
    r'^(?:010[-. ]?0000[-. ]?0000|010[-. ]?1234[-. ]?5678|010[-. ]?1111[-. ]?2222'
    r'|.*@(?:example|test)\.(?:com|org|net)|noreply@anthropic\.com|.*@users\.noreply\.github\.com)$'
)


def git(*args, check=True):
    r = subprocess.run(['git', *args], capture_output=True, text=True, errors='replace')
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} 실패: {r.stderr.strip()}")
    return r.stdout


def mask(value):
    keep = 3 if len(value) > 6 else 1
    return value[:keep] + '*' * min(len(value) - keep, 8)


def load_names():
    path = os.environ.get('CLASSROOM_NAMES_FILE') or os.path.join(git('rev-parse', '--show-toplevel').strip(), '.private', 'names.txt')
    if not os.path.isfile(path):
        return [], None
    with open(path, encoding='utf-8', errors='replace') as f:
        names = [ln.strip() for ln in f if ln.strip() and not ln.lstrip().startswith('#')]
    names = [n for n in names if len(n) >= 2]
    return names, path


def scan_line(path, lineno, text, names, hits):
    if SKIP_MARK in text:
        return
    for label, rx in PATTERNS:
        for m in rx.finditer(text):
            if PLACEHOLDERS.match(m.group(0)):
                continue
            hits.append((path, lineno, label, mask(m.group(0))))
    for n in names:
        if n in text:
            hits.append((path, lineno, '학생 실명(목록)', mask(n)))


def scan_path_name(path, hits):
    low = path.lower()
    if low.endswith(RISKY_EXT):
        hits.append((path, 0, '학생 원자료 파일 형식', os.path.splitext(path)[1]))
    if low.startswith(PRIVATE_DIR) or ('/' + PRIVATE_DIR) in low:
        hits.append((path, 0, '.private/ 안의 파일', '.private/'))


def scan_diff(diff_text, names, hits, files):
    """git diff -U0 출력에서 더해지는 줄만 본다."""
    path, lineno = None, 0
    for ln in diff_text.splitlines():
        if ln.startswith('+++ '):
            p = ln[4:]
            path = None if p == '/dev/null' else (p[2:] if p.startswith('b/') else p)
            if path:
                files.add(path)
        elif ln.startswith('@@'):
            m = re.search(r'\+(\d+)', ln)
            lineno = int(m.group(1)) if m else 0
        elif ln.startswith('+') and path:
            scan_line(path, lineno, ln[1:], names, hits)
            lineno += 1


def scan_whole_file(path, names, hits):
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return
        with open(path, 'rb') as f:
            data = f.read()
    except OSError:
        return
    if b'\0' in data[:8192]:
        return
    for i, text in enumerate(data.decode('utf-8', errors='replace').splitlines(), 1):
        scan_line(path, i, text, names, hits)


def has_head():
    return subprocess.run(['git', 'rev-parse', '--verify', '-q', 'HEAD'], capture_output=True).returncode == 0


def check_pending(names):
    """지금 커밋될 수 있는 모든 것: 스테이징한 것 + 고친 추적 파일 + 새 파일(무시 목록 밖)."""
    hits, files = [], set()
    base = ['diff', 'HEAD'] if has_head() else ['diff', '--cached']
    scan_diff(git(*base, '-U0', '--no-color', '--no-ext-diff'), names, hits, files)
    files.update(git(*base, '--name-only', '--diff-filter=ACMR').split('\n'))
    files.update(git('diff', '--cached', '--name-only', '--diff-filter=ACMR').split('\n'))
    for p in git('ls-files', '--others', '--exclude-standard').split('\n'):
        if p:
            files.add(p)
            scan_whole_file(p, names, hits)
    for p in sorted(f for f in files if f):
        scan_path_name(p, hits)
    return hits


def check_unpushed(names):
    hits, files = [], set()
    shas = git('rev-list', 'HEAD', '--not', '--remotes').split()
    for sha in shas:
        scan_diff(git('show', '-U0', '--no-color', '--no-ext-diff', '--format=', sha), names, hits, files)
        files.update(git('show', '--name-only', '--diff-filter=ACMR', '--format=', sha).split('\n'))
    for p in sorted(f for f in files if f):
        scan_path_name(p, hits)
    return hits


def check_all(names):
    hits = []
    for p in git('ls-files').split('\n'):
        if p:
            scan_path_name(p, hits)
            scan_whole_file(p, names, hits)
    return hits


def report(hits, what, names_path, out):
    seen, uniq = set(), []
    for h in hits:
        if h not in seen:
            seen.add(h)
            uniq.append(h)
    if not uniq:
        print(f'개인정보 점검 통과: {what}' + ('' if names_path else ' (이름 목록 없음: 실명은 점검하지 않음)'), file=out)
        return 0
    print(f'개인정보 점검에서 {len(uniq)}곳이 걸렸어요 ({what}). 공개 저장소라 커밋·푸시를 멈춰요.', file=out)
    for path, lineno, label, shown in uniq[:40]:
        where = f'{path}:{lineno}' if lineno else path
        print(f'  - {where}  {label}  ({shown})', file=out)
    if len(uniq) > 40:
        print(f'  … 외 {len(uniq) - 40}곳', file=out)
    print('고치는 법: 해당 줄에서 개인정보를 빼거나 묶음 숫자·[채울 곳]으로 바꾸고, 원자료 파일은 .private/로 옮겨요.'
          ' 일부러 넣은 가짜 예시라면 그 줄에 privacy-ok를 적어요. 판단이 어려우면 강사님께 물어요.', file=out)
    return 2


GIT_CMD = r'(?:^|[;&|(\s])git(?:\s+-[Cc]\s+\S+|\s+--?[\w-]+(?:=\S+)?)*\s+'


def main():
    args = sys.argv[1:]
    if '--hook' in args:
        try:
            data = json.load(sys.stdin)
        except Exception:
            return 0
        if data.get('tool_name') != 'Bash':
            return 0
        cmd = (data.get('tool_input') or {}).get('command') or ''
        want_commit = re.search(GIT_CMD + r'commit\b', cmd) is not None
        want_push = re.search(GIT_CMD + r'push\b', cmd) is not None
        if not (want_commit or want_push):
            return 0
        cwd = data.get('cwd')
        if cwd and os.path.isdir(cwd):
            os.chdir(cwd)
        m = re.search(r'(?:^|\s)git\s+-C\s+(\S+)', cmd)
        if m and os.path.isdir(os.path.expanduser(m.group(1).strip('"\''))):
            os.chdir(os.path.expanduser(m.group(1).strip('"\'')))
        try:
            names, names_path = load_names()
            hits = []
            if want_commit:
                hits += check_pending(names)
            if want_push:
                hits += check_unpushed(names)
        except Exception as e:  # 점검 자체가 실패하면 커밋·푸시를 멈추고 이유를 알린다
            print(f'개인정보 점검을 돌리지 못해 멈춰요: {e}', file=sys.stderr)
            return 2
        what = '커밋될 변경' if want_commit and not want_push else ('푸시될 커밋' if want_push and not want_commit else '커밋될 변경과 푸시될 커밋')
        code = report(hits, what, names_path, sys.stderr)
        return code

    names, names_path = load_names()
    if '--all' in args:
        hits, what = check_all(names), '저장소 전체'
    elif '--push' in args:
        hits, what = check_unpushed(names), '아직 원격에 없는 커밋'
    else:
        hits, what = check_pending(names), '커밋될 수 있는 변경'
    code = report(hits, what, names_path, sys.stdout)
    return 1 if code else 0


if __name__ == '__main__':
    sys.exit(main())
