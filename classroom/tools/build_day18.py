# Day 18 가이드 1판: 공식 11/18 줄(Lifestyle ⑩ 피칭 데이, 인터랙티브 HTML 발표, 문제-해결-시장-BM-MVP-팀-요청사항, 5분 피치 + 라이브 데모 + 3분 Q&A, 발표 피드백 시트).
# 내 장 HTML(P2) → 조 발표 페이지 합치기(P3) → 링크와 대본(P4) → 오후 발표와 피드백 카드 → 발표 뒤 피드백 정리(P9).
# 저장소 안에서 그대로 돈다: python3 classroom/tools/build_day18.py [출력 경로]. 빌더 공통 부분은 build_day17.py와 같다.
import re, os
TOOLS=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(os.path.dirname(TOOLS))
PATH=os.path.join(REPO,'classroom','student-guide','day18.html')
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
script=script.replace(_d,"ind:'식품',role:'아직 모름',team:'적지 않음',order:'조 번호 순서(1조부터 9조)',fb:'적지 않음'};")
script=script.replace("'l16-","'l18-")
def tok(k,d): return '<b data-v="%s">%s</b>'%(k,d)
B=tok('brand','라라스윗'); P=tok('product','저당 아이스크림'); C=tok('customer','다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인')
ROLE=tok('role','아직 모름'); TASK=tok('task','네가 정해줘')
CO='- 회사: '+B+' ('+P+') / 고객: '+C
TOP=' style="margin-top:12px"'
def box(pid,title,text,style_attr=''):
    return ('<button class="copy" type="button" data-copy="%s"%s><div class="hd"><b>%s</b><span class="btn">눌러서 복사</span></div>\n<pre id="%s">%s</pre></button>'%(pid,style_attr,title,pid,text))
def field(k,label,ph=''):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><input id="v-%s" data-in="%s" type="text" maxlength="90" placeholder="%s" autocomplete="off"></div></div>'%(k,label,k,k,ph)




# ── 1판 프롬프트

# ── 1판 프롬프트: 피칭 데이(공식 11/18 줄). 내 장 HTML → 조 덱 합치기 → 링크와 대본 → 발표 뒤 피드백
TEAM=tok('team','적지 않음'); ORDER=tok('order','조 번호 순서(1조부터 9조)'); FB=tok('fb','적지 않음')
def fieldwide(k,label,ph='',n=1500):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><textarea id="v-%s" data-in="%s" rows="4" maxlength="%d" placeholder="%s" autocomplete="off"></textarea></div></div>'%(k,label,k,k,n,ph)
PR={}
PR['p00']='''이 폴더의 CLAUDE.md를 오늘 수업에 맞게 고쳐줘. 파일이 없으면 새로 만들어줘. 끝나면 3줄로만 알려줘.
1. 기존 규칙(수업 작업 규칙, 사용자 테스트 규칙 등 앞선 수업에서 넣은 것)은 지우지도 바꾸지도 마. 같은 줄이 이미 있으면 그대로 둬.
2. 아래 "# 발표 규칙"이 없으면 맨 아래에 넣어줘. 있으면 그대로 둬.
3. "# 나와 회사"의 값이 처음 값이거나 이미 적힌 값이면 그대로 둬.

# 발표 규칙 (피칭 데이)
- 발표 페이지는 파일 하나짜리 HTML이다. 외부 라이브러리는 Chart.js 4.4.1 한 개만 https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js 에서 불러온다.
- 발표는 5분 안에 끝나게 칸마다 시간과 말할 사람을 정한다.
- 숫자는 근거 파일(research.csv, test_report.md, test_log.md, mvp.md)에 있는 것만 쓴다. 없으면 [채울 곳]으로 둔다.
- 못 찾은 값은 "못 찾음", 안 한 테스트는 "사람 테스트 전"으로 적는다. 발표에서도 숨기지 않는다.
- 발표 파일 맨 아래에 "공개 자료로 만든 학습용 MVP(Minimum Viable Product)이며, 조사한 회사와 관계없습니다"를 넣는다.

# 나와 회사 (오늘은 이 내용으로 작업한다)
- 내가 하고 싶은 일: '''+ROLE+'''
- 회사(브랜드): '''+B+''' ('''+P+''')
- 고객: '''+C+'''
- 회사를 바꿨으면 이 줄에 적고, 발표 파일의 회사 이름도 이 값으로 맞춘다.'''
PR['p01']='''우리 조 5분 발표 순서와 시간표를 team_pitch.md에 확정해줘. 파일이 이미 있어도 아래 조원 카드와 pitch_me.md를 기준으로 처음부터 다시 써. 파일에 있던 옛 카드나 옛 이름은 쓰지 마.
- 조원 카드: '''+TEAM+'''
- 팀은 3인 1조야. 조원 카드에 적힌 사람 수와 나(pitch_me.md)를 합쳐 세 명이 되게 써. 카드에 없는 사람은 만들지 마. 카드가 세 장보다 적으면 빈 자리는 [조원 카드 없음]으로 둬. 나(pitch_me.md)는 이름 대신 "나"로 적어.
- 발표 순서: '''+ORDER+'''
- 칸과 초: 문제 25초 / 해결 20초 / 시장 20초 / BM 20초 / 조원마다 MVP 40초 / 팀 20초 / 요청사항 20초. 합이 5분을 넘지 않게.
- 칸마다 말할 사람을 적어. 조원 이름이 없으면 [조원 A], [조원 B]로 적어.
- 15초 티저(teaser.md)가 있으면 맨 앞 15초로 넣을지 [팀이 정할 곳]으로 두고, 넣는다면 문제 칸을 15초로 줄여.
- 3분 Q&A에 나올 질문 예상 세 개만 적어. 답은 다음 단계에서 쓴다.
되묻지 말고 끝까지 하고, 끝나면 시간표 표(칸 / 초 / 말할 사람) 하나만 보여줘.'''
PR['p02']='''내 MVP 장을 한 파일 HTML로 만들어줘. 파일 이름은 my_slide_내이름.html로 해. 이름을 모르면 my_slide.html.
- 맨 위: pitch_me.md의 제목 한 줄, 누가 매일 하는 어떤 조사인지 한 줄.
- 데모 버튼 세 개: pitch_me.md의 데모 3단계 라벨 그대로. 버튼을 누르면 그 단계의 화면(표의 줄이나 카드)을 보여 줘. 값은 research.csv에서만.
- 숫자 막대 차트: 가장 중요한 숫자 세 개를 Chart.js 4.4.1(cdnjs)로 그리고, 0에서 올라가는 애니메이션을 넣어. 숫자는 test_report.md, research.csv, mvp.md에서만 가져와. 없으면 [채울 곳]으로 두고 막대는 0으로.
- 테스트 숫자 한 칸: "다른 조 학생 ○명 중 ○명이 과업 ○개를 혼자 끝냄". 테스트 전이면 "사람 테스트 전".
- 고친 것 한 줄, 다음에 고칠 것 한 줄.
- 맨 아래: 출처 링크(research.csv의 출처 칸), 그리고 "공개 자료로 만든 학습용 MVP이며, 조사한 회사와 관계없습니다".
파일 하나로, 폰 폭에서도 보이게 만들어. 되묻지 말고 끝까지 만들고, 끝나면 파일 이름과 데모 3단계만 보여줘.'''
PR['p03']='''우리 조 발표 페이지 team_deck.html을 만들어줘. 입력은 team_pitch.md(시간표와 조 공통 칸)와, 작업 폴더의 my_slide_*.html 파일들(조원이 보낸 파일 이름 그대로)이야.
- 순서: 표지(팀 이름과 한 줄 문제) → 문제 → 해결 → 시장 → BM → 조원 MVP 장(my_slide 파일마다 한 장, 장 위에 조원 이름) → 팀 → 요청사항.
- 각 MVP 장은 해당 my_slide 파일의 내용을 그대로 가져와. 파일이 없는 조원 자리는 [조원 파일 없음]으로 두고 발표 순서는 그대로 둬.
- 칸에 없는 내용은 [팀이 정할 곳]으로 둬. 숫자를 새로 만들지 마.
- 화면 아래에 이전 / 다음 버튼과 키보드 ← → 로 넘기기. 장마다 말할 시간(team_pitch.md의 초)을 표시.
- 발표 시작 버튼을 누르면 5분을 세고, 1분 남으면 색이 바뀌게.
- 외부 라이브러리는 Chart.js 4.4.1(cdnjs)만. 나머지는 파일 안에 넣어.
- 맨 아래: "공개 자료로 만든 학습용 MVP이며, 조사한 회사와 관계없습니다".
파일 하나로 만들고, 끝나면 장 목록(번호 / 제목 / 말할 사람)과 빠진 파일이 있으면 그 이름만 보여줘. 되묻지 말고 끝까지.'''
PR['p04']='''team_deck.html을 발표 링크로 만들어줘. 아티팩트로 발행하고 링크를 알려줘. 발행이 안 되면 team_deck.html 파일 이름을 알려줘.
그다음 발표 대본 team_script.md를 써줘.
- 장마다 말할 문장 한두 개. 소리 내어 읽었을 때 team_pitch.md의 초에 맞는 길이로.
- 말할 사람은 team_pitch.md의 이름 그대로. 숫자는 파일에 있는 것만.
- 예상 질문 세 개와 답 한 줄씩: (1) 시장이 얼마나 큰지 (2) 못 찾은 칸이 많으면 믿을 수 있는지 (3) 엑셀이나 기존 도구와 뭐가 다른지. 답할 숫자가 없으면 "지금 숫자로는 말할 수 없어요. 확인해서 알려 드릴게요"라고 쓴다.
되묻지 말고 끝까지 하고, 끝나면 링크(또는 파일 이름)와 예상 질문 세 개만 보여줘.'''
PR['p05']='''teaser.md의 15초 영상을 team_deck.html 맨 앞에 넣어줘.
- 영상 파일이나 링크가 있으면 그대로 넣고, 없으면 teaser.md의 1번 컷 화면을 회색 박스로 두고 "영상 자리"라고 적어.
- 문제 칸의 말할 시간을 25초에서 15초로 줄이고, team_pitch.md와 team_script.md를 맞춰.
- 5분 시간표의 합이 5분을 넘지 않는지 확인하고, 넘으면 줄여.
되묻지 말고 끝까지 하고, 끝나면 바꾼 곳 세 줄만 보여줘.'''
PR['p06']='''발표 Q&A 3분에 대비해서 질문 열 개와 답을 qa.md로 써줘.
- 열 개 가운데 네 개는 약점 질문이야: "못 찾은 칸이 많다", "숫자가 가정이다", "왜 AI 에이전트인가", "우리 회사에 맞나".
- 답은 한두 문장. 숫자는 파일에 있는 것만. 없으면 "확인해서 알려 드릴게요"라고 답해.
- 나머지 여섯 개는 동료가 물을 만한 질문(누가 쓰나, 얼마나 빨라지나, 비용, 보안, 다음 단계 등).
- 질문마다 답할 사람(조장, 조원 이름)을 적어.
되묻지 말고 끝까지 하고, 끝나면 질문 목록만 보여줘.'''
PR['p07']='''team_deck.html에 숫자가 움직이며 올라가는 장을 하나 추가해줘. 숫자는 test_report.md나 research.csv에서만.
- 숫자를 0에서 실제 값까지 2초에 올려. 옆에 이 숫자가 어느 파일의 어느 줄에서 왔는지 작게 적어.
- 숫자가 "못 찾음"이면 숫자 대신 "못 찾은 칸이 ○개"를 움직여.
- 기존 장은 건드리지 마. 추가한 장의 말할 시간 15초를 team_script.md에 넣어.
되묻지 말고 끝까지 하고, 끝나면 추가한 장 번호와 숫자 한 줄만 보여줘.'''
PR['p08']='''발표 리허설 도구를 rehearsal.md로 써줘.
- 장마다 말할 시간(team_pitch.md)과, 실제로 소리 내어 읽었을 때 걸린 시간을 적는 빈 칸.
- 연습 순서 세 가지: (1) 혼자 소리 내어 5분 (2) 조원 앞에서 5분 (3) 예상 질문 세 개를 받고 답하기.
- 발표 직전 체크 다섯 가지: 링크가 열리는지, 장 넘기기가 되는지, 데모 버튼이 눌리는지, 영상(있으면) 소리, 폰 폭에서 보이는지.
되묻지 말고 끝까지 하고, 끝나면 체크 다섯 가지와 연습 순서만 보여줘.'''
PR['p09']='''받은 피드백으로 고칠 목록을 feedback_plan.md로 써줘. 입력은 아래 피드백 카드야.
- 피드백 카드: '''+FB+'''
- 피드백마다: 무엇을 / 누가 / 고칠 곳(파일과 장) / 발표 전에 고칠지, 다음에 할지.
- 고칠 곳은 최대 두 개. 나머지는 "다음에"로 적어.
- 칭찬 한 가지도 적어. 발표 첫 문장에 쓸 수 있게.
- 고치기로 정한 것은 team_deck.html에 반영하는 한 줄 프롬프트로 만들어 줘.
되묻지 말고 끝까지 하고, 끝나면 고칠 두 곳과 칭찬 한 가지만 보여줘.'''
PR['w2']='''오늘 이 폴더에서 한 피칭 준비를 내 포트폴리오에 넣을 한 장으로 정리해서 portfolio_1118.md로 써줘.
- 내가 하고 싶은 일: '''+ROLE+'''. CLAUDE.md의 "# 나와 회사" 값이 있으면 그 값을 먼저 써.
- 내 장 한 줄: 어떤 조사를 줄이는 MVP인지, 파일 이름.
- 발표에서 받은 피드백 세 가지: 피드백 카드에 적힌 말만 옮겨. 적히지 않은 피드백은 만들지 마.
- 내가 바꾼 것 한 가지와 이유. 발표 전에 바꾼 곳이 없으면 "바꾼 것 없음"이라고 적어.
- 이 결과물이 회사에서 쓰이는 곳: why.md가 있으면 공고 문장과 한 줄로 잇고, 없으면 (가정).
- 수업에서 배운 방법: 수업이 시킨 방법 가운데 내가 실제로 따라 한 것을 세 줄로. 이건 내 결정이 아니야.
- 내가 내린 결정: 발표 순서 정하기, 고칠 곳 고르기, 질문에 "모른다"고 답하기, 어떤 숫자를 말할지 고르기 중에서 내가 한 것만. "Claude가 고름"으로 적은 것은 옆에 [내가 적을 곳: 받아들인 이유]를 남겨.
- 면접에서 말할 세 문장: 무엇을 만들었고, 누구에게 무엇을 듣고 무엇을 바꿨고, 다음에 무엇을 확인할지. 내가 내리지 않은 결정을 내가 한 것처럼 쓰지 마. 쓸 결정이 없으면 [내가 적을 곳]으로 남겨.
되묻지 말고 끝까지 쓰고, 끝나면 "면접에서 말할 세 문장"과 [내가 적을 곳]이 남은 자리만 보여줘.'''
R={'r1':'되묻지 말고 네가 가정해서 끝까지 만들어줘. 가정한 곳만 (가정)이라고 표시해줘.',
'r2':'너무 길어. 3줄로만 다시 말해줘.',
'r3':'없는 자료는 없는 대로 두고, 지금 있는 것으로 끝까지 만들어줘.',
'r6':'방금 만든 파일의 내용을 그대로 보여줘. CSV면 앞 10줄을 표로, HTML이면 코드 말고 화면에 무엇이 어떤 순서로 있는지 알려줘.',
'r8':'team_deck.html을 브라우저로 열어 줘.',
'r9':'team_deck 링크가 안 열려. 같은 파일로 다시 발행하고 링크를 알려줘. 그래도 안 되면 파일 이름을 알려줘.',
'r10':'발표에서 말하려는 숫자가 맞는지 근거 파일의 줄을 찾아 알려 줘. 틀렸으면 team_deck.html과 team_script.md를 같이 고쳐줘.'}
OPEN2='team_deck.html을 브라우저로 열어 줘.'
RUN='발표 장 넘기기 연습'
PUB='team_deck.html을 아티팩트로 발행하고 링크를 알려줘.'

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

# ── 1판 본문

body='''
<div class="wrap">
<nav id="nav" aria-label="구간 이동">
<a href="#s0">오늘</a><a href="#s1">준비</a><a href="#s2">1교시</a><a href="#s3">2교시</a><a href="#s4">3교시</a><a href="#s5">4교시</a><a href="#s6">발표</a><a href="#s7">마무리</a><a href="#remote">리모컨</a><a href="#s8">막히면</a>
</nav>

<section id="s0">
<span class="eyebrow">Day 18 / 52 · 11/18(수)</span>
<h1>Day 18 · 인터랙티브 HTML로 발표하는 날</h1>
<p class="lead">오늘은 내 MVP를 <b>브라우저에서 눌러 보이는 발표 한 장</b>으로 만들어요. 오전에는 내 장을 만들고, 조원의 장을 모아 조 발표 페이지를 합치고, 링크로 내놓아요. 오후에는 조마다 5분 발표하고 3분 질문을 받아요. 발표 페이지는 정적 PPT가 아니라 버튼을 누르면 숫자가 움직이는 HTML이에요.</p>

<h3 class="gap">오늘 한눈에</h3>
<div class="acts">
<div><b>① 만들기</b><span>09:20–12:00</span></div>
<div><b>② 쉬고 준비</b><span>12:00–14:00</span></div>
<div><b>③ 발표와 피드백</b><span>14:00–18:00</span></div>
</div>
<div class="map">
<div class="grp">시작</div>
<div class="row rest"><span class="t">09:00</span><span class="w">오늘 한눈에 보기, 어제 파일 확인</span></div>
<a class="row" href="#s1"><span class="t">09:20</span><span class="w"><b>준비 · 규칙 이어 쓰기, 내 일 확인</b><small>남는 것: CLAUDE.md</small></span></a>
<div class="grp">① 만들기 · 내 장을 HTML 한 장으로, 조 발표 페이지를 합쳐요</div>
<a class="row" href="#s2"><span class="t">09:40</span><span class="w"><b>1교시 · 피치 일곱 칸, 우리 조 5분 시간표</b><small>남는 것: team_pitch.md</small></span></a>
<a class="row" href="#s3"><span class="t">10:20</span><span class="w"><b>2교시 · 내 장을 눌러 보는 HTML로</b><small>남는 것: my_slide_내이름.html</small></span></a>
<a class="row" href="#s4"><span class="t">11:00</span><span class="w"><b>3교시 · 조 발표 페이지 합치기</b><small>남는 것: team_deck.html</small></span></a>
<a class="row" href="#s5"><span class="t">11:40</span><span class="w"><b>4교시 · 링크, 대본, 질문 대비</b><small>남는 것: 발표 링크, team_script.md, qa.md</small></span></a>
<div class="row rest"><span class="t">12:00</span><span class="w">점심</span></div>
<div class="grp">③ 발표와 피드백 · 순서대로 조가 발표하고, 기다리는 조는 메뉴를 해요</div>
<a class="row" href="#s6"><span class="t">14:00</span><span class="w"><b>발표 · 9개 조가 차례로, 조당 9분</b><small>5분 발표 + 3분 질문 + 교체 1분</small></span></a>
<a class="row" href="#s6"><span class="t">15:30</span><span class="w"><b>피드백 시트 · 두 조 이상 듣고 적기</b><small>남는 것: 피드백 카드 기록</small></span></a>
<a class="row" href="#s7"><span class="t">17:00</span><span class="w"><b>마무리 · 피드백 정리, 포트폴리오 한 장, 링크</b><small>남는 것: feedback_plan.md, portfolio_1118.md</small></span></a>
</div>
<p class="sub">줄을 누르면 그 구간으로 가요. <b>꼭 하는 것</b>은 오전의 P0 → P1 → P2 → P3 → P4, 발표 때 피드백 카드, 마무리의 P9와 W2예요. 이것만 끝내도 오늘은 통과예요.</p>

<h3 class="gap">오늘 수업, 이렇게 보면 돼요</h3>
<details><summary>피칭은 "짧게 설득하기"예요</summary><div class="body">
<p>피칭은 짧은 시간에 "왜 이것이 필요한지"를 듣는 사람에게 납득시키는 발표예요. 식당의 메뉴판과 같아요. 한 입 맛보기로 음식이 맛있는지 알게 하고, 주문은 듣는 사람이 해요. 오늘은 5분 안에 문제, 해결, 시장, 비즈니스 모델, 내 MVP, 팀, 요청을 차례로 보여 줘요.</p></div></details>
<details><summary>발표 페이지는 왜 HTML이에요?</summary><div class="body">
<p>정적 슬라이드는 넘기기만 해요. HTML은 버튼을 누르면 실제 화면이 나오고, 숫자가 0에서 올라가요. 발표자는 "이 숫자는 어디서 왔는지"를 같은 화면에서 바로 보여 줄 수 있어요. 파일을 인터넷 주소로 올리면 누구나 링크로 열 수 있어요.</p></div></details>
<details><summary>못 찾은 것도 발표해도 돼요?</summary><div class="body">
<p>네. 오히려 그래야 해요. "못 찾은 칸이 40%예요. 그래서 이 숫자는 참고용이에요"라고 말하면 질문이 줄어요. 숨긴 숫자는 질문 한 번에 무너져요.</p></div></details>
<h3 class="gap">용어</h3>
<details><summary>오늘 처음 나오는 말</summary><div class="body">
<ul><li><b>피치 구조</b> · 문제 → 해결 → 시장 → BM → MVP → 팀 → 요청사항. 발표의 순서예요.</li><li><b>BM(Business Model)</b> · 비즈니스 모델. 누구에게 무엇을 주고 어떻게 돈을 버는지, 사내 도구라면 무엇을 아끼는지예요.</li><li><b>라이브 데모</b> · 발표하면서 실제로 눌러 보이는 화면이에요. 30초로 줄여 말해요.</li><li><b>라이브 차트</b> · 버튼을 누르면 숫자가 움직이며 올라가는 그래프예요. Chart.js라는 도구로 그려요.</li><li><b>발표 링크</b> · 만든 HTML을 인터넷 주소로 올린 것이에요. 아티팩트로 만들거나, Vercel에 올려요.</li><li><b>Q&A</b> · 발표 뒤 3분 동안 듣는 사람이 묻고 답하는 시간이에요.</li><li><b>피드백 카드</b> · 발표를 들은 사람이 적는 네 가지 질문이에요. 점수와 한 줄을 적어요.</li></ul></div></details>
</section>

<section id="s1">
<span class="eyebrow">시작 · 09:20–09:40 · 준비</span>
<h2>규칙을 이어 쓰고, 내 일과 회사를 확인해요</h2>
<p class="why"><b>왜 해요?</b> 어제까지의 규칙에 발표 규칙을 더해 두면, 오늘 프롬프트가 같은 방식으로 움직여요.</p>
<div class="card checks">
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="a1"><span>Claude Code에서 <b>어제 작업 폴더</b>를 열고 <b>새 대화</b>를 시작했어요. 어제 파일이 없으면 Day 17의 C0을 먼저 보내요</span></label>
<label class="check"><input type="checkbox" data-k="a2"><span>아래 입력 칸에 <b>내가 하고 싶은 일</b>과 회사를 적었어요. 어제와 같으면 비워 둬도 돼요</span></label>
<label class="check"><input type="checkbox" data-k="a3"><span><b>P0</b>을 실행했어요</span></label>
</div>
<details><summary>프롬프트 쓰는 법과 허락 창 (어제 못 왔으면 꼭 펼쳐 봐요)</summary><div class="body">
<ol><li>박스를 누르면 복사돼요. Claude Code 입력창에 붙여 넣고 보내요.</li><li>프롬프트 하나는 1분 안팎이에요. P2는 3~5분, P4는 2~3분 걸려요. 멈춘 게 아니에요. 답이 한참 그대로면 허락 창이 떠 있는지 봐요.</li><li>발표 파일(.html)은 답에 나온 파일 이름을 누르면 옆 창에 열려요. 브라우저로 여는 상자는 리모컨에 있어요.</li></ol>
<p><b>허락 창</b> · 방금 보낸 프롬프트가 시킨 일이면 Yes를 눌러요. 파일 만들기와 고치기, 웹 검색, 링크 만들기, 브라우저 열기가 그래요. 파일을 통째로 지우겠다고 하면 누르지 말고 강사님을 불러요.</p></div></details>
<div class="card" id="profileCard">
<h3>내 일과 회사를 확인해요</h3>
<p class="sub">여기 적은 것이 프롬프트의 <b class="tok">파란 글자</b>로 들어가요. 비워 두면 칸 안에 흐리게 보이는 처음 값이 들어가요. 어제 적은 값이 있으면 그대로 두면 돼요.</p>
<div class="field"><label for="v-role">내가 하고 싶은 일. 예: 콘텐츠 마케터, MD, CX 기획자, 서비스 기획자, 데이터 분석가</label><input id="v-role" data-in="role" type="text" maxlength="40" placeholder="비워 두면: 아직 모름 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-brand">회사(브랜드) 이름</label><input id="v-brand" data-in="brand" type="text" maxlength="40" placeholder="비워 두면: 라라스윗 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-product">제품·서비스 한 줄</label><input id="v-product" data-in="product" type="text" maxlength="60" placeholder="비워 두면: 저당 아이스크림 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-customer">그 회사의 고객 한 줄</label><input id="v-customer" data-in="customer" type="text" maxlength="90" placeholder="비워 두면: 라라스윗 고객 (어제 적은 것이 있으면 그대로)" autocomplete="off"></div>
<button class="ghost" id="resetProfile" type="button">처음 값으로 되돌리기</button>
</div>
'''+box('p00','P0 · 발표 규칙 이어 쓰기 (꼭)',PR['p00'])+'''
<div class="card soft"><p><b>P0은 어제 규칙을 두고 발표 규칙만 더해요.</b> 발표 페이지는 한 파일이고, 숫자는 근거 파일에 있는 것만 써요. 못 찾은 것은 "못 찾음", 안 한 테스트는 "사람 테스트 전"으로 적어요.</p></div>
</section>

<section id="s2">
<span class="eyebrow">① 만들기 · 09:40–10:20 · 1교시</span>
<h2>피치 일곱 칸을 알고, 우리 조 5분 시간표를 정해요</h2>
<p class="why"><b>왜 해요?</b> 5분 안에 일곱 칸을 다 말하려면 칸마다 시간과 말할 사람이 정해져 있어야 해요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>팀 발표의 일곱 칸 · 5분</h3>
<div class="pairs">
<div class="row"><span class="k">문제</span><span class="w"><b>25초 · 조 공통</b><small>신입이 매일 손으로 하는 조사 한 문장</small></span></div>
<div class="row"><span class="k">해결</span><span class="w"><b>20초 · 조 공통</b><small>조사를 AI 에이전트에게 맡긴 조사 도우미</small></span></div>
<div class="row"><span class="k">시장</span><span class="w"><b>20초 · 조 공통</b><small>같은 조사를 매일 하는 직무와 회사, 몇 명인지 (근거가 없으면 [팀이 정할 곳])</small></span></div>
<div class="row"><span class="k">BM</span><span class="w"><b>20초 · 조 공통</b><small>사내 도구면 아끼는 시간, 서비스면 받을 돈</small></span></div>
<div class="row"><span class="k">MVP</span><span class="w"><b>조원마다 40초</b><small>3인 1조면 장이 세 장이에요(나 포함). 장마다 데모 30초와 테스트 숫자 10초</small></span></div>
<div class="row"><span class="k">팀</span><span class="w"><b>20초 · 조 공통</b><small>누가 무엇을 만들었나</small></span></div>
<div class="row"><span class="k">요청사항</span><span class="w"><b>20초 · 조 공통</b><small>듣는 사람에게 바라는 것 하나</small></span></div>
</div>
<p class="sub" style="margin-top:12px">합하면 4분 정도예요. 나머지 1분은 교체와 숨 고르기예요. 칸의 순서는 공식 일정표의 피치 구조예요.</p></div>
<span class="pill">따라 하기</span>
<div class="card soft" style="margin-top:12px"><p><b>내 결정 1 · 발표 순서와 말할 사람 정하기.</b> 조 번호 순서로 발표해요. 칸마다 말할 사람을 조원 이름으로 적어요. 같은 사람이 두 칸을 맡지 않게 해요.</p></div>
'''+fieldwide('team','우리 조 조원 카드 (조원마다 "내 카드" 여덟 줄을 붙여요. Day 17 P9에서 만든 카드예요. 없으면 비워 둬요)','비워 두면: 적지 않음',4000)+'\n'+field('order','발표 순서 (기본값은 조 번호 순서예요)','비워 두면: 조 번호 순서(1조부터 9조)')+'\n'+box('p01','P1 · 우리 조 5분 시간표 확정 (꼭)',PR['p01'],TOP)+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="b1"><span>team_pitch.md가 생겼고, 칸마다 초와 말할 사람이 있어요</span></label>
<label class="check"><input type="checkbox" data-k="b2"><span>합계가 5분을 넘지 않아요</span></label>
<label class="check"><input type="checkbox" data-k="b3"><span>내가 말할 칸을 알고 있어요 (내 결정 1)</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 내가 말할 칸을 소리 내어 읽어 보고, 시간을 재요. 40초를 넘으면 한 문장을 줄여요.</p></div>
</section>

<section id="s3">
<span class="eyebrow">① 만들기 · 10:20–11:00 · 2교시</span>
<h2>내 장을 눌러 보는 HTML 한 장으로 만들어요</h2>
<p class="why"><b>왜 해요?</b> 발표에서 "이게 실제로 돌아가요"를 보여 주는 장이에요. 데모 버튼과 숫자 막대가 있으면, 질문이 들어와도 화면에서 바로 답할 수 있어요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>내 장에 들어가는 것</h3>
<ul><li><b>데모 버튼 세 개</b> · 어제 pitch_me.md의 데모 3단계예요. 누르면 그 단계의 화면이 보여요.</li><li><b>숫자 막대 차트</b> · 가장 중요한 숫자 세 개가 0에서 올라가요. 숫자는 근거 파일에서만 가져와요.</li><li><b>테스트 숫자 한 칸</b> · "다른 조 학생 ○명 중 ○명이 과업을 혼자 끝냄"처럼 적어요. 테스트를 안 했으면 "사람 테스트 전"이라고 적어요.</li><li><b>출처 링크</b> · 숫자를 가져온 주소를 맨 아래에 모아요.</li></ul></div>
<span class="pill">따라 하기</span>
'''+box('p02','P2 · 내 장을 눌러 보는 HTML로 (꼭)',PR['p02'],TOP)+'''
<p class="sub"><b>P2는 3~5분 걸려요.</b> 파일이 끝나면 답에 나온 파일 이름을 눌러 옆 창에서 열어 봐요. 버튼 세 개를 한 번씩 누르고, 막대가 올라가는지 봐요.</p>
<div class="card soft"><p><b>내 결정 2 · 발표에 쓸 숫자 하나 고르기.</b> 막대 세 개 가운데 발표 처음에 보여 줄 숫자를 하나 골라요. 예: "가장 싼 곳이 얼마인지". 고른 이유를 Claude에게 한 줄로 말해 두면 포트폴리오에 내 결정으로 남아요.</p></div>
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="c1"><span>my_slide 파일이 생겼고, 파일 이름을 눌러 옆 창에서 열렸어요</span></label>
<label class="check"><input type="checkbox" data-k="c2"><span>데모 버튼 세 개가 눌리고, 막대가 올라가요</span></label>
<label class="check"><input type="checkbox" data-k="c3"><span>발표에 쓸 숫자를 골라 한 줄 말했어요 (내 결정 2)</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 폰 크기로 보기 위해 브라우저 창을 폰만큼 좁혀 봐요. 화면이 옆으로 넘치면 "폰 화면에서 글자가 넘쳐. 고쳐줘"라고 보내요.</p></div>
</section>

<section id="s4">
<span class="eyebrow">① 만들기 · 11:00–11:40 · 3교시</span>
<h2>조원의 장을 모아 조 발표 페이지를 합쳐요</h2>
<p class="why"><b>왜 해요?</b> 발표는 한 파일로 해요. 세 명이 각자 만든 장을 조장의 한 파일로 모아야 발표할 때 넘기기만 하면 돼요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>파일이 오가는 길</h3>
<ol><li><b>조원</b>이 my_slide 파일을 조장에게 보내요. 메신저 파일 첨부나 드라이브 어느 쪽이든 좋아요.</li><li><b>조장</b>이 받은 파일을 작업 폴더에 <b>그대로 파일 이름</b>으로 넣어요.</li><li><b>조장</b>이 P3을 보내면 조 발표 페이지 team_deck.html이 만들어져요.</li></ol>
<p class="sub">조장이 아니면 내 파일을 조장에게 보내고, 조장의 발표 링크가 열리는지 한 번 봐요.</p></div>
'''+box('p03','P3 · 조 발표 페이지 team_deck.html 만들기 (꼭, 조장)',PR['p03'],TOP)+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="d1"><span>team_deck.html이 생겼고, 장 목록에 조원 이름이 있어요</span></label>
<label class="check"><input type="checkbox" data-k="d2"><span>옆 창에서 열어 장을 넘기면 조원의 장이 보여요</span></label>
<label class="check"><input type="checkbox" data-k="d3"><span>빠진 조원 파일이 있으면 [조원 파일 없음]으로 남았다는 것을 알고 있어요</span></label>
</div>
<div class="card soft"><p><b>먼저 끝났다면</b> 발표 시작 버튼을 누르고 5분이 세어지는지, 1분 남았을 때 색이 바뀌는지 봐요.</p></div>
</section>

<section id="s5">
<span class="eyebrow">① 만들기 · 11:40–12:00 · 4교시</span>
<h2>발표 링크를 만들고, 대본과 질문을 준비해요</h2>
<p class="why"><b>왜 해요?</b> 링크가 있어야 듣는 사람이 자기 화면으로 발표를 다시 볼 수 있어요. 대본과 질문 대비가 있으면 3분 질문이 덜 흔들려요.</p>
<span class="pill">따라 하기</span>
'''+box('p04','P4 · 발표 링크, 대본, 예상 질문 (꼭)',PR['p04'],TOP)+'''
<div class="card"><h3>링크가 두 가지예요</h3>
<ul><li><b>기본: Claude 아티팩트 링크.</b> P4가 만든 링크를 실습시트에 적어요. 공유 메뉴에서 "링크가 있는 사람은 누구나"로 바꿔요.</li><li><b>대안: Vercel 배포.</b> 공식 일정표의 방법이에요. 계정을 새로 만들어야 해서 시간이 더 걸려요. 원하는 조는 강사님 화면을 보고 따라 해요.</li></ul>
<p class="sub">링크가 안 열리면 "발표 페이지 링크가 안 열려요"를 리모컨에서 보내요.</p></div>
<div class="card soft"><p><b>내 결정 3 · 질문에 "모른다"고 답할 문장 고르기.</b> 예상 질문 세 개 가운데 숫자가 없는 질문에는 "지금 숫자로는 말할 수 없어요. 확인해서 알려 드릴게요"라고 답해요. 이 문장을 대본에 넣어 두면 발표 중에 당황하지 않아요.</p></div>
<h3 class="gap">질문 대비와 리허설 · 골라서 하나 이상</h3>
<p class="sub">오후 발표를 기다리는 조는 이 메뉴 가운데 하나를 해요. 발표 중인 조는 듣기만 해요.</p>
<div class="grid">
<div class="card path"><h3>A · 15초 영상 넣기</h3><p class="sub">Day 17에서 만든 teaser.md의 영상을 발표 맨 앞에 넣어요. 없으면 영상 자리만 두고 넘어가요.</p><p><b>P5</b> · 1분</p></div>
<div class="card path"><h3>B · 예상 질문 열 개</h3><p class="sub">약점 질문 네 개와 동료 질문 여섯 개에 답을 준비해요. 숫자가 없는 질문에는 "확인해서 알려 드릴게요"라고 답해요.</p><p><b>P6</b> · 1~2분</p></div>
<div class="card path"><h3>C · 숫자가 움직이는 장</h3><p class="sub">가장 중요한 숫자 하나가 0에서 올라가는 장을 추가해요. 데이터 조는 여기에 먼저 손대요.</p><p><b>P7</b> · 1~2분</p></div>
<div class="card path"><h3>D · 리허설 시트</h3><p class="sub">5분을 소리 내어 연습하고, 장마다 걸린 시간을 적어요. 발표 직전 체크 다섯 가지를 만들어요.</p><p><b>P8</b> · 1분</p></div>
</div>
'''+box('p05','P5 · 15초 영상 넣기 (A)',PR['p05'])+'''
'''+box('p06','P6 · 예상 질문 열 개 (B)',PR['p06'])+'''
'''+box('p07','P7 · 숫자가 움직이는 장 (C)',PR['p07'])+'''
'''+box('p08','P8 · 발표 리허설 시트 (D)',PR['p08'])+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="e1"><span>발표 링크가 생겼고, 실습시트에 적었어요 (또는 파일 이름을 적었어요)</span></label>
<label class="check"><input type="checkbox" data-k="e2"><span>team_script.md에 장마다 말할 문장이 있고, 질문 세 개에 답이 있어요</span></label>
<label class="check"><input type="checkbox" data-k="e3"><span>메뉴 A~D 가운데 하나를 했어요 (발표 기다리는 동안 해도 돼요)</span></label>
</div>
</section>

<section id="s6">
<span class="eyebrow">③ 발표와 피드백 · 14:00–17:00 · 다 같이</span>
<h2>조마다 5분 발표하고, 듣는 사람은 피드백 카드를 써요</h2>
<p class="why"><b>왜 해요?</b> 발표는 말하는 쪽의 연습이고, 피드백은 듣는 쪽의 연습이에요. 남의 발표에서 무엇이 와닿았는지 적어야 내 발표를 고칠 수 있어요.</p>
<div class="card"><h3>발표 순서 · 14:00 시작, 조당 9분</h3>
<ol>
<li>14:00–14:05 강사님 오프닝과 피드백 카드 설명</li>
<li>14:05부터 <b>조 번호 순서</b>로 한 조씩. 발표 5분, 질문 3분, 교체 1분. 9개 조면 14:05–15:26</li>
<li>15:26–15:40 쉬는 시간. 피드백 시트에 적기 시작</li>
<li>15:40–16:10 피드백 시트: <b>내가 듣지 않은 조는 적지 않아요. 들은 조 가운데 두 조 이상</b> 적어요</li>
<li>16:10–16:40 강사님 총평, 가장 잘한 조 두 곳의 데모를 다시 보기</li>
</ol>
<p class="sub">발표 중에는 화면을 보는 사람은 발표하는 조원뿐이에요. 나머지는 듣고 적어요. 발표를 기다리는 조는 위의 메뉴 A~D 가운데 하나를 해요.</p></div>
<h3 class="gap">피드백 카드 · 발표 한 조마다 네 문항</h3>
<div class="card soft"><ol>
<li><b>문제가 와닿았나요?</b> 1~5점, 이유 한 줄</li>
<li><b>데모가 30초 안에 무엇을 보여 줬나요?</b> 한 문장</li>
<li><b>숫자를 믿을 수 있었나요?</b> 1~5점, 어떤 숫자가 걸렸는지 한 줄</li>
<li><b>하나만 고친다면?</b> 한 문장. 칭찬도 한 줄</li>
</ol>
<p class="sub">칭찬은 구체적으로 적어요. "좋았어요"보다 "가격 막대가 올라가는 것이 한눈에 보였어요"가 발표자에게 도움이 돼요.</p></div>
'''+field('fb','내가 들은 조 피드백을 여기에 적어요. 발표 뒤 Claude에게 보내면 피드백 정리에 쓰여요','비워 두면: 적지 않음')+'''
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="f1"><span>두 조 이상 듣고 피드백 카드를 네 문항으로 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="f2"><span>우리 조가 발표했다면, 받은 피드백을 한 줄씩 적었어요</span></label>
</div>
</section>

<section id="s7">
<span class="eyebrow">③ 발표와 피드백 · 17:00–18:00 · 마무리(다 같이)</span>
<h2>받은 피드백을 정리하고, 포트폴리오 한 장을 남겨요</h2>
<p class="why"><b>왜 해요?</b> 발표는 한 번으로 끝나지만, 받은 피드백으로 무엇을 고쳤는지 남기면 12월 포트폴리오에 바로 쓸 수 있어요.</p>
<div class="card"><h3>피드백 정리 · P9</h3><p>발표 카드에 적은 말(위의 피드백 칸)을 P9에 넣어요. 고칠 곳 두 개와 칭찬 한 가지가 나와요.</p></div>
'''+box('p09','P9 · 받은 피드백으로 고칠 목록 (꼭)',PR['p09'],TOP)+'''
<div class="card"><h3>오늘을 포트폴리오 한 장으로 남겨요</h3>
<p><b>W2는 아침부터 쓰던 폴더와 대화에서 보내요.</b> Claude가 못 본 것(발표 중에 한 말, 질문에 답한 것)은 W2 아래에 한 줄씩 덧붙여요. 줄을 바꿀 때는 Shift+Enter를 눌러요.</p></div>
'''+box('w2','W2 · 오늘을 포트폴리오 한 장으로 (꼭)',PR['w2'])+'''
<div class="card soft" style="margin-top:12px"><p><b>[내가 적을 곳]은 말로 채워요.</b> 예: "발표에서 숫자를 먼저 보여 준 이유는 가장 와닿는 숫자였기 때문이야. 포트폴리오에 적어줘." 면접에서 말할 세 문장부터 채워요.</p></div></div>
<div class="card checks">
<h3>내가 할 일 네 가지</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g1"><span>발표 링크(또는 파일 이름)를 실습시트에 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="g2"><span><b>portfolio_1118.md</b>의 [내가 적을 곳]을 말해서 채웠어요 (세 문장부터)</span></label>
<label class="check"><input type="checkbox" data-k="g3"><span>실습시트에 <b>회고 4줄</b>을 적었어요: 발표에서 한 것 / 질문에 가장 당황한 것 / 받은 피드백 하나 / 다음에 바꿀 것</span></label>
<label class="check"><input type="checkbox" data-k="g4"><span>오늘 만든 파일을 <b>하나도 지우지 않았어요</b></span></label>
</div>
<div class="card soft"><h3>내일과 모레</h3>
<ul><li><b>목요일</b> · 피드백을 반영하고 AI 이해 수업으로 넘어가요. 발표 파일은 링크로 그대로 두어요.</li></ul></div>
<div class="card blue"><div class="big">오늘 여러분은 눌러 보이는 발표를 만들고,<br>듣는 사람의 말로 한 번 고쳤어요.</div></div>
</section>

<section id="remote">
<h3 class="gap">리모컨 여섯 개 · 필요할 때만 꺼내 써요</h3>
<details><summary>리모컨 펼치기 (지금 보내는 상자가 아니에요)</summary><div class="body">
<p class="sub">하루 중에 Claude가 마음에 안 들게 움직이면 긴 설명 대신 이 짧은 상자를 보내요.</p>
'''+box('r1','되물을 때',R['r1'])+'\n'+box('r2','말이 길 때',R['r2'])+'\n'+box('r3','자료가 없다고 멈췄을 때',R['r3'])+'\n'+box('r6','파일 내용 보기',R['r6'])+'\n'+box('open2','발표 페이지를 브라우저로 열기',OPEN2)+'\n'+box('r9','발표 페이지 링크가 안 열려요',R['r9'])+'\n'+box('r10','발표에서 말할 숫자가 맞는지 확인',R['r10'])+'''
</div></details>
</section>

<section id="s8">
<span class="eyebrow">막히면</span>
<h2>긴 설명 대신 한 줄을 보내요</h2>
<details><summary>화면이 통째로 비어 있어요, 버튼이 안 눌려요</summary><div class="body"><p>화면 파일의 스크립트에 오류가 있으면 표도 버튼도 안 보여요. "team_deck.html을 열었더니 화면이 비어 있어. 버튼이 안 눌려. 스크립트 오류를 찾아 고쳐줘."라고 보내고, 끝나면 파일 이름을 다시 눌러 봐요.</p></div></details>
<details><summary>조원 파일이 안 왔어요</summary><div class="body"><p>P3은 빠진 장을 [조원 파일 없음]으로 남기고 나머지를 만들어요. 발표 전에 파일을 받아 P3을 한 번 더 보내요. 그래도 안 오면 그 장은 발표 시간에서 빼고 "내 장 파일이 없어 발표에서 빠져요"라고 말해요.</p></div></details>
<details><summary>발표 링크가 안 열려요</summary><div class="body"><p>리모컨 "발표 페이지 링크가 안 열려요"를 보내요. 그래도 안 되면 파일 이름을 적고, 내 노트북에서 파일을 열어 발표해요.</p></div></details>
<details><summary>숫자가 어디서 왔는지 모르겠어요</summary><div class="body"><p>리모컨 "발표에서 말할 숫자가 맞는지 확인"을 보내요. 근거 파일의 줄을 찾아 줘요. 찾지 못하면 그 숫자는 발표에서 빼고 "못 찾음"이라고 말해요.</p></div></details>
<details><summary>Q&A에서 답이 생각나지 않아요</summary><div class="body"><p>"지금 숫자로는 말할 수 없어요. 확인해서 알려 드릴게요"라고 말해도 돼요. 그 질문은 피드백 카드에 적히고, 나중에 확인해서 답하면 돼요.</p></div></details>
<details><summary>말할 시간이 5분을 넘어요</summary><div class="body"><p>장마다 한 문장을 빼요. 문제 칸부터 줄이고, 데모는 30초를 지켜요. 리모컨 "말이 길 때"를 보내도 돼요.</p></div></details>
<details><summary>Chart.js가 안 그려져요</summary><div class="body"><p>인터넷이 끊기면 외부 라이브러리를 불러오지 못해요. 막대 대신 숫자를 글로 적고, "막대는 인터넷이 있을 때 보여요"라고 적어 둬요.</p></div></details>
</section>
</div>

<button class="theme" id="themeBtn" type="button">다크 모드</button>
<div class="toast" id="toast" role="status" aria-live="polite">복사됐어요</div>
'''
body=expand_mvp_html(body)
out='<meta name="claude:viewport-fit-sides" content="cover">\n<title>Day 18 · 인터랙티브 HTML 발표(MVP)</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap">\n'+style+'\n'+body+'\n'+script+'\n'
import sys
dest=sys.argv[1] if len(sys.argv)>1 else PATH
open(dest,'w',encoding='utf-8').write(out)
print('written',dest,len(out),'boxes',out.count('class="copy"'))
