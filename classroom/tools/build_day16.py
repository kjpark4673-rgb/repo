# Day 16 가이드 6판: 강사 지시(11/15) "매일 하던 조사 노가다(광고 소재, 경쟁사 가격, 증정품·프로모션, 상세페이지, 팝업, 교육 프로그램)를 AI 에이전트로 줄이는 업무 간편화 MVP".
# 오전은 다 같이 기초(조사 설계서 → 조사 표 → 보는 화면 → 다듬기), 오후는 각자 심화 메뉴. 수업 예시는 라라스윗의 경쟁사 가격·프로모션 조사.
# 저장소 안에서 그대로 돈다: python3 classroom/tools/build_day16.py [출력 경로]
# 새 날짜는 이 파일을 build_dayNN.py로 복사해 PR(프롬프트)과 body(본문)만 바꾼다. 쓰는 법은 .claude/skills/class-day-guide/ 참고
import re, os
TOOLS=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(os.path.dirname(TOOLS))
PATH=os.path.join(REPO,'classroom','student-guide','day16.html')
src=open(os.path.join(TOOLS,'guide_base.html'),encoding='utf-8').read()
style=re.search(r'<style>.*?</style>',src,flags=re.S).group(0)
script=re.search(r'<script>.*?</script>',src,flags=re.S).group(0)
EXTRA_CSS='''
/* 하루 지도: 맨 앞에서 하루의 구조를 보여 주는 목차. 세 덩어리(정하기, 만들기, 확인하기)와 시간표 */
.acts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:0 0 12px}
.acts div{background:var(--blue-soft);border-radius:16px;padding:14px 8px;text-align:center;min-width:0}
.acts b{display:block;color:var(--blue);font-size:clamp(18px,3.2vw,26px);font-weight:800}
.acts span{font-size:clamp(14px,2.4vw,18px);font-variant-numeric:tabular-nums}
.map{background:var(--card);border-radius:24px;padding:6px 24px;margin:0 0 16px}
.map .grp{color:var(--blue);font-weight:800;font-size:18px;line-height:1.5;padding:22px 0 6px}
.map .row{display:grid;grid-template-columns:3.4em 1fr;gap:12px;align-items:baseline;padding:14px 0;border-top:1px solid var(--line);text-decoration:none;color:inherit}
.map .grp + .row{border-top:0}
.map .t{font-weight:800;font-variant-numeric:tabular-nums}
.map .w b{display:block;font-weight:800}
.map .w small{display:block;color:var(--sub);font-size:18px;line-height:1.5}
.map .rest .w{color:var(--sub)}
.map a.row:hover .w b{color:var(--blue)}
.map a.row:focus-visible{outline:3px solid var(--blue);outline-offset:3px;border-radius:8px}
.why{color:var(--sub);margin:-12px 0 24px}
.roles{display:grid;gap:10px;margin-top:12px}
.role{background:var(--bg);border-radius:16px;padding:16px 18px}
.role h4{font-size:20px;font-weight:800;margin:0 0 6px}
.role p{margin:0 0 8px;font-size:18px}
.role p span{display:block;font-weight:800;color:var(--sub);font-size:15px;line-height:1.4}
.story{background:var(--card);border-radius:24px;padding:28px 28px 20px;margin:0 0 16px;border-left:6px solid var(--blue)}
.story .tag{display:inline-block;color:var(--blue);font-weight:800;font-size:18px;margin-bottom:6px}
.story .grid{margin:16px 0 4px}
.story .grid .card{background:var(--bg);padding:20px}
.story .grid h3{font-size:22px}
.why b{color:var(--ink)}
.steps li{margin-bottom:8px}
.steps small{color:var(--sub);font-size:16px;font-weight:700;margin-left:4px}
.path{border:3px solid var(--blue-soft)}
.role .pickbtn{margin-top:8px}
.field textarea{font:inherit;font-size:18px;line-height:1.5;color:var(--ink);background:var(--code);border:2px solid var(--line);border-radius:14px;padding:14px 16px;width:100%;min-width:0;resize:vertical}
.field textarea:focus{outline:none;border-color:var(--blue)}
.agentfig{margin:0 0 16px}
.agentfig svg{display:block;width:100%;max-width:560px;height:auto;margin:0 auto;color:var(--sub);font-family:inherit}
.agentfig .box{fill:var(--card);stroke:var(--line);stroke-width:1.5}
.agentfig .box.hl{stroke:var(--blue);stroke-width:2.5}
.agentfig .box.web{stroke-dasharray:5 4;stroke:var(--sub)}
.agentfig .chip{fill:var(--bg)}
.agentfig .inner{fill:var(--blue-soft)}
.agentfig .ar{stroke:currentColor;stroke-width:1.6;fill:none}
.agentfig .t{fill:var(--ink);font-size:12.5px}
.agentfig .b{font-weight:800}
.agentfig .s{fill:var(--sub);font-size:11px}
.agentfig .lab{fill:var(--blue);font-size:12.5px;font-weight:800}
.agentfig figcaption{color:var(--sub);margin:14px auto 0;max-width:640px}
.agentfig figcaption b{color:var(--ink)}
.ab{font-weight:500;font-size:.78em;color:var(--sub);letter-spacing:0}
.shots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:12px}
@media (min-width:760px){.shots{grid-template-columns:repeat(3,minmax(0,1fr))}}
.shots figure{margin:0}
.shots img{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--line)}
.shots figcaption{font-size:16px;line-height:1.45;color:var(--sub);margin-top:8px}
.shots figcaption b{color:var(--ink)}
.pairs{background:var(--card);border-radius:24px;padding:6px 24px;margin:0 0 16px}
.pairs .row{display:grid;grid-template-columns:6.6em 1fr;gap:12px;align-items:baseline;padding:14px 0;border-top:1px solid var(--line)}
.pairs .row:first-child{border-top:0}
.pairs .k{font-weight:800}
.pairs .w b{display:block;font-weight:800}
.pairs .w small{display:block;color:var(--sub);font-size:17px;line-height:1.5}
'''
assert style.count('</style>')==1
style=style.replace('</style>',EXTRA_CSS+'</style>')
_d="ind:'식품'};"
assert script.count(_d)==1
_f="i.value=f[i.getAttribute('data-in')]"
assert script.count(_f)==1
script=script.replace(_f,"i.value=val(prof[i.getAttribute('data-in')])")
script=script.replace(_d,"ind:'식품',tone:'네가 정해줘',role:'아직 모름',pick:'네가 정해줘',rivals:'네가 정해줘',focus:'네가 정해줘',more:'경쟁사 2곳 더',said:'적지 않음',fb:'적지 않음',sec:'적지 않음',ads:'적지 않음'};")
def tok(k,d): return '<b data-v="%s">%s</b>'%(k,d)
B=tok('brand','라라스윗'); P=tok('product','저당 아이스크림'); C=tok('customer','다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인')
ROLE=tok('role','아직 모름'); TASK=tok('task','네가 정해줘')
CO='- 회사: '+B+' ('+P+') / 고객: '+C
TOP=' style="margin-top:12px"'
def box(pid,title,text,style_attr=''):
    return ('<button class="copy" type="button" data-copy="%s"%s><div class="hd"><b>%s</b><span class="btn">눌러서 복사</span></div>\n<pre id="%s">%s</pre></button>'%(pid,style_attr,title,pid,text))
def field(k,label,ph=''):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><input id="v-%s" data-in="%s" type="text" maxlength="90" placeholder="%s" autocomplete="off"></div></div>'%(k,label,k,k,ph)


# ── 6판 프롬프트: 매일 하던 조사를 AI로 줄이는 업무 간편화 MVP (11/15 강사 지시)
PICK=tok('pick','네가 정해줘'); RIV=tok('rivals','네가 정해줘')
PR={}
PR['p00']='''이 폴더의 CLAUDE.md를 오늘 수업에 맞게 고쳐줘. 파일이 없으면 새로 만들어줘. 끝나면 3줄로만 알려줘.
1. "멈추고 묻기", "아카이브에 없는 것은 쓰지 않기"처럼 금요일에 넣은 규칙이 있으면 그 줄만 지워줘. 다른 내용은 건드리지 마.
2. 아래 내용을 맨 아래에 넣어줘. 같은 제목이 이미 있으면 바꿔 넣어줘.

# 수업 작업 규칙 (다른 규칙과 부딪히면 이 규칙이 먼저다)
- 되묻지 않는다. 정보가 모자라면 스스로 가정하고 끝까지 만든다.
- 가정하거나 추측한 곳에는 (가정)이라고 표시한다. 숫자, 가격, 후기를 사실처럼 꾸미지 않는다.
- 웹에서 조사한 값에는 조사한 날짜와 출처 링크를 붙인다. 찾지 못한 값은 "못 찾음"으로 둔다.
- 표(CSV)는 엑셀에서 한글이 깨지지 않게 UTF-8 BOM으로 저장하고, 쉼표, 큰따옴표, 줄바꿈이 든 값은 큰따옴표로 감싼다.
- 필요한 파일이 없어도 멈추지 않는다. 없는 대로 진행한다.
- 결과는 파일로 저장하고, 끝나면 3줄로만 보고한다: 만든 파일 / 핵심 한 줄 / 내가 다음에 할 일 한 줄. 내용을 보여 달라고 하면 그대로 보여 준다.
- 모든 결과는 한국어로, 쉬운 말로 쓴다.

# 나와 회사 (오늘은 이 내용으로 작업한다)
- 내가 하고 싶은 일: '''+ROLE+'''
- 회사(브랜드): '''+B+''' ('''+P+''')
- 고객: '''+C+'''
- 내가 하고 싶은 일이나 조사할 것이 이 회사에 없는 일이면, 그 일이 있는 비슷한 가상의 회사로 바꿔서 작업하고, 바꾼 회사를 이 파일의 회사 줄에 적고 한 줄로 알린다.'''
PR['w1']='''내가 하고 싶은 일의 채용 공고에, 오늘 수업에서 하는 일이 실제로 나오는지 찾아서 why.md로 정리해줘.
- 내가 하고 싶은 일: '''+ROLE+'''
- 오늘 하는 일 여섯 가지: 경쟁사 조사(광고, 가격, 프로모션, 상세페이지, 서비스 기능 같은 것) / 조사 결과를 표로 정리하기 / 한눈에 보는 화면 만들기(대시보드, 리포트) / 반복 업무를 자동화하기 / 생성형 AI 도구로 일하기 / 조사 결과로 개선안 내기
- 일마다, 그 일이 주요 업무나 자격 요건, 우대 사항에 적힌 최근 채용 공고를 웹에서 1개씩 찾아줘. 낱말이 달라도 같은 일이면 돼(예: 경쟁사 조사는 "경쟁사 모니터링", "시장 조사", "가격 모니터링", "레퍼런스 조사". 표 정리는 "데이터 정리", "보고서 작성". 화면 만들기는 "대시보드 구축", "리포트 자동화". 자동화는 "업무 자동화", "RPA", "데이터 수집(크롤링)". 개선안은 "프로모션 기획", "개선안 도출"). 같은 공고를 여러 번 써도 돼.
- 하고 싶은 일이 "아직 모름"이면 직무를 가리지 말고 찾고, 어떤 직무의 공고인지 같이 적어줘.
- 찾지 못한 일은 "못 찾음"이라고 써. 억지로 잇지 마.
- 공고 원문을 열어 확인하지 못한 문장은 (가정)이라고 표시해. 원문이 열리지 않아도 멈추지 말고 검색 결과로 끝까지 해.
- 이 직무의 공고에 자주 나오는데 오늘 수업에서는 하지 않는 일도 3가지 적어줘.
되묻지 말고 끝까지 하고, 끝나면 표 하나(오늘 하는 일 / 공고에 적힌 문장 / 회사와 링크), "오늘 이걸 하는 이유" 세 줄, "오늘 하지 않는 일" 한 줄만 보여줘.'''
PR['p01']='''내가 매일 손으로 하던 조사를 AI 에이전트로 줄이는 MVP를 만들 거야. 먼저 조사 설계서 한 장을 mvp.md로 써줘.
- 내가 하고 싶은 일: '''+ROLE+'''
- 조사할 것: '''+PICK+'''
- 경쟁사: '''+RIV+'''
'''+CO+'''
- 조사할 것이 "네가 정해줘"이면 하고 싶은 일에 맞춰 골라줘. 마케터는 광고 소재, MD·온라인 영업은 경쟁사 가격과 증정품·프로모션, 브랜드·공간 마케터는 팝업스토어, CX는 상세페이지, 서비스 기획·개발·데이터 분석(테크 트랙)은 경쟁 서비스 기능, 교육 회사 운영·기획은 교육 프로그램, 그 밖의 일이나 "아직 모름"은 경쟁사 가격과 증정품·프로모션.
- 보기: 광고 소재 / 경쟁사 가격 / 증정품·프로모션 / 상세페이지 / 팝업스토어 / 교육 프로그램(커리큘럼, 강사진, 운영안) / 경쟁 서비스 기능(경쟁사 자사몰이나 앱의 기능). 보기에 없는 조사를 적었으면 그대로 해줘.
- 경쟁사가 "네가 정해줘"이면 우리와 같은 고객을 두고 경쟁하는 곳 3곳을 골라줘(우리보다 훨씬 큰 대기업은 빼고).
- 회사가 조사할 것과 맞지 않으면(예: 교육 프로그램인데 아이스크림 회사) 그 일이 있는 비슷한 가상의 회사로 바꾸고 한 줄로 알려줘. 바꾼 회사는 mvp.md 맨 위와 CLAUDE.md의 회사 줄에도 적어줘.
- 칸: 누가, 언제, 왜 이 조사를 매일 하나(지금 손으로 하면 하루 몇 분인지, 모르면 (가정)) / 경쟁사 3곳과 고른 이유 / 표에 적을 칸 5~7개와 칸마다 어디서 찾나 / 만들지 않을 것 3가지 / 확인할 숫자 2가지(예: 걸린 시간, 못 찾은 칸 수) / 성공 기준
- 가격을 조사하면 판매처(몰) 칸을 꼭 넣어줘(같은 제품도 몰마다 값이 달라). 용량은 단위(g, ml)까지 적게 해줘.
- 로그인해야 보이는 값이나 자동 접속을 막는 쇼핑몰의 실시간 가격처럼 웹에서 찾기 어려운 칸에는 "못 찾을 수 있음"이라고 적어줘.
되묻지 말고 끝까지 쓰고, 끝나면 "조사할 것", "경쟁사 3곳", "표에 적을 칸"만 보여줘.'''
PR['p02']='''mvp.md대로 웹에서 조사해서 research.csv로 저장해줘. 오늘 MVP의 재료가 되는 표야.
- 경쟁사마다 한 줄 이상. 맨 앞 두 칸은 조사일과 경쟁사, 맨 끝 칸은 출처 링크로 해줘.
- 찾지 못한 값은 "못 찾음"이라고 쓰고, 지어내지 마. 가격은 원 단위 숫자만 적어줘.
- 엑셀에서 열어도 한글이 깨지지 않게 저장해줘(UTF-8 BOM). 칸 이름이나 값에 쉼표가 들어가면 큰따옴표로 감싸서 칸이 밀리지 않게 해줘.
- mvp.md가 없으면 CLAUDE.md의 회사로 경쟁사 3곳의 가격과 증정품·프로모션을 조사해줘.
되묻지 말고 끝까지 하고, 끝나면 표의 앞 5줄과 "못 찾음"이 몇 칸인지만 보여줘.'''
PR['p02b']='''내가 직접 보고 복사한 광고를 research.csv에 더해줘. 웹에서 못 찾은 칸을 채우는 거야.
- 내가 본 광고: '''+tok('ads','적지 않음')+'''
- 광고마다 한 줄로 넣고, 맨 앞 두 칸은 조사일과 경쟁사, 맨 끝 출처 칸에는 "내가 직접 봄"과 내가 붙인 링크를 적어줘. 링크가 없으면 "메타 광고 라이브러리"라고만 적어줘.
- 표의 칸(훅, 약속, 형식 같은 것)에 맞춰 나눠 넣고, 내가 붙인 글에 없는 칸은 "못 찾음"으로 둬. 내가 붙인 글을 고치거나 보태지 마.
- 같은 광고가 이미 표에 있으면 새 줄을 만들지 말고 "못 찾음"이던 칸만 채워줘.
- 광고가 아니라 가격이나 혜택을 붙였으면 표의 그 칸에 맞춰 넣어줘.
- 내가 본 광고가 "적지 않음"이면 아무것도 더하지 말고, 메타 광고 라이브러리에서 경쟁사 광고를 찾아 복사하는 방법만 3줄로 알려줘.
되묻지 말고 끝까지 하고, 끝나면 더한 줄과 "못 찾음"이 몇 칸 줄었는지만 보여줘.'''
PR['p03']='''research.csv를 한눈에 보는 화면 mvp.html을 만들어줘. 파일 하나로, 외부 라이브러리 없이, 폰과 PC에서 다 보이게.
- 화면에서 꼭 볼 것: '''+tok('focus','네가 정해줘')+'''
- 맨 위: 이 화면이 해 주는 일 한 줄과 조사일, 경쟁사 수, "못 찾음" 칸 수
- 가운데: 경쟁사별로 나란히 비교하는 표나 카드. 출처 링크는 눌러서 열리게.
- 경쟁사나 칸으로 걸러 보는 버튼
- research.csv의 내용을 화면 파일 안에도 넣어서, 파일을 더블클릭해 열어도 바로 보이게 해줘. 화면에서 다른 CSV를 고르면 그 내용으로 바뀌게 해줘(쉼표나 따옴표가 든 칸도 제대로 읽게).
- "못 찾음"은 흐리게 보여 줘. 맨 아래에 "공개 자료로 만든 학습용 MVP이며, 조사한 회사와 관계없습니다"라고 적어줘.
research.csv가 없으면 mvp.md대로 먼저 조사하고 이어서 해줘. 되묻지 말고 끝까지 만들고, 끝나면 3줄로만 알려줘.'''
PR['p04']='''mvp.html을 처음 보는 사람이 5초 안에 "무엇을 하는 화면인지" 알 수 있게 다듬어줘.
- 맨 위에는 이 화면이 해 주는 일 한 줄과, 가장 중요한 숫자나 결과 하나만 크게(예: 가장 싼 곳, 새 증정품 수, 새 광고 수).
- 글꼴은 두 가지 이하, 색은 이름을 붙인 4~6가지. 우리 회사의 색이나 분위기: '''+tok('tone','네가 정해줘')+'''
- 표의 내용과 기능은 바꾸지 마. 고치기 전 파일은 mvp_before.html로 남겨줘.
mvp.html이 없으면 research.csv로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 "5초 안에 보이는 것"을 한 줄로만 알려줘.'''
PR['p05']='''research.csv의 출처 링크부터 다시 열어, 같은 경쟁사와 칸으로 다시 조사해서 research_new.csv로 저장하고, research.csv와 비교해줘.
- 같은 제품, 같은 기획전끼리 비교해서 값이 바뀐 칸(가격, 혜택, 기간, 새 광고, 새 강사 같은 것), 새로 생긴 줄, 사라진 줄을 찾아줘.
- "못 찾음"이 값으로 바뀌었거나 출처가 바뀐 칸은 바뀐 곳이 아니라 (확인 필요)로 따로 보여 줘.
- mvp.html에 "바뀐 곳" 칸을 만들어 바뀐 값은 색으로 표시하고, 앞 값과 새 값을 같이 보여 줘.
- 바뀐 곳이 없으면 "바뀐 곳 없음"과 비교한 시각을 보여 줘.
- 고치기 전 화면은 mvp_v1.html로 남겨줘. 이미 있으면 다음 번호(mvp_v2.html)로.
research.csv가 없으면 mvp.md대로 먼저 조사하고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 바뀐 곳과 (확인 필요)만 표로 보여줘. 둘 다 없으면 "바뀐 곳 없음"만.'''
PR['p06']='''research로 시작하는 조사 표 가운데 가장 최근 것을 보고(바뀐 곳을 찾았으면 그것도), 우리 회사가 내일 할 대응안 한 장을 plan.md로 써줘.
- 내가 하고 싶은 일: '''+ROLE+''' / 회사: '''+B+''' ('''+P+'''). 회사를 바꿨으면 CLAUDE.md에 적힌 회사로 해줘.
- 경쟁사에게서 보인 것 3가지(숫자와 출처 링크를 같이) → 우리가 할 일 3가지 → 하지 않을 일 1가지 → 확인할 숫자
- 마케터면 광고 시안 3개의 카피와 방향을, MD·온라인 영업이면 가격·증정품·기획전 제안을, 교육 회사면 커리큘럼·운영 개선안을, 테크 트랙(서비스 기획·개발·데이터)이면 우리 서비스에 먼저 만들 기능 하나와 그 이유를 넣어줘.
- 지어낸 숫자는 쓰지 말고, 내가 확인할 값은 [채울 곳]으로 둬.
research.csv가 없으면 mvp.md대로 먼저 조사하고 이어서 해줘. 되묻지 말고 끝까지 쓰고, 끝나면 "우리가 할 일 3가지"만 보여줘.'''
PR['p07']='''plan.md의 대응안으로 랜딩페이지 landing.html 한 장과, 이미지 AI에 붙일 프롬프트 kv.md를 만들어줘.
- landing.html: 폰 화면 기준, 파일 하나. 위에서 아래로 문제 → 공감 → 제품 → 근거 → 남의 말 → 쓰는 장면 → 걱정 풀기 → 지금 사기. 사진 자리는 회색 박스, 가격과 후기는 [채울 곳]. 맨 아래에 "학습용 MVP이며 실제 회사와 무관합니다".
- kv.md: 랜딩페이지 첫 화면에 넣을 키비주얼 1장(kv.png)과 인스타그램 광고 시안 3장(sns1.png, sns2.png, sns3.png)의 이미지 프롬프트. 장마다 한국어로 3문장 안(장면, 빛, 구도, 색)과 이미지 위에 얹을 큰 카피 한 줄. 프롬프트 끝마다 "글자, 실제 브랜드 로고, 실제 제품 포장은 그리지 않는다".
- plan.md가 없으면 research.csv로 먼저 대응안을 정하고 이어서 해줘.
되묻지 말고 끝까지 만들고, 끝나면 이미지 프롬프트 4개만 파일 이름과 함께 보여줘.'''
PR['p08']='''조사를 넓혀줘: '''+tok('more','경쟁사 2곳 더')+'''
- mvp.md의 경쟁사나 칸에 더하고, 웹에서 조사해 research.csv에 이어서 저장해줘. 출처 링크와 조사일을 붙이고, 못 찾은 값은 "못 찾음".
- 다른 조사(보기)를 적었으면 research2.csv로 따로 저장하고, mvp.html에 탭을 하나 더 만들어줘.
- mvp.html도 새 내용으로 바꿔줘. 고치기 전 화면은 mvp_v1.html로 남겨줘. 이미 있으면 다음 번호(mvp_v2.html)로.
되묻지 말고 끝까지 하고, 끝나면 늘어난 경쟁사나 칸과 "못 찾음"이 몇 칸인지만 보여줘.'''
PR['p09']='''짝꿍이 mvp.html을 처음 써 본 결과야. 이걸로 mvp.html을 한 곳만 고쳐줘.
- 짝꿍이 5초 보고 말한 것: '''+tok('said','적지 않음')+'''
- 할 일을 끝내는 데 걸린 시간: '''+tok('sec','적지 않음')+'''
- 짝꿍이 헷갈려한 곳(내가 고른 것): '''+tok('fb','적지 않음')+'''
- 고치기 전 화면은 mvp_v1.html로 남겨줘. 이미 있으면 다음 번호(mvp_v2.html)로. 헷갈려한 곳 하나만 고치고, 다른 곳은 건드리지 마.
- mvp.md 맨 아래에 "써 본 결과" 칸을 만들어 적어줘: 누가 써 봤나 / 5초 보고 말한 것 / 걸린 시간 / 헷갈려한 곳 / 고친 것 / 다음에 확인할 숫자
- 짝꿍 결과가 "적지 않음"이면, 처음 보는 사람이 가장 헷갈릴 만한 곳 하나를 네가 골라 고치고 "써 본 결과" 칸에 (가정)이라고 적어줘.
mvp.html이 없으면 research.csv로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 고친 곳 한 줄과 "써 본 결과" 칸만 보여줘.'''
PR['p10']='''오늘 한 조사를 다음에도 한 줄로 다시 돌릴 수 있게 스킬로 묶어줘.
- 저장할 곳: .claude/skills/daily-research/SKILL.md (맨 위에 name과 description. description에 "오늘 조사 돌려줘"를 넣어서 그 한 줄로 불리게)
- "오늘 조사 돌려줘"라고 하면: mvp.md의 경쟁사와 칸으로 웹에서 다시 조사 → research_날짜.csv로 저장 → 바로 앞 조사 파일과 같은 제품끼리 비교해 바뀐 곳 찾기("못 찾음"이 값으로 바뀌었거나 출처가 바뀐 칸은 (확인 필요)로 따로) → mvp.html에 새 내용과 바뀐 곳 표시
- 조사일과 출처 링크를 붙이고, 못 찾은 값은 "못 찾음"으로 두고, 값을 지어내지 않는 규칙을 넣어줘.
- 회사 이름은 넣지 말고, mvp.md를 읽어서 쓰게 해줘.
되묻지 말고 끝까지 만들고, 끝나면 이 스킬을 부르는 한 줄만 알려줘.'''
PR['w2']='''오늘 이 폴더에서 한 일을 내 포트폴리오에 넣을 한 장으로 정리해서 portfolio_1116.md로 써줘.
- 내가 하고 싶은 일: '''+ROLE+''' / 조사할 것: '''+PICK+''' / 회사: '''+B+'''. 회사를 바꿨으면 CLAUDE.md에 적힌 회사로 써줘.
- 무엇을 만들었나: 어떤 조사를 줄이는 MVP인지 한 줄과 파일 이름
- 줄인 것: 손으로 하면 걸리던 시간과 에이전트로 걸린 시간(내가 덧붙인 값이 있으면 그 값, 없으면 mvp.md의 값에 (가정)), 못 찾은 칸 수
- 수업에서 배운 방법: 수업 프롬프트가 시킨 방법 가운데 내가 실제로 따라 한 것을 3줄로 적어줘(예: 조사 설계서부터 쓰기, 출처 링크 붙이기, 한눈에 보는 화면 만들기). 이건 내 결정이 아니야.
- 내가 내린 결정: 아래 세 가지만 적어줘.
  - 조사할 것, 경쟁사, 회사, 화면에서 꼭 볼 것, 오후에 고른 심화. "아직 모름", "네가 정해줘", 수업 연습용 회사인 "라라스윗"은 내가 정한 게 아니야.
  - 프롬프트의 빈 자리에 내가 적어 넣은 것. "네가 정해줘", "적지 않음"만 있으면 적은 게 아니야.
  - 내가 따로 말해서 바꾼 것, 출처를 열어 확인하거나 바로잡은 것, 이유를 말하고 받아들인 것.
- 네가 골랐고 내가 그대로 받은 것은 "Claude가 고름"이라고 쓰고, 옆에 [내가 적을 곳: 받아들인 이유]를 남겨줘. 큰 것 5개까지만.
- 이 결과물이 회사에서 쓰이는 곳: why.md가 있으면 거기 공고 문장과 연결해줘. 없으면 (가정)이라고 표시하고 써줘.
- 면접에서 말할 세 문장: 무엇을 만들었고, 무엇을 결정했고, 다음에 무엇을 고칠지. 내가 내리지 않은 결정을 내가 한 것처럼 쓰지 마. 쓸 결정이 없으면 그 문장은 [내가 적을 곳]으로 남겨줘.
되묻지 말고 끝까지 쓰고, 끝나면 "면접에서 말할 세 문장"과 [내가 적을 곳]이 남은 자리만 보여줘.'''
R={'r1':'되묻지 말고 네가 가정해서 끝까지 만들어줘. 가정한 곳만 (가정)이라고 표시해줘.',
'r2':'너무 길어. 3줄로만 다시 말해줘.',
'r3':'없는 자료는 없는 대로 두고, 지금 있는 것으로 끝까지 만들어줘.',
'r4':'더 깊게. 왜 그런지 한 단계만 더 파고들어줘.',
'r5':'방금 쓴 글을 장면으로 다시 써줘. 시간, 장소, 손에 든 것, 혼잣말이 보이게.',
'r6':'방금 만든 파일의 내용을 그대로 보여줘. CSV면 앞 10줄을 표로, HTML이면 코드 말고 화면에 무엇이 어떤 순서로 있는지 알려줘.',
'r7':'landing.html에서 우리 업종의 광고 규정에 걸릴 수 있는 표현 가운데 가장 위험한 5개만 표로 보여 주고(원래 표현 / 이유 / 고친 표현), 화면도 그렇게 고쳐줘. 확실하지 않은 것은 (확인 필요)라고 표시해줘. 표 말고 다른 설명은 3줄 안으로 해줘.'}
TASK1='짝꿍에게 mvp.html을 1분 동안 써 보게 할 거야. 이 화면으로 짝꿍이 찾아야 할 것 하나를 한 문장으로 만들어줘(예: 가장 싼 곳, 증정품이 있는 곳). 어디를 누르라는 말이나 정답은 넣지 마.'
CMP1='mvp_before.html과 mvp.html을 브라우저 탭 두 개로 열어줘.'
CMP2='mvp_v 뒤 번호가 가장 큰 파일과 mvp.html을 브라우저 탭 두 개로 열어줘.'
IMG='images 폴더의 kv.png를 landing.html 첫 화면의 회색 박스에 넣어줘. 이름이나 확장자가 달라도 그림을 보고 맞춰줘. 이미지가 없으면 어떤 이름으로 넣으면 되는지만 알려줘.'
RUN='오늘 조사 돌려줘'
FOLD='이 폴더에 images 폴더를 만들고, 그 폴더를 파일 탐색기(맥은 Finder)로 열어줘.'
PUB='mvp.html을 아티팩트로 발행하고 링크를 알려줘.'
OPEN='mvp.html을 브라우저로 열어줘.'

# MVP 표기(강사 지시): 프롬프트는 줄마다 처음 한 번 "MVP(Minimum Viable Product)", 본문은 문단(블록)마다 처음 한 번, 괄호 부분은 흐리게
def expand_mvp_plain(t):
    out=[]
    for ln in t.split('\n'):
        if 'Minimum Viable Product' not in ln:
            ln=re.sub(r'MVP(?!\s*\()','MVP(Minimum Viable Product)',ln,count=1)
        out.append(ln)
    return '\n'.join(out)
for _k in list(PR): PR[_k]=expand_mvp_plain(PR[_k])
_BLOCK=re.compile(r'</?(p|li|h1|h2|h3|h4|summary|div|small|figcaption|td|th|label|button|section|ul|ol|details|figure)\b',re.I)
def expand_mvp_html(h):
    out=[];done=False;in_pre=False
    for tok in re.split(r'(<[^>]+>)',h):
        if tok.startswith('<'):
            low=tok.lower()
            if low.startswith('<pre'): in_pre=True
            elif low.startswith('</pre'): in_pre=False
            if _BLOCK.match(low): done=False
            out.append(tok); continue
        if in_pre or 'MVP' not in tok:
            out.append(tok); continue
        if 'Minimum Viable Product' in tok:
            done=True; out.append(tok); continue
        parts=re.split(r'(MVP(?!\s*\())',tok); buf=[]
        for part in parts:
            if part=='MVP' and not done:
                buf.append('MVP<span class="ab">(Minimum Viable Product)</span>'); done=True
            else: buf.append(part)
        out.append(''.join(buf))
    return ''.join(out)

# ── 6판 본문
def fieldwide(k,label,ph='',n=1500):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><textarea id="v-%s" data-in="%s" rows="4" maxlength="%d" placeholder="%s" autocomplete="off"></textarea></div></div>'%(k,label,k,k,n,ph)
PICKS=[
('광고 소재 리서치','콘텐츠·퍼포먼스 마케터','경쟁 브랜드 광고를 매일 찾아 캡처하고, 엑셀에 옮겨 적고, 드라이브에 올려요','훅, 약속, 형식(이미지·영상), 올린 곳, 시작일, 링크'),
('경쟁사 가격 조사','MD·온라인 영업','경쟁 제품의 판매가와 할인율을 몰마다 열어 보고 표에 옮겨요','제품, 용량, 정가, 판매가, 할인율, 100g(ml)당 가격, 링크'),
('증정품·프로모션 조사','MD·온라인 영업','경쟁사의 사은품, 1+1, 쿠폰, 기획전을 찾아 정리해요','기획전 이름, 기간, 혜택, 받는 조건, 링크'),
('상세페이지 조사','MD·콘텐츠 마케터·CX','경쟁사 상세페이지를 캡처하고 구성과 문구를 정리해요','첫 화면 문구, 근거(수치·인증), 후기 보여 주는 방식, 구매 유도 장치, 링크'),
('팝업스토어 리서치','브랜드·공간 마케터','요즘 열리는 팝업스토어를 찾아 장소와 콘셉트를 모아요','장소, 기간, 콘셉트, 체험 거리, 굿즈·증정, 예약 방식, 링크'),
('교육 프로그램 리서치','교육 회사 운영·기획','경쟁 교육 과정의 커리큘럼, 강사진, 운영 방식을 비교해요','과정 이름, 기간, 커리큘럼 주제, 강사진, 운영 방식, 수강료·지원, 링크'),
('경쟁 서비스 기능 조사','서비스 기획자·개발자·데이터 분석가(테크 트랙)','경쟁사 자사몰이나 앱에 새 기능이 생겼는지 매번 들어가 보고 정리해요','기능 이름(정기 배송, 리뷰 필터, 장바구니 쿠폰 같은 것), 있음·없음, 어떻게 쓰나, 처음 본 날, 링크'),
]
def pick_card(p):
    return ('<div class="role"><h4>%s</h4><p><span>누가 매일 하나</span>%s</p><p><span>손으로 하면</span>%s</p><p><span>표에 적을 칸 (예)</span>%s</p>'
            '<button class="ghost pickbtn" type="button" data-pick="%s">이걸로 할게요</button></div>')%(p[0],p[1],p[2],p[3],p[0])
PICK_CARDS='\n'.join(pick_card(p) for p in PICKS)

FIG='''<figure class="agentfig">
<svg viewBox="0 0 372 664" role="img" aria-label="내가 붙여 넣은 프롬프트를 에이전트가 CLAUDE.md를 먼저 읽은 뒤 웹에서 찾고 표로 정리하고 화면을 만든다. 결과는 작업 폴더에 파일로 남고 다음 프롬프트가 그 파일을 읽는다. 사람이 확인하고 결정을 한 줄로 말하면 다음 입력이 된다.">
<defs><marker id="agah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>
<rect class="box" x="8" y="8" width="252" height="84" rx="14"/>
<text class="lab" x="18" y="28">① 입력 · 내가 주는 것</text>
<rect class="chip" x="16" y="38" width="73" height="44" rx="9"/><text class="t b" x="52.5" y="56" text-anchor="middle">입력 칸</text><text class="s" x="52.5" y="73" text-anchor="middle">파란 글자</text>
<rect class="chip" x="97" y="38" width="73" height="44" rx="9"/><text class="t b" x="133.5" y="56" text-anchor="middle">프롬프트</text><text class="s" x="133.5" y="73" text-anchor="middle">P0~P10</text>
<rect class="chip" x="178" y="38" width="73" height="44" rx="9"/><text class="t b" x="214.5" y="56" text-anchor="middle">내 결정</text><text class="s" x="214.5" y="73" text-anchor="middle">한 줄 말하기</text>
<line class="ar" x1="134" y1="92" x2="134" y2="126" marker-end="url(#agah)"/><text class="s" x="142" y="114">붙여 넣고 보내기</text>
<rect class="box hl" x="8" y="128" width="252" height="146" rx="14"/>
<text class="lab" x="18" y="148">② 처리 · 내 에이전트(Claude Code)</text>
<rect class="inner" x="16" y="158" width="114" height="48" rx="9"/><text class="t b" x="73" y="178" text-anchor="middle">CLAUDE.md</text><text class="s" x="73" y="196" text-anchor="middle">규칙·내 일·회사</text>
<rect class="inner" x="138" y="158" width="114" height="48" rx="9"/><text class="t b" x="195" y="178" text-anchor="middle">스킬 파일</text><text class="s" x="195" y="196" text-anchor="middle">오후에 만들면 생겨요</text>
<text class="s" x="134" y="224" text-anchor="middle">일을 시작할 때마다 먼저 읽어요</text>
<rect class="chip" x="16" y="236" width="54" height="26" rx="13"/><text class="t" x="43" y="254" text-anchor="middle">찾기</text>
<rect class="chip" x="76" y="236" width="54" height="26" rx="13"/><text class="t" x="103" y="254" text-anchor="middle">정리</text>
<rect class="chip" x="136" y="236" width="54" height="26" rx="13"/><text class="t" x="163" y="254" text-anchor="middle">만들기</text>
<rect class="chip" x="196" y="236" width="54" height="26" rx="13"/><text class="t" x="223" y="254" text-anchor="middle">고치기</text>
<rect class="box web" x="284" y="150" width="72" height="56" rx="12"/><text class="t b" x="320" y="173" text-anchor="middle">웹에서 찾기</text><text class="s" x="320" y="192" text-anchor="middle">광고·가격·후기</text>
<line class="ar" x1="262" y1="178" x2="282" y2="178" marker-start="url(#agah)" marker-end="url(#agah)"/>
<line class="ar" x1="80" y1="274" x2="80" y2="324" marker-end="url(#agah)"/><text class="s" x="88" y="303">파일로 저장</text>
<line class="ar" x1="180" y1="326" x2="180" y2="276" marker-end="url(#agah)"/><text class="s" x="188" y="303">다음 프롬프트가 읽음</text>
<rect class="box" x="8" y="326" width="252" height="200" rx="14"/>
<text class="lab" x="18" y="346">③ 출력 · 작업 폴더에 쌓이는 파일</text>
<rect class="chip" x="16" y="358" width="236" height="22" rx="6"/><text class="t" x="24" y="373">why.md (채용 공고)</text><text class="s" x="244" y="373" text-anchor="end">W1</text>
<rect class="chip" x="16" y="385" width="236" height="22" rx="6"/><text class="t" x="24" y="400">mvp.md (조사 설계서)</text><text class="s" x="244" y="400" text-anchor="end">P1</text>
<rect class="chip" x="16" y="412" width="236" height="22" rx="6"/><text class="t" x="24" y="427">research.csv (조사 표)</text><text class="s" x="244" y="427" text-anchor="end">P2</text>
<rect class="chip" x="16" y="439" width="236" height="22" rx="6"/><text class="t b" x="24" y="454">mvp.html (보는 화면)</text><text class="s" x="244" y="454" text-anchor="end">P3·P4</text>
<rect class="chip" x="16" y="466" width="236" height="22" rx="6"/><text class="t" x="24" y="481">바뀐 곳·대응안·스킬 (오후)</text><text class="s" x="244" y="481" text-anchor="end">P5~P10</text>
<rect class="chip" x="16" y="493" width="236" height="22" rx="6"/><text class="t" x="24" y="508">portfolio_1116.md</text><text class="s" x="244" y="508" text-anchor="end">W2</text>
<line class="ar" x1="80" y1="526" x2="80" y2="564" marker-end="url(#agah)"/><text class="s" x="88" y="550">열어 보고 확인</text>
<rect class="box" x="8" y="566" width="252" height="92" rx="14"/>
<text class="lab" x="18" y="586">④ 검증 · 사람이 하는 일</text>
<rect class="chip" x="16" y="596" width="114" height="26" rx="13"/><text class="t" x="73" y="614" text-anchor="middle">출처 확인</text>
<rect class="chip" x="138" y="596" width="114" height="26" rx="13"/><text class="t" x="195" y="614" text-anchor="middle">꼭 볼 것 정하기</text>
<rect class="chip" x="16" y="626" width="114" height="26" rx="13"/><text class="t" x="73" y="644" text-anchor="middle">짝꿍 5초 보기</text>
<rect class="chip" x="138" y="626" width="114" height="26" rx="13"/><text class="t" x="195" y="644" text-anchor="middle">오후 메뉴 고르기</text>
<polyline class="ar" points="260,612 366,612 366,48 262,48" marker-end="url(#agah)"/>
<text class="s" x="313" y="604" text-anchor="middle">한 줄로 말하면</text><text class="s" x="313" y="40" text-anchor="middle">다음 입력</text>
</svg>
<figcaption><b>내 에이전트는 폴더에 사는 신입 사원과 같아요.</b> 일을 시작할 때마다 업무 수칙(CLAUDE.md)을 먼저 읽고, 내가 붙여 넣은 프롬프트대로 웹에서 찾고, 표로 정리하고, 화면을 만들어요. 결과는 작업 폴더에 파일로 남고, 다음 프롬프트가 그 파일을 이어받아요. 오후에 스킬 파일을 만들면 "오늘 조사 돌려줘" 한 줄로 같은 일을 다시 해요. 맞는지는 내가 보고, 결정을 한 줄로 말하면 그 말이 다음 입력이 돼요.</figcaption>
</figure>
'''

body='''
<div class="wrap">
<nav id="nav" aria-label="구간 이동">
<a href="#s0">오늘</a><a href="#s1">준비</a><a href="#s2">1교시</a><a href="#s3">2교시</a><a href="#s4">3교시</a><a href="#s5">4교시</a><a href="#s6">오후</a><a href="#s7">마무리</a><a href="#remote">리모컨</a><a href="#s8">막히면</a>
</nav>

<section id="s0">
<span class="eyebrow">Day 16 / 52 · 11/16(월)</span>
<h1>Day 16 · 매일 하던 조사를 AI로 줄이는 MVP를 만드는 날</h1>
<p class="lead">현업 신입은 매일 같은 조사를 손으로 해요. 경쟁사 광고를 캡처하고, 가격과 증정품을 엑셀에 옮기고, 상세페이지를 저장해요. 오늘은 이 조사 하나를 골라, <b>AI 에이전트가 대신 찾아 표로 정리하고 한 화면에서 보여 주는 가장 작은 첫 버전(MVP)</b>을 만들어요. 오전에는 다 같이 기초를, 오후에는 각자 심화를 해요.</p>

<h3 class="gap">오늘 한눈에</h3>
<div class="acts">
<div><b>① 정하고 조사</b><span>09:40–11:00</span></div>
<div><b>② 화면 만들기</b><span>11:00–13:00</span></div>
<div><b>③ 심화와 마무리</b><span>14:00–18:00</span></div>
</div>
<div class="map">
<div class="grp">시작</div>
<div class="row rest"><span class="t">09:00</span><span class="w">오늘 한눈에 보기 (지금 이 화면)</span></div>
<a class="row" href="#s1"><span class="t">09:25</span><span class="w"><b>준비 · 규칙 심기, 채용 공고 확인</b><small>남는 것: CLAUDE.md, why.md</small></span></a>
<div class="grp">① 정하고 조사 · 매일 하던 조사 하나를 골라 설계하고, 첫 조사를 돌려요</div>
<a class="row" href="#s2"><span class="t">09:40</span><span class="w"><b>1교시 · MVP 알기, 조사 고르기, 조사 설계서</b><small>남는 것: mvp.md</small></span></a>
<a class="row" href="#s3"><span class="t">10:15</span><span class="w"><b>2교시 · 첫 조사를 돌려 표로 받기, 광고는 내가 본 것 붙이기</b><small>남는 것: research.csv</small></span></a>
<div class="grp">② 화면 만들기 · 표를 한눈에 보는 화면으로 만들고 다듬어요</div>
<a class="row" href="#s4"><span class="t">11:00</span><span class="w"><b>3교시 · 보는 화면 만들기</b><small>남는 것: mvp.html</small></span></a>
<a class="row" href="#s5"><span class="t">12:00</span><span class="w"><b>4교시 · 5초 안에 알아보게 다듬기</b><small>남는 것: 다듬은 mvp.html</small></span></a>
<div class="row rest"><span class="t">13:00</span><span class="w">점심</span></div>
<div class="grp">③ 심화와 마무리 · 메뉴에서 골라 더 똑똑하게 만들고, 다 같이 정리해요</div>
<a class="row" href="#s6"><span class="t">14:00</span><span class="w"><b>오후 · 심화 메뉴에서 하나 이상</b><small>바뀐 곳 표시, 대응안 한 장, 조사 넓히기, 짝꿍 테스트, 한 줄로 다시 돌리기</small></span></a>
<a class="row" href="#s7"><span class="t">17:00</span><span class="w"><b>마무리 · 조 공유, 포트폴리오 한 장, 링크</b><small>남는 것: portfolio_1116.md, 남이 열 수 있는 링크</small></span></a>
</div>
<p class="sub">줄을 누르면 그 구간으로 가요. <b>꼭 하는 것</b>은 오전의 P0 → W1 → P1 → P2 → (광고 소재면 P2-1) → P3 → P4, 오후 메뉴 하나 이상, 마무리의 W2예요. 이것만 끝내도 오늘은 통과예요.</p>

<h3 class="gap">내 에이전트는 이렇게 돌아가요</h3>
'''+FIG+'''
<h3 class="gap">고를 수 있는 조사 일곱 가지</h3>
<p class="sub">현업 신입이 매일 하는 조사예요. 1교시에 이 가운데 하나를 골라요. 하고 싶은 일과 가장 가까운 것을 고르거나, 고치고 싶은 조사를 직접 적어도 돼요.</p>
<div class="pairs">
<div class="row"><span class="k">광고 소재 리서치</span><span class="w"><b>콘텐츠·퍼포먼스 마케터</b><small>경쟁 브랜드 광고의 훅, 약속, 형식</small></span></div>
<div class="row"><span class="k">경쟁사 가격 조사</span><span class="w"><b>MD<span class="ab">(Merchandiser)</span>·온라인 영업</b><small>판매가, 할인율, 100g(ml)당 가격</small></span></div>
<div class="row"><span class="k">증정품·프로모션 조사</span><span class="w"><b>MD·온라인 영업</b><small>사은품, 1+1, 쿠폰, 기획전</small></span></div>
<div class="row"><span class="k">상세페이지 조사</span><span class="w"><b>MD·콘텐츠 마케터·CX<span class="ab">(Customer Experience)</span></b><small>첫 화면 문구, 근거, 후기, 구매 유도</small></span></div>
<div class="row"><span class="k">팝업스토어 리서치</span><span class="w"><b>브랜드·공간 마케터</b><small>장소, 기간, 콘셉트, 체험, 굿즈</small></span></div>
<div class="row"><span class="k">교육 프로그램 리서치</span><span class="w"><b>교육 회사 운영·기획</b><small>커리큘럼, 강사진, 운영 방식</small></span></div>
<div class="row"><span class="k">경쟁 서비스 기능 조사</span><span class="w"><b>서비스 기획·개발·데이터(테크 트랙)</b><small>정기 배송, 리뷰 필터, 장바구니 쿠폰 같은 기능</small></span></div>
</div>
<p class="sub">수업 예시는 라라스윗의 <b>경쟁사 가격·프로모션 조사</b>예요. 강사님이 이걸로 시연해요.</p>
<!--GALLERY-->

<h3 class="gap">오늘 수업, 이렇게 보면 돼요</h3>
<p class="sub">과정 중반에 자주 나오는 궁금증 다섯 가지예요. 궁금한 줄만 눌러 봐요.</p>
<details><summary>오늘은 매일 하던 조사를 AI로 줄이는 MVP를 만들어요</summary><div class="body">
<p>회사에 들어가면 신입이 가장 먼저 맡는 일 가운데 하나가 <b>매일 하는 조사</b>예요. 경쟁사 광고, 가격, 증정품, 상세페이지를 하나씩 열어 캡처하고 표에 옮겨요. 오늘은 이 일을 AI 에이전트에게 맡기는 가장 작은 첫 버전을 만들어요.</p>
<ul>
<li>마케터라면 광고 소재 리서치, MD·온라인 영업이라면 가격·증정품·상세페이지 조사, 교육 회사라면 교육 프로그램 리서치, 테크 트랙이라면 경쟁 서비스 기능 조사가 오늘의 MVP가 돼요.</li>
<li>1교시의 강사님 이야기를 들어 봐요. 손으로 하던 이 일이 광고 리서치 에이전트(스니핏)로 5분의 1 정도로 줄었어요. 오늘은 그 첫 버전을 직접 만들어 봐요.</li>
<li>준비 구간의 <b>W1</b>으로 가고 싶은 일의 채용 공고에 이런 조사와 자동화가 정말 적혀 있는지 직접 확인할 수 있어요.</li>
</ul></div></details>
<details><summary>하고 싶은 일을 아직 정하지 않았어도 괜찮아요</summary><div class="body">
<p>해 보기 전에는 알기 어려워요. 오늘 하루에 <b>서로 다른 일 다섯 가지</b>를 해 봐요. 조사 설계하기, 웹에서 조사하기, 표로 정리하기, 화면 만들기, 다듬기. 마케팅, MD, 운영 쪽 직무는 이 일들을 다르게 섞은 거예요.</p>
<ul>
<li>조사할 것을 정하지 못하면 칸을 비워 두세요. 하고 싶은 일에 맞춰 Claude가 골라요. 하고 싶은 일도 비워 두면 수업 예시(경쟁사 가격·프로모션 조사)로 해요.</li>
<li>저녁에 한 줄만 적어요. 어느 단계에서 시간 가는 줄 몰랐는지. 없었다면 가장 덜 지루했던 단계를 적어요. 그 한 줄이 진로를 정할 때 쓰는 내 자료가 돼요.</li>
</ul></div></details>
<details><summary>오늘은 매일 쓸 수 있는 조사 도구의 첫 버전과 포트폴리오 한 장이 남아요</summary><div class="body">
<p>이런 장을 모아 12월 4일에 포트폴리오 사이트를 만들고, 1월 6일에는 대표 결과물 하나와 내가 내린 결정을 한 사람씩 발표해요.</p>
<ul>
<li><b>오늘 저녁</b> · 조사 설계서, 조사 표, 한눈에 보는 화면, 그리고 내가 무엇을 확인하고 고르고 고쳤는지 적은 포트폴리오 한 장</li>
<li><b>수요일</b> · 피칭 데이(5분 발표와 라이브 데모)를 해 본 경험</li>
<li><b>12월 4일</b> · 내 결과물을 모은 포트폴리오 사이트, 개인 데모 5분, 내 스킬 파일 묶음</li>
<li><b>12월 18일</b> · 새 주제로 한 팀 프로젝트의 최종 발표</li>
<li><b>1월 6일</b> · 한 사람씩 발표해요. 내 대표 결과물, 내가 맡은 역할, 내가 내린 결정, 검증한 결과</li>
</ul>
<p>12월과 1월의 내용은 공식 일정표에 적힌 것이에요. 면접에서 "반복 업무를 이렇게 줄여 봤어요"라고 화면을 보여 주며 말할 수 있어요.</p></div></details>
<details><summary>이 과정은 창업의 순서를 빌린 실무 연습이에요</summary><div class="body">
<p>지역 자산 조사 → 페인포인트 → 비즈니스 모델 → 시장 검증 → 만들기 → 피칭. 지금까지 밟아 온 순서가 창업 교육과 닮아서 창업 과정처럼 보일 수 있어요. 회사가 새 상품이나 캠페인을 내놓을 때도 같은 순서를 밟아요. 그 순서를 <b>연습 재료</b>로 빌려 쓰는 거예요.</p>
<p>요리 학교에서 코스 요리를 처음부터 끝까지 한 번 내 보는 것과 같아요. 주방의 모든 자리에 서 봐야 내 자리가 어디인지 알 수 있어요.</p>
<ul>
<li>사업자 등록이나 서비스 출시는 공식 일정표에 없어요. 오늘 만드는 MVP도 가고 싶은 회사에서 신입이 맡을 조사 업무를 줄이는 첫 버전이에요.</li>
<li>지금 하는 주제는 수요일 피칭으로 한 바퀴가 끝나요. 12월 7일부터는 <b>새 주제</b>로 같은 순서를 한 번 더 돌아요. 그러니까 남는 것은 주제가 아니라 <b>방법과 도구, 그리고 결과물</b>이에요.</li>
<li>마지막 날(1월 7일)에는 취업, 창업, 더 배우기 가운데 <b>내</b> 목표를 정해요.</li>
</ul></div></details>
<details><summary>초안은 Claude가 만들고, 결정은 내가 해요</summary><div class="body">
<p>Claude는 초안을 빨리 만들어요. <b>맞는지, 좋은지는 사람이 정해요.</b> 오늘 내가 내리는 결정은 네 가지예요.</p>
<ul>
<li>무엇을 조사할지, 어느 경쟁사를 볼지 <b>고르기</b></li>
<li>표의 출처 링크를 열어 값이 맞는지 <b>확인하기</b></li>
<li>화면에서 <b>꼭 볼 것</b> 하나 정하기</li>
<li>오후에 어떤 심화를 할지, 무엇을 고칠지 <b>정하기</b></li>
</ul>
<p>가이드에서 <b>"내 결정"</b>이라고 적힌 곳이 그 자리예요.</p></div></details>
<h3 class="gap">용어</h3>
<details><summary>오늘 처음 나오는 말</summary><div class="body">
<ul><li><b>MVP</b> · 가장 작게 만들어서, 진짜 쓸 사람에게 먼저 써 보게 하는 첫 버전이에요. 1교시에 자세히 설명해요.</li><li><b>MD<span class="ab">(Merchandiser)</span></b> · 팔 상품을 고르고 가격, 구성, 기획전을 정하는 사람이에요.</li><li><b>CX<span class="ab">(Customer Experience)</span></b> · 고객 경험이에요. CX 기획자는 고객이 겪는 불편을 찾아 서비스를 고쳐요.</li><li><b>훅</b> · 광고 첫머리에서 눈길을 잡는 한 문장이나 장면이에요.</li><li><b>2534</b> · 25~34세를 줄여 부르는 말이에요.</li><li><b>AI 에이전트</b> · 시킨 일을 스스로 여러 단계로 해내는 AI예요. 오늘은 내 폴더의 Claude Code가 웹에서 찾고, 표로 정리하고, 화면을 만들어요.</li><li><b>조사 설계서(mvp.md)</b> · 무엇을, 어느 경쟁사에서, 어떤 칸으로 조사할지 적은 한 장이에요.</li><li><b>조사 표(research.csv)</b> · 조사 결과를 칸에 맞춰 정리한 표예요. CSV는 엑셀로 열리는 표 파일이에요.</li><li><b>출처 링크</b> · 그 값을 어디서 찾았는지 눌러서 확인할 수 있는 주소예요.</li><li><b>"못 찾음"</b> · Claude가 웹에서 찾지 못한 칸이에요. 지어내지 않고 비워 둔 거라 실패가 아니에요.</li><li><b>보는 화면(mvp.html)</b> · 표를 한눈에 보게 만든 화면이에요. 회사에서는 대시보드라고도 불러요.</li><li><b>첫 화면</b> · 화면을 열었을 때 스크롤하지 않고 맨 처음 보이는 부분이에요.</li><li><b>5초 테스트</b> · 처음 보는 사람에게 첫 화면을 5초 보여 주고 "무엇을 하는 화면인지" 말하게 하는 확인 방법이에요.</li><li><b>스킬</b> · 폴더에 넣어 두는 일 순서표예요. 만들어 두면 한 줄로 같은 일을 다시 시킬 수 있어요.</li><li><b>대응안</b> · 조사 결과를 보고 우리 회사가 할 일을 적은 한 장이에요.</li><li><b>랜딩페이지와 키비주얼</b> · 광고를 누른 사람이 처음 도착하는 웹페이지와, 그 캠페인의 대표 이미지예요. 오후 심화에서 마케터가 고를 수 있어요.</li><li><b>(가정)과 [채울 곳]</b> · (가정)은 Claude가 추측한 곳이라 내가 확인해요. [채울 곳]은 Claude가 지어내면 안 돼서 비워 둔 곳이에요.</li></ul></div></details>
</section>

<section id="s1">
<span class="eyebrow">시작 · 09:25–09:40 · 준비</span>
<h2>규칙을 심고, 내 일을 적어요</h2>
<p class="why"><b>왜 해요?</b> 오늘 하는 조사와 자동화가 채용 공고에 정말 나오는지 직접 확인해요.</p>
<div class="grid">
<div class="card red"><h3>금요일 가이드의 프롬프트</h3><p>"자료가 없으면 쓰지 마. 모르면 나에게 물어봐."</p><p class="sub">가이드가 이렇게 시켜서 Claude가 멈추고, 되묻고, 아무것도 만들지 않았어요. 여러분이 잘못한 게 아니에요.</p></div>
<div class="card ok"><h3>오늘 가이드의 프롬프트</h3><p>"아는 만큼 먼저 만들어. 추측한 곳만 표시해."</p><p class="sub">초안이 먼저 나와요. 맞는지는 그다음에 사람이 봐요.</p></div>
</div>
<div class="card soft"><p><b>신입에게 일을 맡길 때와 같아요.</b> "모르면 물어봐"라고 하면 하루 종일 물어요. "초안부터 가져와, 자신 없는 곳만 표시해"라고 하면 일이 굴러가요. 순서만 바뀌었어요. 판단은 오늘도 여러분이 해요.</p></div>
<div class="card checks">
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="a1"><span>Claude Code에서 작업 폴더를 열고 <b>새 대화</b>를 시작했어요 (하던 폴더 그대로 좋아요)</span></label>
<label class="check"><input type="checkbox" data-k="a2"><span>아래 입력 칸에 <b>내가 하고 싶은 일</b>을 적었어요 (모르면 비워 둬요). 회사를 바꿨으면 회사, 제품, 고객 세 칸을 모두 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="a3"><span><b>P0</b>을 실행했어요</span></label>
</div>
<div class="card"><h3>프롬프트 쓰는 법</h3>
<ol><li>박스를 누르면 복사돼요. Claude Code 입력창에 붙여 넣고 보내요.</li><li>프롬프트 하나는 보통 30초에서 1분 걸려요. 웹을 찾아보는 W1, P2와 오후의 P5, P8, "오늘 조사 돌려줘"는 1~2분 걸려요. 멈춘 게 아니에요. 다만 1분이 지나도 그대로면 Claude 창에 허락 창이 떠 있는지 봐요.</li><li>mvp.html 같은 화면 파일은 답에 나온 파일 이름을 누르면 옆 창에 열려요. 글 파일(.md)이나 표(.csv)를 보고 싶으면 리모컨 <b>"파일 내용 보기"</b>를 보내요. 리모컨은 준비 구간 맨 아래에 있는 짧은 상자예요. 위 메뉴의 "리모컨"을 누르면 바로 가요.</li><li>Claude의 답 끝에 "다음에 할 일"이 나와도, 이 가이드의 다음 박스를 따라가요.</li><li>P는 오늘 만드는 순서대로 붙인 번호(P0~P10)이고, W는 내 일과 잇는 프롬프트(아침 W1 채용 공고, 저녁 W2 포트폴리오)예요. 번호가 붙은 프롬프트는 전부 실제로 돌려 보고 넣었어요. 붙이면 Claude가 되묻지 않고 끝까지 만들어요.</li></ol></div>
<div class="card warn"><h3>허락 창이 뜨면</h3>
<p>"실행해도 될까요?"라는 창은 되묻는 게 아니에요. <b>방금 보낸 프롬프트가 시킨 일이면 Yes</b>를 눌러요. 파일 만들기와 고치기, 웹 검색, 웹페이지 열기(Fetch), 폴더 만들기와 열기, 브라우저 열기, 파일 복사, 링크 만들기(아티팩트 발행)가 그래요. curl, mkdir, open, python 같은 영어 명령으로 보여도 괜찮아요. P2가 표(research.csv)를 저장할 때 python 명령 창이 자주 떠요. P0이 금요일 규칙 줄을 지우는 수정 창(지워지는 줄이 빨갛게 보여요)도 Yes예요.</p><p>파일이나 폴더를 통째로 지우겠다고 하거나(rm, delete), 시키지 않은 일을 하겠다고 하면 누르지 말고 강사를 불러요. python, curl 같은 명령에는 "다시 묻지 않기"를 고르지 말고 그때그때 Yes를 눌러요.</p></div>
<div class="card" id="profileCard">
<h3>내 일과 회사를 적어요</h3>
<p class="sub">여기 적은 것이 프롬프트의 <b class="tok">파란 글자</b>로 들어가요. 모르면 비워 두세요. 비워 두면 칸 안에 흐리게 보이는 처음 값이 들어가요. 정하는 데 1분이 넘으면 비워 두고 넘어가요.</p>
<div class="field"><label for="v-role">내가 하고 싶은 일. 예: 콘텐츠 마케터, MD, 온라인 영업, 운영 매니저(교육 회사), CX 기획자, 서비스 기획자, 데이터 분석가</label><input id="v-role" data-in="role" type="text" maxlength="40" placeholder="비워 두면: 아직 모름" autocomplete="off"></div>
<p class="sub">회사는 해 오던 과제나 가고 싶은 회사가 있으면 그걸로 적어요. 비워 두면 수업 연습용 회사(라라스윗)로 해요. 하고 싶은 일이나 조사할 것이 그 회사에 없는 일이면 Claude가 비슷한 가상의 회사로 바꾸고 한 줄로 알려요. <b>회사를 바꾸면 제품과 고객 칸도 꼭 바꿔요.</b> 비워 두면 라라스윗의 제품(저당 아이스크림)과 고객이 그대로 들어가요.</p>
<div class="field"><label for="v-brand">회사(브랜드) 이름</label><input id="v-brand" data-in="brand" type="text" maxlength="40" placeholder="비워 두면: 라라스윗" autocomplete="off"></div>
<div class="field"><label for="v-product">제품·서비스 한 줄</label><input id="v-product" data-in="product" type="text" maxlength="60" placeholder="비워 두면: 저당 아이스크림" autocomplete="off"></div>
<div class="field"><label for="v-customer">그 회사의 고객 한 줄</label><input id="v-customer" data-in="customer" type="text" maxlength="90" placeholder="비워 두면: 다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인" autocomplete="off"></div>
<button class="ghost" id="resetProfile" type="button">처음 값으로 되돌리기</button>
</div>
<div class="card soft"><p><b>CLAUDE.md는 폴더에 붙여 두는 규칙 파일이에요.</b> 맨 앞 그림 "내 에이전트는 이렇게 돌아가요"의 CLAUDE.md가 이 파일이에요. Claude가 이 폴더에서 일할 때마다 먼저 읽어요. 금요일 프롬프트가 이 파일에 "멈추고 묻기"를 적어 넣은 폴더에서는 오늘도 Claude가 멈춰요. P0이 그 줄을 지우고 오늘 규칙과 내 일, 회사를 넣어요. 낮에 하고 싶은 일이나 회사를 바꾸면 P0을 한 번 더 보내요.</p></div>
'''+box('p00','P0 · 오늘의 작업 규칙과 내 일 심기 (꼭)',PR['p00'])+'''
<h3 class="gap">먼저 확인 · 오늘 하는 일이 채용 공고에 정말 나오는지 봐요</h3>
<p class="sub">오늘 하는 일 여섯 가지(경쟁사 조사, 표 정리, 한눈에 보는 화면, 자동화, AI 도구, 개선안)가 내가 가고 싶은 일의 채용 공고에 적혀 있는지 Claude가 찾아 줘요. 위에 적은 "내가 하고 싶은 일"이 그대로 들어가요. 1~2분 걸려요.</p>
'''+box('w1','W1 · 채용 공고에서 오늘 하는 일 찾기 (꼭)',PR['w1'])+'''
<div class="card soft"><p><b>(가정)</b>이라고 표시된 문장은 Claude가 공고 원문을 열어 보지 못한 문장이에요. 그래서 한 곳은 내 눈으로 확인해요. 공고가 마감되어 안 열리면 다른 곳을 눌러요. 표의 회사는 Claude가 웹에서 찾은 예시예요. 추천이나 채용 연결이 아니에요.</p></div>
<div class="card checks">
<h3>W1이 끝나면</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="w1"><span>표의 링크 <b>한 곳</b>을 눌러, 표의 문장과 비슷한 말이 있는지 내 눈으로 봤어요. 있으면 "○○ 공고는 내가 확인했어. 맞아.", 없으면 "○○ 공고에는 그 말이 없어. 다른 공고로 바꿔줘."라고 Claude에게 말해요</span></label>
<label class="check"><input type="checkbox" data-k="w2"><span>실습시트에 한 문장을 적었어요: <b>"오늘 만드는 것은 나에게 ○○이다."</b> 모르겠으면 "아직 모르겠다"라고 적어도 돼요</span></label>
<p class="sub" style="margin-top:12px">09:40이 되면 덜 끝났어도 1교시를 같이 시작해요. 링크 확인과 한 문장은 점심(13:00) 전까지 하면 돼요.</p>
</div>
<h3 class="gap" id="remote">리모컨 여섯 개 · 필요할 때만 꺼내 써요</h3>
<p class="sub"><b>지금 보내는 상자가 아니에요.</b> 하루 중에 Claude가 마음에 안 들게 움직이면 긴 설명 대신 이 짧은 상자를 보내요.</p>
'''+box('r1','되물을 때',R['r1'])+'\n'+box('r2','말이 길 때',R['r2'])+'\n'+box('r3','자료가 없다고 멈췄을 때',R['r3'])+'\n'+box('r4','한 단계 더 깊게',R['r4'])+'\n'+box('r6','파일 내용 보기',R['r6'])+'\n'+box('r7','광고 규정 점검 (오후에 랜딩페이지를 만들었을 때)',R['r7'])+'''
</section>

<section id="s2">
<span class="eyebrow">① 정하고 조사 · 09:40–10:15 · 1교시</span>
<h2>MVP가 무엇인지 알고, 매일 하던 조사 하나를 골라요</h2>
<p class="why"><b>왜 해요?</b> 현업 신입은 같은 조사를 매일 손으로 해요. 이 일을 AI 에이전트에게 맡기는 가장 작은 첫 버전을 만들면, 나도 팀도 매일 시간을 아껴요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px" id="mvp"><h3>MVP가 뭐예요?</h3>
<p><b>MVP는 Minimum Viable Product의 줄임말이에요.</b> 우리말로는 "최소 기능 제품"이라고 해요. 처음 들으면 낯선 게 당연해요. 현업에서는 직무를 가리지 않고 자주 쓰는 말이라, 오늘 정확히 알고 가요.</p>
<p><b>뜻</b> · 가장 작게 만들어서, 진짜 쓸 사람에게 먼저 써 보게 하는 첫 버전이에요. 목적은 완성이 아니라 확인이에요. "이렇게 바꾸면 정말 나아질까?"를 적은 시간과 돈으로 먼저 알아봐요.</p>
<p><b>쉽게 말하면</b> · 시식 코너예요. 가게를 다 짓기 전에 한 입만 내놓고 반응을 봐요.</p>
<div class="grid" style="margin-top:12px">
<div class="card red"><h3>MVP가 아니에요</h3><ul><li>모든 기능을 갖춘 완성본. 만드는 데 너무 오래 걸려요</li><li>써 볼 수 없는 반쪽짜리. 써 볼 수 없으면 확인도 못 해요</li><li>기획서만 있는 것. 사람이 직접 써 볼 수 없어요</li></ul></div>
<div class="card ok"><h3>MVP예요</h3><ul><li>진짜 쓸 사람이 바로 써 볼 수 있는 가장 작은 것</li><li>하루나 이틀이면 만들 수 있는 것</li><li>써 본 결과를 숫자로 확인할 수 있는 것</li></ul></div>
</div></div>
<div class="story"><span class="tag">현업 이야기 · 강사님</span>
<p>강사님은 500곳이 넘는 회사를 컨설팅하면서 <b>모든 일을 벤치마킹으로 시작했어요.</b> 다이어트 곤약 젤리를 팔 때도, 화장품 회사에서 새 브랜드를 낼 때도요. 실제로 경쟁사의 구매 후기와 상세페이지의 스토리텔링 구성을 보고 반영했을 때 구매 전환율이 상당히 올랐어요.</p>
<div class="grid">
<div class="card"><h3>예전 · 손으로</h3><ul><li>경쟁사 홈페이지를 하나씩 찾아요</li><li>랜딩페이지와 상세페이지를 캡처해 저장해요</li><li>매일 새로 올라오는 광고를 캡처해 엑셀에 옮겨 적고 구글 드라이브에 올려요</li></ul><p class="sub">인턴과 신입이 하루 3~5시간씩 하던 일이에요. 강사님도 10년 차가 될 때까지 했어요.</p></div>
<div class="card"><h3>지금 · 에이전트로</h3><ul><li>광고를 찾고 저장하는 AI 에이전트(스니핏)를 써요</li></ul><p class="sub">강사님은 이 일에 드는 시간이 5분의 1 정도로 줄었어요.</p></div>
</div></div>
<div class="card"><h3>오늘 만드는 MVP는 "조사 도우미"예요</h3>
<p>손으로 하던 조사를 에이전트가 웹에서 찾아 표로 정리하고, 한 화면에서 보여 주는 도구예요. 스니핏처럼 다 갖춘 서비스는 아니에요. 그 <b>첫 버전</b>이에요.</p>
<ol class="steps"><li><b>매일 하던 조사 하나 고르기</b> <small>1교시</small></li><li><b>조사 설계서 쓰기</b> · 무엇을, 어느 경쟁사에서, 어떤 칸으로 <small>1교시 · P1</small></li><li><b>첫 조사를 돌려 표로 받기</b> · 출처 링크를 붙여서. 광고 소재는 내가 본 광고까지 <small>2교시 · P2, P2-1</small></li><li><b>한눈에 보는 화면 만들기</b> <small>3교시 · P3</small></li><li><b>5초 안에 알아보게 다듬기</b> <small>4교시 · P4</small></li><li><b>더 똑똑하게 만들기</b> · 바뀐 곳 표시, 대응안, 한 줄로 다시 돌리기 <small>오후 · P5~P10</small></li></ol></div>
<span class="pill">따라 하기</span>
<div class="card soft" style="margin-top:12px"><p><b>내 결정 1 · 조사할 것 고르기.</b> 아래 카드에서 하나를 골라 "이걸로 할게요"를 누르면 조사할 것 칸에 들어가요. 카드에 없는 조사를 하고 싶으면 칸에 직접 적어요. 테크 트랙이라면 "경쟁 서비스 기능 조사" 카드를 고르거나, 가격 조사를 골라 오후 E로 날마다 쌓이는 수집 표를 만들어도 돼요. 모르면 비워 두세요. 하고 싶은 일에 맞춰 Claude가 골라요. 하고 싶은 일도 비워 두면 수업 예시(경쟁사 가격·프로모션 조사)로 해요.</p></div>
<div class="card"><h3>조사 일곱 가지 · 하나를 골라요</h3><p class="sub">손으로 하던 일을 에이전트가 대신 찾아 표로 정리해요.</p>
<div class="roles">
'''+PICK_CARDS+'''
</div></div>
'''+field('pick','조사할 것 (위 카드를 누르거나 직접 적어요. 모르면 비워 둬요)','비워 두면: 네가 정해줘')+'\n'+field('rivals','볼 경쟁사 (아는 곳이 있으면 적어요. 예: ○○, △△, □□. 모르면 비워 둬요)','비워 두면: 네가 정해줘')+'\n'+box('p01','P1 · 조사 설계서 한 장 (꼭)',PR['p01'])+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="b1"><span>답에 <b>조사할 것, 경쟁사 3곳, 표에 적을 칸</b>이 보여요</span></label>
<label class="check"><input type="checkbox" data-k="b2"><span>칸과 경쟁사를 봤어요. 바꿀 것이 있으면 "○○ 칸도 넣어줘", "경쟁사 △△ 대신 □□로 바꿔줘"라고 한 줄 말했어요. 다 맞으면 "그대로 갈게. 이유는 ○○."라고 말했어요</span></label>
<label class="check"><input type="checkbox" data-k="b3"><span>mvp.md의 "손으로 하면 하루 몇 분"이 내 생각과 다르면 "손으로 하면 하루 ○분 걸려. mvp.md를 고쳐줘."라고 말했어요. 모르면 그대로 둬요</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 손으로 이 조사를 하면 하루에 얼마나 걸릴지 실습시트에 적어 둬요. 오후에 에이전트로 걸린 시간과 비교해요.</p></div>
</section>

<section id="s3">
<span class="eyebrow">① 정하고 조사 · 10:15–11:00 · 2교시</span>
<h2>첫 조사를 돌려 표로 받아요</h2>
<p class="why"><b>왜 해요?</b> 손으로 하면 몇 시간 걸리던 조사를 에이전트가 몇 분 만에 해요. 대신 틀린 값이 섞일 수 있어서, 출처를 열어 확인하는 것까지가 일이에요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>웹에서 찾을 수 있는 것과 없는 것</h3>
<ul><li><b>잘 찾아요</b> · 공식몰과 브랜드 홈페이지, 뉴스와 보도자료 같은 공개 자료</li><li><b>못 찾을 수 있어요</b> · 로그인해야 보이는 값, 자동 접속을 막는 쇼핑몰(쿠팡, 네이버 쇼핑 같은 곳)의 실시간 가격, 순위, 쿠폰. 메타 광고 라이브러리 같은 광고 모음도 사람이 열면 보이지만 Claude는 못 열 때가 많아요</li><li>못 찾은 칸은 <b>"못 찾음"</b>으로 남아요. 지어내지 않고 비워 둔 거라 실패가 아니에요. 수업 전 시험에서는 표 칸의 20~60%가 "못 찾음"이었고, 광고 소재 조사는 절반 안팎이었어요.</li><li><b>꼭 필요한 값을 못 찾았으면 내가 본 것을 붙여요.</b> 광고 소재를 골랐다면 아래 P2-1이 꼭 하는 단계예요. 가격이나 쿠폰도 같은 방법으로 붙일 수 있어요. 칸이나 경쟁사를 바꾸는 건 그다음이에요.</li></ul></div>
<span class="pill">따라 하기</span>
<p class="sub" style="margin-top:12px"><b>보내기 전에 시계를 봐요.</b> 끝나면 걸린 시간을 실습시트에 적어요. 오후에 손으로 하던 시간과 비교해요.</p>
'''+box('p02','P2 · 첫 조사를 돌려 표로 받기 (꼭)',PR['p02'],TOP)+'''
<h3 class="gap">광고 소재를 골랐다면 꼭 · 내가 본 광고 붙여 넣기</h3>
<div class="card"><p class="sub">광고는 Claude가 웹에서 가장 못 찾는 조사예요. P2가 도는 동안 내가 직접 찾아서 붙여요.</p><ol><li>브라우저에서 <b>메타 광고 라이브러리</b>(facebook.com/ads/library)를 열어요. 로그인하지 않아도 돼요.</li><li>국가는 <b>대한민국</b>, 광고 카테고리는 <b>모든 광고</b>로 두고, 검색창에 경쟁사 이름을 쳐요.</li><li>광고 2~3개를 골라 첫 문장, 약속하는 말, 형식(이미지·영상), 시작일을 복사해 아래 칸에 붙여요. 광고마다 번호를 붙이고, 광고 링크가 있으면 같이 붙여요.</li><li>P2-1을 보내요.</li></ol><p class="sub">다른 조사를 골랐어도 꼭 필요한 값(가격, 쿠폰)을 못 찾았으면 몰에서 본 것을 같은 칸에 붙여 P2-1을 보내도 돼요.</p></div>
'''+fieldwide('ads','내가 본 광고 (광고마다 번호를 붙여 이어 붙여요). 예: 1) ○○ · 첫 문장 "…" · 영상 · 11/10 시작 · 광고 링크','비워 두면: 적지 않음')+'\n'+box('p02b','P2-1 · 내가 본 광고 붙여 넣기 (광고 소재면 꼭)',PR['p02b'])+'''
<div class="card soft"><p><b>내 결정 2 · 확인하기.</b> 표에서 가장 중요한 줄(예: 가장 싼 곳, 가장 큰 혜택)의 출처 링크를 열어 값이 맞는지 내 눈으로 봐요. 맞으면 "○○ 값은 내가 확인했어. 맞아.", 다르면 "○○의 가격은 실제로 ○○원이야. research.csv를 고쳐줘."라고 Claude에게 한 줄로 말해요. 광고라면 "○○ 광고의 첫 문장은 실제로 '…'야. research.csv를 고쳐줘."처럼 말해요. 말해 둬야 저녁에 포트폴리오에 남아요.</p></div>
<div class="card"><h3>표를 엑셀로 열어 보기</h3>
<ul><li>작업 폴더의 research.csv를 더블클릭하면 엑셀(맥은 넘버스)로 열려요. 폴더가 어디인지 모르겠으면 Claude에게 "이 폴더를 파일 탐색기(맥은 Finder)로 열어줘"라고 해요.</li><li>Claude 앱에서 보려면 리모컨 "파일 내용 보기"를 보내요.</li><li>엑셀에서는 보기만 해요. 고칠 값은 Claude에게 말해요. 엑셀에서 고쳐 저장하면 한글이나 칸 모양이 바뀔 수 있어요.</li></ul></div>
<div class="card checks">
<h3>이 세 가지(광고 소재는 네 가지)가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="c1"><span>research.csv가 생겼고, 줄마다 <b>조사일과 출처 링크</b>가 있어요</span></label>
<label class="check"><input type="checkbox" data-k="c2"><span>출처 링크 <b>한 곳</b>을 열어 값을 확인하고 Claude에게 말했어요 (내 결정 2)</span></label>
<label class="check"><input type="checkbox" data-k="c3"><span>"못 찾음"이 몇 칸인지 봤어요. 반이 넘으면 꼭 필요한 값은 P2-1로 내가 본 것을 붙이고, 나머지는 "못 찾은 칸을 찾기 쉬운 칸으로 바꿔서 다시 조사해줘. mvp.md의 칸도 같이 바꿔줘."라고 해요</span></label>
<label class="check"><input type="checkbox" data-k="c4"><span><b>광고 소재를 골랐다면</b> 메타 광고 라이브러리에서 본 광고 2~3개를 P2-1로 붙였어요</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> "research.csv의 칸마다 '못 찾음'이 몇 %인지 표로 보여줘"라고 보내요. 어느 칸을 바꾸거나 직접 채울지 숫자로 정할 수 있어요.</p></div>
</section>

<section id="s4">
<span class="eyebrow">② 화면 만들기 · 11:00–12:00 · 3교시</span>
<h2>표를 한눈에 보는 화면으로 만들어요</h2>
<p class="why"><b>왜 해요?</b> 표는 만든 사람만 읽어요. 한눈에 보는 화면이 있으면 팀장과 동료도 바로 알아봐요. 매일 아침 이 화면 하나만 열면 되게 만드는 것이 목표예요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>보는 화면의 세 부분</h3>
<ul><li><b>맨 위</b> · 이 화면이 해 주는 일 한 줄과 숫자 몇 개(조사일, 경쟁사 수, 못 찾은 칸 수)</li><li><b>가운데</b> · 경쟁사를 나란히 놓고 비교하는 표나 카드, 눌러서 열리는 출처 링크</li><li><b>걸러 보기</b> · 경쟁사나 칸으로 골라 보는 버튼</li></ul>
<p class="sub" style="margin-top:12px">회사에서는 이런 화면을 대시보드라고 불러요. 오늘은 파일 하나(mvp.html)로 만들어요.</p></div>
<span class="pill">따라 하기</span>
<div class="card soft" style="margin-top:12px"><p><b>내 결정 3 · 꼭 볼 것 정하기.</b> 이 화면에서 매일 가장 먼저 보고 싶은 것 하나를 아래 칸에 적어요. 예: "100g당 가장 싼 곳이 맨 위", "증정품이 있는 곳만", "이번 주에 새로 올라온 광고". 모르면 비워 두세요.</p></div>
'''+field('focus','화면에서 꼭 볼 것 (모르면 비워 둬요)','비워 두면: 네가 정해줘')+'\n'+box('p03','P3 · 한눈에 보는 화면 만들기 (꼭)',PR['p03'])+'''
<div class="card"><h3>만든 화면 보기</h3>
<ul><li>Claude의 답에 나온 <b>mvp.html</b> 파일 이름을 누르면 Claude 앱 안의 옆 창에 열려요. 고친 뒤에는 파일 이름을 다시 눌러요.</li><li>폰 크기로 보거나 새로고침을 하려면 아래 "브라우저로 열기"를 보내요. 그 브라우저 창을 폰만큼 좁히고, 고친 뒤에는 그 창에서 새로고침(윈도우 F5, 맥 ⌘R)을 해요.</li></ul></div>
'''+box('open','브라우저로 열기',OPEN)+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="d1"><span>mvp.html이 <b>화면에 열려요</b>. 표와 버튼이 안 보이고 비어 있으면 맨 아래 "막히면"의 "화면이 통째로 비어 있어요"를 봐요</span></label>
<label class="check"><input type="checkbox" data-k="d2"><span>출처 링크를 누르면 <b>그 페이지가 열려요</b></span></label>
<label class="check"><input type="checkbox" data-k="d3"><span>걸러 보기 버튼을 누르면 <b>보이는 것이 바뀌어요</b></span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> "우리 회사 줄을 research.csv에도 넣고, 화면에서 경쟁사와 나란히 비교해줘. 모르는 값은 [채울 곳]으로 둬."라고 한 줄 보내요.</p></div>
</section>

<section id="s5">
<span class="eyebrow">② 화면 만들기 · 12:00–13:00 · 4교시</span>
<h2>5초 안에 알아보게 다듬어요</h2>
<p class="why"><b>왜 해요?</b> 처음 보는 사람이 5초 안에 무엇을 하는 화면인지 모르면, 써 보지 않고 닫아요. 팀장이 아침에 열어 보는 화면도 마찬가지예요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>5초 테스트</h3>
<p>처음 보는 사람에게 첫 화면을 5초 보여 주고 "무엇을 하는 화면이에요?"라고 물어요. 바로 말하면 통과예요.</p>
<ul><li>맨 위에는 이 화면이 해 주는 일 한 줄과, <b>가장 중요한 숫자나 결과 하나</b>만 크게 둬요. 예: "오늘 가장 싼 곳", "새 증정품 2개", "새 광고 5개".</li><li>AI가 만든 화면은 서로 닮기 쉬워요. 고른 게 아니라 기본값이 나와서예요. 우리 회사의 색과 분위기를 알려 주면 달라져요.</li></ul></div>
<span class="pill">따라 하기</span>
'''+field('tone','우리 회사의 색이나 분위기를 알면 적어요 (모르면 비워 둬요). 예: 흰색과 하늘색, 깨끗하고 차분하게','비워 두면: 네가 정해줘')+'\n'+box('p04','P4 · 5초 안에 알아보게 다듬기 (꼭)',PR['p04'])+'\n'+box('cmp1','고치기 전과 뒤를 나란히 열기',CMP1)+'''
<div class="card checks">
<h3>이 두 가지가 보이면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="e1"><span>P4가 끝나면 옆 조 사람 한 명과 노트북을 바꿔 첫 화면을 5초씩 봤어요. 상대가 <b>무엇을 하는 화면인지</b> 말했어요 (같은 조 짝꿍은 오후에 처음 보게 아껴 둬요)</span></label>
<label class="check"><input type="checkbox" data-k="e2"><span>mvp_before.html(고치기 전)과 mvp.html(고친 뒤)을 번갈아 보고 <b>달라진 곳 2가지</b>를 말할 수 있어요</span></label>
</div>
</section>

<section id="s6">
<span class="eyebrow">③ 심화와 마무리 · 14:00–17:00 · 오후(각자)</span>
<h2>메뉴에서 골라 더 똑똑하게 만들어요</h2>
<p class="why"><b>왜 해요?</b> 오전에 만든 것은 한 번 돌린 조사예요. 현업에서 쓰려면 매일 돌고, 바뀐 것을 알려 주고, 결과로 다음 행동을 정해야 해요. 오후에는 그중 내가 고치고 싶은 것을 골라요. 하나만 해도 되고, 여러 개를 해도 돼요.</p>
<div class="grid">
<div class="card path"><h3>A · 바뀐 곳 표시</h3><p class="sub">다시 조사해서 앞 조사와 비교하고, 바뀐 가격·혜택·새 광고만 색으로 보여 줘요. 매일 하는 조사의 핵심이에요.</p><p class="sub"><b>끝나면</b> mvp.html에 "바뀐 곳" 칸이 생겨요. 같은 날이면 "바뀐 곳 없음"도 맞는 결과예요.</p><p><b>P5</b> · 1~2분</p></div>
<div class="card path"><h3>B · 우리 대응안 한 장</h3><p class="sub">조사 결과로 우리 회사가 내일 할 일을 정해요. 마케터는 광고 시안과 랜딩페이지·키비주얼까지 갈 수 있어요.</p><p class="sub"><b>끝나면</b> plan.md 한 장. 마케터는 landing.html과 이미지 프롬프트(kv.md)까지.</p><p><b>P6 → (마케터) P7</b></p></div>
<div class="card path"><h3>C · 조사 넓히기</h3><p class="sub">경쟁사나 칸을 늘리거나, 다른 조사 하나를 더 붙여요.</p><p class="sub"><b>끝나면</b> 표와 화면에 경쟁사나 칸이 늘어요. 다른 조사를 붙이면 화면에 탭이 하나 더 생겨요.</p><p><b>P8</b> · 1~2분</p></div>
<div class="card path"><h3>D · 짝꿍 테스트로 고치기</h3><p class="sub">짝꿍에게 1분 써 보게 하고 헷갈려한 곳 하나를 고쳐요.</p><p class="sub"><b>끝나면</b> mvp.md 맨 아래에 "써 본 결과"가 생기고, 화면이 한 곳 고쳐져요.</p><p><b>P9</b></p></div>
<div class="card path"><h3>E · 한 줄로 다시 돌리기</h3><p class="sub">오늘 한 조사를 스킬로 묶어, 내일부터 "오늘 조사 돌려줘" 한 줄이면 다시 돌게 해요.</p><p class="sub"><b>끝나면</b> 새 대화에서 "오늘 조사 돌려줘" 한 줄로 날짜가 붙은 표(research_날짜.csv)가 새로 생겨요.</p><p><b>P10</b></p></div>
</div>
<p class="sub">고르기 어려우면 <b>E → D</b> 순서를 추천해요. E로 한 줄이면 다시 도는 조사 도우미를 만들고, D로 짝꿍에게 써 보게 해서 한 곳을 고쳐요. E의 "오늘 조사 돌려줘"에는 바뀐 곳 표시가 들어 있어서, E를 했으면 A는 건너뛰어도 돼요.</p>

<h3 class="gap">A · 바뀐 곳 표시</h3>
'''+box('p05','P5 · 다시 조사해서 바뀐 곳 표시하기 (A)',PR['p05'])+'''
<p class="sub">조사한 지 얼마 안 됐으면 "바뀐 곳 없음"이 나올 수 있어요. 그것도 맞는 결과예요. 내일 아침에 다시 돌리면 바뀐 곳이 보여요.</p>

<h3 class="gap">B · 우리 대응안 한 장</h3>
'''+box('p06','P6 · 조사 결과로 우리 대응안 한 장 (B)',PR['p06'])+'''
<div class="story"><span class="tag">현업 이야기 · 강사님</span>
<p>광고 이미지를 눌렀는데 랜딩페이지에 <b>다른 제품이 나오거나 다른 기획전이 나오면</b>, 고객은 혼란스러워해요.</p></div>
<div class="card"><p><b>마케터라면 이어서 P7을 보내요.</b> 대응안으로 랜딩페이지 한 장과 이미지 프롬프트를 만들어요. 키비주얼에는 랜딩페이지 첫 화면이 말하는 장면을 그대로 그려요. 그래야 광고를 누르고 들어온 사람이 같은 것을 보고 헷갈리지 않아요.</p>
</div>
'''+box('p07','P7 · 랜딩페이지와 이미지 프롬프트 (B, 마케터)',PR['p07'])+'''
<div class="card"><h3>P7을 보낸 뒤</h3><ol><li>P7이 보여 준 이미지 프롬프트에서 장면 문장만 하나씩 복사해 <b>GPT 에듀</b>에서 이미지를 만들어 내려받아요. "큰 카피" 줄은 붙이지 않아요. 붙이면 이미지에 글자가 들어가요. 시간이 없으면 kv 한 장만 해도 돼요.</li><li>파일 이름을 <b>kv</b>로 바꾸고, 작업 폴더의 images 폴더에 넣어요. 폴더가 없으면 아래 "images 폴더 만들고 열기"를 보내요.</li><li>"이미지를 랜딩페이지에 넣기"를 보내요.</li></ol>
<p class="sub">이미지에는 글자를 넣지 않아요. AI가 그린 한글은 틀릴 때가 있어요. 식품, 화장품, 병원, 금융이면 리모컨 "광고 규정 점검"을 한 번 보내요.</p></div>
'''+box('fold','images 폴더 만들고 열기',FOLD)+'\n'+box('img','이미지를 랜딩페이지에 넣기',IMG)+'''

<h3 class="gap">C · 조사 넓히기</h3>
'''+field('more','무엇을 넓힐지 적어요 (비워 두면 경쟁사 2곳 더). 예: 칸 2개 더(배송비, 리뷰 수), 다른 조사(상세페이지)','비워 두면: 경쟁사 2곳 더')+'\n'+box('p08','P8 · 조사 넓히기 (C)',PR['p08'])+'''

<h3 class="gap">D · 짝꿍 테스트로 고치기</h3>
<div class="card"><p class="sub">짝꿍은 같은 조의 옆자리 사람이에요. 서로 한 번씩 해 줘요.</p><ol><li><b>5초 보기</b> · 짝꿍에게 mvp.html 첫 화면을 5초 보여 주고 "무엇을 하는 화면 같아요?"라고 물어요. 짝꿍이 한 말을 그대로 적어요. 짝꿍이 오전에 내 화면을 이미 봤으면 다른 조 사람과 해요.</li><li><b>1분 써 보기</b> · 찾을 것 하나를 줘요. 예: "가장 싼 곳을 찾아봐", "증정품이 있는 곳을 찾아봐". 생각이 안 나면 아래 "짝꿍에게 줄 할 일 만들기"를 보내요. 나는 설명하지 않고 보기만 하고, 걸린 시간을 휴대폰 타이머로 재요.</li><li><b>고칠 곳 하나</b> · 짝꿍이 멈춘 곳, 다시 물어본 곳 가운데 하나를 골라 아래 칸에 적고 P9를 보내요.</li></ol></div>
'''+box('task1','짝꿍에게 줄 할 일 만들기',TASK1)+'\n'+field('said','짝꿍이 5초 보고 말한 것. 예: 아이스크림 값 비교하는 화면 같아요','비워 두면: 적지 않음')+'\n'+field('sec','짝꿍이 찾는 데 걸린 시간. 예: 40초, 못 찾음','비워 두면: 적지 않음')+'\n'+field('fb','짝꿍이 헷갈려한 곳 하나와 고른 이유. 예: 걸러 보기 버튼을 못 찾았다. 가장 먼저 막혀서','비워 두면: 적지 않음')+'\n'+box('p09','P9 · 짝꿍이 써 본 결과로 한 곳 고치기 (D)',PR['p09'])+'\n'+box('cmp2','고치기 전과 뒤를 나란히 열기',CMP2)+'''

<h3 class="gap">E · 한 줄로 다시 돌리기</h3>
'''+box('p10','P10 · 오늘 한 조사를 스킬로 묶기 (E)',PR['p10'])+'''
<div class="card"><p><b>스킬이 되는지 확인해요.</b> Claude Code에서 <b>같은 작업 폴더</b>로 <b>새 대화</b>를 열고 아래 한 줄을 보내요. 새 대화는 오늘 한 일을 몰라도, 스킬과 mvp.md를 읽고 같은 조사를 다시 해요. 1~2분 걸려요.</p><p class="sub">확인이 끝나면 <b>아침에 쓰던 대화로 돌아가요.</b> 왼쪽 대화 목록에서 아침 대화를 눌러요. 다음 메뉴와 W2는 그 대화에서 해요. 스킬 파일은 작업 폴더의 .claude 폴더 안에 있어요. 맥 Finder에서는 ⌘⇧.(Command+Shift+마침표)를 눌러야 보여요.</p></div>
'''+box('run','스킬로 다시 돌리기 (새 대화에서)',RUN)+'''

<div class="card checks">
<h3>오후에 하나 이상 하면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="h1"><span>오후 메뉴에서 <b>하나 이상</b>을 끝냈어요. 무엇을 왜 골랐는지 실습시트에 한 줄 적었어요 (내 결정 4)</span></label>
<label class="check"><input type="checkbox" data-k="h2"><span>손으로 하면 걸렸을 시간과 오늘 에이전트로 걸린 시간을 실습시트에 나란히 적었어요</span></label>
</div>
<h3 class="gap">16:00부터 · 덜 끝난 것 끝내기</h3>
<div class="grid">
<div class="card"><h3>아직 덜 끝났다면</h3><p class="sub">오전의 꼭 하는 것(P0, W1, P1~P4, 광고 소재면 P2-1)부터 끝내요. 오후 메뉴는 하나만 해도 돼요. 17:00의 포트폴리오 한 장(W2)은 다 같이 해요.</p></div>
<div class="card"><h3>먼저 끝났다면</h3><p class="sub">다른 메뉴를 하나 더 하거나, 짝꿍의 조사 도우미를 써 보고 헷갈린 곳을 알려 줘요.</p></div>
</div>
</section>

<section id="s7">
<span class="eyebrow">③ 심화와 마무리 · 17:00–18:00 · 마무리(다 같이)</span>
<h2>보여 주고, 적고, 퇴근해요</h2>
<p class="why"><b>왜 해요?</b> 만든 것은 남이 볼 수 있어야 내 것이 돼요. 내가 내린 결정까지 적어 두면 면접에서 말할 수 있어요.</p>
<div class="card"><h3>조 공유 · 한 사람 1분</h3><ol>
<li>조 안에서 한 사람씩 화면을 띄워요.</li>
<li>한 문장으로 말해요: <b>어떤 조사를, 손으로는 얼마나 걸리던 것을, 에이전트로 어떻게 줄였나.</b></li>
<li>오후에 무엇을 더했는지 한 줄 말해요.</li>
<li>듣는 사람은 한마디만 해요. 첫 화면을 보고 바로 이해됐는지.</li>
</ol></div>
<div class="card"><h3>오늘을 포트폴리오 한 장으로 남겨요</h3>
<p>결과물만 남기면 절반이에요. <b>내가 무엇을 확인하고, 고르고, 고쳤는지</b>가 같이 남아야 면접에서 말할 수 있어요. 이 한 장은 12월 4일 포트폴리오 사이트에 넣을 재료예요.</p>
<p><b>W2는 아침부터 쓰던 폴더와 대화에서 보내요.</b> Claude가 못 본 결정(이미지를 다시 뽑은 것, 짝꿍 테스트에서 정한 것, 새 대화에서 한 것)은 W2를 붙여 넣은 뒤 보내기 전에 맨 아래에 한 줄씩 적어요. 실습시트에 적은 시간 두 개도 "손으로 하면 하루 ○분, 에이전트로 ○분"처럼 같이 적어요. 줄을 바꿀 때는 Shift+Enter를 눌러요. Enter만 누르면 바로 보내져요. 이미 보냈으면 덧붙임만 따로 보내고 "포트폴리오에 반영해줘"라고 해요.</p>
'''+box('w2','W2 · 오늘을 포트폴리오 한 장으로 (꼭)',PR['w2'])+'''
<div class="card soft" style="margin-top:12px"><p><b>[내가 적을 곳]은 말로 채워요.</b> Claude가 남은 자리를 보여 주면 한 줄씩 말해요. 예: "경쟁사를 이렇게 고른 이유는 ○○야. 포트폴리오에 적어줘." 면접에서 말할 세 문장부터 채워요.</p></div></div>
<div class="card"><h3>남이 열 수 있는 링크로 남겨요</h3>
<p>실습시트에 <b>내 컴퓨터 주소</b>(C:\\로 시작하는 경로, /Users/나 file://로 시작하는 주소, localhost)를 적으면 나만 열려요. 아래 한 줄을 보내 화면을 링크로 만들어요.</p>
'''+box('pub','화면을 링크로 만들기',PUB)+'''
<ol><li>허락 창이 뜨면 Yes를 눌러요. Claude가 링크를 알려 줘요.</li><li>링크를 열어요. 처음에는 나만 볼 수 있어요.</li><li>열린 화면의 <b>공유</b> 메뉴에서 <b>링크가 있는 사람은 누구나</b>로 바꿔요.</li><li>로그인하지 않은 창(시크릿 창)에서 링크를 열어 표가 보이는지 확인하고, 실습시트에 적어요.</li></ol>
<p class="sub">안 되면 mvp.html을 드라이브에 올리고 그 링크를 적어요. 드라이브 링크는 받은 사람이 파일을 내려받아 더블클릭해야 열려요. 링크로 내놓는 방법은 내일 다시 같이 해요.</p></div>
<div class="card checks">
<h3>내가 할 일 네 가지</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g2"><span>오늘 만든 화면의 <b>링크</b>를 실습시트에 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="g6"><span><b>portfolio_1116.md</b>의 [내가 적을 곳]을 Claude에게 말해서 채웠어요 (세 문장부터)</span></label>
<label class="check"><input type="checkbox" data-k="g3"><span>실습시트에 <b>회고 4줄</b>을 적었어요: 오늘 만든 것 / 막힌 곳 / 내일 고칠 것 / <b>가장 시간 가는 줄 몰랐던 단계</b>(없었으면 가장 덜 지루했던 단계)</span></label>
<label class="check"><input type="checkbox" data-k="g5"><span>오늘 만든 파일을 <b>하나도 지우지 않았어요</b> (폴더 안 파일 전부)</span></label>
</div>
<div class="card checks">
<h3>조장 체크</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g1"><span>조원 모두 <b>mvp.md, research.csv, mvp.html</b>이 있어요</span></label>
<label class="check"><input type="checkbox" data-k="g4"><span>도움이 필요한 조원이 있으면 같이 강사를 불렀어요</span></label>
</div>
<div class="card soft"><h3>내일과 모레</h3>
<ul><li><b>화요일</b> 사람에게 보여 주고 고치기, 15초 숏폼 티저(누가 무엇을 하는지는 강사님이 안내해요), 오후 4시부터 발표 자료 뼈대</li><li><b>수요일</b> 피칭 데이. 5분 발표, 라이브 데모, 3분 질문. 무엇을 어떻게 발표하는지는 강사님이 안내해요.</li></ul></div>
<div class="card blue"><div class="big">오늘 여러분은 매일 하던 일을<br>줄이는 도구의 첫 버전을 만들었어요.</div></div>
</section>

<section id="s8">
<span class="eyebrow">막히면</span>
<h2>긴 설명 대신 한 줄을 보내요</h2>
<details><summary>무엇을 조사할지 모르겠어요</summary><div class="body"><p>조사할 것 칸을 비워 두세요. 하고 싶은 일에 맞춰 Claude가 골라요. 하고 싶은 일도 모르면 수업 예시(경쟁사 가격·프로모션 조사)로 해요.</p></div></details>
<details><summary>"못 찾음"이 너무 많아요</summary><div class="body"><p>쇼핑몰이 자동 접속을 막거나 로그인해야 보이는 값일 수 있어요. 이 순서로 해 봐요.</p><ol><li>꼭 필요한 값은 2교시의 P2-1로 내가 본 것을 붙여요. 광고는 메타 광고 라이브러리(facebook.com/ads/library)에서, 가격이나 쿠폰은 몰에서 본 것을 복사해요.</li><li>덜 중요한 칸은 "못 찾은 칸을 찾기 쉬운 칸으로 바꿔서 다시 조사해줘. mvp.md의 칸도 같이 바꿔줘."라고 해요.</li><li>그래도 많으면 경쟁사를 공식몰이 있는 곳으로 바꾸고 "mvp.md도 같이 고쳐줘"라고 해요.</li></ol></div></details>
<details><summary>값이 틀린 것 같아요</summary><div class="body"><p>출처 링크를 열어 실제 값을 보고 "○○의 가격은 실제로 ○○원이야. research.csv와 화면을 고쳐줘."라고 해요. 이게 오늘의 "내 결정 2"예요.</p></div></details>
<details><summary>P2가 끝났는데 research.csv가 없어요</summary><div class="body"><p>Claude 창에 허락 창이 떠 있으면 Yes를 눌러요. 표를 저장하는 명령이 허락을 기다리고 있는 거예요. 창이 없으면 그대로 P3를 보내요. P3가 research.csv부터 만들고 화면을 만들어요. 수업 전 시험에서는 앞에서 조사한 값을 그대로 썼어요.</p></div></details>
<details><summary>엑셀에서 한글이 깨져요</summary><div class="body"><p>"research.csv를 엑셀에서 한글이 안 깨지게 UTF-8 BOM으로 다시 저장해줘"라고 해요.</p></div></details>
<details><summary>화면에 표가 안 보여요</summary><div class="body"><p>"research.csv의 내용을 mvp.html 안에 넣어서 파일을 더블클릭해도 보이게 해줘"라고 해요.</p></div></details>
<details><summary>화면이 통째로 비어 있어요, 버튼이 안 눌려요</summary><div class="body"><p>화면 파일의 스크립트에 오류가 있으면 표도 버튼도 안 보여요. "mvp.html을 열었더니 화면이 비어 있어. 표도 버튼도 안 보여. 스크립트 오류를 찾아 고쳐줘."라고 보내고, 끝나면 파일 이름을 다시 눌러 봐요. 수업 전 시험에서 이 한 줄로 고쳐졌어요.</p></div></details>
<details><summary>스킬을 불렀는데 같은 일을 안 해요</summary><div class="body"><p>새 대화에서 "daily-research 스킬로 오늘 조사 돌려줘"라고 스킬 이름을 넣어 다시 보내요. 그래도 안 되면 P10을 다시 보내요.</p></div></details>
<details><summary>W1이 찾은 공고 링크가 안 열려요</summary><div class="body"><p>마감된 공고일 수 있어요. 표의 다른 링크를 눌러요. 다 안 열리면 채용 사이트에서 표에 나온 직무 이름으로 직접 찾아 한 곳만 봐요.</p></div></details>
<details><summary>Claude가 자꾸 되물어요</summary><div class="body"><p>리모컨 <b>"되물을 때"</b>를 보내요. 그래도 물으면 새 대화를 열고 P0을 다시 실행해요.</p></div></details>
<details><summary>고쳤다는데 화면이 그대로예요</summary><div class="body"><p>옆 창으로 보고 있으면 파일 이름을 다시 눌러요. 브라우저로 보고 있으면 그 창에서 새로고침(윈도우 F5, 맥 ⌘R)을 해요.</p></div></details>
<details><summary>파일이 없다고 멈췄어요</summary><div class="body"><p>리모컨 <b>"자료가 없다고 멈췄을 때"</b>를 보내요. 앞 교시를 못 끝냈어도 뒤 교시를 할 수 있게 만들어 뒀어요.</p></div></details>
<details><summary>답이 너무 길어요</summary><div class="body"><p>리모컨 <b>"말이 길 때"</b>를 보내요.</p></div></details>
<details><summary>짝꿍이 없어요</summary><div class="body"><p>옆 조의 한 사람이나 강사에게 부탁해요. 아무도 없으면 P9의 세 칸을 비워 두고 보내요. Claude가 처음 보는 사람이 헷갈릴 만한 곳을 골라 고치고 (가정)이라고 적어요.</p></div></details>
<details><summary>이미지가 안 만들어져요</summary><div class="body"><p>회색 박스 그대로 두고 넘어가요. 이미지는 오후 B의 선택이라 없어도 오늘은 충분해요.</p></div></details>
<details><summary>폰 화면에서 글자가 넘쳐요</summary><div class="body"><p>"폰 화면에서 글자가 옆으로 넘쳐. 고쳐줘"라고 증상을 그대로 말해요.</p></div></details>
<details><summary>HTML이 코드 글자로 보여요</summary><div class="body"><p>메모장(맥은 텍스트 편집기)으로 열린 거예요. 파일을 인터넷 브라우저 창에 끌어다 놓아요.</p></div></details>
<details><summary>사용량 한도 메시지가 떠요</summary><div class="body"><p>짝꿍 화면을 같이 보면서 기다려요. 한도가 풀리면 이어서 해요. 마무리의 W2를 못 돌리면, 실습시트에 확인한 것, 고른 것, 고친 것을 한 줄씩 적어 두고 내일 아침에 W2를 돌려요.</p></div></details>
<details><summary>새 대화를 열었더니 앞 내용을 몰라요</summary><div class="body"><p>괜찮아요. 프롬프트가 폴더의 파일을 읽게 되어 있어요. 다음 프롬프트를 그대로 붙여요. 다만 내가 말로 남긴 결정은 새 대화가 몰라요. 실습시트에 한 줄씩 적어 뒀다가, 마무리에서 W2를 보낼 때 프롬프트 아래에 덧붙여요.</p></div></details>
</section>
</div>

<button class="theme" id="themeBtn" type="button">다크 모드</button>
<div class="toast" id="toast" role="status" aria-live="polite">복사됐어요</div>
'''
PICKJS='''<script>
(function(){
  [].forEach.call(document.querySelectorAll('[data-pick]'),function(b){
    b.addEventListener('click',function(){
      var i=document.getElementById('v-pick'); if(!i) return;
      i.value=b.getAttribute('data-pick'); i.dispatchEvent(new Event('input'));
      var t=document.getElementById('toast'); if(t){t.textContent='조사할 것 칸에 넣었어요';t.classList.add('show');setTimeout(function(){t.classList.remove('show')},1600)}
    });
  });
})();
</script>'''

import base64, os
GAL=os.path.join(TOOLS,'day16_gallery')
def img64(n): return 'data:image/jpeg;base64,'+base64.b64encode(open(GAL+'/'+n+'.jpg','rb').read()).decode()
SHOTS=[x for x in [
 ('H2','경쟁사 가격 조사','MD · 꼭 볼 것에 "100g당 가장 싼 곳이 맨 위"라고 적었어요'),
 ('H3','증정품·프로모션 조사','온라인 영업 · 꼭 볼 것에 "증정품이 있는 곳만"이라고 적었어요'),
 ('H1','광고 소재 리서치','콘텐츠 마케터 · 광고 문구는 웹에서 못 찾은 칸이 가장 많았어요'),
 ('H4','상세페이지 조사','CX 기획자 · 첫 화면 문구, 영양 표시, 후기 노출을 나란히 봐요'),
 ('H5','팝업스토어 리서치','브랜드 마케터 · 경쟁사 팝업의 장소, 기간, 체험 요소를 나란히 봐요'),
 ('H6','교육 프로그램 리서치','운영 매니저(교육 회사) · 회사 칸을 비워 뒀더니 Claude가 가상의 교육 회사(라라클래스)로 바꾸고 한 줄로 알렸어요'),
 ('T7','경쟁 서비스 기능 조사','데이터 분석가(테크 트랙) · 경쟁사 자사몰과 앱의 기능을 나란히 봐요'),
] if os.path.exists(GAL+'/'+x[0]+'.jpg')]
GALLERY=('<details><summary>시험에서 실제로 나온 화면 보기</summary><div class="body">'
 '<p class="sub">같은 프롬프트(P0~P4)를 보내고 하고 싶은 일과 조사할 것만 바꾼 시험 결과예요. 회사는 모두 그대로(라라스윗)였어요. 여러분의 화면은 이와 달라도 돼요. "못 찾음"이 있는 칸은 웹에서 찾지 못한 값이에요.</p>'
 '<div class="shots">'+''.join('<figure><img src="%s" alt="%s 화면 (시험 결과)" width="390" height="700" loading="lazy"><figcaption><b>%s</b> · %s</figcaption></figure>'%(img64(n),r,r,c) for n,r,c in SHOTS)+'</div></div></details>') if SHOTS else ''
assert body.count('<!--GALLERY-->')==1
body=body.replace('<!--GALLERY-->',GALLERY)
body=expand_mvp_html(body)
out='<meta name="claude:viewport-fit-sides" content="cover">\n<title>Day 16 · 업무 간편화 MVP(Minimum Viable Product) 만들기</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap">\n'+style+'\n'+body+'\n'+script+'\n'+PICKJS+'\n'
import sys
dest=sys.argv[1] if len(sys.argv)>1 else PATH
open(dest,'w',encoding='utf-8').write(out)
print('written',dest,len(out),'boxes',out.count('class="copy"'))
