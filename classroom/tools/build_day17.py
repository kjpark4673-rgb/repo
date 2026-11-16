# Day 17 가이드 1판: 공식 11/17 줄(MVP 고도화, 사용자 테스트 설계, Claude in Chrome 자동 점검 + 사람 테스트, 결과 → 개선 우선순위, 16시 피치덱 뼈대).
# Day 16 6판의 조사 도우미(mvp.md, research.csv, mvp.html)를 다른 조 사람에게 테스트하고, 가장 큰 문제 두 개를 고쳐 MVP v1과 사용자 테스트 결과서를 남긴다.
# 강사 결정(11/15): 크롬은 전원 설치하고 함께 / 수요일은 개인별 피칭(조 안 3분 → 조 대표 5분 + 질문 3분) — 두 세션을 합치며 강사님이 고름(HANDOFF 7-25) / 숏폼은 맥락이 맞으면 활용(피칭 첫머리용 15초 소개 영상 콘티, 오후 메뉴) / 현업 이야기는 Day 16의 1~2주 이야기를 다시 씀.
# 저장소 안에서 그대로 돈다: python3 classroom/tools/build_day17.py [출력 경로]
import re, os
TOOLS=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(os.path.dirname(TOOLS))
PATH=os.path.join(REPO,'classroom','student-guide','day17.html')
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
script=script.replace(_d,"ind:'식품',role:'아직 모름',pick:'네가 정해줘',user:'네가 정해줘',obs1:'적지 않음',obs2:'적지 않음',fix:'네가 추천한 두 곳',obs3:'적지 않음',ask:'네가 정해줘',cards:'적지 않음',clarity:'적지 않음',rec:'적지 않음'};")
script=script.replace("'l16-","'l17-")
def tok(k,d): return '<b data-v="%s">%s</b>'%(k,d)
B=tok('brand','라라스윗'); P=tok('product','저당 아이스크림'); C=tok('customer','다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인')
ROLE=tok('role','아직 모름'); TASK=tok('task','네가 정해줘')
CO='- 회사: '+B+' ('+P+') / 고객: '+C
TOP=' style="margin-top:12px"'
def box(pid,title,text,style_attr=''):
    return ('<button class="copy" type="button" data-copy="%s"%s><div class="hd"><b>%s</b><span class="btn">눌러서 복사</span></div>\n<pre id="%s">%s</pre></button>'%(pid,style_attr,title,pid,text))
def field(k,label,ph=''):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><input id="v-%s" data-in="%s" type="text" maxlength="90" placeholder="%s" autocomplete="off"></div></div>'%(k,label,k,k,ph)



# ── 1판 프롬프트: 어제 만든 조사 도우미를 사람에게 테스트하고 고치는 날 (공식 11/17 줄)
PICK=tok('pick','네가 정해줘'); USER=tok('user','네가 정해줘')
RULES='''# 수업 작업 규칙 (다른 규칙과 부딪히면 이 규칙이 먼저다)
- 되묻지 않는다. 정보가 모자라면 스스로 가정하고 끝까지 만든다.
- 가정하거나 추측한 곳에는 (가정)이라고 표시한다. 숫자, 가격, 후기를 사실처럼 꾸미지 않는다.
- 웹에서 조사한 값에는 조사한 날짜와 출처 링크를 붙인다. 찾지 못한 값은 "못 찾음"으로 둔다.
- 표(CSV)는 엑셀에서 한글이 깨지지 않게 UTF-8 BOM으로 저장하고, 쉼표, 큰따옴표, 줄바꿈이 든 값은 큰따옴표로 감싼다.
- 필요한 파일이 없어도 멈추지 않는다. 없는 대로 진행한다.
- 결과는 파일로 저장하고, 끝나면 3줄로만 보고한다: 만든 파일 / 핵심 한 줄 / 내가 다음에 할 일 한 줄. 내용을 보여 달라고 하면 그대로 보여 준다.
- 모든 결과는 한국어로, 쉬운 말로 쓴다.'''
PR={}
PR['p00']='''이 폴더의 CLAUDE.md를 오늘 수업에 맞게 고쳐줘. 파일이 없으면 새로 만들어줘. 끝나면 3줄로만 알려줘.
1. "멈추고 묻기", "아카이브에 없는 것은 쓰지 않기" 같은 줄이 있으면 그 줄만 지워줘. 다른 내용은 건드리지 마.
2. "# 수업 작업 규칙"이 없으면 아래 첫 묶음을 넣어줘. 있으면 그대로 둬.
3. "# 사용자 테스트 규칙"과 "# 나와 회사"는 맨 아래에 넣어줘. 같은 제목이 이미 있으면 바꿔 넣어줘.
4. 다만 "# 나와 회사"가 이미 있으면, 아래 값 가운데 처음 값("아직 모름", "라라스윗", "저당 아이스크림", "다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인")인 것은 이미 적힌 값을 그대로 둬.

'''+RULES+'''

# 사용자 테스트 규칙
- 사람 테스트 결과는 내가 적은 말 그대로 옮긴다. 내가 적지 않은 결과, 숫자, 사용자의 말을 지어내지 않는다.
- 화면을 고치기 전에는 고치기 전 파일을 남긴다.
- 고치라고 고른 곳만 고치고 다른 곳은 건드리지 않는다.
- 화면 파일을 고친 뒤에는 스크립트에 문법 오류(괄호, 따옴표 짝, 정규식)가 없는지 다시 읽어 확인한다.

# 나와 회사 (오늘은 이 내용으로 작업한다)
- 내가 하고 싶은 일: '''+ROLE+'''
- 회사(브랜드): '''+B+''' ('''+P+''')
- 고객: '''+C+'''
- 내가 하고 싶은 일이나 조사할 것이 이 회사에 없는 일이면, 그 일이 있는 비슷한 가상의 회사로 바꿔서 작업하고, 바꾼 회사를 이 파일의 회사 줄에 적고 한 줄로 알린다.'''
PR['c00']='''어제 수업에서 만드는 조사 도우미를 한 번에 만들어줘. 오늘 사용자 테스트를 할 화면이야.
- 조사할 것: '''+PICK+'''. "네가 정해줘"이면 CLAUDE.md의 하고 싶은 일에 맞춰 골라줘(마케터는 광고 소재, MD·온라인 영업은 경쟁사 가격과 증정품·프로모션, 서비스 기획·개발·데이터 분석은 경쟁 서비스 기능, 그 밖의 일이나 "아직 모름"은 경쟁사 가격과 증정품·프로모션).
- 1) mvp.md: 조사할 것, 경쟁사 3곳(우리보다 훨씬 큰 대기업 말고 같은 고객을 두고 경쟁하는 곳), 표에 적을 칸 5~7개
- 2) research.csv: mvp.md대로 웹에서 조사. 맨 앞 두 칸은 조사일과 경쟁사, 맨 끝 칸은 출처 링크. 못 찾은 값은 "못 찾음", 가격은 원 단위 숫자. UTF-8 BOM으로 저장하고, 쉼표가 든 값은 큰따옴표로 감싸줘.
- 3) mvp.html: research.csv를 한눈에 보는 화면 파일 하나. 맨 위에 이 화면이 해 주는 일 한 줄과 가장 중요한 숫자 하나, 가운데 경쟁사 비교, 경쟁사로 걸러 보는 버튼, 눌러서 열리는 출처 링크. 표 내용을 파일 안에도 넣어서 더블클릭해도 보이게.
- 이미 있는 파일은 다시 만들지 말고 다음 단계로 넘어가.
되묻지 말고 끝까지 하고, 끝나면 3줄로만 알려줘.'''
PR['p01']='''어제 만든 조사 도우미 mvp.html을 처음 쓰는 사람에게 테스트할 거야. 사용자 테스트 설계서 test.md를 써줘.
- 진짜 쓸 사람: '''+USER+'''. "네가 정해줘"이면 CLAUDE.md와 mvp.md를 보고 이 조사 결과를 매일 받아 볼 사람(같은 팀 선배, 팀장 같은 사람)으로 정해줘. 오늘은 다른 조 학생 2명이 그 사람 역할로 테스트해.
- 써 보는 사람에게 읽어 줄 역할 한 줄(예: "당신은 매일 아침 이 표를 받는 MD 팀장이에요").
- 시켜 볼 일 3개: 그 사람이 이 화면으로 실제로 하려는 일(예: 가장 싼 곳 찾기, 새 광고 찾기, 새로 생긴 기능 찾기, 값의 출처 열어 보기). 시켜 볼 일 카드에는 어디를 누르라는 말과 정답을 넣지 마. 시켜 볼 일마다 내가 미리 알아 둘 정답은 따로 적어줘.
- 함정이 되는 일은 만들지 마. 화면에서 틀린 값이나 이상한 곳을 보면 맨 아래 "테스트 전에 고칠 것"에 적어줘.
- 지켜보며 적을 것: 시켜 볼 일마다 해냈나(혼자 / 도움 받고 / 못 함), 걸린 초, 멈추거나 되돌아간 곳, 써 보는 사람이 한 말. 끝나고 물을 질문 3개(1~5점 "쓰기 쉬웠나" 하나 포함, 구글 폼에 옮길 수 있게 객관식은 보기까지).
- 성공 기준: 2명 가운데 몇 명이 시켜 볼 일 몇 개를 혼자 끝내면 되는지. mvp.md에 어제 "써 본 결과"가 있으면 거기 적힌 "다음에 확인할 숫자"도 성공 기준에 넣어줘.
mvp.html이 없으면 mvp.md나 research.csv로 화면부터 만들고 이어서 해줘. 셋 다 없으면 CLAUDE.md의 하고 싶은 일에 맞는 조사(서비스 기획·개발·데이터 분석은 경쟁 서비스 기능, 그 밖은 경쟁사 가격·프로모션)로 경쟁사 3곳을 웹에서 조사해 research.csv와 mvp.html을 먼저 만들어줘. 되묻지 말고 끝까지 쓰고, 끝나면 역할 한 줄과 시켜 볼 일 카드 3장만 보여줘.'''
PR['p02']='''사람에게 보이기 전에, test.md의 시켜 볼 일 3개를 mvp.html에서 처음 쓰는 사람처럼 따라가 보고 걸리는 곳을 auto_check.md로 정리해줘.
- 먼저 화면이 열리는지부터 봐. 스크립트에 문법 오류(정규식, 괄호, 따옴표 짝)가 있으면 화면이 비어 보여. 있으면 "막힘"으로 적고 고쳐줘.
- 화면 파일의 코드를 읽고, 시켜 볼 일마다 사람이 누를 순서대로 따라가 봐. 버튼과 걸러 보기가 동작하는지, 출처 링크가 열리는 주소인지, "못 찾음" 때문에 시켜 볼 일을 끝낼 수 없는 곳이 있는지, 폰 폭에서 넘치는 곳이 있는지 봐.
- 출처가 "내가 직접 봄"인 줄과 네가 열 수 없는 사이트(광고 모음, 로그인이 필요한 몰)의 링크는 고장이 아니라 (확인 필요)로 둬. "못 찾음" 값은 지우거나 채워 넣지 마.
- 표: 몇 번 일 / 무엇이 / 얼마나 심한지(막힘: 그 일을 끝낼 수 없음, 헷갈림, 사소함) / 어떻게 알았나(코드 읽음, 링크 열어 봄, 확인 필요) / 상태(고침, 남음).
- "막힘"과 test.md의 "테스트 전에 고칠 것"만 지금 고치고 상태를 "고침"으로 적어줘. 고치기 전 파일은 mvp_before_check.html로 남기고, 이미 있으면 덮어쓰지 마. 고치다가 시켜 볼 일 카드의 문장이나 정답이 달라지면 test.md도 같이 고쳐줘. 나머지는 사람 테스트 뒤에 고칠 거니까 그대로 둬.
test.md가 없으면 시켜 볼 일 3개를 네가 정해서 test.md부터 쓰고 이어서 해줘. mvp.html이 없으면 research.csv로 먼저 만들어줘. 되묻지 말고 끝까지 하고, 끝나면 걸린 곳 표와, 시켜 볼 일 카드나 정답이 달라졌으면 그 한 줄만 보여줘.'''
PR['chk']='''이 화면에서 아래 시켜 볼 일을 처음 쓰는 사람처럼 직접 눌러 가며 해 봐. 화면의 내용은 바꾸지 마.
- 시켜 볼 일: '''+tok('cards','적지 않음')+'''
- 시켜 볼 일이 "적지 않음"이면 이 화면을 처음 보는 사람이 할 만한 일 3가지를 네가 정해서 해 봐.
- 시켜 볼 일마다 해냈는지, 몇 번 눌렀는지, 어디서 헷갈렸는지, 동작하지 않은 버튼이나 링크를 표로 알려줘. 표 말고 다른 설명은 3줄 안으로.'''
OBS1=tok('obs1','적지 않음'); OBS2=tok('obs2','적지 않음')
PR['p03']='''사람 테스트에서 내가 적은 기록을 테스트 기록 test_log.md로 정리하고, 고칠 순서를 정해줘.
- 써 본 사람 1: '''+OBS1+'''
- 써 본 사람 2: '''+OBS2+'''
- 써 보는 사람은 "다른 조 학생(진짜 쓸 사람 역할)"이라고 적어줘. 써 본 사람마다, 시켜 볼 일 하나하나를 해냈나(혼자 / 도움 받고 / 못 함), 걸린 초, 멈춘 곳, 한 말을 표로. 내가 적은 말은 고치거나 보태지 말고 그대로 옮겨. 내가 적지 않은 칸은 비워 둬.
- auto_check.md에서 상태가 "남음"인 것도 합쳐서 고칠 곳 목록을 만들어줘. "고침"은 넣지 마. 칸: 문제 / 몇 명이 겪었나(자동 점검에서만 나온 것은 "점검") / 시켜 볼 일을 막았나 / 고치기 쉬운가 / 순위. 여러 명이 겪었고 시켜 볼 일을 막은 것이 위로.
- mvp.md에 어제 "써 본 결과"가 있으면 오늘 표와 섞지 말고 "어제(같은 조 1명, 5초 보기와 1분 써 보기)"로 한 줄 따로 적어줘.
- 써 본 사람 1과 2가 모두 "적지 않음"이면 결과를 지어내지 말고, 표에 "사람 테스트 전"이라고 적고 auto_check.md만으로 목록을 만들어줘.
test.md가 없으면 시켜 볼 일은 기록에서 읽어 와. 되묻지 말고 끝까지 하고, 끝나면 고칠 곳 목록의 위 5개와 네가 추천하는 두 곳만 보여줘.'''
PR['p04']='''test_log.md의 고칠 곳 가운데 두 곳을 mvp.html에서 고쳐 MVP v1로 만들고, 사용자 테스트 결과서 test_report.md를 써줘.
- 고칠 것: '''+tok('fix','네가 추천한 두 곳')+'''
- 고치기 전 파일(써 본 사람이 본 화면)은 mvp_before_fix.html로 남겨줘. 이미 있으면 덮어쓰지 마. 고른 두 곳만 고치고 다른 곳은 건드리지 마.
- 고친 화면(MVP v1)은 mvp.html이야. 폴더에 mvp_v1.html, mvp_v2.html이 있으면 어제 고치기 전 화면이니, 결과서에는 파일 이름을 mvp.html로 적어줘.
- test_report.md 한 장: 맨 위 "MVP v1 · 날짜" / 무엇을 누구에게 테스트했나(진짜 쓸 사람, 써 보는 사람은 "다른 조 학생 ○명이 역할을 맡음") / 시켜 볼 일마다의 결과("○명 중 ○명이 혼자 끝냄", 걸린 초) / 찾은 문제 위의 3개 / 고친 두 곳(고치기 전 → 고친 뒤) / 고치지 않은 것과 이유 / 다음 테스트에서 확인할 숫자
- 기록에 없는 숫자는 쓰지 마. 사람 테스트를 하지 않았으면 맨 위에 "사람 테스트 전"이라고 적어줘.
test_log.md가 없으면 auto_check.md로, 그것도 없으면 처음 쓰는 사람이 가장 헷갈릴 곳 두 곳을 네가 골라 고치고 (가정)이라고 적어줘. 되묻지 말고 끝까지 하고, 끝나면 고친 두 곳을 한 줄씩과 시켜 볼 일마다의 결과만 보여줘.'''
PR['p05']='''고친 mvp.html을 새 사람에게 한 번 더 테스트한 기록이야. test_report.md에 2차 결과를 더하고 1차와 비교해줘.
- 써 본 사람 3: '''+tok('obs3','적지 않음')+'''
- test.md의 같은 시켜 볼 일로 1차 → 2차: "○명 중 ○명이 혼자 끝냄", 걸린 초, 같은 곳에서 또 멈췄는지. 내가 적은 말은 그대로 옮겨. 1차와 2차는 사람과 사람 수가 달라서 비교는 참고용이라고 적어줘.
- 같은 곳에서 또 멈췄거나 새로 막힌 곳이 있으면 한 곳만 고쳐줘. 고치기 전 파일은 mvp_before_fix2.html로 남겨줘.
- 기록이 "적지 않음"이면 비교를 지어내지 말고, 2차 테스트 때 볼 것 3가지만 test_report.md에 적어줘.
test_report.md가 없으면 test_log.md로 1차 결과를 먼저 정리하고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 1차와 2차 비교 표만 보여줘.'''
PR['p06']='''mvp.html이 어떤 표를 넣어도 제대로 동작하는지 통과 기준을 세우고, 샘플 데이터로 확인해서 data_check.md로 정리해줘.
- 통과 기준 8개 안팎. 예: 쉼표·큰따옴표·줄바꿈이 든 값 / 빈 값과 "못 찾음" / 칸 순서가 다른 표 / 100줄짜리 표 / "12,900원"처럼 글자가 섞인 가격 / 출처 링크가 없는 줄 / 폰 폭에서 아주 긴 글자 / 걸러 보기 버튼을 연달아 누르기
- samples 폴더에 기준을 시험할 CSV 3개를 만들어줘. 값은 시험용 가짜 값이니 파일 이름을 sample로 시작하고, 칸 이름은 research.csv와 같게 하되 하나는 칸 순서만 바꿔줘.
- mvp.html의 코드를 읽고 기준마다 통과 / 실패 / (확인 필요)를 표로. 실패한 것만 고치고, 고치기 전 파일은 mvp_before_data.html로 남겨줘.
- 표에 "어떻게 알았나" 칸을 두고 지금은 모두 "코드 읽음"으로 적어줘. 화면에 CSV를 고르는 기능이 있으면, 내가 샘플을 하나씩 골라 열어 보는 순서를 3줄로 적어줘. 없으면 그 기능부터 만들어줘.
mvp.html이 없으면 research.csv로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 기준별 결과 표와 열어 보는 순서만 보여줘.'''
PR['p07']='''수요일 발표 첫머리에 틀 15초 소개 영상의 콘티를 teaser.md로 써줘. 내 조사 도우미를 처음 보는 사람에게 소개하는 영상이야.
- 3컷: 0~4초 손으로 매일 조사하던 장면(누가, 언제, 무엇을 캡처하고 옮기나) / 4~11초 조사 도우미 화면(mvp.html을 내 화면 녹화로) / 11~15초 줄어든 시간과 약속 한 줄
- 컷마다 화면, 자막(한 줄, 12자 안팎), 소리
- 1컷과 3컷은 영상 AI(Google Flow, Kling)에 붙일 프롬프트를 한국어 3문장 안으로(장면, 빛, 카메라 움직임). 끝마다 "화면에 글자, 실제 브랜드 로고, 실제 제품 포장은 넣지 않는다"
- 무료 크레딧 계획: 컷마다 몇 번까지 뽑을지, 안 나오면 이미지 한 장과 자막으로 대신하는 법
- 시간과 숫자는 test_report.md, mvp.md, portfolio로 시작하는 파일에서 찾고, 없으면 (가정)
되묻지 말고 끝까지 쓰고, 끝나면 컷 3개(초 / 화면 / 자막)와 영상 AI 프롬프트 2개만 보여줘.'''
PR['p08']='''오늘 한 사용자 테스트 순서를 다음에도 한 줄로 다시 할 수 있게 스킬로 묶어줘.
- 저장할 곳: .claude/skills/user-test/SKILL.md (맨 위에 name과 description. description에 "테스트 준비해줘"와 "테스트 결과 정리해줘"를 넣어서 그 말로 불리게)
- "테스트 준비해줘": 폴더의 화면 파일을 읽고 진짜 쓸 사람, 역할 한 줄, 시켜 볼 일 3개(누를 곳과 정답은 카드에 넣지 않기, 함정 만들지 않기), 지켜보며 적을 것, 질문 3개를 test.md로. test.md가 이미 있으면 덮어쓰지 말고 test_날짜.md로 새로 써.
- "테스트 결과 정리해줘"와 함께 붙인 기록: 기록을 고치지 않고 표로 옮기고, 고칠 순서(여러 명이 겪었고 시켜 볼 일을 막은 것이 위)를 test_log.md로. 이미 있으면 test_log_날짜.md로.
- 기록에 없는 결과와 사용자의 말을 지어내지 않는 규칙을 넣어줘. 회사 이름은 넣지 말고 CLAUDE.md와 mvp.md를 읽어서 쓰게 해줘.
되묻지 말고 끝까지 만들고, 끝나면 이 스킬을 부르는 두 줄만 알려줘.'''
PR['p10']='''고친 mvp.html을 인터넷에 올려 Microsoft Clarity로 사용성 테스트를 녹화할 거야. 올릴 폴더를 만들어줘.
- 내 Clarity 프로젝트 ID: '''+tok('clarity','적지 않음')+'''
- deploy 폴더를 만들고 지금의 mvp.html을 deploy/index.html로 복사해줘. 이미 있으면 새로 덮어써. mvp.html은 건드리지 마.
- index.html이 불러오는 파일(이미지, CSV, js)이 있으면 deploy 폴더에 같은 상대 경로로 복사해줘. 내 컴퓨터 주소(C:로 시작하는 경로, file://, localhost)로 불러오는 곳은 상대 경로로 바꿔줘.
- index.html의 &lt;/head&gt; 바로 앞에 아래 코드를 그대로 넣고, "프로젝트ID" 자리만 내 프로젝트 ID로 바꿔줘:
&lt;script type="text/javascript"&gt;(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window, document, "clarity", "script", "프로젝트ID");&lt;/script&gt;
- 화면 맨 아래에 작은 글씨로 "이 화면은 사용성 개선을 위해 클릭과 화면 이동을 Microsoft Clarity로 기록해요."를 넣어줘.
- 프로젝트 ID가 "적지 않음"이면 코드는 넣지 말고 그 자리에 &lt;!-- Clarity 코드 자리 --&gt;만 남겨줘. 끝에 "Clarity 프로젝트 ID를 칸에 적고 P10을 다시 보내요"라고만 알려줘.
되묻지 말고 끝까지 하고, 끝나면 deploy 폴더의 파일 목록과 넣은 프로젝트 ID만 보여줘.'''
PR['p11']='''Microsoft Clarity의 녹화와 히트맵에서 내가 본 것을 test_report.md에 더해줘.
- 내가 본 것: '''+tok('rec','적지 않음')+'''
- test_report.md 맨 아래에 "녹화로 본 것 (Microsoft Clarity)" 표: 본 것(내가 적은 말 그대로) / 종이 기록(test_log.md)에도 있던 것인지, 녹화로 새로 찾은 것인지 / 고칠 곳 후보
- 녹화는 본 사람 수와 날짜가 종이 테스트와 달라서 숫자를 합치지 마. 내가 적지 않은 클릭 수, 비율, 시간은 지어내지 마.
- 내가 본 것이 "적지 않음"이면 아무것도 더하지 말고, 녹화를 볼 때 확인할 것 3가지만 알려줘.
test_report.md가 없으면 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 더한 표만 보여줘.'''
PR['p09']='''내일(11/18) 피칭 데이에 쓸 내 MVP 피치 뼈대를 pitch.md로 써줘. 내일 이걸로 HTML 발표 화면을 만들어. 발표는 한 사람씩 해(조 안에서 3분, 조 대표는 반 전체 앞에서 5분).
- 듣는 사람: 이 조사를 매일 하는 부서의 팀장과 동료
- 일곱 칸, 칸마다 말할 문장 1~2개와 화면에 보여 줄 것 하나:
  문제(누가 매일 무엇에 몇 분을 쓰나) / 해결(내 MVP가 해 주는 일 한 줄) / 시장(이 조사를 매일 하는 신입과 그 팀이 얼마나 많은지. 어림셈이면 식을 보여 주고 (가정)) / BM(회사 안에서 쓰면 줄인 시간 × 쓰는 사람 수, 밖에 판다면 누가 얼마를 낼지) / MVP(라이브 데모에서 누를 순서 3단계와 사용자 테스트 숫자 하나. "다른 조 학생 ○명 중 ○명"처럼) / 함께 만든 것(테스트해 준 사람 수, 에이전트가 한 일, 내가 내린 결정) / 요청사항(듣는 사람에게 바라는 것 하나)
- 요청사항: '''+tok('ask','네가 정해줘')+'''. "네가 정해줘"이면 일주일 써 볼 동료나 실제 자료 접근처럼 MVP 다음 단계에 꼭 필요한 것 하나로.
- 숫자는 test_report.md, test_log.md, data_check.md, mvp.md, research.csv, portfolio로 시작하는 파일에서 찾고, 옆에 어느 파일에서 왔는지 적어줘. 없는 숫자는 지어내지 말고 [채울 곳]이나 (가정).
- "함께 만든 것"의 내가 내린 결정은 내가 입력 칸에 적은 것과 프롬프트 밖에서 내가 따로 말해 바꾼 것만 써. 수업 프롬프트나 CLAUDE.md에 적힌 규칙과 지시, "적지 않음", "네가 정해줘", "네가 추천한 두 곳"은 내 결정이 아니야. 없으면 [채울 곳: 내가 내린 결정]으로 남겨줘.
- teaser.md(15초 소개 영상 콘티)가 있으면 해결 칸에 "영상 자리"라고 적어줘.
- 맨 아래: 3분 버전(조 안 발표)에서 줄일 칸과 5분 버전(조 대표 발표)에서 늘릴 칸을 한 줄씩, 그리고 "공개 자료로 만든 학습용 MVP이며, 조사한 회사와 관계없습니다".
되묻지 말고 끝까지 쓰고, 끝나면 일곱 칸의 첫 문장만 보여줘.'''
PR['w2']='''오늘 이 폴더에서 한 일을 내 포트폴리오에 넣을 한 장으로 정리해서 portfolio_1117.md로 써줘.
- 내가 하고 싶은 일: '''+ROLE+''' / 회사: '''+B+'''. CLAUDE.md의 "# 나와 회사"에 적힌 값이 있으면 그 값을 먼저 써줘.
- 무엇을 했나: 어떤 조사 도우미를 누구에게 테스트했고, 무엇을 고쳐 MVP v1을 만들었나 한 줄과 파일 이름
- 테스트 숫자: test_report.md에 있는 숫자만, "다른 조 학생 ○명 중 ○명"처럼 써 본 사람이 누구인지와 함께. 사람 테스트를 하지 않았으면 그렇게 적어줘. data_check.md가 있으면 기준 몇 개 중 몇 개 통과(코드 읽음)인지도.
- 수업에서 배운 방법: 수업 프롬프트가 시킨 방법 가운데 내가 실제로 따라 한 것을 3줄로(예: 시켜 볼 일 카드에 정답 넣지 않기, 사람 전에 자동 점검, 여러 명이 겪은 것부터 고치기). 이건 내 결정이 아니야.
- 내가 내린 결정: 아래 세 가지만 적어줘.
  - 진짜 쓸 사람, 고칠 것, 오후에 고른 심화. "네가 정해줘", "적지 않음", "네가 추천한 두 곳"만 있으면 내가 정한 게 아니야.
  - 테스트에서 내가 보고 적은 기록. 프롬프트의 써 본 사람 칸이 "적지 않음"이면 적은 게 아니야.
  - 내가 따로 말해서 바꾼 것, 확인하거나 바로잡은 것, 이유를 말하고 받아들인 것.
- 네가 골랐고 내가 그대로 받은 것은 "Claude가 고름"이라고 쓰고, 옆에 [내가 적을 곳: 받아들인 이유]를 남겨줘. 큰 것 5개까지만.
- 이 결과물이 회사에서 쓰이는 곳: why.md가 있으면 오늘 한 일(사용자 테스트, 개선 우선순위)이 공고의 어떤 문장과 이어지는지 한 줄. 없으면 (가정).
- 면접에서 말할 세 문장: 누구에게 무엇을 테스트했고, 무엇을 보고 무엇을 고쳤고, 다음에 무엇을 확인할지. 내가 내리지 않은 결정을 내가 한 것처럼 쓰지 마. 쓸 결정이 없으면 그 문장은 [내가 적을 곳]으로 남겨줘.
되묻지 말고 끝까지 쓰고, 끝나면 "면접에서 말할 세 문장"과 [내가 적을 곳]이 남은 자리만 보여줘.'''
R={'r1':'되묻지 말고 네가 가정해서 끝까지 만들어줘. 가정한 곳만 (가정)이라고 표시해줘.',
'r2':'너무 길어. 3줄로만 다시 말해줘.',
'r3':'없는 자료는 없는 대로 두고, 지금 있는 것으로 끝까지 만들어줘.',
'r6':'방금 만든 파일의 내용을 그대로 보여줘. CSV면 앞 10줄을 표로, HTML이면 코드 말고 화면에 무엇이 어떤 순서로 있는지 알려줘.',
'r8':'test.md의 역할 한 줄과 시켜 볼 일 카드 3장만 다시 보여줘. 정답은 빼고.',
'r9':'test.md의 시켜 볼 일마다의 정답과 끝나고 물을 질문 3개만 보여줘. 나만 볼 거야.',
'r10':'test_report.md의 내용을 그대로 보여줘.',
'r11':'방금 만든 파일에서 우리 업종의 광고 규정에 걸릴 수 있는 표현 가운데 가장 위험한 5개만 표로 보여 주고(원래 표현 / 이유 / 고친 표현), 파일도 그렇게 고쳐줘. 확실하지 않은 것은 (확인 필요)라고 표시해줘. 표 말고 다른 설명은 3줄 안으로 해줘.'}
CMP='mvp_before_fix.html과 mvp.html을 브라우저 탭 두 개로 열어줘.'
RUN='테스트 준비해줘'
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
    for tok_ in re.split(r'(<[^>]+>)',h):
        if tok_.startswith('<'):
            low=tok_.lower()
            if low.startswith('<pre'): in_pre=True
            elif low.startswith('</pre'): in_pre=False
            if _BLOCK.match(low): done=False
            out.append(tok_); continue
        if in_pre or 'MVP' not in tok_:
            out.append(tok_); continue
        if 'Minimum Viable Product' in tok_:
            done=True; out.append(tok_); continue
        parts=re.split(r'(MVP(?!\s*\())',tok_); buf=[]
        for part in parts:
            if part=='MVP' and not done:
                buf.append('MVP<span class="ab">(Minimum Viable Product)</span>'); done=True
            else: buf.append(part)
        out.append(''.join(buf))
    return ''.join(out)
def fieldwide(k,label,ph='',n=1500):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><textarea id="v-%s" data-in="%s" rows="4" maxlength="%d" placeholder="%s" autocomplete="off"></textarea></div></div>'%(k,label,k,k,n,ph)

# ── 1판 본문
ROLES_TEST=[
('콘텐츠 마케터','광고 시안 두 개를 처음 보는 사람에게 5초씩 보여 주고 "무엇을 파는 광고 같아요?"라고 물어요','맞게 말한 사람 수'),
('MD<span class="ab">(Merchandiser)</span>·온라인 영업','상세페이지에서 가격과 혜택을 찾아보게 하고 지켜봐요','찾는 데 걸린 초, 못 찾은 사람 수'),
('CX<span class="ab">(Customer Experience)</span> 기획자','고객 역할을 맡은 사람에게 문의하지 않고 교환 방법을 찾게 해요','혼자 끝낸 사람 수'),
('서비스 기획자·PM<span class="ab">(Product Manager)</span>','새 기능을 처음 쓰는 사람이 끝까지 가는지 지켜봐요','끝까지 간 비율, 멈춘 단계'),
('데이터 분석가','팀장 역할에게 대시보드에서 오늘 볼 숫자를 찾게 해요','찾는 데 걸린 초'),
('개발자','사람이 누르기 전에 버튼, 링크, 폰 화면을 자동으로 먼저 점검해요','동작하지 않은 곳의 수'),
]
ROLE_ROWS='\n'.join('<div class="row"><span class="k">%s</span><span class="w"><b>%s</b><small>확인할 숫자: %s</small></span></div>'%r for r in ROLES_TEST)

body='''
<div class="wrap">
<nav id="nav" aria-label="구간 이동">
<a href="#s0">오늘</a><a href="#s1">준비</a><a href="#s2">1교시</a><a href="#s3">2교시</a><a href="#s4">3교시</a><a href="#s5">4교시</a><a href="#s6">오후</a><a href="#s7">16시</a><a href="#s8">마무리</a><a href="#remote">리모컨</a><a href="#s9">막히면</a>
</nav>

<section id="s0">
<span class="eyebrow">Day 17 / 52 · 11/17(화)</span>
<h1>Day 17 · 사용자 테스트로 MVP를 고치는 날</h1>
<p class="lead">어제 만든 조사 도우미(mvp.html)를 오늘은 <b>처음 쓰는 사람</b>에게 맡겨 봐요. 어디서 멈추는지 지켜보고, 여러 사람이 걸린 곳부터 두 곳을 고쳐 <b>MVP v1</b>을 만들어요. 오후에는 각자 심화를 하고, 4시부터 수요일 피칭의 뼈대(일곱 칸)를 만들어요.</p>

<h3 class="gap">오늘 한눈에</h3>
<div class="acts">
<div><b>① 테스트 준비</b><span>09:40–11:00</span></div>
<div><b>② 테스트하고 고치기</b><span>11:00–13:00</span></div>
<div><b>③ 심화와 발표 준비</b><span>14:00–18:00</span></div>
</div>
<div class="map">
<div class="grp">시작</div>
<div class="row rest"><span class="t">09:00</span><span class="w">오늘 한눈에 보기, 어제 돌아보기</span></div>
<a class="row" href="#s1"><span class="t">09:20</span><span class="w"><b>준비 · 어제 폴더 열고 규칙 이어 쓰기</b><small>남는 것: CLAUDE.md. 어제 조사 도우미가 없으면 C0으로 만들어요</small></span></a>
<div class="grp">① 테스트 준비 · 누구에게 무엇을 시킬지 정하고, 사람보다 먼저 에이전트가 점검해요</div>
<a class="row" href="#s2"><span class="t">09:40</span><span class="w"><b>1교시 · 사용자 테스트 알기, 테스트 설계서</b><small>남는 것: test.md (시켜 볼 일 카드 3장)</small></span></a>
<a class="row" href="#s3"><span class="t">10:20</span><span class="w"><b>2교시 · 사람 전에 에이전트가 먼저 점검</b><small>남는 것: auto_check.md, 막힌 곳을 고친 mvp.html</small></span></a>
<div class="grp">② 테스트하고 고치기 · 다른 조 사람이 써 보고, 많이 걸린 곳부터 고쳐요</div>
<a class="row" href="#s4"><span class="t">11:00</span><span class="w"><b>3교시 · 다른 조와 서로 테스트하기</b><small>남는 것: 써 본 사람 2명의 관찰 기록(종이나 메모에 적었다가 입력 칸으로)</small></span></a>
<a class="row" href="#s5"><span class="t">12:00</span><span class="w"><b>4교시 · 고칠 순서 정하고 두 곳 고치기</b><small>남는 것: test_log.md(테스트 기록), MVP v1(고친 mvp.html), test_report.md(사용자 테스트 결과서)</small></span></a>
<div class="row rest"><span class="t">13:00</span><span class="w">점심</span></div>
<div class="grp">③ 심화와 발표 준비 · 메뉴에서 골라 더 해 보고, 수요일 발표의 뼈대를 세워요</div>
<a class="row" href="#s6"><span class="t">14:00</span><span class="w"><b>오후 · 심화 메뉴에서 하나 이상</b><small>한 번 더 테스트, 통과 기준과 샘플 데이터, 15초 소개 영상 콘티, 테스트를 스킬로</small></span></a>
<a class="row" href="#s7"><span class="t">16:00</span><span class="w"><b>수요일 발표 준비 · 링크, 내 피치 뼈대 일곱 칸</b><small>남는 것: 남이 열 수 있는 링크, pitch.md</small></span></a>
<a class="row" href="#s8"><span class="t">17:00</span><span class="w"><b>마무리 · 조 공유, 포트폴리오 한 장, 링크</b><small>남는 것: portfolio_1117.md, 실습시트에 적은 링크</small></span></a>
</div>
<p class="sub">줄을 누르면 그 구간으로 가요. <b>꼭 하는 것</b>은 P0 → P1 → P2 → 사람 테스트 → P3 → P4, 오후 메뉴 하나 이상, 16시의 P9, 마무리의 W2예요. 어제 조사 도우미가 없으면 P0 다음에 C0을 먼저 보내요. 이것만 끝내도 오늘은 통과예요.</p>

<h3 class="gap">오늘 수업, 이렇게 보면 돼요</h3>
<p class="sub">궁금한 줄만 눌러 봐요.</p>
<details><summary>어제 만든 것을 오늘 "남이 쓸 수 있는 것"으로 바꿔요</summary><div class="body">
<p>어제의 조사 도우미는 만든 사람 눈에만 쉬워요. 만든 사람은 어디를 누르면 되는지 이미 알거든요. 오늘은 처음 쓰는 사람이 혼자 쓸 수 있는지 확인하고, 막힌 곳을 고쳐요. 공식 일정표에 적힌 오늘의 결과물은 <b>MVP v1</b>과 <b>사용자 테스트 결과서</b>예요.</p></div></details>
<details><summary>테스트는 사람을 시험하는 게 아니라 화면을 시험하는 거예요</summary><div class="body">
<p>써 보는 사람이 헤매면 그 사람 잘못이 아니라 화면이 고칠 곳을 알려 준 거예요. 내 화면이 테스트를 받을 때도 마찬가지예요. 많이 멈출수록 고칠 곳을 많이 찾은 거예요.</p></div></details>
<details><summary>오늘 남는 것은 "고쳐 본 경험"과 숫자예요</summary><div class="body">
<ul><li><b>오늘 저녁</b> · 테스트 설계서, 사용자 테스트 결과서, 고친 화면(MVP v1), 포트폴리오 한 장</li><li><b>수요일</b> · 오늘 만든 피치 뼈대로 내 MVP를 발표해요. 조 안에서 한 사람씩 3분, 조 대표는 반 전체 앞에서 5분이에요. 테스트에서 나온 숫자가 발표의 근거가 돼요</li><li><b>면접에서</b> · "만들었어요"에서 끝나지 않고 "써 보게 했더니 2명 중 1명이 여기서 멈춰서, 이렇게 고쳤어요"까지 말할 수 있어요</li></ul></div></details>
<details><summary>초안은 Claude가 만들고, 결정은 내가 해요</summary><div class="body">
<p>오늘 내가 내리는 결정은 다섯 가지예요. 가이드에서 <b>"내 결정"</b>이라고 적힌 곳이 그 자리예요.</p>
<ul><li>시켜 볼 일 카드 세 장이 진짜 쓸 사람의 일인지 <b>확인하기</b></li><li>자동 점검이 찾은 문제를 내 눈으로 눌러 보고 진짜인지 <b>확인하기</b></li><li>고칠 곳 목록에서 오늘 고칠 두 곳 <b>고르기</b></li><li>오후 메뉴와 발표에서 보여 줄 것 <b>정하기</b></li><li>내일 피치의 <b>요청사항</b> 정하기</li></ul></div></details>
<h3 class="gap">용어</h3>
<details><summary>오늘 쓰는 말 (어제 못 왔으면 MVP부터 봐요)</summary><div class="body">
<ul><li><b>MVP</b> · 최소 기능 제품. 가장 작게 만들어 진짜 쓸 사람에게 먼저 써 보게 하는 첫 버전이에요.</li><li><b>조사 도우미</b> · 어제 만든 MVP예요. 매일 손으로 하던 경쟁사 조사를 에이전트가 웹에서 찾아 표(research.csv)로 정리하고, 한 화면(mvp.html)에서 보여 줘요. 오늘 테스트하는 화면이 이거예요.</li><li><b>사용자 테스트</b> · 진짜 쓸 사람(또는 그 역할을 맡은 사람)에게 할 일을 주고, 혼자 해내는지 옆에서 지켜보며 막히는 곳을 찾는 일이에요. 1교시에 자세히 설명해요.</li><li><b>써 보는 사람</b> · 내 화면을 처음 써 보며 테스트해 주는 사람이에요. 현업에서는 '테스터'라고 불러요.</li><li><b>시켜 볼 일</b> · 테스트에서 써 보는 사람에게 시키는 일 하나예요. 예: "가장 싼 곳을 찾아 주세요". 현업에서는 '과업', '태스크'라고 불러요.</li><li><b>시켜 볼 일 카드</b> · 시켜 볼 일을 한 장에 한 문장으로 적은 것이에요. 어디를 누르라는 말과 정답은 넣지 않아요.</li><li><b>지켜보며 적을 것</b> · 테스트하며 적는 것이에요. 현업에서는 '관찰 지표'라고 불러요. 해냈나, 걸린 초, 멈춘 곳, 써 보는 사람이 한 말.</li><li><b>생각 말하기</b> · 써 보는 사람이 하면서 떠오르는 생각을 소리 내어 말하게 하는 방법이에요. "어, 이건 뭐지?" 같은 말이 고칠 곳을 알려 줘요.</li><li><b>자동 점검</b> · 사람이 써 보기 전에 에이전트가 화면 파일을 읽고 버튼, 링크, 폰 화면을 먼저 확인하는 일이에요.</li><li><b>Claude in Chrome</b> · 크롬 브라우저에 붙이는 Claude 확장 프로그램이에요. 화면을 직접 눌러 보며 점검할 수 있어요. 오늘 2교시에 다 같이 설치해요.</li><li><b>고칠 순서</b> · 무엇부터 고칠지 정한 순서예요. 현업에서는 '우선순위'라고 불러요. 여러 명이 겪었고 시켜 볼 일을 막은 문제가 위로 가요.</li><li><b>MVP v0과 v1</b> · v0은 어제 만든 첫 버전, v1은 테스트 결과로 고친 다음 버전이에요. 오늘 4교시에 고친 mvp.html이 MVP v1이에요. 2교시에 자동 점검이 고치기 전 화면은 mvp_before_check.html로 남아요. 폴더에 mvp_v1.html, mvp_v2.html이 있으면 어제 오후에 고치기 전 화면을 남긴 파일이라, 오늘의 MVP v1과 다른 파일이에요.</li><li><b>통과 기준</b> · "이런 경우에도 제대로 돌아야 한다"를 미리 적어 둔 목록이에요. 현업에서는 '검증 기준'이라고 불러요. 오후 B에서 써요.</li><li><b>테스트 기록(test_log.md)</b> · 써 본 사람과 시켜 볼 일마다 내가 적은 기록을 표로 옮기고, 고칠 곳 순위를 매긴 파일이에요. 결과서(test_report.md)와 다른 파일이에요.</li><li><b>사용자 테스트 결과서(test_report.md)</b> · 누구에게 무엇을 시켰고, 결과가 어땠고, 무엇을 고쳤는지 적은 한 장이에요.</li><li><b>피치덱</b> · 짧은 시간에 아이디어를 설득하려고 만든 발표 자료예요. 수요일에는 브라우저에서 열리는 HTML 피치덱을 만들어요.</li><li><b>BM<span class="ab">(Business Model)</span></b> · 비즈니스 모델. 누구에게 어떤 가치를 주고 어떻게 돈을 벌거나 아끼는지예요.</li><li><b>라이브 데모</b> · 발표 중에 만든 것을 실제로 눌러 보이는 시연이에요.</li><li><b>콘티</b> · 영상을 찍기 전에 컷마다 화면, 자막, 소리를 적어 둔 계획표예요.</li><li><b>크레딧</b> · 영상 AI 같은 도구에서 한 번 만들 때마다 쓰는 사용량 단위예요. 무료 크레딧은 하루나 한 달에 쓸 수 있는 양이 정해져 있어요.</li><li><b>아티팩트</b> · Claude가 만든 화면을 링크로 열 수 있게 올린 것이에요. 마무리에서 "화면을 링크로 만들기"로 만들어요.</li><li><b>테크 트랙</b> · 데이터·서비스 트랙이에요. 서비스 기획자, 개발자, 데이터 분석가를 바라는 학생들이 들어요.</li></ul></div></details>
</section>

<section id="s1">
<span class="eyebrow">시작 · 09:20–09:40 · 준비</span>
<h2>어제 폴더를 열고 규칙을 이어 써요</h2>
<p class="why"><b>왜 해요?</b> 오늘은 어제 만든 화면을 고쳐요. 어제 폴더에서 이어서 해야 Claude가 어제 파일을 읽어요.</p>
<div class="card checks">
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="a1"><span>Claude Code에서 <b>어제 작업 폴더</b>를 열고 <b>새 대화</b>를 시작했어요. 어제 폴더가 없거나 어느 것인지 모르겠으면 새 폴더(예: day17)를 만들어 열고, 오늘은 그 폴더만 써요</span></label>
<label class="check"><input type="checkbox" data-k="a2"><span>아래 입력 칸에 <b>내가 하고 싶은 일</b>과 회사를 적었어요. 어제와 같으면 비워 둬도 돼요</span></label>
<label class="check"><input type="checkbox" data-k="a3"><span><b>P0</b>을 실행했어요</span></label>
<label class="check"><input type="checkbox" data-k="a4"><span>Claude에게 <b>"이 폴더에 mvp.html 있어?"</b>라고 물어봤어요. 없으면 P0 다음에 C0을 보냈어요. 있으면 답에 나온 파일 이름을 눌러 <b>표와 버튼이 보이는지</b> 봤어요. 비어 보이면 맨 아래 "막히면"의 "화면이 비어 보여요"를 봐요</span></label>
</div>
<details><summary>프롬프트 쓰는 법과 허락 창 (어제 못 왔으면 꼭 펼쳐 봐요)</summary><div class="body">
<ol><li>박스를 누르면 복사돼요. Claude Code 입력창에 붙여 넣고 보내요.</li><li>프롬프트 하나는 보통 1분 안팎이에요. 화면과 링크를 확인하는 P1은 1~2분, P2는 3~6분, 웹을 찾아보는 C0은 2~3분 걸려요. 멈춘 게 아니에요. 다만 답이 한참 그대로면 허락 창이 떠 있는지 봐요.</li><li>mvp.html 같은 화면 파일은 답에 나온 파일 이름을 누르면 옆 창에 열려요. 글 파일(.md)은 리모컨 "파일 내용 보기"로 봐요.</li><li>Claude의 답 끝에 "다음에 할 일"이 나와도 이 가이드의 다음 박스를 따라가요.</li><li>번호가 붙은 프롬프트는 전부 수업 전에 실제로 돌려 보고 넣었어요. 크롬 확장 상자 하나만 돌려 보지 못했어요.</li></ol>
<p><b>허락 창</b> · 방금 보낸 프롬프트가 시킨 일이면 Yes를 눌러요. 파일 만들기와 고치기, 웹 검색, 웹페이지 열기, 폴더 만들기, 브라우저 열기, 링크 만들기가 그래요. 고치기 전 파일을 남길 때 cp(파일 복사) 명령 창이 뜰 수 있어요. 파일이나 폴더를 통째로 지우겠다고 하면(rm, delete) 누르지 말고 강사를 불러요.</p></div></details>
<div class="card" id="profileCard">
<h3>내 일과 회사를 적어요</h3>
<p class="sub">여기 적은 것이 프롬프트의 <b class="tok">파란 글자</b>로 들어가요. 오늘 가이드는 새 페이지라 어제 적은 것이 남아 있지 않아요. 어제와 같으면 비워 둬도 돼요. P0이 CLAUDE.md에 이미 적힌 하고 싶은 일과 회사를 그대로 둬요.</p>
<div class="field"><label for="v-role">내가 하고 싶은 일. 예: 콘텐츠 마케터, MD, CX 기획자, 서비스 기획자, 데이터 분석가</label><input id="v-role" data-in="role" type="text" maxlength="40" placeholder="비워 두면: 아직 모름 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<p class="sub">회사를 오늘 바꾸려면 세 칸을 모두 적어요. 비워 두면 어제 CLAUDE.md에 적힌 회사로 해요. 그것도 없으면 수업 연습용 회사(라라스윗)로 해요.</p>
<div class="field"><label for="v-brand">회사(브랜드) 이름</label><input id="v-brand" data-in="brand" type="text" maxlength="40" placeholder="비워 두면: 라라스윗 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-product">제품·서비스 한 줄</label><input id="v-product" data-in="product" type="text" maxlength="60" placeholder="비워 두면: 저당 아이스크림 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-customer">그 회사의 고객 한 줄</label><input id="v-customer" data-in="customer" type="text" maxlength="90" placeholder="비워 두면: 라라스윗 고객 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<button class="ghost" id="resetProfile" type="button">처음 값으로 되돌리기</button>
</div>
<div class="card soft"><p><b>어제 오후 E(스킬)를 만들었다면</b> 오늘은 수요일 발표 전까지 "오늘 조사 돌려줘"를 보내지 않아요. 테스트하는 동안 화면이 바뀌면 1차와 2차를 비교할 수 없어요.</p></div>
<div class="card soft"><p><b>P0은 어제 규칙을 그대로 두고 오늘 규칙만 더해요.</b> 오늘 더하는 것은 "사람 테스트 결과는 내가 적은 말 그대로 옮긴다, 지어내지 않는다"예요. 써 보는 사람이 하지 않은 말이 결과서에 들어가면 테스트가 의미 없어지거든요.</p></div>
'''+box('p00','P0 · 오늘의 작업 규칙 이어 쓰기 (꼭)',PR['p00'])+'''
<h3 class="gap">어제 조사 도우미가 없으면 · C0</h3>
<div class="card"><p class="sub">어제 수업에 없었거나 폴더를 잃어버렸으면, 어제의 조사 설계서(mvp.md) → 조사 표(research.csv) → 보는 화면(mvp.html)을 한 번에 만들어요. 2~3분 걸려요. 이미 있는 파일은 다시 만들지 않아요. 조사할 것을 정하지 못했으면 비워 둬요. 하고 싶은 일에 맞춰 Claude가 골라요.</p></div>
'''+field('pick','조사할 것 (어제와 같은 보기: 광고 소재, 경쟁사 가격, 증정품·프로모션, 상세페이지, 팝업스토어, 교육 프로그램, 경쟁 서비스 기능. 모르면 비워 둬요)','비워 두면: 네가 정해줘')+'\n'+box('c00','C0 · 어제 조사 도우미를 한 번에 만들기 (없을 때만)',PR['c00'])+'''
<h3 class="gap" id="remote">리모컨 여덟 개 · 필요할 때만 꺼내 써요</h3>
<details><summary>리모컨 펼치기 (지금 보내는 상자가 아니에요)</summary><div class="body">
<p class="sub">하루 중에 Claude가 마음에 안 들게 움직이면 긴 설명 대신 이 짧은 상자를 보내요.</p>
'''+box('r1','되물을 때',R['r1'])+'\n'+box('r2','말이 길 때',R['r2'])+'\n'+box('r3','자료가 없다고 멈췄을 때',R['r3'])+'\n'+box('r6','파일 내용 보기',R['r6'])+'\n'+box('r8','시켜 볼 일 카드 다시 보기 (테스트 직전에)',R['r8'])+'\n'+box('r9','정답과 질문 보기 (나만 볼 것)',R['r9'])+'\n'+box('r10','결과서 보기',R['r10'])+'\n'+box('r11','광고 규정 점검 (화장품, 식품, 병원, 금융)',R['r11'])+'''
</div></details>
</section>

<section id="s2">
<span class="eyebrow">① 테스트 준비 · 09:40–10:20 · 1교시</span>
<h2>사용자 테스트가 무엇인지 알고, 시켜 볼 일 카드를 만들어요</h2>
<p class="why"><b>왜 해요?</b> 만든 사람은 어디를 누르면 되는지 이미 알아서, 내 눈으로는 고칠 곳이 안 보여요. 처음 쓰는 사람에게 할 일을 주고 지켜봐야 보여요.</p>
<div class="story"><span class="tag">현업 이야기 · 강사님</span>
<p>새 홈페이지를 열려는 광고 대행사가 있었어요. 홈페이지를 만들기 전에 경쟁사 분석을 했고, 경쟁사 홈페이지에 5~6명이 다 같이 들어가서 어떤 위치에 어떤 메뉴가 있고, 어떤 사진에 어떤 메시지가 나오는지 보면서 평가했어요. 상당히 좋은 인사이트가 나왔고, 경쟁사 홈페이지가 저지른 오류를 넣지 않은 좋은 버전의 홈페이지 UX<span class="ab">(User Experience)</span>, UI<span class="ab">(User Interface)</span>를 설계했어요.</p></div>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px" id="usertest"><h3>사용자 테스트가 뭐예요?</h3>
<p><b>뜻</b> · 진짜 쓸 사람(오늘은 그 역할을 맡은 다른 조 학생)에게 일을 시켜 보고, 혼자 해내는지 옆에서 지켜보며 막히는 곳을 찾는 일이에요. 목적은 사람을 평가하는 게 아니라 <b>화면을 평가</b>하는 거예요.</p>
<p><b>쉽게 말하면</b> · 처음 오는 친구에게 우리 집 가는 길 안내문만 주고, 어디서 헤매는지 지켜보는 것과 같아요. 친구가 헤맨 곳이 안내문의 고칠 곳이에요. 같이 걸어가며 알려 주면 안내문의 문제를 영영 몰라요.</p>
<div class="grid" style="margin-top:12px">
<div class="card red"><h3>사용자 테스트가 아니에요</h3><ul><li>"어때요? 괜찮아요?"라고 묻기. 다들 친절하게 "좋아요"라고 해요</li><li>옆에서 설명해 주며 같이 하기</li><li>만든 내가 직접 써 보기</li></ul></div>
<div class="card ok"><h3>사용자 테스트예요</h3><ul><li>시켜 볼 일을 주고, 돕지 않고 지켜보기</li><li>해냈나, 걸린 초, 멈춘 곳, 한 말을 그대로 적기</li><li>여러 명이 같은 곳에서 멈추면, 그곳부터 고치기</li></ul></div>
</div>
<ol class="steps" style="margin-top:16px"><li><b>시켜 볼 일 정하기</b> · 진짜 쓸 사람이 이 화면으로 하는 일 세 가지. 현업에서는 '과업'이라고 불러요 <small>1교시 · P1</small></li><li><b>사람 전에 자동 점검</b> · 버튼, 링크, 폰 화면 <small>2교시 · P2</small></li><li><b>사람 테스트</b> · 다른 조 2명 <small>3교시</small></li><li><b>고칠 순서 정해 두 곳 고치기</b> → MVP v1 <small>4교시 · P3, P4</small></li><li><b>한 번 더 테스트</b> <small>오후 A · P5</small></li></ol></div>
<div class="card soft"><p><b>어제 오후 D(짝꿍 테스트)를 했다면 오늘은 두 번째 테스트예요.</b> 어제는 같은 조 1명이 5초 보기와 1분 써 보기를 했고, 오늘은 다른 조 2명이 시켜 볼 일 3개를 해요. P1이 어제 mvp.md에 적은 "다음에 확인할 숫자"를 오늘 성공 기준에 넣어요.</p></div>
<details><summary>직무마다 사용자 테스트는 이렇게 생겼어요</summary><div class="body">
<p class="sub">하는 방법은 같아요. 할 일을 주고, 지켜보고, 숫자로 적어요. 무엇을 테스트하는지만 달라요.</p>
<div class="pairs">
'''+ROLE_ROWS+'''
</div></div></details>
<span class="pill">따라 하기</span>
<div class="card soft" style="margin-top:12px"><p><b>진짜 쓸 사람</b>은 내 조사 결과를 매일 받아 볼 사람이에요. 예: "같은 팀 MD 선배", "매일 아침 광고 리포트를 받는 팀장", "새 기능 소식을 매주 받는 서비스 기획 팀장". 아래 칸에 적어요. 모르면 비워 두세요. CLAUDE.md와 mvp.md를 보고 Claude가 정해요. 오늘 테스트는 다른 조 학생이 그 사람 역할을 맡아요.</p></div>
'''+field('user','진짜 쓸 사람 (모르면 비워 둬요). 예: 매일 아침 가격 표를 받는 MD 팀장','비워 두면: 네가 정해줘')+'\n'+box('p01','P1 · 사용자 테스트 설계서 (꼭)',PR['p01'])+'''
<div class="card soft"><p><b>내 결정 1 · 시켜 볼 일 확인하기.</b> 시켜 볼 일 카드 세 장을 소리 내어 읽어 봐요. 진짜 쓸 사람이 이 화면으로 매일 하려는 일인지, 카드에 정답이나 "○○ 버튼을 누르세요"가 들어 있지 않은지 봐요. 맞으면 "그대로 갈게. 이유는 ○○.", 바꿀 것이 있으면 "2번 시켜 볼 일은 ○○로 바꿔줘. test.md도 고쳐줘."라고 한 줄 말해요.</p></div>
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="b1"><span>답에 <b>역할 한 줄과 시켜 볼 일 카드 3장</b>이 보여요</span></label>
<label class="check"><input type="checkbox" data-k="b2"><span>카드에 정답이나 누를 곳이 <b>들어 있지 않아요</b></span></label>
<label class="check"><input type="checkbox" data-k="b3"><span>시켜 볼 일을 확인하고 Claude에게 한 줄 말했어요 (내 결정 1)</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 리모컨 <b>"정답과 질문 보기"</b>로 끝나고 물을 질문 3개를 보고, 구글 폼에 옮겨 두세요(선택). 써 보는 사람이 폼으로 답할 수 있어요. 시켜 볼 일 카드와 정답을 종이에 옮겨 적는 것은 2교시 P2가 끝난 뒤에 해요. P2가 화면의 틀린 값을 고치면서 정답이 달라질 수 있어요.</p></div>
</section>

<section id="s3">
<span class="eyebrow">① 테스트 준비 · 10:20–11:00 · 2교시</span>
<h2>사람에게 보이기 전에 에이전트가 먼저 점검해요</h2>
<p class="why"><b>왜 해요?</b> 버튼이 안 눌리는 화면을 사람에게 보이면, 테스트 시간이 고장 찾기로 끝나요. 고장은 에이전트가 먼저 찾고, 사람에게는 "헷갈리는 곳"을 찾게 해요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>자동 점검과 사람 테스트는 찾는 것이 달라요</h3>
<ul><li><b>자동 점검(에이전트)</b> · 동작하지 않는 버튼, 열리지 않는 링크, 폰에서 넘치는 글자처럼 <b>고장</b>을 찾아요. 빨라요. 다만 P2는 화면 파일의 코드를 읽고 판단해서, 확인하지 못한 곳은 (확인 필요)로 남겨요. 그건 내가 직접 눌러 봐요.</li><li><b>사람 테스트</b> · "이 숫자가 뭐지?", "어디를 눌러야 하지?"처럼 <b>헷갈림</b>을 찾아요. 에이전트는 화면을 처음 보는 사람의 마음을 몰라요.</li><li>그래서 순서가 <b>자동 점검 → 막힘만 고치기 → 사람 테스트</b>예요. 막힘이 아닌 것은 사람 테스트 뒤에 한꺼번에 고칠 순서를 정해 고쳐요.</li></ul></div>
<span class="pill">따라 하기</span>
<p class="sub" style="margin-top:12px"><b>P2는 3~6분 걸려요.</b> 시켜 볼 일마다 화면을 따라가고 링크도 확인해서 길어요. 도는 동안 아래의 Claude in Chrome을 설치해요. 시켜 볼 일 카드와 정답은 P2가 끝난 뒤(10:45 준비)에 종이에 옮겨 적어요.</p>
'''+box('p02','P2 · 사람 전에 자동 점검 (꼭)',PR['p02'])+'''
<h3 class="gap">P2가 도는 동안 · Claude in Chrome 설치 (다 같이)</h3>
<p class="sub">P2가 도는 3~6분 동안 설치해요. 바로 아래에서 Claude가 내 화면을 직접 눌러 보며 점검할 때 써요. 강사님 화면을 보며 같이 해요. 결제나 회원 가입처럼 돈과 개인정보가 오가는 일은 Claude in Chrome이 하지 않게 되어 있어요.</p>
<div class="card"><ol class="steps">
<li><b>Chrome</b> 브라우저를 열어요. 없으면 먼저 설치해요. Edge, 웨일 같은 다른 브라우저 말고 Chrome으로 해요.</li>
<li>Chrome 웹 스토어에서 <b>Claude</b>를 찾아요. 만든 곳이 <b>Anthropic</b>인지 확인하고 <b>Chrome에 추가</b>를 눌러요. 강사님이 링크를 주면 그 링크로 가요.</li>
<li>오른쪽 위 퍼즐 모양 아이콘을 누르고 Claude 옆 <b>압정</b>을 눌러 고정해요.</li>
<li>Claude 아이콘을 눌러 <b>Claude Code와 같은 계정</b>으로 로그인해요. 권한을 묻는 창이 뜨면 허용해요. Claude가 화면을 읽고, 누르고, 입력하는 데 필요한 권한이에요.</li>
<li>주소창에 <b>chrome://extensions</b>를 쳐요. Claude의 <b>세부정보</b>를 누르고 <b>파일 URL에 대한 액세스 허용</b>을 켜요. 내 폴더의 mvp.html을 Chrome에서 Claude가 볼 수 있게 하는 거예요.</li>
<li>Claude 아이콘을 눌러 <b>옆 창</b>이 열리는지 봐요. 바로 아래에서 이 옆 창에 상자를 보내요.</li>
</ol>
<p class="sub">설치가 안 돼도 수업은 그대로 가요. P2의 자동 점검이 화면 파일을 읽어서 점검해요. 설치는 쉬는 시간에 강사님과 마저 해요.</p></div>
<div class="card soft"><p><b>내 결정 2 · 진짜인지 확인하기.</b> 표에서 상태가 <b>"남음"</b>이거나 <b>(확인 필요)</b>인 줄 하나를 골라 mvp.html을 열고 직접 눌러 봐요. "고침"인 줄은 이미 고쳐져서 눌러 봐도 잘 돼요. 폰 폭 문제는 브라우저 창을 폰만큼 좁혀 봐요. 맞으면 "○○은 내가 눌러 봤어. 맞아.", 아니면 "○○은 눌러 보니 잘 돼. auto_check.md에 적어줘."라고 한 줄 말해요.</p></div>
<div class="card"><h3>다 같이 · Claude in Chrome으로 직접 눌러 보며 점검</h3>
<p>P2는 화면 파일의 코드를 읽고 점검해요. 크롬 확장(Claude in Chrome)은 화면을 <b>직접 눌러 보며</b> 점검해요. 강사님 화면을 보며 다 같이 해요.</p>
<p class="sub">방금 설치한 Claude in Chrome으로 해요. 크롬에서 mvp.html을 열고(파일을 크롬 창에 끌어다 놓아요), 크롬의 Claude 옆 창에 아래 상자를 보내요. P1의 시켜 볼 일 카드 세 장을 아래 칸에 붙이면 그 시켜 볼 일로 해요. 크롬이 내 컴퓨터 파일을 못 열면, 마무리의 "화면을 링크로 만들기"로 링크를 만들어 그 링크를 열어요. <b>이 상자는 크롬 확장 화면이라 수업 전에 돌려 보지 못했어요.</b></p></div>
'''+fieldwide('cards','시켜 볼 일 카드 세 장 (P1의 답에서 복사해 붙여요)','비워 두면: 적지 않음')+'\n'+box('chk','크롬 확장에서 보내기 (다 같이, 시험 못 함)',PR['chk'])+'''
<p class="sub">크롬 확장이 안 되면 넘어가요. P2의 자동 점검 결과와 내 결정 2(직접 눌러 보기)로 충분해요. 설치는 쉬는 시간에 강사님과 마저 해요.</p>
<h3 class="gap">10:45부터 · 3교시 테스트 준비</h3>
<div class="card"><ol><li><b>종이 한 장</b>을 준비해요. 테스트하는 동안에는 써 보는 사람이 내 노트북을 쓰니까, 기록은 종이에 적었다가 나중에 입력 칸에 옮겨요. 휴대폰은 타이머로 써요.</li><li>리모컨 <b>"시켜 볼 일 카드 다시 보기"</b>와 <b>"정답과 질문 보기"</b>로 역할 한 줄, 시켜 볼 일 카드 3장, 정답, 질문 3개를 종이에 옮겨 적어요. P2가 시켜 볼 일 문장이나 정답을 고쳤을 수 있어서, P2가 끝난 지금 보는 것이 맞아요.</li><li>아래 상자로 mvp.html을 <b>브라우저로 열어</b> 둬요. 3교시가 시작되면 Claude Code 창과 이 가이드 탭은 내려 둬요. 써 보는 사람에게는 내 화면만 보여야 해요.</li></ol></div>
'''+box('open','브라우저로 열기',OPEN)+'''
<div class="card checks">
<h3>이 다섯 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="c1"><span>답에 <b>걸린 곳 표</b>가 보여요 (몇 번 일 / 무엇이 / 얼마나 심한지)</span></label>
<label class="check"><input type="checkbox" data-k="c2"><span>"막힘"이 있었다면 상태가 "고침"이에요. 고치기 전 화면은 mvp_before_check.html로 남았어요</span></label>
<label class="check"><input type="checkbox" data-k="c4"><span>P2가 끝난 뒤 mvp.html을 열어 <b>표와 버튼이 보이는지</b> 내 눈으로 봤어요 (자동 점검은 코드를 읽는 거라, 화면이 실제로 뜨는지는 내가 봐야 해요)</span></label>
<label class="check"><input type="checkbox" data-k="c3"><span>하나를 직접 눌러 보고 Claude에게 한 줄 말했어요 (내 결정 2)</span></label>
<label class="check"><input type="checkbox" data-k="c5"><span>역할, 시켜 볼 일 카드, 정답, 질문을 <b>종이에 옮겨 적고</b>, mvp.html을 브라우저로 열어 뒀어요</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 다른 조 사람에게는 3교시 전까지 내 화면을 보여 주지 말아요. 처음 보는 화면이어야 테스트가 돼요. 리모컨 "시켜 볼 일 카드 다시 보기"로 카드를 소리 내어 읽는 연습을 해요.</p></div>
</section>

<section id="s4">
<span class="eyebrow">② 테스트하고 고치기 · 11:00–12:00 · 3교시</span>
<h2>다른 조와 서로 테스트해요</h2>
<p class="why"><b>왜 해요?</b> 오늘의 핵심이에요. 처음 쓰는 사람이 어디서 멈추는지는 직접 지켜봐야만 알 수 있어요.</p>
<div class="card"><h3>이렇게 해요 · 12분씩 네 번, 강사님이 바꾸라고 말해요</h3>
<ol><li><b>짝 조</b> · 우리 반은 세 명 조와 두 명 조가 있어요. 강사님이 두 조씩 묶어 짝 조를 만들어요(세 명 조끼리면 여섯 명, 두 명 조끼리면 네 명). 만든 사람은 자기 자리에 앉아 있고, 상대 조 사람이 건너와 내 노트북 앞에 앉아 써 보는 사람이 돼요. 링크를 만들 필요 없어요. 두 조의 인원이 다르거나 다른 짝 조에서 한 명이 더 들어오면, 칸마다 한 사람이 쉬어요.</li><li><b>11:00</b> 한 조는 자리에서 테스트를 받고, 짝 조는 건너와 써 보는 사람 → <b>11:12</b> 써 보는 사람만 옆으로 한 칸 → <b>11:24</b> 두 조가 역할을 바꿔요 → <b>11:36</b> 써 보는 사람만 옆으로 한 칸 → <b>11:48–12:05</b> 내 자리에서 기록을 칸에 옮기기. 한 사람이 테스트를 두 번 받고 두 번 해 줘요. 어느 조가 먼저 받는지는 강사님이 알려 줘요.</li><li><b>어제 내 화면을 본 사람</b>(어제 옆 조 5초 보기나 짝꿍 테스트)은 피해요. 어쩔 수 없으면 기록에 "어제 봄"이라고 적어요.</li><li><b>시작할 때 이렇게 말해요</b> · "오늘 당신은 <b>(역할 한 줄)</b>이에요. 이건 당신을 시험하는 게 아니라 화면을 시험하는 거예요. 생각나는 걸 소리 내어 말하면서 해 주세요. 저는 돕지 않고 지켜만 볼게요."</li><li><b>시켜 볼 일 카드를 한 장씩 읽어 주고</b> 휴대폰 타이머로 시간을 재요.</li><li><b>돕지 않아요</b> · 써 보는 사람이 "이거 눌러요?"라고 물으면 "어떻게 하실 것 같아요?"라고만 되물어요. 설명하고 싶은 순간이 바로 고칠 곳이에요. 1분 넘게 막히면 힌트를 <b>한 번</b>만 줄 수 있어요. 힌트를 줬으면 "도움 받고", 2분이 지나도 못 끝내면 "못 함", 틀린 답으로 끝내면 "못 함(틀린 답)"으로 적고 다음 카드로 가요.</li><li><b>적어요</b> · 시켜 볼 일마다 해냈나, 걸린 초, 멈춘 곳, 써 보는 사람이 한 말을 그대로 종이에 적어요. 끝나면 질문 3개를 물어요. 점수는 써 보는 사람이 종이에 직접 적게 해요(구글 폼을 만들었으면 폼으로).</li><li><b>다음 사람 전에</b> 화면을 새로고침하고 열린 탭을 닫아요. 앞사람이 눌러 둔 상태로 시작하지 않게요.</li></ol></div>
<div class="card"><h3>내가 써 보는 사람일 때</h3>
<ul><li>역할 한 줄의 사람처럼 해요. 이 화면을 처음 본 그 사람이라고 생각해요.</li><li>보이는 것과 하려는 것을 계속 소리 내어 말해요. "음, 여기 누르면 될 것 같은데…"</li><li>끝났으면 "끝, 답은 ○○"라고 말해요. 그래야 시간을 멈출 수 있어요.</li><li>못 하겠으면 "모르겠어요"라고 말해도 돼요. 그것도 중요한 기록이에요.</li><li>"색을 바꾸면 좋겠어요" 같은 조언 말고, 겪은 것만 말해요. 점수는 솔직하게 종이에 직접 적어요.</li></ul></div>
<div class="card soft"><p><b>적을 때는 내 해석 말고 본 것과 들은 것을 적어요.</b> "걸러 보기가 불편해 보였음"보다 "걸러 보기 버튼을 세 번 지나침. '영상만 보는 건 어디 있어요?'"가 고칠 곳을 정확히 알려 줘요. 칸에 적은 것이 그대로 기록이 돼서, P3가 고치지 않고 옮겨요.</p></div>
'''+fieldwide('obs1','써 본 사람 1의 기록. 예: 1번 혼자 35초 / 2번 못 함, 걸러 보기에서 멈춤 "영상만 보는 건 어디 있어요?" / 3번 도움 받고 70초 / 쉬웠나 3점','비워 두면: 적지 않음')+'\n'+fieldwide('obs2','써 본 사람 2의 기록','비워 두면: 적지 않음')+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="t1"><span>다른 조 사람 <b>2명</b>이 내 화면으로 시켜 볼 일 3개를 해 봤어요 (1명이어도 괜찮아요)</span></label>
<label class="check"><input type="checkbox" data-k="t2"><span>시켜 볼 일마다 해냈나, 걸린 초, 멈춘 곳, 한 말을 칸에 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="t3"><span>나도 다른 사람의 써 보는 사람이 돼 줬어요</span></label>
</div>
</section>

<section id="s5">
<span class="eyebrow">② 테스트하고 고치기 · 12:00–13:00 · 4교시</span>
<h2>고칠 순서를 정하고 두 곳을 고쳐 MVP v1을 만들어요</h2>
<p class="why"><b>왜 해요?</b> 다 고치려면 끝이 없어요. 여러 명이 겪었고 할 일을 막은 것부터 고치면, 적게 고치고 많이 나아져요.</p>
<div class="story"><span class="tag">현업 이야기 · 강사님</span>
<p>예전에는 랜딩페이지나 상세페이지 하나를 바꾸는 데 <b>1주에서 2주</b>가 걸렸어요.</p></div>
<p class="sub">오늘 P4가 두 곳을 고치고 결과서를 쓰는 데 걸린 시간은 수업 전 시험에서 <b><!--P4TIME--></b>였어요.</p>
<span class="pill">따라 하기</span>
<p class="sub" style="margin-top:12px"><b>12:05부터 P3를 보내요.</b> 3교시에 적은 두 칸이 그대로 P3에 들어가요. 칸을 비웠으면 P3는 결과를 지어내지 않고 "사람 테스트 전"으로 적어요.</p>
'''+box('p03','P3 · 테스트 기록 정리와 고칠 순서 (꼭)',PR['p03'],TOP)+'''
<div class="card soft"><p><b>내 결정 3 · 고칠 곳 고르기.</b> P3가 보여 준 고칠 곳 목록에서 오늘 고칠 두 곳을 골라 아래 칸에 적어요. 예: "1번, 3번. 3번은 두 사람 모두 말해서". 비워도 괜찮아요. Claude가 추천한 두 곳을 고쳐요. 추천대로 가기로 했으면 "추천대로 갈게. 이유는 ○○."라고 한 줄 말해 두면 내 결정으로 남아요. 써 보는 사람이 모두 혼자 해냈으면 가장 오래 걸린 시켜 볼 일, 써 보는 사람이 한 말, 자동 점검에서 "남음"인 것 가운데 두 곳을 골라요.</p></div>
'''+field('fix','오늘 고칠 두 곳과 이유 (비우면 Claude가 추천한 두 곳)','비워 두면: 네가 추천한 두 곳')+'\n'+box('p04','P4 · 두 곳 고쳐 MVP v1, 사용자 테스트 결과서 (꼭)',PR['p04'])+'\n'+box('cmp','고치기 전과 뒤를 나란히 열기',CMP)+'''
<p class="sub">결과서(test_report.md)는 리모컨 "결과서 보기"로 봐요.</p>
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="e1"><span>mvp.html에서 <b>고른 두 곳</b>이 바뀌었어요. 다른 곳은 그대로예요</span></label>
<label class="check"><input type="checkbox" data-k="e2"><span>test_report.md가 생겼고, 시켜 볼 일마다의 결과에 <b>내가 적은 기록의 숫자</b>만 "○명 중 ○명"으로 있어요</span></label>
<label class="check"><input type="checkbox" data-k="e3"><span>(점심 전에 되면) 같은 사람에게 고친 곳의 시켜 볼 일만 다시 해 보게 하고, "test_report.md에 같은 사람이 다시 해 본 시간 ○초(참고용)를 적어줘"라고 말했어요</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 수요일 라이브 데모 30초를 소리 내어 연습해요. 화면에서 무엇을 누르고 무엇을 보여 줄지 세 단계로요. 3교시에 테스트를 덜 받은 사람이 있으면 써 보는 사람이 돼 줘요.</p></div>
</section>

<section id="s6">
<span class="eyebrow">③ 심화와 발표 준비 · 14:00–16:00 · 오후(각자)</span>
<h2>메뉴에서 골라 더 해 봐요</h2>
<p class="why"><b>왜 해요?</b> 테스트는 한 번으로 끝나지 않아요. 고친 것이 정말 나아졌는지, 다른 표를 넣어도 도는지, 남에게 어떻게 보여 줄지까지 가 봐요. 하나만 해도 되고, 여러 개를 해도 돼요.</p>
<div class="grid">
<div class="card path"><h3>A · 한 번 더 테스트</h3><p class="sub">고친 화면을 <b>새 사람</b> 한 명에게 같은 시켜 볼 일로 테스트하고 1차와 비교해요.</p><p class="sub"><b>끝나면</b> test_report.md에 1차 → 2차 비교 표가 생겨요.</p><p><b>P5</b> · 테스트 12분 + 1분</p></div>
<div class="card path"><h3>B · 통과 기준과 샘플 데이터</h3><p class="sub">쉼표가 든 값, 빈 칸, 100줄짜리 표를 넣어도 화면이 도는지 기준을 세우고 확인해요. 테크 트랙에 추천해요.</p><p class="sub"><b>끝나면</b> data_check.md(기준별 통과·실패)와 samples 폴더의 시험용 표 3개. 샘플을 화면에서 직접 골라 열어 보면 끝이에요.</p><p><b>P6</b> · 4~6분</p></div>
<div class="card path"><h3>C · 15초 숏폼 티저 콘티</h3><p class="sub">수요일 발표 첫머리에 틀 15초 영상을 계획해요. 영상 AI(Google Flow, Kling)에 붙일 프롬프트까지. 마케터에게 추천해요.</p><p class="sub"><b>끝나면</b> teaser.md(컷 3개, 자막, 영상 AI 프롬프트 2개, 크레딧 계획).</p><p><b>P7</b> · 1분 10초</p></div>
<div class="card path"><h3>D · 테스트 순서를 스킬로</h3><p class="sub">오늘 한 테스트 순서를 스킬로 묶어, 다음부터 "테스트 준비해줘" 한 줄로 시켜 볼 일 카드가 나오게 해요.</p><p class="sub"><b>끝나면</b> 새 대화에서 "테스트 준비해줘" 한 줄로 test.md가 다시 나와요.</p><p><b>P8</b></p></div>
<div class="card path"><h3>E · 녹화로 동선 보기 (Clarity)</h3><p class="sub">무료 도구 Microsoft Clarity를 화면에 달아 인터넷에 올리고, 써 보는 사람이 어디를 누르고 어디서 헤맸는지 녹화와 히트맵으로 봐요.</p><p class="sub"><b>끝나면</b> 남이 여는 주소 하나, Clarity에 쌓이는 녹화, test_report.md의 "녹화로 본 것".</p><p><b>P10, P11</b> · 40분</p></div>
</div>
<p class="sub">고르기 어려우면 <b>A부터</b> 해요. 그다음 마케터·MD는 C, 테크 트랙은 B, 스킬 파일을 키우는 사람은 D, 클릭 동선을 녹화로 보고 싶은 사람은 E를 해요. E는 A와 같이 하면 좋아요(2차 테스트를 올린 주소로). A와 B는 둘 다 mvp.html을 고쳐서, 둘 다 하면 A를 먼저 해요. 2차 테스트는 4교시에 고친 화면 그대로 봐야 1차와 비교가 돼요.</p>
<div class="card soft"><p><b>내 결정 4 · 메뉴 고르기.</b> 고른 메뉴와 이유를 Claude에게 한 줄로 말해 둬요. 예: "A를 골랐어. 이유는 두 사람 모두 2번 시켜 볼 일에서 멈춰서." 저녁 포트폴리오에 내 결정으로 남아요.</p></div>

<h3 class="gap">A · 한 번 더 테스트</h3>
<div class="card"><p class="sub">오전이나 어제 내 화면을 본 적 없는 사람에게 부탁해요. A를 고른 사람끼리 손을 들어 서로 써 보는 사람이 돼 주면 빨라요. 오전과 같은 방법(자리 바꾸기, 시켜 볼 일 카드 읽어 주기, 돕지 않기)으로 하고 아래 칸에 적어요. 15:45가 지나면 새 테스트는 시작하지 않아요.</p></div>
'''+fieldwide('obs3','써 본 사람 3의 기록 (고친 화면으로)','비워 두면: 적지 않음')+'\n'+box('p05','P5 · 한 번 더 테스트하고 1차와 비교 (A)',PR['p05'])+'''

<h3 class="gap">B · 통과 기준과 샘플 데이터</h3>
<div class="card"><p class="sub">현업에서는 매일 다른 표가 들어와요. 오늘 표로는 잘 돌아도, 내일 쉼표 하나에 칸이 밀리면 아무도 안 써요. 수업 전 시험에서도 칸 이름의 쉼표 하나로 표 전체가 밀린 적이 있어요.</p></div>
'''+box('p06','P6 · 통과 기준을 세우고 샘플 데이터로 확인 (B)',PR['p06'])+'''
<div class="card"><p class="sub">P6의 표는 코드를 읽고 판단한 결과예요. P6이 알려 준 순서대로 화면에서 샘플 CSV를 하나씩 골라 직접 열어 봐요. 본 대로 "sample1을 열어 보니 칸이 밀려. data_check.md에 '열어 봄'으로 적어줘."처럼 말해요. 직접 열어 본 줄이 포트폴리오에 쓸 근거가 돼요.</p></div>

<h3 class="gap">C · 15초 숏폼 티저 콘티</h3>
<div class="card"><p class="sub">P7이 만든 영상 AI 프롬프트를 Google Flow나 Kling에 붙여 영상을 뽑아요. 무료 크레딧이 안 되거나 다 썼으면, 2컷(내 화면 녹화)만으로도 수요일 발표에 쓸 수 있어요. 화면 녹화는 윈도우 Win+Alt+R, 맥 ⌘⇧5예요.</p></div>
'''+box('p07','P7 · 15초 숏폼 티저 콘티 (C)',PR['p07'])+'''
<p class="sub">화장품, 식품, 병원, 금융처럼 광고 규정이 있는 업종이면 P7 다음에 리모컨 <b>"광고 규정 점검"</b>을 한 번 보내요.</p>

<h3 class="gap">D · 테스트 순서를 스킬로</h3>
'''+box('p08','P8 · 오늘 한 테스트 순서를 스킬로 묶기 (D)',PR['p08'])+'''
<div class="card"><p><b>스킬이 되는지 확인해요.</b> Claude Code에서 <b>같은 작업 폴더</b>로 <b>새 대화</b>를 열고 아래 한 줄을 보내요. 오전의 test.md가 있으면 스킬이 test_날짜.md로 새로 써서 오전 파일은 그대로 남아요. 확인이 끝나면 <b>아침에 쓰던 대화로 돌아가요.</b> 왼쪽 대화 목록에서 아침 대화를 눌러요. 16시와 W2는 그 대화에서 해요.</p></div>
'''+box('run','스킬로 테스트 준비하기 (새 대화에서)',RUN)+'''
<h3 class="gap">E · 녹화로 동선 보기 (Clarity)</h3>
<div class="card"><p><b>Clarity가 뭐예요?</b> 마이크로소프트가 무료로 주는 웹 분석 도구예요. 화면에 코드 한 덩어리를 달면, 들어온 사람이 무엇을 눌렀고 어디서 스크롤을 멈췄는지 <b>녹화</b>와 <b>히트맵</b>(많이 누른 곳이 빨갛게 보이는 지도)으로 보여 줘요. 매장 천장의 CCTV와 비슷해요. 그래서 내 컴퓨터 파일이 아니라 <b>인터넷 주소</b>에 올린 화면에만 달 수 있어요.</p><p class="sub">현업에서는 쇼핑몰 상세페이지, 이벤트 페이지, 신청서에 달아 두고 사람들이 어디서 멈추고 나가는지를 봐요. 오늘은 종이에 적은 기록과 녹화를 견줘요.</p></div>
<div class="card"><h3>이렇게 해요</h3><ol class="steps">
<li><b>clarity.microsoft.com</b>에 들어가 <b>마이크로소프트 계정</b>으로 가입해요(무료).</li>
<li><b>새 프로젝트</b>를 만들어요. 이름은 "내 MVP", 웹사이트 주소는 아직 없으니 아무 주소나 넣고, 6번에서 받은 주소로 설정에서 고쳐요.</li>
<li>설치 방법을 고르는 화면에서 <b>직접 설치(코드 복사)</b>를 골라요. 코드 맨 끝 <b>따옴표 안의 영문·숫자</b>가 프로젝트 ID예요. 아래 칸에 적어요. 강사님 화면을 같이 봐요.</li>
<li><b>P10</b>을 보내요. deploy 폴더가 생기고, 그 안의 index.html에 Clarity 코드가 들어가요. 오늘의 mvp.html은 그대로예요.</li>
<li>아래 "작업 폴더 열기"로 폴더를 열고, 브라우저에서 <b>app.netlify.com/drop</b>에 들어가 <b>deploy 폴더를 통째로 끌어다 놓아요.</b> 1분 안에 주소가 나와요.</li>
<li>로그인하지 않고 올렸으면 <b>1시간 안에</b> 화면의 안내대로 무료 가입해 내 것으로 옮겨야 주소가 남아요. 처음부터 Netlify에 가입하고 올리면 편해요.</li>
<li>받은 주소를 폰으로 열어 몇 번 눌러 보고, Clarity 화면에서 방문이 들어오는지 봐요. 실시간 방문은 곧 보이고, <b>녹화와 히트맵은 뜨는 데 최대 2시간쯤</b> 걸려요.</li>
<li>2차 테스트(A)를 이 주소로 해요. 시작 전에 <b>"화면에서 누르는 것을 녹화해요. 괜찮아요?"</b>라고 묻고 동의를 받아요.</li>
<li>17시나 내일 아침에 Clarity의 <b>녹화(Recordings)</b>와 <b>히트맵(Heatmaps)</b>을 보고, 본 것을 아래 칸에 적어 <b>P11</b>을 보내요. 히트맵 캡처는 내일 발표 화면에 넣어도 좋아요.</li>
</ol></div>
'''+box('fold2','작업 폴더 열기','이 작업 폴더를 파일 탐색기(맥은 Finder)로 열어줘.')+'\n'+field('clarity','Clarity 프로젝트 ID (코드 맨 끝 따옴표 안의 영문·숫자)','비워 두면: 적지 않음')+'\n'+box('p10','P10 · 올릴 폴더 만들고 Clarity 코드 넣기 (E)',PR['p10'])+'''
<div class="card warn"><p><b>녹화는 개인정보예요.</b> 동의한 사람만 테스트하고, 수업이 끝나면 Netlify에서 사이트를 지우거나 Clarity 프로젝트를 지워도 돼요. 카드 번호, 주민번호처럼 민감한 값을 넣는 화면에는 달지 않아요.</p></div>
'''+fieldwide('rec','녹화와 히트맵에서 본 것. 예: 2번 일에서 표 제목을 세 번 눌렀다 / 걸러 보기 버튼 옆 빈 곳을 누름 / 아래까지 내렸다 다시 올라옴','비워 두면: 적지 않음')+'\n'+box('p11','P11 · 녹화로 본 것을 결과서에 더하기 (E)',PR['p11'])+'''
<div class="card checks">
<h3>오후에 하나 이상 하면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="h1"><span>오후 메뉴에서 <b>하나 이상</b>을 끝냈어요. 고른 메뉴와 이유를 Claude에게 한 줄 말했어요 (내 결정 4)</span></label>
</div>
</section>

<section id="s7">
<span class="eyebrow">③ 심화와 발표 준비 · 16:00–17:00 · 다 같이</span>
<h2>내일 피칭의 뼈대, 일곱 칸을 세워요</h2>
<p class="why"><b>왜 해요?</b> 수요일은 피칭 데이예요. 내일 아침에는 이 뼈대로 HTML 발표 화면을 만들어요. 뼈대가 있으면 화면은 금방이에요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>피치가 뭐예요?</h3>
<p>짧은 시간에 듣는 사람이 <b>"해 보자"</b>라고 정하게 만드는 발표예요. 엘리베이터에서 팀장을 만나 1층에 닿기 전에 "그거 한번 써 보자"는 말을 듣는 것과 같아요.</p>
<p>내일은 각자 <b>내 MVP</b>를 발표해요. 조 안에서 한 사람씩 <b>3분</b>, 조마다 대표 한 명이 반 전체 앞에서 <b>5분 발표와 3분 질문</b>을 해요. 듣는 사람은 이 조사를 매일 하는 부서의 팀장과 동료라고 생각해요.</p>
<div class="pairs">
<div class="row"><span class="k">문제</span><span class="w"><b>누가 매일 무엇에 몇 분을 쓰나</b><small>어제 mvp.md에 적은 "하루 몇 분"</small></span></div>
<div class="row"><span class="k">해결</span><span class="w"><b>내 MVP가 해 주는 일 한 줄</b><small>화면 맨 위의 그 한 줄. 오후 C에서 영상 콘티를 만들었으면 영상 자리</small></span></div>
<div class="row"><span class="k">시장</span><span class="w"><b>이 조사를 매일 하는 신입과 그 팀이 얼마나 많은지</b><small>모르면 어림셈 식을 보여 주고 (가정)</small></span></div>
<div class="row"><span class="k">BM</span><span class="w"><b>돈이 되는 길</b><small>회사 안에서 쓰면 줄인 시간 × 쓰는 사람 수. 밖에 판다면 누가 얼마를 낼지</small></span></div>
<div class="row"><span class="k">MVP</span><span class="w"><b>라이브 데모 3단계와 테스트 숫자 하나</b><small>"다른 조 학생 ○명 중 ○명"처럼</small></span></div>
<div class="row"><span class="k">함께 만든 것</span><span class="w"><b>테스트해 준 사람, 에이전트가 한 일, 내가 내린 결정</b><small>공식 피치 구조의 "팀" 칸이에요. 개인 발표라 이렇게 바꿨어요</small></span></div>
<div class="row"><span class="k">요청사항</span><span class="w"><b>듣는 사람에게 바라는 것 하나</b><small>예: 일주일 써 볼 동료 3명, 실제 자료 접근</small></span></div>
</div>
<p class="sub" style="margin-top:12px">일곱 칸의 순서는 공식 일정표에 적힌 피치 구조예요. 칸마다 무엇을 넣을지는 오늘 가이드가 정한 예시예요.</p></div>
<span class="pill">따라 하기</span>
<div class="card" style="margin-top:12px"><h3>먼저 · 내 카드에 붙일 링크 만들기</h3>
<p>수요일 라이브 데모와 실습시트에 쓸 링크예요. 내 컴퓨터 주소(C:\\로 시작하는 경로, /Users/나 file://로 시작하는 주소, localhost)는 나만 열려요. 어제 링크가 있어도 고친 화면으로 새로 만들어요.</p>
'''+box('pub','화면을 링크로 만들기',PUB)+'''
<ol><li>허락 창이 뜨면 Yes를 눌러요. Claude가 링크를 알려 줘요.</li><li>열린 화면의 <b>공유</b> 메뉴에서 <b>링크가 있는 사람은 누구나</b>로 바꿔요.</li><li>로그인하지 않은 창(시크릿 창)에서 링크를 열어 화면이 보이는지 확인해요. 안 되면 "막히면"의 "링크가 안 만들어져요"를 봐요.</li></ol></div>
'''+field('ask','<b>내 결정 5</b> · 내일 발표에서 듣는 사람에게 바랄 것 하나 (요청사항)','비워 두면: 네가 정해줘')+'''
'''+box('p09','P9 · 내일 피치 뼈대 일곱 칸 (꼭)',PR['p09'])+'''
<div class="card soft"><p><b>[채울 곳]은 말로 채워요.</b> 예: "손으로 하면 하루 40분 걸려. pitch.md에 넣어줘." 발표에서 보여 줄 숫자를 바꾸고 싶으면 "발표에는 ○○을 보여 줄게. pitch.md를 고쳐줘."라고 해요.</p></div>
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="p1"><span>pitch.md가 생겼고, 일곱 칸의 첫 문장을 소리 내어 읽어 봤어요 (1분 안팎)</span></label>
<label class="check"><input type="checkbox" data-k="p2"><span>[채울 곳]이 남은 숫자 가운데 내일 아침까지 채울 것 하나를 골랐어요</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 짝에게 라이브 데모 3단계를 해 보고 걸린 시간을 재요. 30초를 넘으면 세 단계 가운데 하나를 빼고 pitch.md를 고쳐 달라고 해요.</p></div>
</section>

<section id="s8">
<span class="eyebrow">③ 심화와 발표 준비 · 17:00–18:00 · 마무리(다 같이)</span>
<h2>보여 주고, 적고, 퇴근해요</h2>
<p class="why"><b>왜 해요?</b> 테스트에서 무엇을 보고 무엇을 고쳤는지 적어 두면, 면접에서 "만들었어요"보다 한 걸음 더 말할 수 있어요.</p>
<div class="card"><h3>조 공유 · 한 사람 1분</h3><ol>
<li>고친 화면(MVP v1)을 띄워요.</li>
<li>한 문장으로 말해요: <b>테스트에서 무엇을 보고 놀랐고, 무엇을 고쳤나.</b></li>
<li>듣는 사람은 한마디만 해요. 고친 뒤 화면이 바로 이해되는지.</li>
</ol></div>
<div class="card"><h3>오늘을 포트폴리오 한 장으로 남겨요</h3>
<p><b>W2는 아침부터 쓰던 폴더와 대화에서 보내요.</b> Claude가 못 본 결정(구글 폼에서 받은 답, 새 대화에서 한 것, 영상을 뽑은 것)은 W2를 붙여 넣은 뒤 보내기 전에 맨 아래에 한 줄씩 적어요. 줄을 바꿀 때는 Shift+Enter를 눌러요.</p>
'''+box('w2','W2 · 오늘을 포트폴리오 한 장으로 (꼭)',PR['w2'])+'''
<div class="card soft" style="margin-top:12px"><p><b>[내가 적을 곳]은 말로 채워요.</b> 예: "2번을 고른 이유는 두 사람 모두 거기서 멈췄기 때문이야. 포트폴리오에 적어줘." 면접에서 말할 세 문장부터 채워요.</p></div></div>
<div class="card"><h3>링크를 실습시트에 적어요</h3><p>16시에 만든 링크를 실습시트에 적어요. 아직 안 만들었으면 16시의 "화면을 링크로 만들기"를 보내요. 오후에 화면을 더 고쳤으면 링크를 한 번 더 만들어 바꿔 적어요.</p></div>
<div class="card checks">
<h3>내가 할 일 네 가지</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g1"><span>고친 화면의 <b>링크</b>를 실습시트에 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="g2"><span><b>portfolio_1117.md</b>의 [내가 적을 곳]을 말해서 채웠어요 (세 문장부터)</span></label>
<label class="check"><input type="checkbox" data-k="g3"><span>실습시트에 <b>회고 4줄</b>을 적었어요: 오늘 만든 것 / 테스트에서 가장 놀란 것 / 수요일에 보여 줄 것 / 가장 시간 가는 줄 몰랐던 단계</span></label>
<label class="check"><input type="checkbox" data-k="g4"><span>오늘 만든 파일을 <b>하나도 지우지 않았어요</b></span></label>
</div>
<div class="card soft"><h3>내일</h3>
<ul><li><b>수요일 피칭 데이</b> · 오전에 pitch.md로 HTML 발표 화면을 만들어 링크로 내놓고, 오후에 조 안에서 한 사람씩 3분 발표해요. 조 대표는 반 전체 앞에서 5분 발표와 3분 질문을 해요.</li></ul></div>
<div class="card blue"><div class="big">오늘 여러분은 남이 쓰는 모습을 보고<br>내 MVP를 한 번 고쳤어요.</div></div>
</section>

<section id="s9">
<span class="eyebrow">막히면</span>
<h2>긴 설명 대신 한 줄을 보내요</h2>
<details><summary>어제 파일이 하나도 없어요</summary><div class="body"><p>P0 다음에 준비 구간의 <b>C0</b>을 보내요. 조사 설계서, 조사 표, 보는 화면을 한 번에 만들어요. 2~3분 걸려요.</p></div></details>
<details><summary>화면이 비어 보여요, 버튼이 안 눌려요</summary><div class="body"><p>화면 파일의 스크립트에 오류가 있으면 표도 버튼도 안 보여요. "mvp.html을 열었더니 화면이 비어 있어. 표도 버튼도 안 보여. 스크립트 오류를 찾아 고쳐줘."라고 보내고, 끝나면 파일 이름을 다시 눌러 봐요. 수업 전 시험에서 이 한 줄로 고쳐졌어요. 사람 테스트 전에 꼭 한 번 열어 봐요.</p></div></details>
<details><summary>11시가 됐는데 내 화면이 아직 덜 됐어요</summary><div class="body"><p>먼저 써 보는 사람이 돼 주고, 내 화면은 11:24 이후 순서나 12:05 뒤에 받아요. 화면이 비어 보이면 바로 위의 "화면이 비어 보여요" 한 줄부터 보내요.</p></div></details>
<details><summary>써 보는 사람이 모두 혼자 해내서 고칠 게 없어요</summary><div class="body"><p>잘 만든 거예요. 그래도 두 곳은 골라요. 가장 오래 걸린 시켜 볼 일, 써 보는 사람이 한 말, 자동 점검에서 "남음"인 것 가운데서 골라요.</p></div></details>
<details><summary>시켜 볼 일 카드에 정답이나 누를 곳이 들어 있어요</summary><div class="body"><p>"시켜 볼 일 카드에서 누를 곳과 정답을 빼고, 할 일만 한 문장으로 다시 써줘. test.md도 고쳐줘."라고 보내요.</p></div></details>
<details><summary>자동 점검이 "문제 없음"만 말해요</summary><div class="body"><p>코드를 읽어서 찾은 고장이 없다는 뜻이에요. 정말 다 되는지는 몰라요. 버튼 하나와 링크 하나를 직접 눌러 보고, 헷갈리는 곳은 사람 테스트에서 찾아요.</p></div></details>
<details><summary>써 보는 사람이 없어요</summary><div class="body"><p>옆 조의 한 사람이나 강사에게 부탁해요. 아무도 없으면 써 본 사람 칸을 비워 두고 P3, P4를 보내요. 결과를 지어내지 않고 자동 점검만으로 고쳐요. 결과서 맨 위에 "사람 테스트 전"이라고 적혀요. 오후 A에서 한 명에게라도 테스트해 봐요.</p></div></details>
<details><summary>기록을 적지 못하고 말로만 기억해요</summary><div class="body"><p>기억나는 대로 칸에 적어요. 시간을 못 쟀으면 "시간 못 잼"이라고 적어요. 지어낸 숫자보다 빈칸이 나아요.</p></div></details>
<details><summary>P4가 고르지 않은 곳까지 고쳤어요</summary><div class="body"><p>"고른 두 곳만 남기고 나머지는 mvp_before_fix.html대로 되돌려줘"라고 보내요. mvp_before_fix.html은 써 본 사람이 본 화면이에요.</p></div></details>
<details><summary>구글 폼으로 답을 받았어요</summary><div class="body"><p>폼의 답을 3교시의 써 본 사람 칸에 옮겨 적고 P3를 보내요. 폼 답은 P3가 직접 읽지 못해요.</p></div></details>
<details><summary>고쳤다는데 화면이 그대로예요</summary><div class="body"><p>옆 창으로 보고 있으면 파일 이름을 다시 눌러요. 브라우저로 보고 있으면 새로고침(윈도우 F5, 맥 ⌘R)을 해요. 브라우저로 열려면 3교시의 "브라우저로 열기"를 보내요.</p></div></details>
<details><summary>링크가 안 만들어져요</summary><div class="body"><p>실습시트에 "링크 못 만듦"이라고 적어요. 수요일 라이브 데모는 내 노트북에서 mvp.html을 직접 열어 보여 줘요. 내 카드의 링크 자리에도 "내 노트북으로 데모"라고 적어요.</p></div></details>
<details><summary>"오늘 조사 돌려줘"를 보내도 돼요?</summary><div class="body"><p>수요일 발표 전까지는 보내지 않아요. 화면이 바뀌면 오늘 테스트 결과와 맞지 않아요.</p></div></details>
<details><summary>영상 AI가 안 돼요</summary><div class="body"><p>무료 크레딧이 없거나 가입이 안 되면 영상은 건너뛰어요. teaser.md의 2컷(내 화면 녹화)만으로도 발표에 쓸 수 있어요.</p></div></details>
<details><summary>Claude가 자꾸 되물어요</summary><div class="body"><p>리모컨 <b>"되물을 때"</b>를 보내요. 그래도 물으면 새 대화를 열고 P0을 다시 보내요.</p></div></details>
<details><summary>답이 너무 길어요</summary><div class="body"><p>리모컨 <b>"말이 길 때"</b>를 보내요.</p></div></details>
<details><summary>새 대화를 열었더니 앞 내용을 몰라요</summary><div class="body"><p>괜찮아요. 프롬프트가 폴더의 파일을 읽어요. 다만 써 본 사람 칸에 적은 기록과 내가 말로 남긴 결정은 새 대화가 몰라요. 써 본 사람 칸은 그대로 남아 있으니 P3부터 다시 보내고, 결정은 W2 아래에 덧붙여요.</p></div></details>
<details><summary>사용량 한도 메시지가 떠요</summary><div class="body"><p>짝의 화면을 같이 보며 테스트를 도와줘요. 한도가 풀리면 이어서 해요.</p></div></details>
</section>
</div>

<button class="theme" id="themeBtn" type="button">다크 모드</button>
<div class="toast" id="toast" role="status" aria-live="polite">복사됐어요</div>
'''
P4TIME='평균 1분 30초 안팎(40초~3분)'
body=body.replace('<!--P4TIME-->',P4TIME)
body=expand_mvp_html(body)
out='<meta name="claude:viewport-fit-sides" content="cover">\n<title>Day 17 · 사용자 테스트와 MVP(Minimum Viable Product) v1</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap">\n'+style+'\n'+body+'\n'+script+'\n'
import sys
dest=sys.argv[1] if len(sys.argv)>1 else PATH
open(dest,'w',encoding='utf-8').write(out)
print('written',dest,len(out),'boxes',out.count('class="copy"'))
