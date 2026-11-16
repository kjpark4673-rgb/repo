# 쉬운 말 규칙 (11/16 강사 지시): 축약된 한자어·업계어를 학생 자료에 그대로 쓰지 않는다.
# 쓰는 법: python3 classroom/tools/easy_words.py check <가이드.html ...>   → 남아 있는 옛말을 찾는다(있으면 종료 코드 1)
#          python3 classroom/tools/easy_words.py apply <파일>               → 조사까지 맞춰 바꾼다(바꾼 뒤 사람이 읽어 본다)
# 바꿈말 표와 이유는 classroom/standards/easy-words.md. 새 말을 더하면 WORDS와 그 문서를 같이 고친다.
import re, sys
# 공식 일정표를 그대로 옮긴 말과, 채용 공고에서 찾아야 하는 현업 말은 바꾸지 않는다
KEEP = ['과업·질문·관찰 지표', '해결 가능성으로 우선순위', '맥락, 과업, 제약', '개선 우선순위', '추천 흐름 동작 검증 기준', '추천 흐름 검증 기준',
        "'과업'", "'태스크'", "'테스터'", "'관찰 지표'", "'우선순위'", "'검증 기준'", '(과업)', '(관찰 지표)', '(우선순위)', '(검증 기준)', '(테스터)']
WORDS = {'과업': '시켜 볼 일', '테스터': '써 보는 사람', '관찰 지표': '지켜보며 적을 것', '우선순위': '고칠 순서', '검증 기준': '통과 기준'}
RULES = [  # 순서대로. 조사와 붙는 모양을 먼저
 (r'과업별로', '시켜 볼 일마다'), (r'과업별 ', '시켜 볼 일마다의 '), (r'과업으로', '시켜 볼 일로'), (r'과업', '시켜 볼 일'),
 (r'두 테스터가 모두', '써 본 사람 1과 2가 모두'), (r'테스터 (\d)', r'써 본 사람 \1'), (r'테스터 칸', '써 본 사람 칸'), (r'테스터마다', '써 본 사람마다'),
 (r'테스터가', '써 보는 사람이'), (r'테스터는', '써 보는 사람은'), (r'테스터를', '써 보는 사람을'), (r'테스터와', '써 보는 사람과'),
 (r'테스터로', '써 보는 사람으로'), (r'테스터예요', '써 보는 사람이에요'), (r'테스터', '써 보는 사람'),
 (r'관찰 지표를', '지켜보며 적을 것을'), (r'관찰 지표는', '지켜보며 적을 것은'), (r'관찰 지표가', '지켜보며 적을 것이'), (r'관찰 지표와', '지켜보며 적을 것과'), (r'관찰 지표', '지켜보며 적을 것'),
 (r'고칠 곳의 우선순위', '고칠 순서'), (r'고칠 곳 우선순위', '고칠 순서'), (r'우선순위', '고칠 순서'),
 (r'검증 기준', '통과 기준'),
]
def _mask(t):
    for i, k in enumerate(KEEP): t = t.replace(k, '\x00%d\x00' % i)
    return t
def _unmask(t):
    for i, k in enumerate(KEEP): t = t.replace('\x00%d\x00' % i, k)
    return t
def apply(t):
    t = _mask(t)
    for a, b in RULES: t = re.sub(a, b, t)
    return _unmask(t)
def find(t):
    import html as _h
    t = _h.unescape(t)
    t = _mask(re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S))
    out = []
    for w in WORDS:
        for m in re.finditer(re.escape(w), t):
            out.append((w, re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', _unmask(t[max(0, m.start()-30):m.end()+30])))))
    return out
if __name__ == '__main__':
    mode, files = sys.argv[1], sys.argv[2:]
    bad = 0
    for f in files:
        t = open(f, encoding='utf-8').read()
        if mode == 'apply':
            open(f, 'w', encoding='utf-8').write(apply(t)); print('바꿈', f)
        else:
            hits = find(t); bad += len(hits)
            print(f, '→', '통과' if not hits else '옛말 %d곳' % len(hits))
            for w, ctx in hits[:20]: print('   [%s → %s] …%s…' % (w, WORDS[w], ctx))
    sys.exit(1 if bad else 0)
