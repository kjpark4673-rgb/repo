# Day 18 가이드 1판: 공식 일정표 11/18 [Lifestyle ⑩] "피칭 가이드 & Lifestyle 피칭 데이 - 인터랙티브 발표"
# (인터랙티브 HTML 발표, 슬라이드 스킬로 개요 → HTML 피치덱, PDF 백업, 피치 구조 일곱 칸과 라이브 데모 요령, 오후 피칭·피드백, NotebookLM 리허설, Vercel 배포, [크] 숏폼 연출, [데] Chart.js 라이브 차트)
# 강사 문답(11/15): 개인별 피칭, 조 안에서 먼저(3분) → 조 대표만 반 전체 앞(5분 + 3분 질문). 링크는 아티팩트가 기본, Vercel은 선택.
#                  피드백은 전체 발표 = 구글 폼(강사가 만듦), 조 안 발표 = 피드백 카드 페이지. 숏폼 티저는 내 MVP 소개(Day 17 오후 C의 15초 소개 영상 콘티 teaser.md).
# 저장소 안에서 그대로 돈다: python3 classroom/tools/build_day18.py [출력 경로]
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide_common import *
PATH=os.path.join(REPO,'classroom','student-guide','day18.html')
TOP=' style="margin-top:12px"'
FEEDBACK_URL='https://claude.ai/artifact/1qRcFTCRostToaCzG4iutz'
CHARTJS='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.5.1/chart.umd.min.js'

B=tok('brand','라라스윗'); P=tok('product','저당 아이스크림'); C=tok('customer','다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인')
HAND=tok('hand','재지 않음'); MINE=tok('mine','재지 않음'); ROLE=tok('role','아직 모름'); ME=tok('me','[이름]'); LINK=tok('mvplink','mvp.html'); FB=tok('fb','적지 않음'); REC=tok('rec','적지 않음')
PR={}
PR['p00']='''오늘은 11/18 피칭 데이야. 어제 쓰던 이 폴더에서 시작할게. 아래를 해줘.
1. CLAUDE.md에 "수업 작업 규칙"과 "나와 회사"가 있으면 그대로 두고, 없으면 만들어줘.
- 수업 작업 규칙: 되묻지 않고 가정해서 끝까지 만든다 / 추측한 곳은 (가정) / 웹에서 찾은 값에는 조사일과 출처 링크, 못 찾은 값은 "못 찾음" / 끝나면 3줄로만 보고하고, 내용을 보여 달라고 하면 그대로 보여 준다 / 한국어로 쉽게
- 나와 회사: 하고 싶은 일 '''+ROLE+''' / 회사 '''+B+''' ('''+P+''') / 고객 '''+C+'''
2. CLAUDE.md 맨 아래에 "# 오늘 규칙 (11/18 피칭 데이)"를 넣어줘. 같은 제목이 있으면 바꿔 넣어줘.
- 발표 화면의 숫자는 이 폴더의 파일에서만 가져오고, 어느 파일에서 왔는지 적는다. 없는 숫자는 [채울 곳], 어림셈은 (가정).
- 발표 화면을 고치기 전에는 그때의 화면을 pitch_backup_지금시각.html로 남긴다.
3. pitch.md, test_report.md, mvp.html이 있는지 봐줘. mvp.html이 없으면 CLAUDE.md의 회사로 경쟁사 가격과 증정품·프로모션을 조사해 research.csv와 mvp.html부터 만들어줘. pitch.md가 없으면 폴더의 파일로 일곱 칸 뼈대(문제 / 해결 / 시장 / BM / MVP / 함께 만든 것 / 요청사항)를 만들어줘.
되묻지 말고 끝까지 하고, 끝나면 "있던 파일 / 새로 만든 파일 / pitch.md에 남은 [채울 곳] 개수"를 3줄로만 알려줘.'''
PR['c1']='''어제 Microsoft Clarity로 녹화한 것을 보고 내가 본 것이야. test_report.md에 더해줘.
- 내가 본 것: '''+REC+'''
- test_report.md 맨 아래에 "녹화로 본 것 (Microsoft Clarity)" 표가 없으면 만들고, 있으면 그 아래에 이어서 더해줘: 본 것(내가 적은 말 그대로) / 종이 기록(test_log.md)에도 있던 것인지, 녹화로 새로 찾은 것인지 / 고칠 곳 후보
- 녹화는 본 사람 수와 날짜가 종이 테스트와 달라서 숫자를 합치지 마. 내가 적지 않은 클릭 수, 비율, 시간은 지어내지 마.
- 내가 본 것이 "적지 않음"이면 아무것도 더하지 말고, 녹화를 볼 때 확인할 것 3가지만 알려줘.
test_report.md가 없으면 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 더한 표만 보여줘.'''
PR['p01']='''pitch.md로 내 MVP 발표 화면 pitch.html을 만들어줘. 브라우저에서 넘기며 발표하는 HTML 발표 자료야. 파일 하나로.
- 슬라이드 9장: 표지(MVP 이름, 한 줄 약속, 발표자 '''+ME+''') / 문제 / 해결 / 시장 / BM / MVP 라이브 데모 / 사용자 테스트 결과 / 함께 만든 것 / 요청사항
- 장마다 큰 글자 한 문장과 보여 줄 것 하나. 글은 장마다 3줄 안.
- 넘기기: 키보드 ←→와 스페이스, 화면 왼쪽·오른쪽 누르기, 폰에서는 밀기. 오른쪽 아래에 쪽 번호(3/9).
- 숫자 하나는 움직이는 차트로: 하루 조사에 손으로 걸리던 시간과 내 MVP로 걸릴 시간을 같은 단위(분)로 막대 두 개(Chart.js '''+CHARTJS+'''). 잰 값이 아니면 차트에 (가정)이라고 적어줘. 차트가 안 뜨면 숫자 글자로 보이게.
- 내가 직접 잰 시간(같은 질문 하나를 찾는 데): 손으로 '''+HAND+''' / 내 화면으로 '''+MINE+'''. 둘 다 적혀 있으면 차트를 이 두 값으로 그리고(같은 단위로) "직접 잼 · 질문 하나 · 1회"라고 적어줘. 문제 장에도 이 값을 쓰고 pitch.md의 문제 칸에 적어줘. 하나라도 "재지 않음"이면 위처럼 pitch.md의 값으로 그려줘.
- 사용자 테스트 결과 장: test_report.md에 "녹화로 본 것 (Microsoft Clarity)" 표가 있으면 그 표의 본 것 한두 줄을 "녹화로 본 것"으로 더해줘(적힌 말 그대로, 숫자를 새로 만들지 마). images 폴더에 heatmap.png가 있으면 이 장에 같이 넣어줘. 표가 없으면 이 줄은 건너뛰어.
- 라이브 데모 장: 데모 순서 3단계와 큰 버튼 "MVP 열기". 버튼 주소: '''+LINK+'''
- 해결 장: 이 폴더에 teaser.mp4가 있으면 영상을 넣고(같은 폴더의 파일로), 없으면 영상 자리 없이 한 줄 약속만. landing.html이 있으면 "랜딩페이지 보기" 버튼도.
- 함께 만든 것 장의 "내가 내린 결정"은 pitch.md에 적힌 것만 옮겨. pitch.md에 [채울 곳: 내가 내린 결정]이면 그 장의 큰 문장에도 "제가 정했다", "방향은 제가" 같은 말을 쓰지 말고, 결정 칸을 [채울 곳: 내가 내린 결정]으로 둬. 수업 프롬프트와 CLAUDE.md의 규칙은 내 결정이 아니야.
- images 폴더에 kv.png가 있으면 표지 배경으로.
- 인쇄하면 한 장이 한 쪽으로 나오게 해줘(PDF 백업용). 맨 아래 작은 글씨로 "학습용 MVP 발표이며 실제 회사와 관계없습니다".
pitch.md가 없으면 폴더의 파일로 일곱 칸을 먼저 정하고 이어서 해줘. 되묻지 말고 끝까지 만들고, 끝나면 장마다 큰 문장만 9줄로 보여줘.'''
PR['p02']='''pitch.html로 발표할 대본을 script.md로 써줘. 오늘 오후에 조 안에서 3분 발표해.
- 장마다: 말할 문장(소리 내어 읽기 쉬운 말), 걸리는 초, 누를 것. 모두 3분(180초) 안에 끝나게. pitch.md 맨 아래에 "3분 버전에서 줄일 칸"이 있으면 그 칸을 줄여. 라이브 데모는 40초 안.
- 첫 15초는 문제를 숫자로 열어줘(예: "매일 ○분"). 마지막 문장은 요청사항.
- 데모: 무엇을 누르고, 어디를 가리키며, 무슨 말을 할지 3단계. 데모가 안 될 때 말할 한 문장과 대신 보여 줄 장(사용자 테스트 결과).
- pitch.md나 pitch.html에 [채울 곳]이 남은 숫자는 숫자 없이 말하는 문장으로 바꿔줘. [채울 곳: 내가 내린 결정]은 지어내지 말고 "(여기서 내가 정한 것을 한 줄 말해요)"로 둬.
pitch.html이 없으면 pitch.md로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 쓰고, 끝나면 대본 전체를 보여줘.'''
PR['p03']='''내 발표를 들은 깐깐한 팀장이 3분 질문 시간에 물을 질문을 뽑아 qa.md로 써줘.
- 질문 8개: 숫자의 근거 / 조사 값이 틀리면 어떻게 아나 / 매일 쓰는 데 드는 시간과 비용 / 이미 있는 서비스와 다른 점 / 누가 먼저 써 보나 / 안 되면 무엇을 배우나 같은 것.
- 질문마다 20초 안의 답 하나. 폴더의 파일에 근거하고 파일 이름을 적어줘. 근거가 없으면 "아직 확인하지 못했어요. ○○로 확인할게요"처럼 솔직하게.
- 가장 아픈 질문 3개에 ★.
- 맨 아래: 모르는 질문을 받았을 때 쓸 한 문장.
pitch.md가 없으면 폴더의 파일로 해줘. 되묻지 말고 끝까지 쓰고, 끝나면 ★ 질문 3개와 답만 보여줘.'''
PR['p05']='''나는 조 대표로 반 전체 앞에서 5분 발표와 3분 질문을 해. pitch.html과 script.md를 5분 버전으로 늘려줘.
- 조 안 발표에서 받은 피드백: '''+FB+'''
- 늘릴 곳: pitch.md 맨 아래의 "5분 버전에서 늘릴 칸"(없으면 시장과 BM). 라이브 데모는 1분.
- 받은 고칠 점 가운데 가장 많이 나온 것 하나를 발표 화면에 고쳐 넣고, 받은 질문과 답을 qa.md에 더해줘. 받은 피드백이 "적지 않음"이면 늘리기만 해줘.
- 고치기 전 화면은 pitch_backup_지금시각.html로 남겨줘.
pitch.html이 없으면 pitch.md로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 늘린 곳과 고친 곳만 3줄로 알려줘.'''
PR['p06']='''오늘 내 발표에 받은 피드백이야. 이걸로 발표 화면을 고치고 MVP의 다음 할 일을 정리해줘.
- 받은 피드백: '''+FB+'''
- pitch.html: 가장 많이 나온 고칠 점 2개만 고쳐줘. 고치기 전 화면은 pitch_backup_지금시각.html로 남겨줘.
- qa.md: 받은 질문과 더 나은 답을 더해줘. qa.md가 없으면 새로 만들어줘.
- next.md: 피드백에서 나온 MVP(mvp.html)의 다음 고칠 것 3개와 다음 주에 확인할 숫자 하나.
- 받은 피드백이 "적지 않음"이면 pitch.html은 고치지 말고, qa.md의 ★ 질문(없으면 네가 고른 질문 3개)으로 next.md만 써줘. 받은 말을 지어내지 마.
되묻지 말고 끝까지 하고, 끝나면 고친 곳 2줄과 next.md의 3개만 보여줘.'''
PR['w2']='''오늘 피칭 데이에 한 일을 내 포트폴리오에 넣을 한 장으로 정리해서 portfolio_1118.md로 써줘.
- 무엇을 했나: 어떤 MVP를 누구 앞에서 몇 분 발표했는지 한 줄과 파일(pitch.html, script.md, qa.md, next.md). 발표 화면 링크가 이 대화에 있으면 그 링크도.
- 받은 것: 받은 피드백의 별점 평균과 고칠 점, 받은 질문과 내 답. 받은 피드백에 없는 것은 쓰지 마.
- 수업에서 배운 방법 3줄(예: 문제를 숫자로 열기, 데모는 3단계로, 모르는 질문에는 확인 계획으로 답하기). 이건 내 결정이 아니야.
- 내가 내린 결정: 대본에서 내 말로 바꾼 것, ★ 질문에 내가 정한 답, 조 대표를 정한 것, 피드백 가운데 받아들인 것과 받아들이지 않은 것과 이유, 오늘 요청사항을 바꿨으면 그것. 내가 적거나 말한 것만 써. "적지 않음", "네가 정해줘"만 있으면 내가 정한 게 아니야.
- 네가 골랐고 내가 그대로 받은 것은 "Claude가 고름"이라고 쓰고, 옆에 [내가 적을 곳: 받아들인 이유]를 남겨줘. 큰 것 5개까지만.
- 이번 주 한 바퀴: 조사 도우미 만들기(11/16) → 사용자 테스트로 고치기(11/17) → 발표(11/18). portfolio_1116.md, portfolio_1117.md가 있으면 거기서 한 줄씩.
- 면접에서 말할 세 문장: 무엇을 만들어 누구 앞에서 발표했고, 어떤 질문을 받았고, 다음에 무엇을 고칠지. 내가 내리지 않은 결정을 내가 한 것처럼 쓰지 마. 쓸 결정이 없으면 그 문장은 [내가 적을 곳]으로 남겨줘.
되묻지 말고 끝까지 쓰고, 끝나면 "면접에서 말할 세 문장"과 [내가 적을 곳]이 남은 자리만 보여줘.'''
PR['x1']='''pitch.html의 BM 장에 슬라이더 세 개(쓰는 사람 수, 한 사람이 하루 줄이는 분, 시급)를 넣고, 움직이면 "한 달에 아끼는 시간과 돈" 막대 차트가 바로 바뀌게 해줘(Chart.js '''+CHARTJS+''').
- 처음 값은 pitch.md와 mvp.md의 값으로, 없으면 쓰는 사람 5명, 하루 30분, 시급 1만 5천 원으로 하고 (가정)이라고 화면에 적어줘. 한 달은 근무일 20일로.
- 범위: 사람 1~50명, 하루 줄이는 분은 0부터 mvp.md의 "손으로 하면 하루 몇 분"까지(없으면 120분), 시급 1만~5만 원.
- 차트 아래에 계산식을 한 줄로 보여 줘(사람 수 × 하루 줄인 분 × 20일 ÷ 60 = 시간, 시간 × 시급 = 원).
- 고치기 전 화면은 pitch_backup_지금시각.html로 남겨줘.
pitch.html이 없으면 pitch.md로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 처음 값과 그때의 결과만 한 줄로 알려줘.'''
PR['x2']='''발표 화면을 Vercel Drop에 올릴 폴더를 만들어줘.
- 이 폴더 안에 deploy 폴더를 만들고, pitch.html을 index.html이라는 이름으로 복사해줘. mvp.html, teaser.mp4(있으면), images 폴더(있으면)도 deploy 폴더에 복사해줘.
- deploy/index.html의 "MVP 열기" 버튼이 같은 폴더의 mvp.html을 열게 고쳐줘. 원래 pitch.html은 건드리지 마.
- 끝나면 deploy 폴더를 파일 탐색기(맥은 Finder)로 열어줘.
되묻지 말고 끝까지 하고, 끝나면 deploy 폴더에 든 파일만 알려줘.'''
for _k in list(PR): PR[_k]=expand_mvp_plain(PR[_k])
R={'r1':'되묻지 말고 네가 가정해서 끝까지 만들어줘. 가정한 곳만 (가정)이라고 표시해줘.',
'r2':'너무 길어. 3줄로만 다시 말해줘.',
'r3':'없는 자료는 없는 대로 두고, 지금 있는 것으로 끝까지 만들어줘.',
'r6':'방금 만든 파일의 내용을 그대로 보여줘. HTML이면 코드 말고 화면에 무엇이 어떤 순서로 있는지 알려줘.'}
OPEN='pitch.html을 브라우저로 열어줘.'
PUB='pitch.html을 아티팩트로 발행하고 링크를 알려줘.'
MVPPUB='mvp.html을 아티팩트로 발행하고 링크를 알려줘.'
REPUB='pitch.html을 고쳤어. 아까 발행한 아티팩트를 같은 링크로 다시 발행해줘. 같은 링크로 안 되면 새로 발행하고 새 링크를 알려줘.'

import base64
GALLERY_IMG='data:image/jpeg;base64,'+base64.b64encode(open(os.path.join(TOOLS,'day18_gallery','deck_marketer.jpg'),'rb').read()).decode()
STORY18=''
STORY_HTML=('<div class="story"><span class="tag">현업 이야기 · 강사님</span>'+STORY18+'</div>') if STORY18 else ''

body='''
<div class="wrap">
<nav id="nav" aria-label="구간 이동">
<a href="#s0">오늘</a><a href="#s1">준비</a><a href="#s2">1교시</a><a href="#s3">2교시</a><a href="#s4">3교시</a><a href="#s5">4교시</a><a href="#s6">조 안 발표</a><a href="#s7">전체 발표</a><a href="#s8">마무리</a><a href="#remote">리모컨</a><a href="#s9">막히면</a>
</nav>

<section id="s0">
<span class="eyebrow">Day 18 / 52 · 11/18(수)</span>
<h1>Day 18 · 내 MVP를 3분 안에 피칭하는 날</h1>
<p class="lead">이번 주에 만든 조사 도우미를 <b>듣는 사람이 "한번 써 보자"고 말하게</b> 발표해요. 오전에는 브라우저에서 넘기는 HTML 발표 화면과 대본을 만들고 링크로 내놓아요. 오후에는 조 안에서 한 사람씩 3분 발표하고, 조 대표가 반 전체 앞에서 5분 발표와 3분 질문을 해요.</p>

<h3 class="gap">오늘 한눈에</h3>
<div class="acts">
<div><b>① 발표 화면</b><span>09:10–10:40</span></div>
<div><b>② 연습과 링크</b><span>10:40–13:00</span></div>
<div><b>③ 피칭과 고치기</b><span>14:00–18:00</span></div>
</div>
<div class="map">
<div class="grp">시작</div>
<div class="row rest"><span class="t">09:00</span><span class="w">오늘 한눈에 보기 (지금 이 화면)</span></div>
<a class="row" href="#s1"><span class="t">09:05</span><span class="w"><b>준비 · 어제 폴더 확인</b><small>남는 것: 오늘 규칙이 더해진 CLAUDE.md</small></span></a>
<div class="grp">① 발표 화면 · 어제의 뼈대로 넘기는 발표 화면과 대본을 만들어요</div>
<a class="row" href="#s2"><span class="t">09:10</span><span class="w"><b>1교시 · 2026년의 발표, 피치 일곱 칸, HTML 발표 화면</b><small>남는 것: pitch.html</small></span></a>
<a class="row" href="#s3"><span class="t">10:00</span><span class="w"><b>2교시 · 3분 대본과 라이브 데모 순서</b><small>남는 것: script.md</small></span></a>
<div class="grp">② 연습과 링크 · 아픈 질문에 미리 답하고, 남이 여는 링크로 내놓아요</div>
<a class="row" href="#s4"><span class="t">10:40</span><span class="w"><b>3교시 · 깐깐한 질문 연습, 짝꿍 리허설</b><small>남는 것: qa.md</small></span></a>
<a class="row" href="#s5"><span class="t">11:40</span><span class="w"><b>4교시 · 링크로 내놓기, PDF 백업, 심화</b><small>남는 것: 발표 화면 링크, PDF</small></span></a>
<div class="row rest"><span class="t">13:00</span><span class="w">점심</span></div>
<div class="grp">③ 피칭과 고치기 · 발표하고, 받은 피드백으로 고쳐요</div>
<a class="row" href="#s6"><span class="t">14:00</span><span class="w"><b>조 안 발표 · 한 사람씩 3분, 피드백 카드, 조 대표 정하기</b><small>남는 것: 받은 피드백 카드</small></span></a>
<a class="row" href="#s7"><span class="t">15:00</span><span class="w"><b>전체 발표 · 조 대표 5분 + 질문 3분, 구글 폼 피드백</b><small>남는 것: 발표 경험, 받은 질문</small></span></a>
<a class="row" href="#s8"><span class="t">16:30</span><span class="w"><b>고치기와 마무리 · 피드백으로 고치기, 포트폴리오 한 장</b><small>남는 것: next.md, portfolio_1118.md</small></span></a>
</div>
<p class="sub">줄을 누르면 그 구간으로 가요. <b>꼭 하는 것</b>은 P0 → 직접 재 보기 → P1 → P2 → P3 → 링크, 조 안 발표, P6, W2예요. 조 대표는 P5도 해요.</p>

<div class="card"><h3>오늘 듣는 사람이 보는 세 가지</h3>
<p class="sub">조 안 발표와 전체 발표 모두 이 세 가지를 5점으로 매겨요. 공식 평가 점수가 아니라 서로 주는 피드백이에요.</p>
<ol class="steps"><li><b>문제가 분명했어요</b> · 누가 매일 무엇에 시간을 쓰는지 바로 이해됐나요?</li><li><b>데모를 보고 믿음이 갔어요</b> · 화면이 정말 그 일을 줄여 줄 것 같았나요?</li><li><b>요청사항이 분명했어요</b> · 발표자가 무엇을 바라는지 한 문장으로 말할 수 있나요?</li></ol></div>

<div class="card soft"><h3>어제 못 끝냈어도 괜찮아요</h3><p>P0이 pitch.md와 mvp.html이 있는지 보고, 없으면 먼저 만들어요. 그 경우 3~5분 걸려요. 어제와 <b>같은 작업 폴더</b>를 열고 시작해요.</p></div>

<h3 class="gap">오늘 수업, 이렇게 보면 돼요</h3>
<details><summary>오늘은 Lifestyle 단원의 마지막 날이에요</summary><div class="body">
<p>공식 일정표에서 11월 5일에 시작한 Lifestyle 단원이 오늘 끝나요. 조사하고, 만들고, 사람에게 시켜 보고, 오늘 발표해요. 내일(11/19)부터는 Modeling 단원이 시작돼요.</p>
<p>오늘 발표하는 주제는 오늘로 한 바퀴가 끝나요. 12월 7일부터는 새 주제로 같은 순서를 한 번 더 돌아요. 그러니까 남는 것은 주제가 아니라 <b>방법과 도구, 그리고 결과물</b>이에요.</p></div></details>
<details><summary>발표 자료는 PPT가 아니라 브라우저에서 넘기는 HTML이에요</summary><div class="body">
<p>공식 일정표의 오늘 첫 줄이 "정적 PPT → 브라우저에서 돌아가는 인터랙티브 HTML 발표(애니메이션·라이브 차트·데모 임베드)"예요. 링크 하나로 누구나 열어 보고, 발표 중에 진짜 화면(MVP)을 바로 열고, 숫자가 움직이는 차트를 보여 줄 수 있어요. PDF는 백업으로만 만들어요.</p></div></details>
<details><summary>초안은 Claude가 만들고, 결정은 내가 해요</summary><div class="body">
<p>오늘 내가 내리는 결정은 네 가지예요. 가이드에서 <b>"내 결정"</b>이라고 적힌 곳이에요.</p>
<ul><li>대본을 <b>내 말로</b> 바꾸기</li><li>아픈 질문에 <b>내 답</b> 정하기</li><li>조 안에서 <b>조 대표</b> 정하기</li><li>받은 피드백 가운데 <b>무엇을 받아들일지</b> 정하기</li></ul></div></details>

<h3 class="gap">용어</h3>
<details><summary>오늘 처음 나오는 말</summary><div class="body">
<ul><li><b>피칭(피치)</b> · 짧은 시간에 듣는 사람이 "해 보자"고 정하게 만드는 발표예요.</li><li><b>피치덱</b> · 피칭에 쓰는 발표 화면 묶음이에요. 오늘은 pitch.html 한 파일이에요.</li><li><b>인터랙티브 HTML 발표</b> · 브라우저에서 넘기며 보여 주는 발표예요. 누르면 열리고, 숫자가 움직여요.</li><li><b>라이브 데모</b> · 발표 중에 진짜 화면을 열어 직접 눌러 보이는 것이에요.</li><li><b>Q&A<span class="ab">(Questions and Answers)</span></b> · 발표 뒤 질문과 답 시간이에요. 오늘 전체 발표는 3분이에요.</li><li><b>BM<span class="ab">(Business Model)</span></b> · 돈이 되는 길이에요. 회사 안 도구라면 아끼는 시간, 밖에 판다면 누가 얼마를 내는지예요.</li><li><b>요청사항</b> · 발표 끝에 듣는 사람에게 바라는 것 하나예요. 예: "일주일 써 볼 동료 3명을 주세요."</li><li><b>Chart.js</b> · 웹페이지에 움직이는 차트를 그려 주는 도구예요. 공식 일정표의 데이터·서비스 트랙 도구예요.</li><li><b>배포</b> · 내 컴퓨터의 파일을 남이 열 수 있는 링크로 올리는 일이에요. 오늘 기본은 아티팩트 발행, 선택은 Vercel이에요.</li><li><b>리허설</b> · 실제처럼 미리 해 보는 연습이에요.</li><li><b>한 줄 약속</b> · 이 MVP가 해 주는 일을 한 문장으로 쓴 것이에요. 어제 화면 맨 위의 그 한 줄이에요.</li><li><b>피드백 카드 페이지</b> · 강사님이 만든 웹페이지예요. 카드를 쓰고 복사하는 곳, 받은 카드를 모아 평균을 내는 곳이 있어요. 아무 데도 저장하지 않아요.</li><li><b>W2</b> · 하루를 포트폴리오 한 장으로 남기는 저녁 프롬프트예요.</li><li><b>Gemini Notebook(옛 NotebookLM)</b> · 자료를 넣으면 두 사람이 대화하듯 요약해 주는 Google의 무료 도구예요. 7월에 이름이 바뀌었어요.</li></ul></div></details>
</section>

<section id="s1">
<span class="eyebrow">시작 · 09:05–09:10 · 준비</span>
<h2>어제 폴더를 열고 오늘 규칙을 더해요</h2>
<p class="why"><b>왜 해요?</b> 발표의 숫자는 이번 주에 만든 파일에서 나와요. 같은 폴더에서 시작해야 Claude가 그 파일을 읽어요.</p>
<div class="card checks">
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="a1"><span>Claude Code에서 <b>어제와 같은 작업 폴더</b>를 열고 새 대화를 시작했어요</span></label>
<label class="check"><input type="checkbox" data-k="a2"><span>아래 칸에 <b>발표자 이름</b>과 <b>어제 화면 링크</b>를 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="a3"><span><b>P0</b>을 실행했어요</span></label>
</div>
<div class="card" id="profileCard">
<h3>발표에 들어갈 것</h3>
<div class="field"><label for="v-me">발표 화면 표지에 넣을 내 이름</label><input id="v-me" data-in="me" type="text" maxlength="30" placeholder="비워 두면: [이름] (나중에 '표지 이름을 ○○로 바꿔줘'라고 말해요)" autocomplete="off"></div>
<div class="field"><label for="v-mvplink">어제 고친 화면(mvp.html)의 링크. 실습시트에 적은 claude.ai 링크를 붙여요</label><input id="v-mvplink" data-in="mvplink" type="text" maxlength="90" placeholder="비워 두면: mvp.html (내 노트북에서만 열려요)" autocomplete="off"></div>
<p class="sub">어제 링크가 없으면 <b>P1보다 먼저</b> 아래 상자로 만들어 칸에 붙여요. 시간이 없으면 비워 두고 발표는 내 노트북으로 해요.</p>'''+box('mvppub','어제 화면 링크 만들기',MVPPUB)+'''<p class="sub">어제 P0을 보낸 폴더라면 아래 네 칸은 비워 둬도 돼요. Claude가 CLAUDE.md에 적힌 것을 그대로 써요.</p>
<div class="field"><label for="v-role">내가 하고 싶은 일</label><input id="v-role" data-in="role" type="text" maxlength="40" placeholder="비워 두면: 아직 모름 (CLAUDE.md에 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-brand">회사(브랜드) 이름</label><input id="v-brand" data-in="brand" type="text" maxlength="40" placeholder="비워 두면: 라라스윗" autocomplete="off"></div>
<div class="field"><label for="v-product">제품·서비스 한 줄</label><input id="v-product" data-in="product" type="text" maxlength="60" placeholder="비워 두면: 저당 아이스크림" autocomplete="off"></div>
<div class="field"><label for="v-customer">그 회사의 고객 한 줄</label><input id="v-customer" data-in="customer" type="text" maxlength="90" placeholder="비워 두면: 다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인" autocomplete="off"></div>
<button class="ghost" id="resetProfile" type="button">처음 값으로 되돌리기</button>
</div>
'''+box('p00','P0 · 어제 폴더 확인하고 오늘 규칙 더하기 (꼭)',PR['p00'])+'''
<div class="card path"><span class="pill deep">Clarity를 달았다면 · 테크 트랙</span><h3>어제 녹화를 아직 못 봤다면 지금 봐요</h3>
<p class="sub">어제 오후 E에서 Clarity를 달았다면, 녹화와 히트맵은 뜨는 데 최대 2시간쯤 걸려서 어제 못 본 사람이 있어요. clarity.microsoft.com의 <b>녹화(Recordings)</b>와 <b>히트맵(Heatmaps)</b>을 열어 3분만 보고, 본 것을 칸에 적어요. 어제 P11까지 했다면 건너뛰어요. Clarity를 하지 않은 사람도 건너뛰어요.</p>
<p class="sub">히트맵을 발표에 쓰고 싶으면 화면을 캡처해 images 폴더에 <b>heatmap.png</b>로 저장해요. P1이 사용자 테스트 결과 장에 넣어 줘요.</p>
'''+fieldwide('rec','녹화와 히트맵에서 본 것. 예: 2번 일에서 표 제목을 세 번 눌렀다 / 걸러 보기 버튼 옆 빈 곳을 누름','비워 두면: 적지 않음')+'\n'+box('c1','녹화로 본 것을 결과서에 더하기 (Clarity)',PR['c1'])+'''</div>
<div class="card warn"><h3>허락 창이 뜨면</h3>
<p><b>방금 보낸 프롬프트가 시킨 일이면 Yes</b>를 눌러요. 오늘 자주 뜨는 것: 파일 만들기와 고치기, 파일 복사(cp, copy), 브라우저 열기(open, start), 링크 만들기(아티팩트 발행). 파일이나 폴더를 통째로 지우겠다고 하면(rm, delete) 누르지 말고 강사를 불러요.</p></div>
<h3 class="gap" id="remote">리모컨 네 개 · 필요할 때만 꺼내 써요</h3>
<p class="sub"><b>지금 보내는 상자가 아니에요.</b> Claude가 마음에 안 들게 움직이면 긴 설명 대신 이 짧은 상자를 보내요.</p>
'''+box('r1','되물을 때',R['r1'])+'\n'+box('r2','말이 길 때',R['r2'])+'\n'+box('r3','자료가 없다고 멈췄을 때',R['r3'])+'\n'+box('r6','파일 내용 보기',R['r6'])+'''
</section>

<section id="s2">
<span class="eyebrow">① 발표 화면 · 09:10–10:00 · 1교시</span>
<h2>피치 일곱 칸을 HTML 발표 화면으로 만들어요</h2>
<p class="why"><b>왜 해요?</b> 회사에서는 좋은 도구를 만들어도 팀장이 "써 보자"고 해야 쓰여요. 그 한마디를 듣는 3분이 피칭이에요.</p>
'''+STORY_HTML+'''
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>2026년의 발표는 이렇게 달라요</h3>
<div class="grid">
<div class="card red"><h3>예전 발표</h3><ul><li>PPT 파일을 보내고 화면을 넘겨요</li><li>숫자는 멈춘 그림이에요</li><li>"실제 화면은 나중에 보여 드릴게요"</li></ul></div>
<div class="card ok"><h3>오늘 발표</h3><ul><li>링크 하나로 누구나 열어요</li><li>숫자가 움직이는 차트로 보여요</li><li>발표 중에 진짜 화면을 열어 눌러요(라이브 데모)</li></ul></div>
</div></div>
<div class="card"><h3>피치 일곱 칸 (어제 pitch.md의 순서)</h3>
<p>공식 피치 구조는 <b>문제 - 해결 - 시장 - BM - MVP - 팀 - 요청사항</b>이에요. 오늘은 개인 발표라 "팀" 칸을 <b>함께 만든 것</b>(테스트해 준 사람, 에이전트가 한 일, 내가 내린 결정)으로 써요. 발표 화면은 표지와 사용자 테스트 결과를 더해 9장이에요.</p>
<p><b>비유:</b> 엘리베이터에서 팀장을 만나 1층에 닿기 전에 "그거 한번 써 보자"는 말을 듣는 것과 같아요. 문제로 귀를 열고, 데모로 믿게 하고, 요청으로 끝내요.</p></div>
<div class="card soft"><h3>라이브 데모 요령 세 가지</h3><ol><li><b>세 번만 누른다.</b> 데모 순서 3단계를 미리 정해요. 2교시 대본에 들어가요.</li><li><b>열어 두고 시작한다.</b> 발표 전에 MVP 화면을 탭 하나에 열어 둬요.</li><li><b>안 될 때 할 말을 정해 둔다.</b> "화면이 안 열리면 테스트 결과로 보여 드릴게요"처럼. 사용자 테스트 결과 장이 대신 보여 줄 장이에요.</li></ol></div>
<span class="pill">따라 하기</span>
<div class="card"><h3>먼저 5분 · 직접 재 보기</h3>
<p>발표의 "몇 분 걸리던 일이 몇 분으로"는 지금 어림셈(가정)이에요. 직접 잰 숫자 하나가 있으면 발표가 훨씬 단단해져요.</p>
<ol class="steps"><li>내 화면이 답해 주는 <b>질문 하나</b>를 정해요. 어제 시켜 볼 일 카드 가운데 하나가 좋아요. 예: "오늘 100ml당 가장 싼 곳은?"</li><li><b>손으로</b> 찾아봐요. 내 화면을 보지 않고 쇼핑몰이나 검색으로 직접 찾으며 휴대폰으로 시간을 재요. 5분이 넘으면 멈추고 "5분 넘음"이라고 적어요.</li><li><b>내 화면으로</b> 같은 질문의 답을 찾으며 시간을 재요.</li><li>아래 두 칸에 적어요. 적은 값이 P1의 차트와 문제 장에 들어가요.</li></ol>
<p class="sub">한 번 잰 값이에요. 발표에서도 "질문 하나를 한 번 재 본 값"이라고 말해요. 에이전트가 조사를 돌리는 시간은 여기에 들어 있지 않아요. 재지 못했으면 칸을 비워 둬요. 어제 값에 (가정)을 붙여 그려요.</p></div>
'''+field('hand','손으로 찾는 데 걸린 시간. 예: 4분 20초','비워 두면: 재지 않음')+'''
'''+field('mine','내 화면으로 찾는 데 걸린 시간. 예: 15초','비워 두면: 재지 않음')+'''
<details><summary>완성하면 이런 모습이에요 · 시험에서 나온 발표 화면 9장</summary><div class="body"><p class="sub">수업 전 시험에서 콘텐츠 마케터 갈래가 P1로 만든 발표 화면이에요. 여러분의 화면은 이와 달라도 돼요. 숫자는 시험 날의 어림셈과 웹에서 찾은 값이라 확인된 값이 아니에요.</p><div class="shots" style="grid-template-columns:1fr"><figure><img src="'''+GALLERY_IMG+'''" alt="시험에서 나온 발표 화면 9장: 표지, 문제, 해결, 시장, BM, 라이브 데모, 사용자 테스트 결과, 함께 만든 것, 요청사항" width="1920" height="1179" loading="lazy"><figcaption><b>9장</b> · 표지 → 문제 → 해결 → 시장 → BM → 라이브 데모 → 사용자 테스트 결과 → 함께 만든 것 → 요청사항</figcaption></figure></div></div></details>
'''+box('p01','P1 · 발표 화면 pitch.html (꼭)',PR['p01'],TOP)+'''
'''+box('open','발표 화면을 브라우저로 열기',OPEN)+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="b1"><span>브라우저에서 pitch.html을 열고 → 키로 9장을 넘겨 봤어요</span></label>
<label class="check"><input type="checkbox" data-k="b2"><span>차트 장에서 막대가 움직였어요 (안 보이면 숫자 글자로 보여도 괜찮아요)</span></label>
<label class="check"><input type="checkbox" data-k="b3"><span>"MVP 열기" 버튼을 눌러 내 화면이 열렸어요</span></label>
</div>
<div class="card soft"><p><b>어제 오후 C에서 15초 소개 영상 콘티(teaser.md)를 만들었다면</b> 영상 AI와 화면 녹화로 만든 영상을 작업 폴더에 teaser.mp4로 저장해 두면 P1이 해결 장에 넣어요. 이미 P1을 보냈다면 "teaser.mp4를 해결 장에 넣어줘"라고 해요. 영상이 없으면 그대로 발표해요. 공식 일정표의 크리에이티브 트랙 과제("키비주얼·숏폼을 발표 흐름에 녹이는 연출")예요.</p></div>
</section>

<section id="s3">
<span class="eyebrow">① 발표 화면 · 10:00–10:40 · 2교시</span>
<h2>3분 대본과 데모 순서를 정해요</h2>
<p class="why"><b>왜 해요?</b> 3분은 생각보다 짧아요. 장마다 몇 초를 쓸지 정해 두지 않으면 데모 전에 시간이 끝나요.</p>
'''+box('p02','P2 · 3분 대본과 데모 순서 (꼭)',PR['p02'])+'''
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="c1"><span>대본을 소리 내어 읽으며 시간을 재 봤어요 (휴대폰 스톱워치)</span></label>
<label class="check"><input type="checkbox" data-k="c2"><span><b>내 결정 1</b> · 내 입에 안 붙는 문장을 내 말로 바꿨어요. "3장 문장을 '○○'로 바꿔줘. script.md도 고쳐줘."라고 말해요</span></label>
</div>
<details><summary>3분이 넘어요</summary><div class="body"><p>"script.md에서 시장과 BM 장을 한 문장씩으로 줄여서 3분 안에 맞춰줘."라고 해요. 데모는 줄이지 않아요.</p></div></details>
</section>

<section id="s4">
<span class="eyebrow">② 연습과 링크 · 10:40–11:40 · 3교시</span>
<h2>아픈 질문에 미리 답하고, 짝꿍 앞에서 한 번 해 봐요</h2>
<p class="why"><b>왜 해요?</b> 질문 시간에 무너지면 앞의 3분이 다 흔들려요. 아픈 질문은 미리 받아 보는 게 가장 좋은 연습이에요.</p>
'''+box('p03','P3 · 깐깐한 팀장의 질문 연습 (꼭)',PR['p03'])+'''
<div class="card soft"><p><b>모르는 질문을 받으면</b> 지어내지 말고 확인 계획으로 답해요. "아직 확인하지 못했어요. 다음 주에 동료 3명이 써 보면서 확인할게요." 현업에서도 가장 믿음이 가는 답이에요.</p></div>
<div class="card"><h3>짝꿍 리허설 (한 사람에 5분)</h3>
<ol class="steps"><li>짝꿍 앞에서 pitch.html로 3분 발표해요. 짝꿍은 시간을 재요.</li><li>짝꿍은 qa.md의 ★ 질문 하나를 골라 물어요.</li><li>짝꿍은 "오늘 듣는 사람이 보는 세 가지"로 한마디씩 해 줘요.</li><li>바꿔서 해요.</li></ol></div>
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="d1"><span>짝꿍 앞에서 3분 발표를 끝까지 해 봤어요</span></label>
<label class="check"><input type="checkbox" data-k="d2"><span><b>내 결정 2</b> · ★ 질문 3개의 답을 내 말로 정했어요. 바꿨으면 "★2의 답을 '○○'로 바꿔줘."라고 말해요</span></label>
</div>
<details><summary>먼저 끝났다면 · Gemini Notebook(옛 NotebookLM)으로 남의 귀로 듣기</summary><div class="body">
<p>공식 일정표의 리허설 도구예요. 내 대본을 넣으면 두 사람이 대화하듯 요약해 줘요. <b>그 두 사람이 내 문제와 해결을 한 문장으로 말하면</b> 잘 전달되는 발표예요.</p>
<ol><li>notebooklm.google.com을 열고 개인 Google 계정으로 로그인해요(무료). 7월에 이름이 Gemini Notebook으로 바뀌었고 주소는 그대로 이어져요.</li><li>새 노트북을 만들고 script.md를 올려요. 안 올라가면 "script.md 내용을 그대로 보여줘"로 받은 글을 붙여 넣어요.</li><li>설정에서 출력 언어를 한국어로 바꾸고 오디오 개요를 만들어요. 3~5분 걸려요.</li><li>들으면서 두 사람이 내 문제와 해결을 어떻게 말하는지 적어요. 엉뚱하게 말하면 그 장의 문장을 고쳐요.</li></ol>
<p class="sub">하루 만들 수 있는 횟수는 정해져 있어요. 한 번만 만들어요.</p></div></details>
</section>

<section id="s5">
<span class="eyebrow">② 연습과 링크 · 11:40–13:00 · 4교시</span>
<h2>발표 화면을 남이 여는 링크로 내놓아요</h2>
<p class="why"><b>왜 해요?</b> 피드백을 주는 사람도, 나중에 포트폴리오를 볼 사람도 링크로 열어요. 내 컴퓨터 주소는 나만 열려요.</p>
<div class="card"><h3>기본 · 아티팩트로 발행하기</h3>
'''+box('pub','발표 화면을 링크로 만들기 (꼭)',PUB)+'''
<ol><li>허락 창이 뜨면 Yes를 눌러요. Claude가 링크를 알려 줘요.</li><li>열린 화면의 <b>공유</b> 메뉴에서 <b>링크가 있는 사람은 누구나</b>로 바꿔요.</li><li>로그인하지 않은 창(시크릿 창)에서 링크를 열어 9장이 넘어가는지 확인해요.</li><li>실습시트에 적어요.</li></ol>
<p class="sub">링크 버전에는 teaser.mp4 영상이 들어가지 않아요. <b>발표는 내 노트북의 pitch.html로</b> 해요. 영상까지 한 링크에 넣고 싶으면 아래 Vercel을 써요. 발행한 뒤에 pitch.html을 고치면 링크 화면은 그대로예요. 고칠 때마다 아래 상자로 다시 발행해요.</p>'''+box('repub','고친 발표 화면 다시 발행하기',REPUB)+'''</div>
<div class="card soft"><p><b>"MVP 열기" 버튼이 mvp.html로 되어 있으면</b> 내 노트북에서만 열려요. 준비 구간의 "어제 화면 링크 만들기"로 링크를 만들고 "MVP 열기 버튼 주소를 이 링크로 바꿔줘: (링크)"라고 말한 뒤 다시 발행해요.</p></div>
<div class="card"><h3>PDF 백업 만들기</h3><p>공식 일정표에서 PDF는 백업용이에요. 인터넷이 끊기거나 화면이 안 열릴 때 써요.</p><ol><li>Chrome에서 pitch.html을 열어요.</li><li><b>Ctrl+P</b>(맥은 <b>⌘P</b>)를 눌러요.</li><li>대상을 <b>PDF로 저장</b>, 레이아웃을 <b>가로</b>로 하고 저장해요. 파일 이름은 pitch.pdf.</li></ol></div>
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="e1"><span>시크릿 창에서 내 발표 링크가 열렸고, 실습시트에 적었어요</span></label>
<label class="check"><input type="checkbox" data-k="e2"><span>pitch.pdf를 만들었어요</span></label>
</div>
<h3 class="gap">먼저 끝났다면 · 심화 두 가지</h3>
<p class="sub"><b>데이터·서비스 트랙(테크)은 4교시에 심화 1을 꼭 해요.</b> 공식 일정표의 트랙 과제예요. 리허설은 3교시에 짧게 해요.</p>
<div class="card path"><span class="pill">데이터·서비스 · 움직이는 BM 차트</span><h3>슬라이더를 움직이면 숫자가 바뀌어요</h3><p>공식 일정표의 데이터·서비스 트랙 과제("라이브 차트로 숫자를 움직이며 설득")예요. 듣는 사람이 "우리 팀은 10명인데?"라고 물으면 그 자리에서 바꿔 보여 줄 수 있어요. <b>끝나면 보이는 것:</b> BM 장의 슬라이더 두 개와 바뀌는 막대 · 20분</p>'''+box('x1','심화 1 · 움직이는 BM 차트',PR['x1'])+'''</div>
<div class="card path"><span class="pill">선택 · Vercel</span><h3>영상과 MVP까지 한 링크로 (Vercel Drop)</h3><p>공식 일정표의 배포 도구예요. 폴더를 끌어다 놓으면 링크가 나와요. <b>끝나면 보이는 것:</b> vercel.app 링크 하나에 발표 화면, MVP, 영상 · 20분</p>'''+box('x2','심화 2 · Vercel Drop에 올릴 폴더 만들기',PR['x2'])+'''
<ol><li>vercel.com/drop을 열고, 열린 deploy 폴더를 통째로 끌어다 놓아요.</li><li>나온 링크를 시크릿 창에서 열어 봐요.</li><li><b>Claim을 꼭 눌러요.</b> 계정 없이 올린 링크는 1시간 뒤에 사라져서 오후 발표 전에 없어져요. Claim을 눌러 무료 계정(Google이나 GitHub로 가입)을 만들면 계속 남아요.</li><li>발표 전에 pitch.html을 고쳤다면 심화 2 상자를 다시 보내 deploy 폴더를 새로 만들고 다시 끌어다 놓아요.</li></ol>
<p class="sub">11/15에 Vercel 공식 안내로 확인한 방법이에요. 화면이 다르면 강사님께 물어요.</p></div>
</section>

<section id="s6">
<span class="eyebrow">③ 피칭과 고치기 · 14:00–15:00 · 조 안 발표</span>
<h2>조 안에서 한 사람씩 3분, 피드백 카드를 주고받아요</h2>
<p class="why"><b>왜 해요?</b> 작은 자리에서 먼저 해 보면 큰 자리에서 덜 떨려요. 받은 카드로 고칠 곳도 미리 찾아요.</p>
<div class="card"><h3>이렇게 해요</h3>
<ol class="steps"><li>조에서 시간 재는 사람을 한 명 정해요. 한 사람에 <b>3분 발표 + 1분 질문</b>이에요. 세 명인 조는 12분, 두 명인 조는 8분쯤 걸려요.</li><li>듣는 사람은 발표가 끝나면 <b>피드백 카드 페이지</b>(아래 버튼, 강사님이 만든 웹페이지)의 "카드 쓰기"에서 발표자 이름, 별점 세 개(오늘 듣는 사람이 보는 세 가지), 좋았던 점·고칠 점·궁금한 것 한 줄씩을 적고 <b>카드 복사</b>를 눌러 <b>조 단톡방</b>에 올려요. 1분이면 써요.</li><li>모두 끝나면 조 단톡방의 카드를 보고 <b>조 대표</b>를 한 명 정해요. 별점이 높고, 반 전체가 보면 좋을 발표를 골라요.</li><li>발표자는 단톡방에서 내 카드를 복사해 피드백 카드 페이지의 <b>받은 카드 모으기</b>에 붙이고, <b>프롬프트에 붙일 글 복사</b>를 눌러 아래 "받은 피드백" 칸에 붙여요.</li></ol>
<p><a class="ghost" href="'''+FEEDBACK_URL+'''" target="_blank" rel="noopener">피드백 카드 페이지 열기</a></p></div>
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="f1"><span>조 안에서 3분 발표를 했어요</span></label>
<label class="check"><input type="checkbox" data-k="f2"><span>조원 모두에게 피드백 카드를 보냈어요</span></label>
<label class="check"><input type="checkbox" data-k="f3"><span><b>내 결정 3</b> · 조 대표를 같이 정했어요</span></label>
</div>
'''+fieldwide('fb','받은 피드백. 피드백 카드 페이지의 "프롬프트에 붙일 글 복사"를 누르고 여기에 붙여요. 받은 말을 직접 적어도 돼요','비워 두면: 적지 않음')+'''
<div class="card path"><span class="pill">조 대표만</span><h3>5분 버전으로 늘리기 (14:40–15:00)</h3><p>반 전체 앞에서는 5분 발표와 3분 질문이에요. 받은 카드를 위 칸에 붙이고 보내요. 끝나면 바로 다시 발행해요(4교시의 "고친 발표 화면 다시 발행하기").</p>'''+box('p05','P5 · 조 대표의 5분 버전',PR['p05'])+'''</div>
<div class="card soft"><p><b>조 대표가 아닌 사람</b>은 이 20분 동안 마무리의 <b>P6</b>을 보내 받은 카드로 고쳐요. P6은 <b>한 번만</b> 보내면 돼요. 16:30에는 W2만 보내요. 조 대표는 16:30에 P6을 보내요.</p></div>
</section>

<section id="s7">
<span class="eyebrow">③ 피칭과 고치기 · 15:00–16:30 · 전체 발표</span>
<h2>조 대표가 반 전체 앞에서 5분 발표하고 3분 질문을 받아요</h2>
<p class="why"><b>왜 해요?</b> 듣는 사람이 많아지면 질문도 달라져요. 다른 조의 발표에서 내 발표에 가져올 것을 찾아요.</p>
<div class="card"><h3>듣는 사람이 할 일</h3>
<ol class="steps"><li>발표자의 링크를 열어 같이 넘겨 봐도 돼요.</li><li>발표마다 <b>강사님이 주는 구글 폼</b>에 별점 세 개와 한 줄을 남겨요. 모인 결과는 강사님이 나중에 발표자에게 나눠 줘요.</li><li>질문 시간에 손을 들어 물어요. 좋은 질문은 "숫자가 어디서 왔어요?", "누가 먼저 써 봐요?"처럼 구체적인 질문이에요.</li></ol></div>
<div class="card"><h3>발표자(조 대표)가 할 일</h3>
<ol class="steps"><li>내 차례 전에 pitch.html과 MVP 화면을 탭 두 개로 열어 둬요. 앞 화면에 연결하는 방법은 강사님이 알려 줘요.</li><li>5분 안에 발표하고, 3분 동안 질문을 받아요. 모르는 질문에는 확인 계획으로 답해요.</li><li>받은 질문을 끝나고 바로 적어 둬요. 마무리에서 위 받은 피드백 칸에 더해요.</li></ol></div>
<div class="card checks">
<h3>이게 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="h1"><span>모든 발표에 구글 폼을 남겼고, 내 발표에 가져올 것 하나를 적었어요</span></label>
</div>
</section>

<section id="s8">
<span class="eyebrow">③ 피칭과 고치기 · 16:30–18:00 · 마무리</span>
<h2>받은 피드백으로 고치고, 오늘을 한 장으로 남겨요</h2>
<p class="why"><b>왜 해요?</b> 피드백은 받은 날 고쳐야 남아요. 오늘 받은 질문은 면접에서 받을 질문과 닮았어요.</p>
<div class="card soft"><p><b>조 대표</b>는 위 <b>받은 피드백</b> 칸에 조 안 카드와 전체 발표에서 받은 질문을 모두 넣고 P6을 보내요. 14:40에 P6을 보낸 사람은 건너뛰고 W2로 가요. 칸을 비워 두면 발표 화면은 그대로 두고 qa.md의 질문으로 다음 할 일만 정해요.</p></div>
'''+box('p06','P6 · 받은 피드백으로 고치기 (꼭)',PR['p06'])+'''
<div class="card checks">
<h3>이게 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g1"><span><b>내 결정 4</b> · 받아들인 피드백과 받아들이지 않은 피드백을 한 줄씩 말해 뒀어요. "○○는 받아들였어. △△는 이번엔 안 해. 이유는 ○○."</span></label>
</div>
<div class="card soft"><p>W2는 <b>아침부터 쓰던 대화</b>에서 보내요. 대화를 바꿨다면 W2 아래에 오늘 정한 것을 한 줄씩 덧붙여 같이 보내요.</p></div>
'''+box('w2','W2 · 오늘을 포트폴리오 한 장으로 (꼭)',PR['w2'])+'''
<div class="card checks">
<h3>내가 할 일 네 가지</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g2"><span>고친 발표 화면을 4교시의 "다시 발행하기" 상자로 다시 발행했어요. 새 링크가 나왔으면 실습시트를 고쳤어요</span></label>
<label class="check"><input type="checkbox" data-k="g3"><span><b>portfolio_1118.md</b>의 [내가 적을 곳]을 Claude에게 말해서 채웠어요 (세 문장부터)</span></label>
<label class="check"><input type="checkbox" data-k="g4"><span>실습시트에 <b>회고 4줄</b>을 적었어요: 오늘 발표한 것 / 가장 아팠던 질문 / 다음에 고칠 것 / 이번 주에 가장 시간 가는 줄 몰랐던 단계</span></label>
<label class="check"><input type="checkbox" data-k="g5"><span>이번 주 파일을 <b>하나도 지우지 않았어요</b> (12월 포트폴리오 사이트에 써요)</span></label>
</div>
<div class="card soft"><h3>내일부터</h3><p>내일(11/19)부터 Modeling 단원이 시작돼요. 첫날은 AI 모델이 어떻게 움직이는지, 같은 과제를 여러 AI로 견줘 보는 날이에요. 12월 4일에는 개인 데모와 포트폴리오 사이트가 있어요. 이번 주 파일이 그 재료예요.</p></div>
<div class="card blue"><div class="big">이번 주 여러분은 매일 하던 일을 줄이는 도구를<br>만들고, 시켜 보고, 발표했어요.</div></div>
</section>

<section id="s9">
<span class="eyebrow">막히면</span>
<h2>긴 설명 대신 한 줄을 보내요</h2>
<details><summary>pitch.md가 없어요 (어제 못 끝냈어요)</summary><div class="body"><p>P0을 보내면 먼저 만들어요. 3~5분 걸려요. 그사이 1교시 강의를 들어요.</p></div></details>
<details><summary>차트가 안 보여요</summary><div class="body"><p>인터넷이 끊기면 차트 도구를 못 불러와서 숫자 글자로 보여요. 그대로 발표해도 돼요. 다시 그리려면 "차트가 안 보여. Chart.js를 불러오는지 확인하고 고쳐줘."라고 해요.</p></div></details>
<details><summary>"MVP 열기" 버튼을 누르면 안 열려요</summary><div class="body"><p>버튼 주소가 mvp.html이면 내 노트북에서만 열려요. 4교시의 "어제 화면 링크 만들기"로 링크를 만들고 "MVP 열기 버튼 주소를 이 링크로 바꿔줘: (링크)"라고 해요.</p></div></details>
<details><summary>폰에서 발표 화면이 옆으로 밀려요</summary><div class="body"><p>"폰 폭(390px)에서 발표 화면이 옆으로 밀려. 고쳐줘."라고 해요. 발표는 노트북으로 하니 급하지 않아요.</p></div></details>
<details><summary>슬라이드가 안 넘어가요</summary><div class="body"><p>발표 화면을 한 번 누른 뒤 → 키를 눌러요. 그래도 안 되면 "키보드 →와 화면 오른쪽 누르기로 넘어가지 않아. 고쳐줘."라고 해요.</p></div></details>
<details><summary>대본이 3분을 넘어요</summary><div class="body"><p>"script.md에서 시장과 BM 장을 한 문장씩으로 줄여서 3분 안에 맞춰줘."라고 해요.</p></div></details>
<details><summary>영상이 발표 화면에 안 나와요</summary><div class="body"><p>teaser.mp4가 pitch.html과 <b>같은 폴더</b>에 있는지 봐요. 링크 버전에는 영상이 들어가지 않아요. 발표는 내 노트북의 pitch.html로 해요.</p></div></details>
<details><summary>발표 중에 화면이 멈췄어요</summary><div class="body"><p>당황하지 말고 pitch.pdf를 열어 이어서 해요. 데모는 "테스트 결과로 보여 드릴게요"라고 말하고 사용자 테스트 결과 장을 보여 줘요.</p></div></details>
<details><summary>고친 게 마음에 안 들어요</summary><div class="body"><p>고치기 전 화면은 pitch_backup_시각.html로 남아 있어요. "가장 최근 pitch_backup 파일로 pitch.html을 되돌려줘"라고 해요.</p></div></details>
<details><summary>Claude가 자꾸 되물어요</summary><div class="body"><p>리모컨 <b>"되물을 때"</b>를 보내요. 그래도 물으면 새 대화를 열고 P0을 다시 실행해요.</p></div></details>
<details><summary>사용량 한도 메시지가 떠요</summary><div class="body"><p>오후 발표는 Claude 없이도 할 수 있어요. 오전에 만든 pitch.html과 script.md로 해요. W2를 못 돌리면 실습시트에 오늘 받은 질문과 고칠 것을 한 줄씩 적고 내일 아침에 돌려요.</p></div></details>
<details><summary>새 대화를 열었더니 앞 내용을 몰라요</summary><div class="body"><p>괜찮아요. 프롬프트가 폴더의 파일을 읽게 되어 있어요. 내가 말로 남긴 결정만 새 대화가 몰라요. W2를 보낼 때 프롬프트 아래에 한 줄씩 덧붙여요.</p></div></details>
</section>
</div>

<button class="theme" id="themeBtn" type="button">다크 모드</button>
<div class="toast" id="toast" role="status" aria-live="polite">복사됐어요</div>
'''
body=expand_mvp_html(body)
out=build_page('Day 18 · 내 MVP(Minimum Viable Product) 3분 피칭',body,
  {'role':'아직 모름','me':'[이름]','mvplink':'mvp.html','fb':'적지 않음','hand':'재지 않음','mine':'재지 않음','rec':'적지 않음'},'l18-')
write_page(out,PATH)
