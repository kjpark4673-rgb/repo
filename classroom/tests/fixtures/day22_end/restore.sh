#!/bin/bash
# 11/24(Day 22)를 끝낸 시험용 학생 폴더를 되살린다.
# 사용: classroom/tests/fixtures/day22_end/restore.sh <이름> <빈 폴더>
#   이름: fx_md / fx_content / fx_ops / fx_tech (README.md 표 참고)
# 저장소에 둘 때 CLAUDE.md는 _CLAUDE.md로, .claude는 _claude로 이름을 바꿔 두었다(저장소 안에서 스킬·규칙 파일로 읽히지 않게).
# 되살릴 때 원래 이름으로 돌려놓고, 그 폴더에서 runchain.py를 돌릴 때 쓸 입력 칸 값(TOK)을 알려 준다.
set -e
D="$(cd "$(dirname "$0")" && pwd)"
src="$D/$1"; dst="$2"
if [ -z "$1" ] || [ -z "$2" ] || [ ! -d "$src" ]; then
  echo "사용: restore.sh <이름> <빈 폴더>   이름: $(cd "$D" && ls -d fx_*/ 2>/dev/null | tr -d '/' | tr '\n' ' ')"; exit 1
fi
mkdir -p "$dst"
cp -r "$src"/. "$dst"/
[ -f "$dst/_CLAUDE.md" ] && mv "$dst/_CLAUDE.md" "$dst/CLAUDE.md"
if [ -d "$dst/_claude" ]; then mkdir -p "$dst/.claude"; cp -r "$dst/_claude"/. "$dst/.claude"/; rm -rf "$dst/_claude"; fi
mv "$dst/persona.json" "$dst/../$(basename "$dst").persona.json" 2>/dev/null || rm -f "$dst/persona.json"
echo "되살림: $dst"
echo "입력 칸 값(TOK): $(cat "$src/persona.json")"
echo "예: export TOK='$(cat "$src/persona.json")'; cd $dst && python3 <저장소>/classroom/tools/runchain.py <가이드.html> . <결과.json> p00 ..."
