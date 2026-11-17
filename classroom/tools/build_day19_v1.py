# 보관본: Day 19 가이드 1판(11/17, 발행 Version 1). 강사 검토 "너무 초보자 수준"으로 2판(build_day19.py)으로 다시 설계함. 다시 만들면 day19_v1.html로 나옴
# Day 19 가이드 1판: 공식 일정표 11/19 [Modeling ①] "AI 이해 · 2026 모델 지형과 LLM의 한계"
# (LLM 원리(토큰·컨텍스트·확률적 생성), 추론·에이전트 모델, 2026 모델 지형과 '작업별로 고르기', 컨텍스트 열화와 세션 관리, AI 산출물의 저작권·개인정보·상표,
#  [크] 이미지·영상 모델 지형, [데] API로 모델 호출하는 구조. 도구: Claude / ChatGPT(무료) / Gemini(무료) 동일 과제 블라인드 비교, Claude Code(평가표 자동 집계).
#  공통 실습: 동일 과제 3개 모델 블라인드 비교 → 평가 기준표, 개인 AI 사용 가이드라인. [크] 기획·카피 과제로 비교, [데] 데이터 분석·코드 과제로 비교. 결과물: 모델 비교 평가표, 개인 AI 사용 가이드라인)
# 강사 문답(11/17): 견줄 일 = 내 MVP의 일(이번 주 파일로 직무마다) / 이름 가리기 = 조원이 섞어 줌 / 세 회사 그대로 / 테크 API = 오후 심화 한 장 / 현업 이야기 카드 없음
# 쉬운 말(11/17 강사 고름): 블라인드 비교 → 이름 가리고 견주기, 컨텍스트 열화 → 앞 내용이 흐려져요, 세션 관리 → 새 대화로 옮기기, 평가 기준표 → 점수 기준표, 개인 AI 사용 가이드라인 → 내 AI 사용 규칙
# 저장소 안에서 그대로 돈다: python3 classroom/tools/build_day19.py [출력 경로]
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide_common import *
PATH=os.path.join(REPO,'classroom','student-guide','day19_v1.html')
TOP=' style="margin-top:12px"'
CHARTJS='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.5.1/chart.umd.min.js'

B=tok('brand','라라스윗'); P=tok('product','저당 아이스크림'); C=tok('customer','다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인')
ROLE=tok('role','아직 모름'); KIND=tok('kind','네가 정해줘'); CRIT=tok('crit','네가 정해줘'); SCORE=tok('score','채점 전'); KEY=tok('key','공개 전')
RULE=tok('rule','적지 않음'); TEAM=tok('team','적지 않음'); IMGS=tok('imgscore','채점 전')

PR={}
PR['p00']='''오늘은 11/19 AI 이해 날이야. 이번 주에 쓰던 이 폴더에서 시작할게. 아래를 해줘.
1. CLAUDE.md에 "수업 작업 규칙"과 "나와 회사"가 있으면 그대로 두고, 없으면 만들어줘.
- 수업 작업 규칙: 되묻지 않고 가정해서 끝까지 만든다 / 추측한 곳은 (가정) / 웹에서 찾은 값에는 조사일과 출처 링크, 못 찾은 값은 "못 찾음" / 끝나면 3줄로만 보고하고, 내용을 보여 달라고 하면 그대로 보여 준다 / 한국어로 쉽게
- 나와 회사: 하고 싶은 일 '''+ROLE+''' / 회사 '''+B+''' ('''+P+''') / 고객 '''+C+'''
"나와 회사"가 이미 있으면 이미 적힌 값이 맞아. 위 값이 처음 값("아직 모름", "라라스윗", "저당 아이스크림", "다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인")이 아닌 것만 내가 새로 적은 것이니 그 줄을 바꿔줘.
2. CLAUDE.md 맨 아래에 "# 오늘 규칙 (11/19 AI 이해)"를 넣어줘. 같은 제목이 있으면 바꿔 넣고, 지난 날짜의 "# 오늘 규칙"은 제목만 "# 지난 규칙 (날짜)"로 바꿔줘.
- 다른 AI에 붙여 넣을 글은 한국어로 쓰고, 그 AI가 이 폴더를 못 봐도 알 수 있게 필요한 자료를 글 안에 넣는다. 실명, 연락처, 면담 내용은 넣지 않는다.
- 다른 AI가 쓴 답은 고치거나 보태지 않고 받은 그대로 저장한다.
- 점수는 내가 매긴 것만 적는다. 네가 점수를 매기거나 어느 AI의 답인지 추측하지 않는다.
3. 이 폴더에 pitch.md, mvp.md, mvp.html, research.csv가 있는지 봐줘. 없어도 오늘은 괜찮아.
되묻지 말고 끝까지 하고, 끝나면 "있던 파일 / 나와 회사의 하고 싶은 일과 회사 / CLAUDE.md에 더한 것"을 3줄로만 알려줘.'''
PR['p01']='''AI가 답을 만드는 방법을 내 파일로 보여줘. ai_basics.md로 저장해줘.
1. 토큰: 이 폴더의 글 파일(.md, .csv, .html)마다 글자 수와 토큰 수를 표로. 백업 파일(이름에 backup이 든 것)과 deploy 폴더는 빼줘. 어림한 값이면 (어림)이라고 적고, 가장 큰 파일 하나에 "새 대화에 통째로 넣기엔 큰 편인지" 한 줄.
2. 다음 낱말 맞히기: CLAUDE.md의 회사로 광고 문장의 앞부분 하나를 만들고("○○은 밤에 먹어도"처럼), 다음에 올 말 후보 5개를 그럴듯한 순서로 표에. 후보마다 높음·중간·낮음. 표 위에 "실제 확률이 아니라 설명용 예시예요"라고 적어줘.
3. 같은 질문에도 답이 매번 달라지는 이유를 2번 표로 한 줄.
글 파일이 없으면 CLAUDE.md만으로, CLAUDE.md도 없으면 '''+B+'''('''+P+''')로 해줘. 되묻지 말고 끝까지 하고, 끝나면 1번의 가장 큰 파일 한 줄, 2번 표, 3번 한 줄만 보여줘.'''
PR['p02']='''오늘 세 AI(Claude, ChatGPT, Gemini)에 똑같이 붙여 넣을 과제를 task.md로 만들어줘. 조원이 세 AI에 돌리고 이름을 가려서 돌려줄 거야.
- 견줄 일: '''+KIND+'''. "네가 정해줘"면 CLAUDE.md의 하고 싶은 일로 정해: 콘텐츠·브랜드 마케터 → 상세페이지 첫 화면 카피 3안 / MD·온라인 영업 → 경쟁사 가격·프로모션과 우리 판매가·마진 하한을 보고 우리 대응 프로모션 3안 / CX·서비스 기획 → 자주 오는 고객 문의 하나에 보낼 답변 3안 / 운영·인사 → 자주 보내는 안내문 하나의 3안 / 데이터·개발 → research.csv를 읽어 요약 표를 만드는 파이썬 코드와 그 결과 표 / 그 밖이나 아직 모름 → 상세페이지 첫 화면 카피 3안.
- 붙여 넣을 글: 한국어 1,200자 안. 그 AI는 이 폴더를 못 보니 필요한 자료(research.csv 몇 줄, pitch.md·mvp.md·mvp.html의 고객과 약속 같은 것)를 글 안에 넣어줘. 모르는 값(우리 판매가, 마진 같은 것)은 (가정)이라고 붙여 넣어줘. 코드 과제면 파일 이름 research.csv와 열 이름을 머리줄 그대로 적고 pandas까지만 쓰라고 해줘. 답의 모양(3안, 표, 코드)을 정해 주고, 실명·연락처·면담 내용은 넣지 마.
- 붙여 넣을 글은 "--- 여기부터 복사 ---"와 "--- 여기까지 ---" 줄 사이에 넣어줘. 점수 기준은 그 밖에 둬.
- 점수 기준 4개(각 1~5점), 기준마다 5점과 1점의 모습 한 줄. 하나는 "숫자와 사실이 자료와 맞나"로 해줘. 내가 넣고 싶은 기준: '''+CRIT+'''. "네가 정해줘"면 나머지를 네가 정하고, 적혀 있으면 그 기준을 꼭 넣어줘.
이번 주 파일이 없으면 CLAUDE.md의 회사로 자료 몇 줄을 (가정)으로 만들어 넣어줘. 되묻지 말고 끝까지 하고, 끝나면 붙여 넣을 글 전체(두 줄 표시 포함)와 기준 4개를 그대로 보여줘.'''
PR['p03']='''조원이 세 AI에 내 과제를 돌리고 이름을 가려서 보내 준 메시지를 이 프롬프트 아래에 붙였어(답 A, 답 B, 답 C). 점수만 고쳐 다시 보낼 때는 아래에 글이 없어. 이름 가리고 견주는 점수표를 만들어줘.
- 내 점수(task.md의 기준 순서): '''+SCORE+'''
1. blind 폴더에 A.md, B.md, C.md로 받은 글을 그대로 저장해줘. 고치거나 보태지 마. 이미 받은 글이 든 파일은 덮지 말고 그대로 둬. 아래에 답이 없고 그 파일도 없으면 "받지 못함"이라고만 적어줘.
2. eval.md에 표: 답 / 기준 4개 점수 / 합계 / 글자 수. 내 점수만 쓰고, 점수가 "채점 전"이면 점수 칸을 비워 둬. 그때는 표 아래에 셀 수 있는 사실(안의 개수, 표·코드가 있는지, 과제 글의 답 모양과 글자 수 조건을 지켰는지)만 답마다 한 줄씩 적어줘. 어느 쪽이 낫다는 말은 쓰지 마.
3. score.csv(답,기준,점수)로도 저장해줘. UTF-8 BOM.
네가 점수를 매기거나 어느 AI의 답인지 추측하지 마. task.md가 없으면 기준 4개를 먼저 정해 task.md에 쓰고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 eval.md의 표만 보여줘.'''
PR['p04']='''조원이 알려 준 답의 주인이야: '''+KEY+'''. 이름을 붙여 견주는 화면을 만들어줘.
- eval.md 표와 score.csv에 AI 이름 칸을 더해줘. 모델 이름이나 모드가 적혀 있으면 그것도. "공개 전"이면 A·B·C 그대로 둬.
- compare.html: 맨 위에 견준 일 한 줄(task.md에서), 기준마다 세 AI의 점수 막대(Chart.js '''+CHARTJS+''')와 합계. 차트가 안 뜨면 표로 보이게.
- 화면 아래에 "한 가지 일을 한 번 돌린 결과예요. 같은 AI도 다시 물으면 답이 달라져요."와 "이 일엔 이걸 쓸래요: [내가 적을 곳]".
- 점수가 비어 있으면 막대 대신 "채점 전"이라고 보여줘. 점수를 지어내지 마.
- 만든 뒤 스크립트 문법 오류(괄호, 따옴표 짝)가 없는지 다시 읽어 확인해줘.
eval.md가 없으면 blind 폴더와 task.md로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 기준마다 가장 높은 답만 4줄로 알려줘.'''
PR['p05']='''오늘 배운 것으로 내 AI 사용 규칙 한 장을 my_ai_rules.md로 써줘.
1. 일마다 고를 AI: eval.md나 compare.html에 내가 말한 "이 일엔 이걸 쓸래요"가 있으면 그대로, 없으면 [내가 적을 곳]. 내 일(CLAUDE.md의 하고 싶은 일)에서 자주 하는 다른 일 2개는 "아직 안 견줌".
2. 새 대화로 옮기기: 대화가 길어져 앞 내용이 흐려지는 신호 3가지와 옮기는 순서. 옮길 때 쓸 인계 메모 handoff.md도 이 폴더의 파일로 채워 만들어줘(나와 회사 / 이번 주 파일과 한 줄 설명 / CLAUDE.md와 파일에 적힌 결정 / 남은 일).
3. AI에 넣지 않을 것: 개인정보와 회사 안의 자료 예시 5개.
4. 내놓기 전에 볼 것(저작권·상표·개인정보): pitch.html, mvp.html, landing.html 가운데 있는 것을 읽고 남의 이미지·로고·글, 실제 회사 이름과 상표, 사람 이름, "학습용" 문구를 점검해 고칠 곳 후보를 3개까지 표로(파일 / 어디 / 왜 / 고칠 방법). 파일은 고치지 마. 표 아래에 "법률 판단이 아니라 점검 목록이에요" 한 줄.
5. 내 다짐: '''+RULE+'''. "적지 않음"이면 [내가 적을 곳].
되묻지 말고 끝까지 하고, 끝나면 4번 표와 [내가 적을 곳]이 남은 자리만 보여줘.'''
PR['p06']='''오늘 가장 높았던 AI에 task.md의 붙여 넣을 글을 새 대화 두 개에서 한 번씩 보냈어. 두 답을 이 프롬프트 아래에 붙였어(첫째 답, 둘째 답).
again.md로: 두 답에서 같은 것 / 달라진 것을 표로, 그리고 "한 번 돌린 결과로 AI를 고르면 안 되는 이유" 한 줄. 받은 글은 고치지 말고 맨 아래에 그대로 붙여줘. 아래에 답이 없으면 해 보는 순서만 3줄로 알려줘.
my_ai_rules.md가 있으면 1번 아래에 "같은 일을 두 번 이상 돌려 보고 정하기" 한 줄을 더해줘. 되묻지 말고 끝까지 하고, 끝나면 표만 보여줘.'''
PR['p07']='''우리 조원들이 각자 견준 결과야. 조 점수표를 team_eval.md로 만들어줘.
- 조원 결과: '''+TEAM+'''
- 표: 조원(직무만) / 견준 일 / 1등 AI / 합계 점수. 내 결과는 eval.md에서 가져와줘.
- 일의 종류(글쓰기, 표·숫자, 코드 같은 것)마다 1등이 같은지 한 줄씩. 맨 위에 "몇 명이 한 번씩 돌린 결과"라고 적고, "○○가 항상 낫다"처럼 넓혀 말하지 마.
- 조원 결과가 "적지 않음"이면 내 결과만 넣고 조원 칸은 [조원 결과 붙이기]로 둬.
eval.md가 없으면 내 줄도 [내 결과 붙이기]로 둬. 되묻지 말고 끝까지 하고, 끝나면 표만 보여줘.'''
PR['p08']='''이미지 AI 두 곳(ChatGPT, Gemini)에 똑같이 넣을 이미지 과제를 image_task.md로 만들어줘.
- 무엇: CLAUDE.md 회사의 광고에 쓸 배경·분위기 이미지 한 장(세로 4:5). 제품은 나중에 실제 제품 사진을 얹는다고 보고, 제품이 들어갈 자리를 비워 둬. pitch.md나 kv.md(Day 16에 쓴 키비주얼 설명)가 있으면 그 약속과 장면으로.
- 넣을 글: 한국어 3문장 안. 이미지 안에 글자를 넣지 말라고 적어줘.
- 실제 회사 로고, 남의 캐릭터, 실존 인물을 넣지 말라는 줄.
- 점수 기준 3개(각 1~5점): 약속이 보이나 / 브랜드 분위기 / 실제 제품 사진을 얹어 쓸 수 있나.
- 이 폴더 안에 images 폴더가 없으면 만들고, 파일 탐색기(맥은 Finder)로 열어줘.
되묻지 말고 끝까지 하고, 끝나면 넣을 글과 기준만 보여줘.'''
PR['p09']='''image_task.md의 글로 만든 이미지를 images 폴더에 img_chatgpt.png와 img_gemini.png로 저장했어. 내 점수: '''+IMGS+'''.
image_eval.md로: 이미지마다 파일 / 기준 3개 점수 / 합계. 내 점수만 쓰고, "채점 전"이면 점수 칸을 비워 둬. 없는 이미지는 "저장 전"이라고 적어줘. 네가 점수를 매기지 마.
my_ai_rules.md가 있으면 1번 아래에 "광고 이미지: [내가 적을 곳]" 한 줄을 더해줘. image_task.md가 없으면 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 하고, 끝나면 표만 보여줘.'''
PR['p10']='''채팅창과 API의 차이를 내 MVP로 설명하는 한 장을 api.html로 만들어줘. 실제로 호출하지는 마.
- 그림: 사람 → 채팅창 → 모델 / 프로그램 → API → 모델. "Claude Code도 API로 모델을 부르는 프로그램이에요" 한 줄.
- 요청과 응답 예시: Anthropic Messages API로 요청(모델 이름, 최대 길이, 메시지)과 응답(글, 쓴 토큰 수)을 짧은 JSON으로, 같은 요청을 보내는 파이썬 코드 10줄 안(키는 환경 변수에서 읽기). "예시이며 실행하지 않았어요"라고 적어줘.
- 키 관리 세 줄: 키는 비밀번호와 같다 / 코드와 GitHub에 넣지 않는다 / 쓴 토큰만큼 돈이 든다.
- 내 MVP라면: mvp.md(없으면 mvp.html)와 research.csv를 보고 API를 넣을 곳 한 군데(예: 표의 줄마다 분류하기), 하루에 몇 번 부를지 (가정), 하루 비용 어림(부르는 횟수 × 한 번에 쓰는 토큰 어림 × 공식 가격 페이지의 단가. 단가에는 조사일과 링크, 못 찾으면 "못 찾음").
- 폰 폭(390px)에서도 화면이 옆으로 밀리지 않게 하고(코드와 JSON 상자는 상자 안에서만 옆으로 넘기기), 만든 뒤 스크립트 문법 오류(괄호, 따옴표 짝)가 없는지 다시 읽어 확인해줘.
mvp.md와 mvp.html이 모두 없으면 CLAUDE.md의 회사로 해줘. 되묻지 말고 끝까지 하고, 끝나면 "내 MVP라면" 부분만 3줄로 알려줘.'''
PR['p11']='''handoff.md를 읽고 이번 주에 내가 만든 것과 남은 일을 3줄로 말해줘. handoff.md만으로 몰라서 다른 파일을 열어 본 것이 있으면 무엇인지, handoff.md에 무엇을 더하면 좋을지도 한 줄로. handoff.md가 없으면 이 폴더의 파일로 먼저 만들고 이어서 해줘. 되묻지 말고 끝까지 해줘.'''
PR['w2']='''오늘 AI 이해 날에 한 일을 내 포트폴리오에 넣을 한 장으로 정리해서 portfolio_1119.md로 써줘.
- 무엇을 했나: 어떤 일을 세 AI에 시켜 이름 가리고 견줬는지 한 줄과 파일(task.md, eval.md, compare.html, my_ai_rules.md). 오후에 만든 파일이 있으면 그것도.
- 결과: eval.md의 점수표를 그대로. 점수가 비어 있으면 "채점 전". 한 가지 일을 한 번 돌린 결과라는 것도 적어줘.
- 수업에서 배운 방법 3줄(예: 같은 글을 세 AI에 넣기, 이름을 가리고 점수 매기기, 긴 대화는 인계 메모를 남기고 새 대화로 옮기기). 이건 내 결정이 아니야.
- 내가 내린 결정: 점수 기준에 넣은 것, 내가 매긴 점수, "이 일엔 이걸 쓸래요"와 이유, 내 다짐. 내가 적거나 말한 것만 써. "적지 않음", "네가 정해줘", "채점 전"만 있으면 내가 정한 게 아니야.
- 네가 골랐고 내가 그대로 받은 것은 "Claude가 고름"이라고 쓰고, 옆에 [내가 적을 곳: 받아들인 이유]를 남겨줘. 큰 것 5개까지만.
- 면접에서 말할 세 문장: 어떤 일에 어떤 AI를 왜 고르는지, 그걸 어떻게 확인했는지, 지키는 규칙 하나(내 다짐에서만. 수업 프롬프트와 CLAUDE.md의 규칙은 내 결정이 아니야). 내가 내리지 않은 결정을 내가 한 것처럼 쓰지 마. 쓸 결정이 없으면 그 문장은 [내가 적을 곳]으로 남겨줘.
되묻지 말고 끝까지 쓰고, 끝나면 "면접에서 말할 세 문장"과 [내가 적을 곳]이 남은 자리만 보여줘.'''
for _k in list(PR): PR[_k]=expand_mvp_plain(PR[_k])
R={'r1':'되묻지 말고 네가 가정해서 끝까지 만들어줘. 가정한 곳만 (가정)이라고 표시해줘.',
'r2':'너무 길어. 3줄로만 다시 말해줘.',
'r3':'없는 자료는 없는 대로 두고, 지금 있는 것으로 끝까지 만들어줘.',
'r6':'방금 만든 파일의 내용을 그대로 보여줘. HTML이면 코드 말고 화면에 무엇이 어떤 순서로 있는지 알려줘.'}
OPEN='compare.html을 브라우저로 열어줘.'
PICK='이 일엔 ○○를 쓸래. 이유는 ○○. compare.html과 eval.md에 적어줘.'
CODE='blind 폴더의 답에 든 파이썬 코드를 A.py, B.py, C.py로 저장하고 research.csv로 돌려 줘. 코드는 고치지 마. 답마다 돌아가는지, 출력이 답에 적힌 결과 표와 같은지를 표로 알려줘.'
CRITSHOW='task.md의 점수 기준 4개만 다시 보여줘.'
PICK1='기준은 그대로 갈게. 이유는 ○○. task.md 맨 아래에 적어줘.'
FIX='my_ai_rules.md 4번 표(내놓기 전에 볼 것)의 1번을 고쳐줘. 고치기 전 파일은 파일이름_backup_지금시각으로 남겨줘(확장자는 원래 파일과 같게). my_ai_rules.md가 없으면 이 폴더의 pitch.html, mvp.html, landing.html에서 남의 이미지·로고·글, 실제 회사 이름과 상표, 사람 이름을 점검해 그 표부터 만들고, 점검할 화면도 없으면 "점검할 화면 없음"이라고만 알려줘. 되묻지 말고 끝까지 하고, 끝나면 고친 곳만 3줄로 알려줘.'

body='''
<div class="wrap">
<nav id="nav" aria-label="구간 이동">
<a href="#s0">오늘</a><a href="#s1">준비</a><a href="#s2">1교시</a><a href="#s3">2교시</a><a href="#s4">3교시</a><a href="#s5">4교시</a><a href="#s6">오후</a><a href="#s7">마무리</a><a href="#remote">리모컨</a><a href="#s9">막히면</a>
</nav>

<section id="s0">
<span class="eyebrow">Day 19 / 52 · 11/19(목)</span>
<h1>Day 19 · 같은 일을 세 AI에 시켜 보고 고르는 날</h1>
<p class="lead">오늘부터 Modeling 단원이에요. 3주 동안 써 온 AI가 <b>어떻게 답을 만드는지</b> 알고, 내 일 하나를 <b>Claude, ChatGPT, Gemini</b>에 똑같이 시켜 이름을 가리고 견줘요. 저녁에는 일마다 어떤 AI를 쓸지, 무엇을 조심할지 적은 <b>내 AI 사용 규칙</b> 한 장이 남아요.</p>

<h3 class="gap">오늘 한눈에</h3>
<div class="acts">
<div><b>① AI 알기</b><span>09:05–10:50</span></div>
<div><b>② 견주고 고르기</b><span>10:50–13:00</span></div>
<div><b>③ 넓히고 남기기</b><span>14:00–18:00</span></div>
</div>
<div class="map">
<div class="grp">시작</div>
<div class="row rest"><span class="t">09:00</span><span class="w">오늘 한눈에 보기 (지금 이 화면)</span></div>
<a class="row" href="#s1"><span class="t">09:05</span><span class="w"><b>준비 · 이번 주 폴더 열고 오늘 규칙 더하기</b><small>남는 것: 오늘 규칙이 더해진 CLAUDE.md</small></span></a>
<div class="grp">① AI 알기 · AI가 답을 만드는 방법을 알고, 견줄 과제를 만들어요</div>
<a class="row" href="#s2"><span class="t">09:15</span><span class="w"><b>1교시 · 토큰, AI가 보는 책상, 다음 낱말 맞히기</b><small>남는 것: ai_basics.md</small></span></a>
<a class="row" href="#s3"><span class="t">10:00</span><span class="w"><b>2교시 · 2026년의 AI 고르기, 세 AI에 넣을 과제와 점수 기준표</b><small>남는 것: task.md</small></span></a>
<div class="grp">② 견주고 고르기 · 이름을 가리고 점수를 매긴 뒤, 내 규칙을 정해요</div>
<a class="row" href="#s4"><span class="t">10:50</span><span class="w"><b>3교시 · 조원 과제 돌려 주기, 이름 가리고 점수 매기기, 이름 공개</b><small>남는 것: eval.md, compare.html</small></span></a>
<a class="row" href="#s5"><span class="t">11:50</span><span class="w"><b>4교시 · 긴 대화와 새 대화로 옮기기, 저작권·개인정보·상표, 내 AI 사용 규칙</b><small>남는 것: my_ai_rules.md, handoff.md</small></span></a>
<div class="row rest"><span class="t">13:00</span><span class="w">점심</span></div>
<div class="grp">③ 넓히고 남기기 · 각자 하나 이상 골라 더 깊게 해요</div>
<a class="row" href="#s6"><span class="t">14:00</span><span class="w"><b>오후 메뉴 · 두 번 돌리기, 조 점수, 이미지 AI, API 한 장, 새 대화로 옮겨 보기, 내놓기 전 고치기</b><small>남는 것: 고른 메뉴의 파일</small></span></a>
<a class="row" href="#s7"><span class="t">17:20</span><span class="w"><b>마무리 · 포트폴리오 한 장</b><small>남는 것: portfolio_1119.md</small></span></a>
</div>
<p class="sub">줄을 누르면 그 구간으로 가요. <b>꼭 하는 것</b>은 P0 → P1 → P2 → 조원 과제 돌려 주기 → P3 → P4 → 내 결정 3 → P5, 오후 메뉴 하나, W2예요.</p>

<div class="card soft"><h3>이번 주 파일이 없어도 괜찮아요</h3><p>오늘 견줄 일은 이번 주에 만든 파일(pitch.md, mvp.md, mvp.html, research.csv)을 재료로 써요. 파일이 없으면 P2가 CLAUDE.md의 회사로 자료 몇 줄을 (가정)으로 만들어 넣어요. 이번 주와 <b>같은 작업 폴더</b>를 열고 시작해요.</p></div>

<h3 class="gap">오늘 수업, 이렇게 보면 돼요</h3>
<details><summary>3주 동안 쓴 AI를 한 번 정리하는 날이에요</summary><div class="body">
<p>공식 일정표에서 오늘 단원의 부제는 "3주 사용 경험의 체계화"예요. 매일 Claude Code에 프롬프트를 보내며 겪은 일(대화가 길어지면 앞 내용을 놓치기, 같은 질문에 다른 답, 그럴듯하지만 틀린 말)이 왜 일어나는지 알면, 내일 배우는 CLAUDE.md와 스킬을 더 잘 만들 수 있어요.</p></div></details>
<details><summary>회사에 가면 쓰는 AI를 내가 고르지 못할 수도 있어요</summary><div class="body">
<p>회사마다 쓰는 AI가 다를 수 있어요. 그래서 신입에게는 "이 일엔 이 AI가 낫고, 근거는 이 점수표예요"라고 말하는 힘이 필요해요. 공식 일정표의 "작업별로 고르기"가 이것이에요. 오늘 세 AI를 견주는 이유예요.</p></div></details>
<details><summary>초안은 Claude가 만들고, 결정은 내가 해요</summary><div class="body">
<p>오늘 내가 내리는 결정은 네 가지예요. 가이드에서 <b>"내 결정"</b>이라고 적힌 곳이에요.</p>
<ul><li>점수 기준에 <b>무엇을 넣을지</b> 정하기</li><li>세 답에 <b>내가 점수</b> 매기기</li><li>이 일엔 <b>어떤 AI를 쓸지</b> 정하기</li><li>내 AI 사용 규칙에 <b>내 다짐</b> 한 줄 적기</li></ul>
<p>점수는 Claude Code가 매기지 않아요. Claude가 만든 답을 Claude가 채점하면 공정하지 않으니까요.</p></div></details>

<h3 class="gap">용어</h3>
<details><summary>오늘 처음 나오는 말</summary><div class="body">
<ul><li><b>LLM<span class="ab">(Large Language Model)</span></b> · 글을 엄청나게 많이 읽고 다음에 올 말을 맞히도록 배운 AI예요. Claude, ChatGPT, Gemini가 모두 LLM이에요. 우리말로 대규모 언어 모델이에요.</li><li><b>AI 모델</b> · 같은 회사 안에서도 크고 똑똑한 것, 작고 빠른 것처럼 여러 개가 있어요. 그 하나하나가 모델이에요.</li><li><b>토큰</b> · AI가 글을 읽고 쓰는 조각이에요. 낱말 하나가 한 조각일 때도, 여러 조각일 때도 있어요.</li><li><b>AI가 보는 책상</b> · AI가 지금 답을 만들 때 보는 모든 것(프롬프트, 앞 대화, 읽은 파일)이에요. 현업에서는 '컨텍스트'라고 불러요.</li><li><b>다음 낱말 맞히기</b> · AI가 앞 글을 보고 다음에 올 조각을 하나씩 고르며 쓰는 방식이에요. 현업에서는 '확률적 생성'이라고 불러요.</li><li><b>추론 모델</b> · 답하기 전에 속으로 풀이를 길게 써 보는 모델이에요.</li><li><b>이름 가리고 견주기</b> · 어느 AI의 답인지 모르게 가리고 점수를 매기는 것이에요. 현업에서는 '블라인드 비교'라고 불러요.</li><li><b>점수 기준표</b> · 무엇을 몇 점으로 볼지 미리 적은 표예요. 공식 이름은 '평가 기준표'예요.</li><li><b>앞 내용이 흐려져요</b> · 대화가 길어지면 AI가 앞에서 정한 것을 놓치는 일이에요. 현업에서는 '컨텍스트 열화'라고 불러요.</li><li><b>새 대화로 옮기기</b> · 인계 메모를 남기고 새 대화에서 이어 가는 것이에요. 현업에서는 '세션 관리'라고 불러요.</li><li><b>인계 메모</b> · 새 대화가 읽고 이어 갈 수 있게 지금까지를 한 장에 적은 것이에요. 오늘은 handoff.md예요.</li><li><b>내 AI 사용 규칙</b> · 일마다 어떤 AI를 쓰고 무엇을 조심할지 적은 나만의 한 장이에요. 공식 이름은 '개인 AI 사용 가이드라인'이에요.</li><li><b>API<span class="ab">(Application Programming Interface)</span></b> · 사람이 아니라 프로그램이 AI를 부르는 문이에요. 오후 D에서 다뤄요.</li><li><b>할루시네이션</b> · AI가 그럴듯하지만 틀린 말을 하는 것이에요.</li><li><b>에이전트</b> · 답만 하지 않고 파일을 읽고 쓰고 검색하며 일을 하는 AI예요. 이번 주에 쓴 Claude Code예요.</li><li><b>GPT 에듀 계정</b> · 수업에서 받은 ChatGPT 계정이에요.</li><li><b>W2</b> · 하루를 포트폴리오 한 장으로 남기는 저녁 프롬프트예요(이번 주 매일 쓴 것).</li></ul></div></details>
</section>

<section id="s1">
<span class="eyebrow">시작 · 09:05–09:15 · 준비</span>
<h2>이번 주 폴더를 열고 오늘 규칙을 더해요</h2>
<p class="why"><b>왜 해요?</b> 오늘 견줄 과제는 이번 주에 만든 파일로 만들어요. 같은 폴더에서 시작해야 Claude가 그 파일을 읽어요.</p>
<div class="card checks">
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="a1"><span>Claude Code에서 <b>이번 주와 같은 작업 폴더</b>를 열고 새 대화를 시작했어요. P0이 "있던 파일"에 이번 주 파일을 하나도 말하지 않으면 다른 폴더를 연 거예요. 폴더를 다시 골라 새 대화에서 P0부터 보내요</span></label>
<label class="check"><input type="checkbox" data-k="a2"><span>오늘 쓸 세 곳에 로그인했어요: <b>claude.ai</b>, <b>ChatGPT</b>(GPT 에듀 계정), <b>Gemini</b>(gemini.google.com, 구글 계정)</span></label>
<label class="check"><input type="checkbox" data-k="a3"><span><b>P0</b>을 실행했어요</span></label>
</div>
<div class="card" id="profileCard">
<h3>나와 회사</h3>
<p class="sub">이번 주에 P0을 보낸 폴더라면 비워 둬도 돼요. Claude가 CLAUDE.md에 적힌 것을 그대로 써요. 칸에 적은 것만 새 값으로 바뀌어요. P0의 답 둘째 줄에서 하고 싶은 일과 회사가 맞는지 봐요. <b>"아직 모름"으로 나오면 첫 칸에 직무를 적고 P0을 한 번 더 보내요.</b> 오늘 견줄 일이 직무로 정해져요.</p>
<div class="field"><label for="v-role">내가 하고 싶은 일</label><input id="v-role" data-in="role" type="text" maxlength="40" placeholder="비워 두면: 아직 모름 (CLAUDE.md에 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-brand">회사(브랜드) 이름</label><input id="v-brand" data-in="brand" type="text" maxlength="40" placeholder="비워 두면: 라라스윗" autocomplete="off"></div>
<div class="field"><label for="v-product">제품·서비스 한 줄</label><input id="v-product" data-in="product" type="text" maxlength="60" placeholder="비워 두면: 저당 아이스크림" autocomplete="off"></div>
<div class="field"><label for="v-customer">그 회사의 고객 한 줄</label><input id="v-customer" data-in="customer" type="text" maxlength="90" placeholder="비워 두면: 다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인" autocomplete="off"></div>
<button class="ghost" id="resetProfile" type="button">처음 값으로 되돌리기</button>
</div>
'''+box('p00','P0 · 이번 주 폴더 확인하고 오늘 규칙 더하기 (꼭)',PR['p00'])+'''
<div class="card soft"><p><b>늦게 왔다면</b> P0 → P2를 먼저 보내 과제 글을 단톡방에 올리고, P1은 나중에 해요. 조원이 내 과제를 기다려요.</p></div>
<div class="card warn"><h3>허락 창이 뜨면</h3>
<p><b>방금 보낸 프롬프트가 시킨 일이면 Yes</b>를 눌러요. 오늘 자주 뜨는 것: 파일 만들기와 고치기, P1의 글자 세기(wc), 폴더 만들기(mkdir), 브라우저와 폴더 열기(open, start, explorer), 3교시 테크 트랙 상자의 코드 돌리기(python). 파일이나 폴더를 통째로 지우겠다고 하면(rm, delete) 누르지 말고 강사님을 불러요.</p></div>
<h3 class="gap" id="remote">리모컨 네 개 · 필요할 때만 꺼내 써요</h3>
<p class="sub"><b>지금 보내는 상자가 아니에요.</b> Claude가 마음에 안 들게 움직이면 긴 설명 대신 이 짧은 상자를 보내요.</p>
'''+box('r1','되물을 때',R['r1'])+'\n'+box('r2','말이 길 때',R['r2'])+'\n'+box('r3','자료가 없다고 멈췄을 때',R['r3'])+'\n'+box('r6','파일 내용 보기',R['r6'])+'''
</section>

<section id="s2">
<span class="eyebrow">① AI 알기 · 09:15–10:00 · 1교시</span>
<h2>AI는 다음 낱말을 맞히며 답을 만들어요</h2>
<p class="why"><b>왜 해요?</b> 같은 질문에 답이 달라지고, 대화가 길어지면 앞 내용을 놓치는 이유를 알면 AI를 덜 믿고 더 잘 쓰게 돼요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>세 가지만 알면 돼요</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">토큰</span><span class="w"><b>AI는 글을 레고 조각처럼 잘라 읽고 써요</b><small>그 조각이 토큰이에요. 같은 글도 모델마다 자르는 법이 달라 조각 수가 달라요. 사용량과 한도도 주고받은 조각의 양으로 늘어요. 긴 파일을 통째로 넣으면 조각을 많이 써요.</small></span></div>
<div class="row"><span class="k">AI가 보는 책상</span><span class="w"><b>AI는 책상 위에 올라온 것만 보고 답해요</b><small>책상에는 프롬프트, 앞 대화, 읽은 파일이 올라와요. 답할 때마다 책상 전체를 다시 읽어요. 책상 크기는 정해져 있어요. 책상에 없는 것(어제 다른 대화에서 한 말)은 몰라요. CLAUDE.md와 채팅 서비스의 기억 기능은 책상에 자동으로 올려 주는 것이에요. 현업에서는 '컨텍스트'라고 불러요.</small></span></div>
<div class="row"><span class="k">다음 낱말 맞히기</span><span class="w"><b>휴대폰 자판의 다음 낱말 추천을 아주 크게 키운 것이에요</b><small>앞 글을 보고 그럴듯한 다음 조각을 하나씩 골라 이어 써요. 매번 후보 가운데서 고르니 같은 질문에도 답이 달라져요. 현업에서는 '확률적 생성'이라고 불러요.</small></span></div>
</div></div>
<div class="grid">
<div class="card ok"><h3>그래서 잘하는 것</h3><ul><li>그럴듯한 글을 빨리 쓰기</li><li>주어진 자료를 묶고 바꾸기</li><li>여러 안을 한 번에 내기</li></ul></div>
<div class="card red"><h3>그래서 조심할 것</h3><ul><li>사실을 꺼내 오는 검색창이 아니에요. 그럴듯하지만 틀린 말(할루시네이션)이 나와요</li><li>책상에 없는 것은 몰라요</li><li>한 번 돌린 답으로 판단하면 운이 섞여요</li></ul></div>
</div>
<div class="card soft"><h3>추론 모델과 에이전트</h3><p><b>추론 모델</b>은 연습장에 풀이를 먼저 쓰고 답을 내는 학생과 같아요. 느리고 조각을 더 쓰지만 복잡한 일에 강해요. <b>에이전트</b>는 답만 하지 않고 파일을 읽고, 쓰고, 검색하는 AI예요. 이번 주에 쓴 Claude Code가 에이전트예요. Day 16의 그림 "폴더에 사는 신입 사원"이 이것이에요.</p></div>
<span class="pill">따라 하기</span>
'''+box('p01','P1 · 내 파일로 보는 토큰과 다음 낱말 (꼭)',PR['p01'],TOP)+'''
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="b1"><span>내 폴더에서 가장 큰 파일이 무엇인지 봤어요</span></label>
<label class="check"><input type="checkbox" data-k="b2"><span>다음 낱말 후보 5개를 보고, 왜 같은 질문에 답이 달라지는지 한 문장으로 말할 수 있어요</span></label>
</div>
<details><summary>먼저 끝났다면 · 직접 확인해 보기</summary><div class="body"><p>claude.ai에서 <b>새 채팅을 두 개</b> 열고, 두 곳에 똑같이 "우리 회사 광고 첫 문장 하나만 써줘. 회사: (내 회사)"를 보내 봐요. 두 답이 같은지 달라지는지 봐요. 3교시에 쓸 감각이에요.</p></div></details>
</section>

<section id="s3">
<span class="eyebrow">① AI 알기 · 10:00–10:50 · 2교시</span>
<h2>세 AI에 똑같이 넣을 과제와 점수 기준표를 만들어요</h2>
<p class="why"><b>왜 해요?</b> 같은 과제를 같은 조건으로 넣어야 견줄 수 있어요. 점수 기준을 먼저 정해야 마음에 드는 답에 기준을 맞추지 않아요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>2026년의 AI는 여러 곳에 있어요</h3>
<p>오늘 견주는 세 곳은 <b>Claude</b>(Anthropic), <b>ChatGPT</b>(OpenAI), <b>Gemini</b>(Google)예요. 회사마다 크고 똑똑한 모델과 작고 빠른 모델이 있고, 무료로 쓸 수 있는 범위는 자주 바뀌어요. 그래서 "어느 AI가 최고"보다 <b>"이 일엔 이 AI"</b>를 내 일로 직접 확인해 두는 편이 오래가요. 공식 일정표의 말로 "작업별로 고르기"예요.</p></div>
<div class="card"><h3>이름 가리고 견주기는 이렇게 해요</h3>
<p><b>비유:</b> 콜라 블라인드 테스트와 같아요. 상표를 가리면 "Claude가 좋다더라" 같은 선입견 없이 맛(결과)으로만 골라요. 현업에서는 '블라인드 비교'라고 불러요.</p>
<ol class="steps"><li><b>같은 글</b>을 세 곳에 넣어요. 한 글자도 바꾸지 않아요.</li><li>세 곳 모두 <b>새 채팅</b>에서, <b>한 번만</b> 보내요. 이어 묻지 않아요.</li><li>Claude도 Claude Code가 아니라 <b>claude.ai 새 채팅</b>에 넣어요. 세 곳 모두 내 폴더를 못 보는 같은 조건이에요. 그래서 과제 글 안에 필요한 자료를 넣어요.</li><li><b>돌리는 사람(조원)과 점수 매기는 사람(나)이 달라요.</b> 조원이 A·B·C로 이름을 가려서 돌려줘요.</li></ol></div>
<div class="card soft"><h3>직무마다 견줄 일 (칸을 비우면 이렇게 정해요)</h3><ul><li><b>콘텐츠·브랜드 마케터</b> · 상세페이지 첫 화면 카피 3안 (공식 일정표의 크리에이티브 트랙 "기획·카피 과제")</li><li><b>MD·온라인 영업</b> · 경쟁사 가격·프로모션을 보고 우리 대응 프로모션 3안</li><li><b>CX(Customer Experience) 기획·서비스 기획</b> · 자주 오는 고객 문의 하나에 보낼 답변 3안</li><li><b>운영 매니저·인사</b> · 자주 보내는 안내문 하나의 3안 (예: 교육 회사의 조퇴·외출 안내)</li><li><b>데이터 분석가·개발자(테크 트랙)</b> · 조사 표를 요약하는 표와 그 표를 만드는 파이썬 코드 (공식 일정표의 데이터·서비스 트랙 "데이터 분석·코드 과제")</li><li><b>아직 모름</b> · 상세페이지 첫 화면 카피 3안</li></ul><p class="sub">다른 일로 견주고 싶으면 아래 첫 칸에 적어요. 예: 인스타그램 광고 문구 5개, 경쟁사 상세페이지 요약. <b>테크 트랙</b>은 CLAUDE.md의 하고 싶은 일이 데이터·개발이 아니면 첫 칸에 "research.csv를 요약하는 파이썬 코드"라고 적어요.</p></div>
'''+field('kind','견줄 일. 예: 상세페이지 첫 화면 카피 3안','비워 두면: 네가 정해줘 (위 목록대로)')+'''
'''+field('crit','점수 기준에 꼭 넣고 싶은 것. 예: 2534 직장인 말투인가 / 마진 하한을 지켰나 / 고객이 다시 묻지 않아도 되나 / 코드가 그대로 돌아가나','비워 두면: 네가 정해줘')+'''
'''+box('p02','P2 · 세 AI에 넣을 과제와 점수 기준표 (꼭)',PR['p02'],TOP)+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="c1"><span>Claude가 보여 준 <b>붙여 넣을 글</b>을 읽어 봤어요. 자료가 글 안에 들어 있어요</span></label>
<label class="check"><input type="checkbox" data-k="c2"><span><b>내 결정 1</b> · 점수 기준 4개를 보고 고칠 것을 말했어요. 그대로면 아래 상자의 ○○를 고쳐 보내요. task.md에 남아 저녁 포트폴리오에 들어가요</span></label>
<label class="check"><input type="checkbox" data-k="c3"><span><b>10:45까지</b> "--- 여기부터 복사 ---"와 "--- 여기까지 ---" 사이만 복사해 <b>조 단톡방</b>에 올렸어요. 점수 기준은 올리지 않아요</span></label>
</div>
'''+box('pick1','내 결정 1 · 기준 그대로 가기 (○○를 고쳐서 보내요)',PICK1)+'''
</section>

<section id="s4">
<span class="eyebrow">② 견주고 고르기 · 10:50–11:50 · 3교시</span>
<h2>조원 과제를 세 AI에 돌려 주고, 내 답에 점수를 매겨요</h2>
<p class="why"><b>왜 해요?</b> 내가 돌리면 어느 답이 어느 AI인지 알아 버려요. 조원이 돌리고 가려 줘야 진짜 이름 가리고 견주기가 돼요.</p>
<div class="card"><h3>10:50 · 누구 과제를 돌리나</h3>
<ul><li><b>번호</b>는 조 안에서 이름 가나다순으로 1번, 2번, 3번이에요.</li><li><b>세 명 조</b> · 1번이 2번 과제를, 2번이 3번 과제를, 3번이 1번 과제를 돌려요.</li><li><b>두 명 조</b> · 서로 바꿔서 돌려요.</li><li><b>조원이 오늘 없으면</b> · 세 명 조는 남은 둘이 서로 바꿔요. 두 명 조에 혼자 남았으면 옆의 두 명 조와 합쳐 세 명 조처럼 돌려요. 그래도 안 맞으면 강사님께 말해요.</li><li><b>열쇠</b>는 <b>내 과제를 돌린 사람</b>에게 받아요.</li></ul></div>
<div class="card"><h3>10:55 · 조원 과제 돌려 주기 (한 사람 15분쯤)</h3>
<ol class="steps"><li>조 단톡방에서 조원의 <b>붙여 넣을 글</b>을 복사해요.</li><li><b>claude.ai</b>, <b>ChatGPT</b>, <b>Gemini</b>에서 각각 <b>새 채팅</b>을 열고 똑같이 붙여 한 번만 보내요. 모델은 처음 뜨는 것 그대로 써요. 대화 기억 기능이 있으면 예전 대화가 섞일 수 있어서, <b>임시 채팅</b>이 보이면 그걸 써요. AI가 답하지 않고 되물으면 그 되물음을 그대로 답으로 보내요.</li><li>메모장을 열고 세 답을 답 화면의 <b>복사 버튼</b>으로 하나씩 옮겨요. 돌린 순서와 다르게 A·B·C를 붙이고, 첫인사·끝인사와 AI 이름이 나오는 줄("저는 Claude예요")은 지워요.</li><li>휴대폰 메모에 <b>열쇠</b>를 적어요(예: A=ChatGPT 기본, B=Gemini 기본, C=Claude 기본). 이 예와 다르게 섞어요. 공개 전까지 말하지 않아요.</li><li>메모장 글을 통째로 복사해 조 단톡방에 <b>한 메시지로</b> 보내요. 첫 줄은 "○○ 과제 · 답 A"처럼 누구 과제인지 적어요.</li></ol>
<p class="sub">말투나 꾸밈새로 어느 AI인지 짐작될 수도 있어요. 짐작됐으면 점수를 매길 때 "짐작됨"이라고 말해 두면 돼요. 완전히 가려지지 않아도 이름을 보고 매기는 것보다 공정해요.</p></div>
<div class="card"><h3>11:10 · 내 답에 점수 매기기</h3>
<ol class="steps"><li>조원이 보낸 메시지를 읽고, task.md의 기준 4개로 A·B·C에 1~5점을 매겨요. 기준이 안 보이면 아래 "기준 다시 보기" 상자를 보내요.</li><li>아래 칸에 점수를 적어요. 예: A 4 3 5 2 / B 3 4 4 4 / C 5 2 3 3</li><li>P3 상자를 눌러 복사해 Claude Code 입력창에 붙이고, <b>보내기 전에</b> 그 아래에 조원이 보낸 메시지 전체를 복사해 붙여요. 그다음 보내요.</li></ol></div>
'''+box('critshow','기준 다시 보기',CRITSHOW)+'''
<div class="card soft"><p><b>테크 트랙</b>은 점수를 매기기 전에 코드를 돌려 볼 수 있어요. 순서: 점수 칸을 비우고 P3 보내기(답이 blind 폴더에 저장돼요) → 아래 "세 답의 코드 돌려 보기" → 점수 적고 P3 한 번 더. 허락 창에 python이 뜨면 Yes를 눌러요. 돌아가는지는 사실 확인이고, 점수는 내가 매겨요.</p></div>
'''+field('score','내 점수 (기준 순서대로). 예: A 4 3 5 2 / B 3 4 4 4 / C 5 2 3 3','비워 두면: 채점 전')+'''
'''+box('p03','P3 · 이름 가리고 점수표 만들기 (꼭) · 아래에 조원 메시지를 붙여서 보내요',PR['p03'],TOP)+'''
'''+box('code','세 답의 코드 돌려 보기 (테크 트랙, 선택)',CODE)+'''
<div class="card soft"><p>점수를 아직 못 매겼으면 칸을 비우고 보내요. Claude가 답마다 셀 수 있는 사실(안의 개수, 표·코드가 있는지, 조건을 지켰는지)만 짚어 줘요. 점수를 정해 칸에 적은 뒤 P3을 <b>한 번 더</b> 보내요. 이번엔 메시지를 다시 붙이지 않아요. 받은 답은 blind 폴더에 그대로 남아요.</p></div>
<div class="card"><h3>11:30 · 이름 공개</h3><p>점수를 다 매겼으면 <b>내 과제를 돌린 사람</b>에게 열쇠를 받아 아래 칸에 적고 P4를 보내요.</p></div>
'''+field('key','답의 주인. 예: A=Claude 기본, B=ChatGPT 기본, C=Gemini 기본','비워 두면: 공개 전')+'''
'''+box('p04','P4 · 이름 붙여 견주는 화면 compare.html (꼭)',PR['p04'],TOP)+'''
'''+box('open','견주는 화면을 브라우저로 열기',OPEN)+'''
'''+box('pick','내 결정 3 · 이 일엔 이걸 쓸래요 (꼭, ○○를 고쳐서 보내요)',PICK)+'''
<div class="card checks">
<h3>이 세 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="d1"><span><b>내 결정 2</b> · 세 답에 내가 점수를 매겼어요</span></label>
<label class="check"><input type="checkbox" data-k="d2"><span>브라우저에서 compare.html을 열어 기준마다 막대(또는 표)를 봤어요</span></label>
<label class="check"><input type="checkbox" data-k="d3"><span><b>내 결정 3</b> · 이 일엔 어떤 AI를 쓸지 정해서 위 상자를 고쳐 보냈어요</span></label>
</div>
<div class="card soft"><p><b>11:45까지 P3·P4를 못 끝냈어도</b> 4교시 강의를 들어요. 남은 것은 오후 첫 30분에 마무리해요.</p></div>
</section>

<section id="s5">
<span class="eyebrow">② 견주고 고르기 · 11:50–13:00 · 4교시</span>
<h2>긴 대화와 권리를 알고, 내 AI 사용 규칙을 써요</h2>
<p class="why"><b>왜 해요?</b> 오늘 본 결과와 조심할 것을 한 장에 적어 두면, 내일 CLAUDE.md와 스킬을 만들 때도, 회사에서 처음 AI를 쓸 때도 꺼내 써요.</p>
<span class="pill">짧은 강의</span>
<div class="card" style="margin-top:12px"><h3>대화가 길어지면 앞 내용이 흐려져요</h3>
<p><b>비유:</b> 책상에 종이가 계속 쌓이면 맨 아래 종이가 잘 안 보여요. 대화가 아주 길어지면 Claude Code는 앞 대화를 요약해 줄이기도 해요. 그때 작은 결정이 빠질 수 있어요. 현업에서는 '컨텍스트 열화'라고 불러요.</p>
<p><b>이런 신호가 보이면</b> 아까 정한 것을 다시 묻거나, CLAUDE.md 규칙을 안 지키거나, 답이 눈에 띄게 느려지고 길어져요.</p>
<p><b>그럴 땐 새 대화로 옮기기.</b> 교대 근무의 인수인계처럼 지금까지를 <b>인계 메모</b> 한 장에 남기고, 같은 폴더에서 새 대화를 열어 "handoff.md를 읽고 이어서 해줘"라고 해요. 현업에서는 '세션 관리'라고 불러요.</p></div>
<div class="card"><h3>내놓기 전에 볼 세 가지</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">저작권</span><span class="w"><b>남이 만든 사진·캡처·글을 내 결과물에 그대로 쓰지 않아요</b><small>경쟁사 광고 캡처는 조사 자료로만 써요. AI가 만든 결과물에 누가 권리를 갖는지는 나라마다 기준이 다르고 아직 정리되는 중이에요.</small></span></div>
<div class="row"><span class="k">상표</span><span class="w"><b>실제 회사 이름과 로고로 그 회사가 만든 것처럼 보이게 하지 않아요</b><small>이번 주 발표 화면 맨 아래에 "학습용 MVP이며 실제 회사와 관계없습니다"를 넣은 이유예요. 이미지 AI에 실제 로고나 캐릭터를 그려 달라고 하지 않아요.</small></span></div>
<div class="row"><span class="k">개인정보</span><span class="w"><b>사람을 알아볼 수 있는 정보는 AI에 넣지 않아요</b><small>실명, 연락처, 테스트해 준 사람의 이름, 면담 내용이에요. 회사에 가면 회사 안의 숫자와 문서도 회사 규칙을 먼저 봐요.</small></span></div>
</div>
<p class="sub">수업의 점검 목록이에요. 실제 판단은 회사의 법무 담당이 해요.</p></div>
<span class="pill">따라 하기</span>
'''+field('rule','내 다짐 한 줄. 예: 숫자가 들어간 답은 출처 링크를 한 번 열어 본다','비워 두면: 적지 않음')+'''
'''+box('p05','P5 · 내 AI 사용 규칙 my_ai_rules.md (꼭)',PR['p05'],TOP)+'''
<div class="card checks">
<h3>이 두 가지가 되면 성공</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="e1"><span>4번 표(내놓기 전에 볼 것)에서 내 발표 화면이나 MVP 화면의 고칠 곳 후보를 봤어요. 고치려면 오후 메뉴 6에서 해요. 점검할 화면이 없으면 건너뛰어요</span></label>
<label class="check"><input type="checkbox" data-k="e2"><span><b>내 결정 4</b> · 내 다짐 한 줄을 칸에 적었거나, [내가 적을 곳]을 Claude에게 말해 채웠어요</span></label>
</div>
</section>

<section id="s6">
<span class="eyebrow">③ 넓히고 남기기 · 14:00–17:20 · 오후</span>
<h2>오후 메뉴에서 하나 이상 골라요</h2>
<p class="why"><b>왜 해요?</b> 오전의 결과는 한 가지 일을 한 번 돌린 것이에요. 오후에 한 번 더 돌리거나, 조원 결과와 모으거나, 다른 종류의 AI로 넓히면 내 규칙이 단단해져요.</p>
<div class="card soft"><p><b>14:00–14:30 · 오전에 못 끝낸 것부터.</b> P3·P4·내 결정 3·P5가 남았으면 먼저 끝내요. 다 끝냈으면 바로 메뉴로 가요.</p></div>
<p class="sub"><b>테크 트랙은 메뉴 4를 꼭 해요</b>(공식 일정표의 데이터·서비스 트랙 "API로 모델 호출하는 구조 이해"). 콘텐츠·브랜드 마케터는 메뉴 3을 권해요(크리에이티브 트랙 "이미지·영상 모델 지형"). MD와 그 밖의 직무는 메뉴 1을 권해요. 고르기 어려우면 <b>메뉴 1 → 5 → 6</b> 순서로 혼자 해요. 메뉴 1은 P4 뒤, 메뉴 5·6은 P5 뒤, 메뉴 2는 조원이 P4를 끝낸 뒤에 할 수 있어요.</p>

<div class="card path"><span class="pill">메뉴 1 · 같은 AI에 두 번</span><h3>한 번 돌린 결과로 골라도 될까요?</h3><p>오늘 가장 높았던 AI에 task.md의 붙여 넣을 글을 <b>새 채팅 두 개</b>에서 한 번씩 보내고, 두 답을 메모장에 모아요. 메뉴 1 상자를 붙이고 그 아래에 "첫째 답", "둘째 답"을 붙여 보내요. <b>끝나면 보이는 것:</b> again.md의 같은 것·달라진 것 표 · 25분</p>'''+box('p06','메뉴 1 · 같은 AI에 두 번 돌려 보기 · 아래에 두 답을 붙여서 보내요',PR['p06'])+'''</div>

<div class="card path"><span class="pill">메뉴 2 · 조 점수 모으기</span><h3>조원들은 어떤 일에 어떤 AI가 높았을까요?</h3><p>조원마다 compare.html의 결과를 한 줄로 조 단톡방에 올려요. 예: "콘텐츠 마케터 · 카피 3안 · 1등 Claude 17점, 2등 Gemini 15점, 3등 ChatGPT 12점". 모은 줄을 칸에 붙여 보내요. <b>끝나면 보이는 것:</b> team_eval.md · 20분</p>
'''+fieldwide('team','조원 결과 (한 사람 한 줄). 내 줄은 빼도 돼요','비워 두면: 적지 않음')+'\n'+box('p07','메뉴 2 · 조 점수표 team_eval.md',PR['p07'])+'''</div>

<div class="card path"><span class="pill">메뉴 3 · 이미지 AI 견주기</span><h3>광고 배경 이미지는 어느 AI가 나을까요?</h3><p>Claude는 이미지를 만들지 않아서 ChatGPT와 Gemini 두 곳을 견줘요. 실제 회사의 제품은 AI가 똑같이 그리지 못하니, 제품 자리를 비운 배경·분위기 이미지를 만들고 나중에 실제 제품 사진을 얹는다고 봐요. 영상 AI는 Day 17에 쓴 Google Flow와 Kling이 있어요. 무료로 만들 수 있는 양은 자주 바뀌니 그날 화면에서 확인해요. <b>끝나면 보이는 것:</b> image_task.md, 이미지 두 장, image_eval.md · 40분</p>
<ol class="steps"><li>메뉴 3-1 상자를 보내 넣을 글을 받아요. images 폴더가 열려요.</li><li>ChatGPT와 Gemini의 새 채팅에 똑같이 넣고 이미지를 만들어요. 한쪽 계정에서 이미지가 안 되면 되는 곳 하나만 해요.</li><li>이미지를 내려받아 열린 images 폴더에 <b>img_chatgpt.png</b>, <b>img_gemini.png</b>로 저장해요.</li><li>점수를 칸에 적고 메뉴 3-2를 보내요. 이미지는 이름을 알고 매기니, "어느 AI인지"보다 기준을 먼저 봐요.</li></ol>
'''+box('p08','메뉴 3-1 · 이미지 AI에 넣을 과제',PR['p08'])+'''
'''+field('imgscore','이미지 점수 (기준 3개). 예: ChatGPT 4 3 3 / Gemini 3 4 4','비워 두면: 채점 전')+'\n'+box('p09','메뉴 3-2 · 이미지 점수표 image_eval.md',PR['p09'])+'''</div>

<div class="card path"><span class="pill">메뉴 4 · API 한 장 · 테크 트랙은 꼭</span><h3>채팅창은 사람이, API는 프로그램이 쓰는 문이에요</h3><p><b>비유:</b> 채팅은 매장에 가서 직접 주문하는 것이고, API는 배달 앱이 가게 주문 시스템에 자동으로 주문을 넣는 것이에요. 리뷰 1,000줄도 채팅창에 파일로 올려 분류할 수는 있어요. 하지만 매일 같은 방식으로 자동으로 돌리거나 다른 프로그램(대시보드, 자동화 도구)에 잇는 일은 프로그램이 API로 불러야 해요. 실제 호출과 키 발급은 하지 않아요. <b>끝나면 보이는 것:</b> api.html(그림, 요청·응답 예시, 파이썬 코드 예시, 하루 비용 어림) · 30분</p>'''+box('p10','메뉴 4 · API 구조 한 장 api.html',PR['p10'])+'''</div>

<div class="card path"><span class="pill">메뉴 5 · 새 대화로 옮겨 보기</span><h3>인계 메모만으로 새 대화가 이어 갈 수 있을까요?</h3><p>4교시에 만든 handoff.md를 시험해요. <b>같은 작업 폴더에서 새 대화</b>를 열고 메뉴 5 상자를 보내요. 새 대화도 CLAUDE.md는 자동으로 읽어요. 답이 틀린 곳이 있으면 handoff.md를 고쳐요. 끝나면 <b>아침부터 쓰던 대화로 돌아가요</b>(왼쪽 대화 목록에서 열어요). <b>끝나면 보이는 것:</b> 새 대화가 말한 3줄과 handoff.md에 더할 것 · 15분</p>'''+box('p11','메뉴 5 · 새 대화에서 인계 메모 읽기',PR['p11'])+'''</div>

<div class="card path"><span class="pill">메뉴 6 · 내놓기 전 고치기</span><h3>4번 표의 고칠 곳을 고쳐요</h3><p>P5의 4번 표(내놓기 전에 볼 것)에서 고칠 곳을 하나 골라 고쳐요. 1번이 아니면 상자의 "1번"을 고쳐 보내요. 실습시트에 링크로 내놓은 화면이면, 고친 뒤 "이 링크의 아티팩트를 고친 파일로 다시 발행해줘: (실습시트의 링크)"라고 해요. 새 링크가 나오면 실습시트를 고쳐요. <b>끝나면 보이는 것:</b> 고친 화면과 백업 파일 · 15분</p>'''+box('fix','메뉴 6 · 4번 표의 고칠 곳 고치기',FIX)+'''</div>
</section>

<section id="s7">
<span class="eyebrow">③ 넓히고 남기기 · 17:20–18:00 · 마무리</span>
<h2>오늘을 포트폴리오 한 장으로 남겨요</h2>
<p class="why"><b>왜 해요?</b> "AI를 쓸 줄 알아요"보다 "이 일엔 이 AI를, 이렇게 확인해서 골라요"가 면접에서 훨씬 단단해요.</p>
<div class="card soft"><p>W2는 <b>아침부터 쓰던 대화</b>에서 보내고, <b>W2 아래에 오늘 정한 것</b>(점수 기준, 내가 매긴 점수, 이 일엔 이걸 쓸래요, 내 다짐)을 한 줄씩 덧붙여 같이 보내요. 하루 종일 쓴 대화라 앞 내용이 흐려졌을 수 있어서예요. 아침 대화가 너무 느리면 새 대화에서 "handoff.md를 읽고 이어서 해줘"를 먼저 보내고 W2를 보내도 돼요.</p></div>
'''+box('w2','W2 · 오늘을 포트폴리오 한 장으로 (꼭)',PR['w2'])+'''
<div class="card checks">
<h3>내가 할 일 세 가지</h3>
<div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g1"><span><b>portfolio_1119.md</b>의 [내가 적을 곳]을 Claude에게 말해서 채웠어요 (세 문장부터)</span></label>
<label class="check"><input type="checkbox" data-k="g2"><span>실습시트에 <b>회고 4줄</b>을 적었어요: 오늘 견준 일 / 이 일엔 어떤 AI와 그 이유 / 의외였던 것 / 내 다짐</span></label>
<label class="check"><input type="checkbox" data-k="g3"><span>오늘 파일을 <b>하나도 지우지 않았어요</b> (내일 CLAUDE.md와 스킬에 써요)</span></label>
</div>
<div class="card soft"><h3>내일부터</h3><p>내일(11/20)은 공식 일정표의 "프롬프트 → 컨텍스트 엔지니어링" 날이에요. 오늘 쓴 내 AI 사용 규칙과 인계 메모가 CLAUDE.md와 스킬의 재료가 돼요.</p></div>
<div class="card blue"><div class="big">오늘 여러분은 AI를 믿는 사람에서<br>골라 쓰는 사람이 됐어요.</div></div>
</section>

<section id="s9">
<span class="eyebrow">막히면</span>
<h2>긴 설명 대신 한 줄을 보내요</h2>
<details><summary>조원이 아직 답을 안 보냈어요</summary><div class="body"><p>그동안 4교시 강의 카드를 먼저 읽어요. 11:15에도 안 오면 조원에게 어디까지 했는지 물어요. <b>11:20까지 못 받으면</b> 내 과제를 내가 직접 세 곳에 돌리고, 메모장에서 A·B·C를 붙여 P3 아래에 붙여 보내요. 이름을 알고 매긴 것이니 "이름 알고 매김. eval.md에 적어줘."라고 말해 둬요. Claude Code에게 세 AI의 답을 대신 만들게 하지는 않아요.</p></div></details>
<details><summary>조원이 아직 과제 글을 안 올렸어요</summary><div class="body"><p>10:50에도 없으면 조원에게 "P0 다음 P2부터 보내요"라고 알려 줘요. 11:00까지 안 오면 강사님 시연 과제(강사님이 단톡방에 올린 글)를 대신 돌려요.</p></div></details>
<details><summary>P0이 이번 주 파일이 없대요</summary><div class="body"><p>이번 주에 파일을 만들었다면 다른 폴더를 연 거예요. 새 대화를 열 때 이번 주 작업 폴더를 다시 골라 P0부터 보내요. 정말 파일이 없으면 그대로 가요. P2가 (가정) 자료로 과제를 만들어요.</p></div></details>
<details><summary>ChatGPT나 Gemini에 로그인이 안 돼요</summary><div class="body"><p>되는 두 곳으로 먼저 돌려 주고, 조원에게 "답 C는 못 받음"이라고 알려요. P3이 그 파일에 "받지 못함"이라고 적어요. 로그인은 1교시 P1이 도는 동안 손을 들어 강사님께 물어요.</p></div></details>
<details><summary>답 안에 "저는 ChatGPT예요"처럼 이름이 보여요</summary><div class="body"><p>돌리는 사람이 그 줄만 지우고 보내요. 이미 봤다면 그 답은 "이름을 봄"이라고 점수 칸 옆에 적어 둬요.</p></div></details>
<details><summary>붙여 넣을 글이 너무 길어요</summary><div class="body"><p>"task.md의 붙여 넣을 글을 800자 안으로 줄여줘. 자료는 줄 수만 줄이고 빼지 마."라고 해요. 이미 조원이 돌렸다면 그대로 둬요.</p></div></details>
<details><summary>compare.html의 차트가 안 보여요</summary><div class="body"><p>인터넷이 끊기면 차트 도구를 못 불러와서 표로 보여요. 그대로 써도 돼요. 다시 그리려면 "차트가 안 보여. Chart.js를 불러오는지 확인하고 고쳐줘."라고 해요.</p></div></details>
<details><summary>Claude가 점수를 매겨 버렸어요</summary><div class="body"><p>"점수는 내가 매긴 것만 써. 네가 매긴 점수는 지우고 칸을 비워줘."라고 해요.</p></div></details>
<details><summary>Claude가 자꾸 되물어요</summary><div class="body"><p>리모컨 <b>"되물을 때"</b>를 보내요. 그래도 물으면 새 대화를 열고 P0을 다시 실행해요.</p></div></details>
<details><summary>사용량 한도 메시지가 떠요</summary><div class="body"><p>세 AI 돌리기와 점수 매기기는 Claude Code 없이도 할 수 있어요. 점수는 실습시트에 적어 두고, 한도가 풀리면 P3부터 이어서 보내요. 오늘 1교시에 본 것처럼 긴 파일을 통째로 읽히면 조각을 많이 써요.</p></div></details>
<details><summary>새 대화를 열었더니 앞 내용을 몰라요</summary><div class="body"><p>오늘 배운 그대로예요. 프롬프트가 폴더의 파일을 읽게 되어 있어요. 4교시 뒤라면 "handoff.md를 읽고 이어서 해줘"라고 먼저 보내요. 말로 남긴 결정은 W2 아래에 한 줄씩 덧붙여요.</p></div></details>
</section>
</div>

<button class="theme" id="themeBtn" type="button">다크 모드</button>
<div class="toast" id="toast" role="status" aria-live="polite">복사됐어요</div>
'''
body=expand_mvp_html(body)
out=build_page('Day 19 · AI 이해와 일마다 AI 고르기',body,
  {'role':'아직 모름','kind':'네가 정해줘','crit':'네가 정해줘','score':'채점 전','key':'공개 전','rule':'적지 않음','team':'적지 않음','imgscore':'채점 전'},'l19-')
write_page(out,PATH)
