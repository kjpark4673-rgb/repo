# Day 20 가이드 1판: 공식 일정표 11/20 [Modeling ②] "프롬프트 → 컨텍스트 엔지니어링 · CLAUDE.md와 스킬 만들기"
# (프롬프트 기본 구조, 2026 핵심 역량 컨텍스트 엔지니어링, CLAUDE.md와 스킬 설계, 공개 스킬 찾아 설치·수정, 구조화 출력(JSON·표).
#  [크] 브랜드 톤 카피 스킬·콘텐츠 캘린더 스킬, [데] 상품 정보 → JSON 변환 스킬·리뷰 분류 스킬. 도구 Claude Code, GitHub(스킬 저장소). 결과물 팀 CLAUDE.md, 개인 스킬 3종)
# 강사 지시(11/17): Day 19 자료는 수업에서 뺌(보관본), "Day 20 자료 만들기", 방향은 "더 수준높게 고차원으로", 라라스윗 TF와는 잇지 않음.
# 수준 근거: 수강생 상위 약 8명은 CLAUDE.md·.claude/agents 에이전트 팀·스킬 배포까지 함 → "만들기"가 아니라 컨텍스트 아키텍처·스킬 엔지니어링·계약과 강제
# 저장소 안에서 그대로 돈다: python3 classroom/tools/build_day20.py [출력 경로]
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide_common import *
PATH=os.path.join(REPO,'classroom','student-guide','day20.html')
TOP=' style="margin-top:12px"'
CHARTJS='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.5.1/chart.umd.min.js'

B=tok('brand','라라스윗'); P=tok('product','저당 아이스크림'); C=tok('customer','다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인')
ROLE=tok('role','아직 모름'); LEVEL=tok('level','표준'); CTX=tok('ctx','적지 않음'); PUB=tok('pub','네가 정해줘'); SKL=tok('skills','네가 정해줘'); TEAM=tok('team','적지 않음')
GP='기본(general-purpose) 서브에이전트'

PR={}
PR['p00']='''오늘은 11/20 Day 20, 내 AI 직원에게 업무 매뉴얼을 만들어 주는 날(컨텍스트 엔지니어링)이야. 이번 주에 쓰던 이 폴더에서 시작할게. 아래를 순서대로 해줘.
1. 지금 CLAUDE.md를 CLAUDE_v1.md로 복사해 둬. 이미 있으면 그대로 둬. CLAUDE.md가 없으면 아래 2·3번으로 새로 만들어.
2. "수업 작업 규칙"과 "나와 회사"는 그대로 두고, 없으면 만들어줘.
- 수업 작업 규칙: 되묻지 않고 가정해서 끝까지 만든다 / 추측한 곳은 (가정) / 웹에서 찾은 값에는 조사일과 출처 링크, 못 찾은 값은 "못 찾음" / 끝나면 3줄로만 보고하고, 내용을 보여 달라고 하면 그대로 보여 준다 / 한국어로 쉽게
- 나와 회사: 하고 싶은 일 '''+ROLE+''' / 회사 '''+B+''' ('''+P+''') / 고객 '''+C+'''
"나와 회사"가 이미 있으면 이미 적힌 값이 맞아. 위 값이 처음 값("아직 모름", "라라스윗", "저당 아이스크림", "다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인")이 아닌 것만 내가 새로 적은 것이니 그 줄을 바꿔줘.
3. 맨 아래에 "# 오늘 규칙 (11/20 컨텍스트)"를 넣어줘. 같은 제목이 있으면 바꿔 넣어줘.
- 이 폴더 밖의 파일(사용자 폴더의 .claude 안 스킬·설정 포함)은 고치지 않는다. "내 스킬"은 이 폴더의 .claude/skills에 있는 것이다.
- 공개 스킬은 SKILL.md와 딸린 스크립트를 먼저 읽고 점검표를 쓴 뒤에만 설치한다. 설치 전에는 스크립트를 실행하지 않는다.
- 새 스킬은 시험 케이스를 먼저 쓰고 만든다(이미 있는 절차를 옮기기만 하는 스킬은 빼고).
- 숫자에는 [실측](도구가 보여 준 값, 직접 센 값)과 [어림]을 붙인다.
- CLAUDE.md, 스킬, 에이전트, 설정 파일을 고치기 전에는 고치기 전 판을 남긴다. CLAUDE.md는 같은 자리에 CLAUDE_v번호.md로, .claude 안의 파일은 _backup/ 폴더에 이름_v번호로(예: _backup/writer_v1.md, _backup/detail-page_SKILL_v1.md, _backup/settings_v1.json). 이미 있으면 덮지 않고 다음 번호를 쓴다. 보고서와 decisions.md처럼 이어 쓰는 파일은 남기지 않아도 된다.
- 내가 정한 것은 decisions.md에 날짜, 정한 것, 이유, "내가 정함"으로 한 줄씩 더한다.
- 서브에이전트는 따로 말하지 않으면 '''+GP+'''를 쓴다.
- 보고 끝에는 "쉽게 말하면" 한 줄을 붙인다: 방금 한 일이 회사에서 어떤 일과 같은지, 나에게 무엇이 좋아졌는지.
- 하다가 막히거나 실패하면 멈춘 이유를 쉬운 말 한 줄로 알리고, 내가 다음에 보낼 한 줄을 따옴표로 적어 준다.
4. python3 --version을 실행해 이 컴퓨터에 파이썬이 있는지 봐줘. 안 되면 python --version도.
되묻지 말고 끝까지 하고, 끝나면 "CLAUDE.md 줄 수와 '#' 덩어리 수 / .claude 안의 skills·agents 개수, settings.json 유무, 파이썬 버전(없으면 없음) / 나와 회사의 하고 싶은 일과 회사"를 3줄로만 알려줘.'''
PR['p01']='''내 에이전트가 매 턴 싣는 맥락을 감사해서 context_audit.md로 써줘.
- 내가 붙인 /context 출력: '''+CTX+'''. "적지 않음"이 아니면 항목별 토큰을 [실측] 표로.
- 목록: CLAUDE.md(줄 수, 글자 수, "#" 덩어리마다 줄 수), 하위 폴더의 CLAUDE.md, .claude/skills(이름, description 글자 수, 본문 줄 수), .claude/agents(이름, tools, model, 본문 줄 수), .claude/settings.json(권한, 훅). 없는 것은 "없음".
- CLAUDE.md의 규칙을 한 줄씩 다섯 자리로 나눠: 루트에 남김(모든 일에 매번 필요) / 스킬로 옮김(특정 일의 절차·예시) / 하위 폴더 CLAUDE.md나 docs/로(특정 폴더에서만, 가끔 필요한 긴 참고) / 훅·권한으로(꼭 지켜야 하는데 말로는 못 막음) / 지움(낡음·중복·지난 날짜). "# 오늘 규칙 (11/20 컨텍스트)"는 루트에 남김. 서로 부딪히는 규칙 쌍은 따로 표로(CLAUDE.md와 에이전트·스킬 지시문 사이도).
- 맨 아래: 지금 매 턴 싣는 무게 한 줄과 재설계 방향 세 줄.
되묻지 말고 끝까지 하고, 끝나면 다섯 자리별 줄 수와 부딪히는 쌍만 보여줘.'''
PR['p02']='''context_audit.md대로 내 CLAUDE.md를 다시 설계해줘. CLAUDE_v1.md는 건드리지 마.
- 루트 CLAUDE.md: 모든 일에 매번 필요한 것만 60줄 안. 맨 위 "나와 회사", 그다음 작업 규칙, 맨 아래 "# 오늘 규칙 (11/20 컨텍스트)" 하나만. 지난 날짜의 규칙 덩어리는 루트에 남기지 마. "# 오늘 규칙 (11/20 컨텍스트)"는 줄을 빼거나 옮기지 말고 그대로 둬.
- 특정 일의 절차는 .claude/skills/이름/SKILL.md로 옮겨(name, 언제 쓰고 언제 쓰지 않는지 적은 description, 본문). 이미 같은 스킬이 있으면 그 스킬에 합쳐. 특정 폴더에서만 쓰는 규칙은 그 폴더의 CLAUDE.md로. 길지만 가끔 필요한 참고 자료는 docs/로 빼고 루트에는 "필요할 때 docs/파일이름을 읽는다" 한 줄만 둬(@로 불러오면 통째로 실려 무게가 줄지 않아).
- 부딪히는 규칙이 에이전트·스킬 지시문에 있으면 그 파일도 고쳐. 고치기 전 판은 오늘 규칙대로 남겨.
- 훅·권한 후보는 hooks_todo.md에 적기만 해(오후에 만들어).
- 바꾸는 것은 CLAUDE.md, .claude/skills, .claude/agents, 하위 폴더의 CLAUDE.md, docs/, hooks_todo.md, context_audit.md뿐이야. research.csv 같은 자료 파일과 화면 파일은 옮기거나 고치지 마.
- 부딪히던 규칙은 어느 쪽을 골랐는지와 이유, 지운 규칙은 이유와 함께.
- context_audit.md 끝에 v1 → v2 바뀐 곳 표(규칙 / 전 자리 / 새 자리)와 전후 줄 수·글자 수 [실측].
되묻지 말고 끝까지 하고, 끝나면 전후 줄 수와 옮긴 곳별 개수만 보여줘.'''
PR['p03']='''Anthropic 공식 스킬 저장소(github.com/anthropics/skills의 skills 폴더)에서 내 일에 쓸 공개 스킬 2개를 골라 받아서 공급망 점검을 해줘. 설치는 내가 정한 뒤에 해.
- 내가 고른 것: '''+PUB+'''. "네가 정해줘"면 CLAUDE.md의 하고 싶은 일로: 콘텐츠·브랜드·아직 모름 → brand-guidelines, internal-comms / MD·영업·CX·운영 → internal-comms, xlsx / 데이터·개발 → xlsx, pdf.
- 파일은 https://raw.githubusercontent.com/anthropics/skills/main/skills/스킬이름/SKILL.md 와 그 안에서 가리키는 파일·스크립트를 받아 읽어. 받은 것은 아무것도 실행하지 마.
- 받은 파일은 _incoming/스킬이름/에 받은 그대로 두고, 같은 폴더 UPSTREAM.md에 주소·날짜·라이선스를 적어. .claude/skills에는 아직 넣지 마.
- supply_check.md 표(스킬마다): 하는 일 / 부르는 조건(description 요약) / SKILL.md 맨 위의 allowed-tools(있으면 그 스킬을 부른 턴에 허락 없이 쓰는 도구) / 실행하는 스크립트와 명령 / 읽고 쓰는 파일과 네트워크 접근 / 필요한 설치(pip 같은 것) / 라이선스와 다시 내도 되는지 / 받은 주소와 날짜 / 위험 / 네 판단(설치·고쳐서 설치·안 함)과 이유. 다른 회사 전용 내용(예: 그 회사의 색·글꼴)이 든 스킬이라도 구조를 내 회사로 고쳐 쓸 수 있으면 "고쳐서 설치".
열리지 않으면 멈추지 말고 표에 "열리지 않음"이라고 적고 점검할 항목만 남겨. 되묻지 말고 끝까지 하고, 끝나면 스킬마다 네 판단 한 줄과 위험만 보여줘.'''
PR['p04']='''설치한 공개 스킬 하나를 내 회사에 맞게 고치고, 무엇이 효과를 냈는지 재줘.
- 고를 스킬: .claude/skills에서 UPSTREAM.md가 있는 것 가운데 내 일에 더 가까운 것 하나. 하나도 설치하지 않았으면 Anthropic 공식 저장소에서 내 일에 맞는 다른 스킬 하나를 P3처럼 점검해 supply_check.md에 더하고, 위험이 없을 때만 .claude/skills에 넣어 써.
- 원본 SKILL.md는 같은 폴더에 SKILL_upstream.md로 남기고, SKILL.md를 내 회사(CLAUDE.md의 나와 회사)용으로 고쳐: description은 언제 쓰고 언제 쓰지 않는지 분명하게, 본문은 짧게. 우리 회사 기준은 references/company.md로 따로 두고 SKILL.md에는 "필요할 때 references/company.md를 읽는다"고만 적어. 기준은 직무에 맞게: 콘텐츠·브랜드는 색, 말투, 금지어, 고객 / MD·영업·데이터는 비교표 양식, 칸 이름, 단위, 반올림 / CX·운영은 답변 말투, 금지 표현, 처리 기준.
- 시험: 이 스킬로 할 일 3개를 tests/스킬이름/cases.md(과제와 통과 조건)로 먼저 써. 과제에 필요한 자료는 과제 글에 다 넣어 웹을 찾지 않아도 풀리게 하고, 통과 조건은 references/company.md의 우리 회사 기준에서 골라 과제 글에는 적지 마. 그다음 haiku 모델의 '''+GP+''' 셋에게 같은 과제 글을 줘: (가) SKILL_upstream.md만 / (나) SKILL_upstream.md와 references/company.md / (다) 고친 SKILL.md와 references/company.md. 셋 다 Skill 도구는 쓰지 말고 준 파일만 읽게 해. 통과 조건으로 채점해서 표(과제 / 가 / 나 / 다 / 토큰 [실측]). 가 → 나는 회사 기준의 효과, 나 → 다는 구조를 고친 효과야.
- tests/스킬이름/report.md: 시험 표, 두 효과를 한 줄씩, 원본 → 고친 판 바뀐 곳 표. 과제 3개 1회는 참고 신호라 1개 차이는 "비슷함".
되묻지 말고 끝까지 하고, 끝나면 시험 표와 두 효과만 보여줘.'''
PR['p05']='''내 일의 스킬을 시험 케이스부터 만들어줘. 레벨 '''+LEVEL+''': 기본 1개 / 표준 2개 / 심화 2개와 호출 정확도. 스킬은 하나씩 끝내고 다음으로 가.
- 만들 스킬: '''+SKL+'''. "네가 정해줘"면 CLAUDE.md의 하고 싶은 일로: 콘텐츠·브랜드·아직 모름 → 브랜드 톤 카피, 콘텐츠 캘린더 / 데이터·개발 → 상품 정보 → JSON 변환, 리뷰 분류 / MD·영업 → 경쟁사 가격·프로모션 비교표, 상품 정보 → JSON 변환 / CX·서비스 기획 → 고객 문의 분류와 답변, 리뷰 분류 / 운영 → 안내문, 요청 분류.
- 이미 있는 스킬(P2가 옮긴 것, P4의 공개 스킬)과 하는 일이 겹치면 범위를 좁혀 겹치지 않게 하고, description에 그 스킬과 다른 점을 적어.
- 스킬마다 순서는 꼭 이대로:
① tests/스킬이름/cases.json: 시험 케이스 5개. 입력에는 답에 필요한 자료를 모두 넣어(이 폴더의 research.csv 같은 자료에서, 없으면 가상의 자료로 만들고 "가상"이라고 표시) 웹을 찾지 않아도 풀리게. 출력 형식(칸 이름, JSON 모양)은 과제 글에 넣고, 통과 조건은 우리 회사 기준(분류 기준, 계산 규칙, 말투, 금지어)에서 골라 스크립트로 확인할 수 있게. 이 스킬을 불러야 할 말 3개와 부르면 안 되는 말 2개도.
② 기준선: 스킬을 만들기 전에 haiku 모델의 '''+GP+'''에게 케이스 5개의 과제 글만 주고 한꺼번에 풀게 해서 tests/스킬이름/answers_없음.json으로.
③ .claude/skills/스킬이름/SKILL.md: name, 언제 쓰고 언제 쓰지 않는지 분명한 description, 본문 80줄 안. 우리 회사 기준은 references/에, 긴 예시는 examples/, 정해진 계산·검사는 scripts/. 결과가 표나 JSON이면 schema.json과 scripts/validate.py.
④ 같은 과제 글을 SKILL.md와 딸린 파일을 읽은 haiku '''+GP+'''에게 풀게 해서 answers_있음.json으로.
⑤ 채점: scripts/validate.py와 통과 조건으로. 스크립트로 못 보는 조건은 어느 쪽 답인지 모르게 이름을 가려 다른 haiku '''+GP+'''가. 통과 수 [실측]. 5개 1회는 참고 신호라 1개 차이는 "비슷함".
⑥ 레벨이 심화면 호출 정확도(대리 측정): 이 폴더 .claude/skills의 모든 스킬 name과 description만 준 haiku '''+GP+'''에게 불러야 할 말·안 될 말 5개를 한 번에 주고 말마다 어느 스킬을 쓸지(없으면 "없음") 고르게 해 맞은 수. 실제 호출은 메인 모델이 대화 전체를 보고 정하니 대리 측정이라고 적어.
- tests/skills_report.md: 스킬마다 스킬 없음/있음 통과 수, 토큰 [실측], (심화) 호출 정확도, 떨어진 케이스와 고칠 점 한 줄.
되묻지 말고 끝까지 하고, 끝나면 skills_report.md의 표만 보여줘.'''
PR['p06']='''내 일의 흐름에서 한 단계가 다음 단계로 넘기는 결과를 JSON 계약으로 만들어줘.
- 넘기는 쌍 하나(보내는 쪽 → 받는 쪽): .claude/agents에 에이전트가 둘 이상이면 그중 넘기는 둘(예: 조사 → 작성). 없으면 오늘 만든 스킬 가운데 결과를 넘길 수 있는 둘, 그것도 없으면 "조사 표 → 보는 화면". P5에서 만든 schema.json이 있으면 그것을 계약의 바탕으로 써.
- contracts/이름.schema.json: 필수 칸, 타입, 허용 값, 숫자 칸의 단위, 출처 링크와 조사일 칸, 못 찾은 값 표시 방법. contracts/validate.py: 통과/실패와 칸별 이유를 한 줄씩(P5의 scripts/validate.py가 있으면 넓혀 써).
- contracts/samples/에 좋은 예 1개와 나쁜 예 2개(필수 칸 빠짐, 숫자 자리에 글)를 만들어 돌린 결과 표.
- 보내는 쪽 지시문(에이전트 파일이나 SKILL.md)에는 "결과를 contracts/이름.schema.json 모양의 JSON으로 낸다"를, 받는 쪽 지시문에는 "받은 JSON을 contracts/validate.py로 먼저 검사하고, 실패하면 만들지 말고 이유를 보고한다"를 넣어줘. 고치기 전 판은 오늘 규칙대로 남겨.
되묻지 말고 끝까지 하고, 끝나면 샘플 검사 결과 표와 고친 파일 이름만 보여줘.'''
PR['p07']='''hooks_todo.md에서 하나를 골라 훅으로 만들어, 말로 하던 부탁을 강제로 바꿔줘.
- hooks_todo.md가 없거나 비었으면 내 일에 맞는 하나를 골라: (가) .html을 저장하면 스크립트 문법 검사(node가 있을 때만) / (나) .csv를 저장하면 "못 찾음" 비율과 출처 칸이 빈 줄 수 검사 / (다) rm으로 지우는 명령을 막기.
- 먼저 python3(안 되면 python, 가는 node도)가 있는지 확인해. 없으면 등록하지 말고 hook_test.md에 "등록 안 함"과 이유만. 훅 명령에는 이 컴퓨터에서 되는 이름(python3 또는 python)을 써.
- .claude/hooks/이름.py: 입력은 표준 입력으로 오는 JSON. 막아야 하면 종료 코드 2로 끝내고 이유는 표준 오류(stderr)로 써(그래야 Claude에게 전해져). 검사만 하는 훅은 결과를 한 줄로.
- .claude/settings.json에 등록할 때 명령의 경로는 "$CLAUDE_PROJECT_DIR"/.claude/hooks/이름.py처럼 써(폴더를 옮겨 다녀도 파일을 찾게). settings.json이 이미 있으면 고치기 전 판을 오늘 규칙대로 남기고 기존 설정에 더해.
- hook_test.md: 맨 위에 "이 훅이 내 컴퓨터에서 자동으로 돌리는 명령" 한 줄, 걸리는 상황 하나와 안 걸리는 상황 하나를 스크립트에 직접 입력을 넣어 시험한 결과, 등록한 뒤 ls 같은 평범한 명령이 막히지 않는지 확인한 결과, 바로 안 걸리면 새 대화에서 확인한다는 한 줄.
되묻지 말고 끝까지 하고, 끝나면 등록한 훅 한 줄과 시험 결과 세 줄만 보여줘.'''
PR['p08']='''우리 조의 팀 CLAUDE.md 초안을 만들어줘. 조원들이 단톡방에 올린 규칙: '''+TEAM+'''
- team/CLAUDE.md: 맨 위 한 줄 "개인 규칙이 팀 규칙과 부딪히면 팀 규칙을 따르고 개인 쪽을 고친다", 그다음 조가 함께 지킬 규칙 30줄 안(출처·숫자 표기, 파일 이름, 넘기는 JSON 계약, 공개 스킬 점검, 개인정보). 내 CLAUDE.md와 조원 규칙에서 겹치는 것은 하나로.
- team/conflicts.md: 부딪히는 규칙 표(번호 / 규칙 / 누구(나·조원 1·조원 2) / 고른 쪽 / 이유). 정하기 어려운 것은 [조가 정할 곳].
- team/skills/README.md: 조가 함께 쓸 스킬 목록(이름, 하는 일, 만든 사람의 직무, 시험 통과 수), 설치법(.claude/skills로 복사), 버전 적는 법(날짜와 바뀐 곳 한 줄).
- 하위 폴더의 CLAUDE.md는 그 폴더를 다룰 때만 실리니, 내 루트 CLAUDE.md의 "나와 회사" 바로 아래에 "@team/CLAUDE.md" 한 줄을 넣어 팀 규칙이 늘 실리게 하고, 팀 규칙과 겹치는 줄은 내 CLAUDE.md에서 빼. 고치기 전 판은 오늘 규칙대로 남겨.
조원 규칙이 "적지 않음"이면 내 규칙으로 초안만 만들고 조원 칸은 [조원 규칙 붙이기]. 되묻지 말고 끝까지 하고, 끝나면 conflicts.md 표만 보여줘.'''
PR['xa']='''내 에이전트들을 최소 권한과 맞는 모델로 다시 설계해줘. .claude/agents가 없으면 "에이전트 없음"이라고만 하고 끝내.
- 에이전트마다 표: 이름 / 하는 일 / 지금 tools / 꼭 필요한 tools / 지금 model / 제안 model(쉬운 반복은 haiku, 판단은 sonnet, 어려운 종합만 opus) / 이유. 읽기만 하는 검수 에이전트는 쓰기 도구를 빼.
- 고치기 전 판은 오늘 규칙대로 남기고, 에이전트 파일의 tools와 model만 바꿔.
- 가장 자주 쓰는 에이전트 하나에 작은 과제를 시켜 바꾸기 전과 후의 토큰·시간 [실측]과 결과가 같은 일을 했는지를 agents_report.md에.
되묻지 말고 끝까지 하고, 끝나면 표와 전후 [실측]만 보여줘.'''
PR['xb']='''내 스킬 하나의 description을 고쳐 호출 정확도를 올려줘.
- 스킬: 이 폴더의 .claude/skills에서 고른다. tests/skills_report.md에서 호출 정확도가 가장 낮은 것, 없으면 오늘 만든 스킬 가운데 하나. 이 폴더에 스킬이 없으면 "고칠 스킬 없음"이라고만 하고 끝내. 이 폴더 밖의 스킬은 고치지 마.
- 말부터 먼저 써: tests/스킬이름/trigger.json의 "고르기용"에 불러야 할 말 5개와 안 될 말 5개(비슷하지만 다른 일), "확인용"에 처음 보는 말 6개(불러야 할 말 3, 안 될 말 3).
- 그다음 description을 세 판(지금 판, 짧고 분명한 판, "이럴 때 쓰고 이럴 때 쓰지 않는다"를 예로 적은 판)으로 써.
- 판마다 haiku 모델의 '''+GP+'''에게 이 폴더 .claude/skills의 모든 스킬 name과 그 판의 description, 고르기용 말을 주고 말마다 어느 스킬을 쓸지(없으면 "없음") 고르게 해서 맞은 수 [실측]. 같은 판을 두 번씩 돌려 흔들림도.
- 가장 좋은 판과 지금 판만 확인용 말로 한 번 더 재. 확인용에서도 같거나 나으면 그 판으로 SKILL.md를 고쳐(고치기 전 판은 오늘 규칙대로).
- tests/스킬이름/trigger_report.md에 표. 실제 호출은 메인 모델이 대화 전체를 보고 정하니 대리 측정이라고 적어.
되묻지 말고 끝까지 하고, 끝나면 판별 맞은 수 표만 보여줘.'''
PR['xc']='''우리 조 스킬을 GitHub 스킬 저장소로 낼 준비를 해줘. 올리기(push)는 내가 해. 이 폴더 안의 것만 쓰고, 이 폴더의 .claude/skills에 스킬이 없으면 "내보낼 스킬 없음"이라고만 하고 끝내.
- team-skills/ 폴더: README.md(무엇이 들었나, 설치법, 스킬마다 시험 통과 수와 시험 방법, 맨 아래 "학습용이며 실제 회사와 관계없습니다"), 스킬 폴더들(.claude/skills에서 오늘 만든 것과 고친 공개 스킬을 복사. 고친 공개 스킬은 UPSTREAM.md와 원래 라이선스 파일을 그대로 함께), CHANGELOG.md(날짜와 바뀐 곳), .gitignore(개인 파일, 키, CLAUDE_v1.md 같은 것).
- 내보내기 전 점검표 publish_check.md: 실명·연락처·면담 내용·회사 내부 숫자·키가 파일에 있는지 찾아 줄과 함께 / 공개 스킬마다 라이선스가 다시 내는 것을 허락하는지와 표기가 빠졌는지 / 실존 회사의 상표·로고·내부 정보처럼 보이는 것.
- team-skills에서 git 저장소를 시작하고 첫 커밋까지 해(이미 있으면 그대로). 원격 저장소 주소를 붙이고 올리는 명령 두 줄은 실행하지 말고 보여만 줘.
되묻지 말고 끝까지 하고, 끝나면 publish_check.md에서 걸린 것과 올리는 명령 두 줄만 보여줘.'''
PR['xd']='''구조화 출력이 정말 지켜지는지 재고, 검사-재시도 고리로 단단하게 만들어줘. 결과는 tests/structured_report.md.
- 대상: 이 폴더의 .claude/skills에서 오늘 만든 스킬 가운데 결과가 JSON인 것(schema.json이 있는 것). 없으면 상품 정보 → JSON 변환을 tests/json_task/ 안에서 작게 만들어(입력 5개, schema.json, validate.py).
- 1차: haiku 모델의 '''+GP+'''에게 입력 5개를 그 스킬로 바꾸게 해서 validate.py 통과 수 [실측].
- 2차: 실패한 것은 validate.py가 낸 이유를 그대로 붙여 같은 서브에이전트 방식으로 한 번만 다시 시키고 통과 수 [실측]. 몇 번 만에 통과했는지와 늘어난 토큰.
- 맨 아래: 이 스킬의 SKILL.md에 "검사 → 실패 이유를 붙여 한 번 다시 → 그래도 실패면 멈추고 보고" 규칙을 넣고(고치기 전 판은 오늘 규칙대로), 언제 사람이 봐야 하는지 한 줄.
되묻지 말고 끝까지 하고, 끝나면 1차·2차 통과 수와 늘어난 토큰만 보여줘.'''
PR['w2']='''오늘 Day 20을 포트폴리오에 넣을 사례 연구 한 장으로 만들어줘. portfolio_1120.html로.
- 순서: 문제(내 에이전트가 매 턴 무엇을 싣고 있었나, context_audit.md) → 재설계(CLAUDE.md 전후 줄 수와 다섯 자리) → 공개 스킬 공급망 점검과 고친 효과(supply_check.md, tests의 report.md) → 내 스킬과 시험 결과(skills_report.md, 막대 차트 Chart.js '''+CHARTJS+''') → 계약과 강제(contracts, hook_test.md) → 팀 CLAUDE.md와 고른 쪽(team/conflicts.md) → 한계와 다음.
- 맨 위 "한눈에" 세 줄: 무엇을 만들었나 / 숫자로 본 효과 / 회사에서 쓰는 장면(내 직무의 일로). 채용 담당자가 1분 안에 읽게 쉬운 말로 쓰고, 기술 용어에는 괄호로 쉬운 말을 붙여.
- 숫자는 [실측]/[어림] 그대로. 케이스 5개 1회 같은 작은 시험은 "참고 신호"라고 적어.
- "내가 한 것" 상자: 수업에서 배운 방법 3줄(내 결정이 아님) / 내가 내린 결정(decisions.md의 "내가 정함" 줄과 이 대화에서 내가 말한 것만. "네가 정해줘", "적지 않음"만 있으면 내가 정한 게 아님) / Claude가 고르고 내가 받은 것(옆에 [내가 적을 곳: 받아들인 이유], 큰 것 5개까지).
- 면접에서 말할 세 문장: 에이전트의 맥락을 어떻게 설계했는지(숫자로), 스킬을 어떻게 시험하고 고쳤는지, 규칙을 무엇으로 강제했는지. 내가 내리지 않은 결정을 내가 한 것처럼 쓰지 마. 쓸 결정이 없으면 [내가 적을 곳].
- 폰 폭에서 밀리지 않게, 만든 뒤 스크립트 문법 오류가 없는지 다시 읽어 확인해줘.
없는 파일이 있으면 있는 것으로 만들고 빈 곳은 [채울 곳]. 되묻지 말고 끝까지 하고, 끝나면 "면접에서 말할 세 문장"과 [내가 적을 곳]이 남은 자리만 보여줘.'''
for _k in list(PR): PR[_k]=expand_mvp_plain(PR[_k])
R={'r1':'되묻지 말고 네가 가정해서 끝까지 만들어줘. 가정한 곳만 (가정)이라고 표시해줘.',
'r2':'너무 길어. 3줄로만 다시 말해줘.',
'r3':'없는 자료는 없는 대로 두고, 지금 있는 것으로 끝까지 만들어줘.',
'r6':'방금 만든 파일의 내용을 그대로 보여줘. HTML이면 코드 말고 화면에 무엇이 어떤 순서로 있는지 알려줘.'}
CHECK='이 폴더의 규칙 가운데 숫자와 출처, 파일 저장, 나와 회사에 관한 것을 한 줄씩 말해줘. 줄마다 어느 파일에서 읽었는지도.'
PICK1='루트 CLAUDE.md에서 ○○ 규칙은 (다시 넣어줘 / 빼줘). 이유는 ○○. context_audit.md의 바뀐 곳 표에 "내가 고침"으로 적고, decisions.md에도 더해줘.'
PICK2='supply_check.md를 보고 정했어. ○○ 스킬은 (설치해 / 설치하지 마), ○○ 스킬은 (설치해 / 설치하지 마). 이유는 ○○. 설치하는 것만 _incoming에서 .claude/skills로 복사하고, 표의 판단 칸과 decisions.md에 "내가 정함"과 이유를 적어줘.'
PICK3='○○ 케이스가 떨어진 이유는 ○○ 같아. SKILL.md를 이렇게 고치고(고치기 전 판은 오늘 규칙대로) 떨어진 케이스만 다시 시험해줘: ○○. decisions.md에도 더해줘.'
PICK4='conflicts.md의 ○번은 ○○로 정했어. 이유는 ○○. conflicts.md와 team/CLAUDE.md에 반영하고 decisions.md에도 더해줘.'
TEAMSAVE='아래 글이 우리 조의 최종 팀 규칙이야. team/CLAUDE.md를 이 글로 바꾸고(고치기 전 판은 오늘 규칙대로), 내 루트 CLAUDE.md에 "@team/CLAUDE.md" 한 줄이 있는지 확인해줘.\n(여기에 조장이 올린 글을 붙여요)'

EASY1='루트 CLAUDE.md는 네가 정리한 그대로 둘게. 남긴 규칙마다 왜 남겼는지 쉬운 말로 한 줄씩 설명해줘. decisions.md에는 "Claude 판단을 받음"으로 적어줘.'
EASY2='supply_check.md의 네 판단대로 해줘. 설치하는 것만 _incoming에서 .claude/skills로 복사하고, 스킬마다 가장 큰 위험 하나와 왜 괜찮은지 쉬운 말로 한 줄씩 설명해줘. decisions.md에는 "Claude 판단을 받음"으로 적어줘.'
EASY3='tests/skills_report.md에서 떨어진 케이스 하나(없으면 가장 아슬아슬했던 케이스)를 골라 왜 그랬는지 쉬운 말로 설명하고, 고칠 방법 두 가지를 보여줘. 아직 고치지는 마. 내가 고를게.'
EASY4='team/conflicts.md의 줄마다 고를 수 있는 쪽과 장단점을 쉬운 말로 한 줄씩 보여줘. 아직 정하지는 마. 조원과 정할게.'
F={'f1':'방금 하던 일을 이어서 끝까지 해줘. 이미 만든 파일은 그대로 두고 남은 것만 해줘.',
'f2':'방금 내가 거절한 것을 다시 해줘. 이번에는 허락할게.',
'f3':'파이썬 없이 할 수 있는 데까지 해줘. 검사는 네가 통과 조건과 직접 대조하고, 그 결과에는 [어림]을 붙여줘.',
'f4':'.claude/settings.json에서 오늘 더한 훅만 빼줘. 다른 설정은 그대로 둬.',
'f5':'지금 CLAUDE.md는 오늘 규칙대로 남기고, CLAUDE_v1.md의 내용으로 CLAUDE.md를 되돌려줘.',
'f6':'haiku 모델을 쓸 수 없으면 sonnet으로 바꿔서 같은 시험을 해줘. 보고서에 어떤 모델로 했는지 적어줘.',
'f7':'지금까지 한 일과 남은 일을 handoff_1120.md로 정리해줘. 새 대화에서 이어서 할 거야.',
'f8':'이 폴더의 handoff_1120.md와 decisions.md를 읽고, 남은 일부터 이어서 해줘.',
'f9':'방금 답을 쉬운 말로 다시 설명해줘. 회사 일에 견줘서 세 줄로, 그리고 내가 다음에 할 일 한 줄.',
'f10':'지우지 말고 이름 끝에 _old를 붙여줘.',
'f11':'이 글이 그 스킬의 SKILL.md야. _incoming에 저장하고 점검해줘.\n(여기에 붙여요)',
'f12':'방금 고친 파일 목록을 보여줘. 이 폴더 밖의 파일을 고쳤으면 원래대로 되돌려줘.'}

body='''
<div class="wrap">
<nav id="nav" aria-label="구간 이동">
<a href="#s0">왜 해요</a><a href="#map">오늘 순서</a><a href="#s1">준비</a><a href="#s2">규칙 정리</a><a href="#s3">공개 매뉴얼</a><a href="#s4">내 매뉴얼</a><a href="#s5">양식·잠금</a><a href="#s6">조 규칙</a><a href="#s7">선택</a><a href="#s8">마무리</a><a href="#remote">리모컨</a><a href="#s9">막히면</a>
</nav>

<section id="s0">
<span class="eyebrow">Day 20 / 52 · 11/20(금)</span>
<h1>Day 20 · 내 AI 직원에게 업무 매뉴얼을 만들어 주는 날</h1>
<p class="lead">3주 동안 여러분은 AI에게 일을 시킬 때마다 말로 다시 설명했어요. 오늘은 그 설명을 <b>한 번 써 두면 계속 쓰는 업무 매뉴얼</b>로 바꿔요. 파란 상자를 복사해 붙여 넣으면 Claude가 만들고, 여러분은 결과를 보고 네 번만 정하면 돼요. 이 일의 공식 이름이 "컨텍스트 엔지니어링"이에요.</p>

<div class="card"><h3>내 취업에 이렇게 도움이 돼요</h3>
<ul><li>면접에서 "AI 써 봤어요"는 이제 누구나 하는 말이에요. 오늘이 끝나면 <b>"AI에게 맡길 일을 매뉴얼로 만들었고, 매뉴얼이 있을 때와 없을 때를 시험해서 숫자로 확인했어요"</b>라고 말할 수 있어요.</li><li>그 증거가 오늘 저녁에 남아요. 포트폴리오 한 장(portfolio_1120.html)과 면접에서 말할 세 문장이에요.</li><li>공식 일정표는 오늘 주제를 "2026 핵심 역량"이라고 적었어요. 프롬프트 한 줄을 잘 쓰는 것에서, AI가 일할 환경을 갖춰 두는 것으로 무게가 옮겨 갔다는 뜻이에요.</li></ul>
<p class="sub">면접 문장의 모양(숫자는 오늘 내 결과로 채워요): "저는 AI에게 일을 시킬 때 매번 설명하지 않고 업무 매뉴얼(스킬)로 만들어 둡니다. [내 일] 매뉴얼은 시험 5건에서 [ ]건이던 통과가 [ ]건이 됐고, 떨어진 건은 원인을 찾아 고쳤습니다."</p></div>

<div class="card"><h3>회사에 들어가면 이렇게 써요</h3>
<ul><li>신입으로 들어가면 업무 매뉴얼, 보고 양식, 팀 규칙을 받아요. 오늘 만드는 것이 그 AI 판이에요.</li><li>매뉴얼이 있으면 같은 설명을 반복하지 않아요. 누가 시켜도 같은 품질이 나오고, 내가 자리를 비워도 팀원이 그대로 써요.</li><li>자기 일을 남이 그대로 할 수 있게 정리해 두는 것을 회사에서는 인수인계, 표준화라고 불러요. 오늘은 그 상대가 AI예요.</li></ul></div>

<div class="card"><h3>다음 수업(11/23 월) 산업 리포트와 이렇게 이어져요</h3>
<p>월요일에는 한 줄만 시키면 산업 리포트가 나오게 만들어요(공식 일정표 "AI 기반 산업 리포트 자동 생성"). 그때 쓰는 부품을 오늘 만들어요.</p>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">오늘 정리한 규칙</span><span class="w"><b>리포트의 숫자와 출처 기준이 돼요</b><small>CLAUDE.md, 조의 공통 규칙</small></span></div>
<div class="row"><span class="k">오늘 만든 내 매뉴얼</span><span class="w"><b>리포트의 한 꼭지를 만드는 방법이 돼요</b><small>가격 비교표, 카피, 분류 같은 내 스킬</small></span></div>
<div class="row"><span class="k">오늘 정한 양식</span><span class="w"><b>조사한 것을 글 쓰는 단계로 넘기는 모양이 돼요</b><small>넘기는 양식(JSON 계약)</small></span></div>
</div>
<p class="sub">오늘 매뉴얼을 만들어 두지 않으면 월요일에 다시 말로 설명해야 해요.</p></div>

<div class="card"><h3>직무마다 오늘 저녁에 손에 남는 것</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">콘텐츠·브랜드</span><span class="w"><b>브랜드 톤 카피, 콘텐츠 캘린더 매뉴얼</b><small>"이번 주 문구 5개"만 시켜도 우리 브랜드 말투와 금지어를 지킨 문구가 나와요</small></span></div>
<div class="row"><span class="k">MD·영업</span><span class="w"><b>경쟁사 가격·프로모션 비교표 매뉴얼</b><small>아침마다 하던 가격 비교가 늘 같은 칸, 같은 계산으로 나와요</small></span></div>
<div class="row"><span class="k">CX·서비스 기획</span><span class="w"><b>고객 문의 분류와 답변 매뉴얼</b><small>문의가 같은 기준으로 나뉘고, 답변 말투가 사람마다 달라지지 않아요</small></span></div>
<div class="row"><span class="k">운영</span><span class="w"><b>안내문, 요청 분류 매뉴얼</b><small>공지와 요청 처리가 매번 같은 기준으로 나와요</small></span></div>
<div class="row"><span class="k">데이터·개발</span><span class="w"><b>상품 정보를 정해진 모양으로 바꾸는 매뉴얼</b><small>사람이 쓴 글을 프로그램이 읽는 모양으로 바꾸고, 틀리면 스스로 다시 해요</small></span></div>
</div></div>

<div class="card"><h3>오늘의 방식 · 복사, 붙여넣기, 읽기, 정하기</h3>
<ol class="steps"><li><b>복사</b> · 파란 상자를 눌러요</li><li><b>붙여넣기</b> · Claude Code에 붙이고 보내요. 만드는 일은 Claude가 해요</li><li><b>읽기</b> · 끝나면 짧은 보고가 와요. 보고 끝의 "쉽게 말하면" 한 줄만 읽어도 무슨 일이 일어났는지 알 수 있어요</li><li><b>정하기</b> · "내 결정" 상자 네 곳에서만 내 생각을 한 줄 적어요. 모르겠으면 그 아래 "잘 모르겠으면" 상자를 보내요</li></ol>
<p>용어를 외울 필요는 없어요. 막히거나 낯선 메시지가 뜨면 맨 아래 <a href="#s9">"이런 메시지가 뜨면"</a>에서 그 메시지를 찾아 한 줄을 복사해 보내요.</p></div>

<div class="card"><h3>오늘 나오는 말, 회사에서는 이것이에요</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">CLAUDE.md</span><span class="w"><b>사무실 벽에 붙인 팀 규칙</b><small>AI가 일할 때마다 처음부터 끝까지 읽어요. 그래서 짧아야 해요</small></span></div>
<div class="row"><span class="k">스킬</span><span class="w"><b>서랍 속 업무 매뉴얼</b><small>그 일을 할 때만 꺼내 읽어요</small></span></div>
<div class="row"><span class="k">공개 스킬</span><span class="w"><b>다른 회사가 공개한 매뉴얼</b><small>가져다 고쳐 쓰면 빨라요. 들이기 전에 안전한지 봐요</small></span></div>
<div class="row"><span class="k">시험 케이스</span><span class="w"><b>매뉴얼이 정말 도움이 되는지 보는 연습 문제</b><small>매뉴얼 없이 한 답과 보고 한 답을 견줘요</small></span></div>
<div class="row"><span class="k">JSON 계약</span><span class="w"><b>부서 사이에 주고받는 정해진 양식</b><small>칸이 비거나 숫자 칸에 글이 있으면 받는 쪽이 돌려보내요</small></span></div>
<div class="row"><span class="k">훅</span><span class="w"><b>자동 잠금장치</b><small>"지우지 마"라고 부탁하는 대신 시스템이 막아요</small></span></div>
<div class="row"><span class="k">팀 CLAUDE.md</span><span class="w"><b>우리 조의 공통 규칙</b><small>조원 누구의 AI도 같은 기준으로 일해요</small></span></div>
</div></div>

<div class="card soft"><h3>일을 맡길 때 정하는 네 칸</h3>
<p>오늘 배우는 것을 한 줄로 줄이면 이거예요. 사람 후배에게 일을 맡길 때도 똑같이 써요.</p>
<ol class="steps"><li><b>입력</b> · 무엇을 보고 일하나 → 규칙(CLAUDE.md)과 자료</li><li><b>처리</b> · 어떤 순서로 하나 → 업무 매뉴얼(스킬)</li><li><b>출력</b> · 어떤 모양으로 내나 → 정해진 양식(표, JSON 계약)</li><li><b>확인</b> · 잘됐는지 어떻게 아나 → 시험 케이스, 검사, 자동 잠금(훅)</li></ol></div>

<h3 class="gap" id="map">오늘 순서</h3>
<div class="acts">
<div><b>① 규칙 정리</b><span>09:00–10:30</span></div>
<div><b>② 매뉴얼 만들기</b><span>10:30–13:00</span></div>
<div><b>③ 양식·잠금·조 규칙</b><span>14:00–18:00</span></div>
</div>
<div class="map">
<div class="grp">① 규칙 정리 · 내 AI가 매번 읽는 규칙을 가볍게</div>
<a class="row" href="#s1"><span class="t">09:00</span><span class="w"><b>준비 · 고치기 전 규칙을 남겨 두기 (P0)</b><small>남는 것: CLAUDE_v1.md, decisions.md</small></span></a>
<a class="row" href="#s2"><span class="t">09:10</span><span class="w"><b>강사님 설명 · AI가 매번 읽는 것, 규칙의 다섯 자리</b><small>20분</small></span></a>
<a class="row" href="#s2"><span class="t">09:30</span><span class="w"><b>P1 규칙 점검 · P2 규칙 정리 · 새 대화에서 확인 · 내 결정 1</b><small>남는 것: context_audit.md, 가벼워진 CLAUDE.md</small></span></a>
<div class="grp">② 매뉴얼 만들기 · 남의 것은 점검하고 들이고, 내 것은 시험으로 확인</div>
<a class="row" href="#s3"><span class="t">10:30</span><span class="w"><b>강사님 설명 · 잘 만든 매뉴얼의 모양, 들이기 전 점검</b><small>15분</small></span></a>
<a class="row" href="#s3"><span class="t">10:45</span><span class="w"><b>P3 공개 매뉴얼 받아 점검 · 내 결정 2 · P4 우리 회사용으로 고치고 효과 재기</b><small>남는 것: supply_check.md, 고친 공개 스킬 1</small></span></a>
<a class="row" href="#s4"><span class="t">11:40</span><span class="w"><b>P5 내 일의 매뉴얼 2개 · 시험 먼저 · 내 결정 3</b><small>남는 것: 내 스킬 2, skills_report.md</small></span></a>
<div class="row rest"><span class="t">13:00</span><span class="w">점심</span></div>
<div class="grp">③ 양식·잠금·조 규칙 · 넘기는 양식을 정하고, 중요한 규칙은 잠그고, 조 규칙으로</div>
<a class="row" href="#s5"><span class="t">14:00</span><span class="w"><b>강사님 설명 · P6 넘기는 양식 · P7 자동 잠금</b><small>남는 것: contracts/, .claude/hooks, hook_test.md</small></span></a>
<a class="row" href="#s6"><span class="t">15:10</span><span class="w"><b>P8 우리 조의 공통 규칙 · 내 결정 4</b><small>남는 것: team/CLAUDE.md, conflicts.md</small></span></a>
<a class="row" href="#s7"><span class="t">15:50</span><span class="w"><b>선택 하나 이상 · A 권한 줄이기 / B 매뉴얼이 제때 불리게 / C 조 매뉴얼 공개 준비 / D 양식 검사와 다시 하기</b><small>남는 것: 고른 선택의 파일</small></span></a>
<a class="row" href="#s8"><span class="t">17:20</span><span class="w"><b>W2 포트폴리오 한 장과 면접 세 문장</b><small>남는 것: portfolio_1120.html</small></span></a>
</div>
<p class="sub"><b>꼭 하는 것:</b> P0 → P1 → P2 → 새 대화 확인 → 내 결정 1 → P3 → 내 결정 2 → P4 → P5 → 내 결정 3 → P6 → P7 → P8 → 내 결정 4 → 선택 하나 → W2. 공식 일정표의 결과물 "개인 스킬 3종"은 P4(고친 공개 스킬)와 P5(내 스킬 2개), "팀 CLAUDE.md"는 P8이에요.</p>

<div class="card"><h3>레벨 · P5에 들어가요</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">기본</span><span class="w"><b>내 매뉴얼 1개</b><small>오늘 따라잡는 사람. 최소 완주선: P0 → P1 → P2 → P3 → 내 결정 2 → P4 → P5 → P8 → W2(개인 스킬 2종). P6·P7·선택은 건너뛰어도 돼요</small></span></div>
<div class="row"><span class="k">표준</span><span class="w"><b>내 매뉴얼 2개</b><small>대부분. 비워 두면 표준이에요</small></span></div>
<div class="row"><span class="k">심화</span><span class="w"><b>내 매뉴얼 2개 + 제때 불리는지 재기</b><small>에이전트 팀이나 스킬을 배포해 본 사람, 테크 트랙. 오후 선택은 테크 트랙이면 D, 에이전트 팀이 있으면 A</small></span></div>
</div></div>

<details><summary>더 정확한 말이 궁금하면 (오늘 쓰는 말)</summary><div class="body">
<ul><li><b>컨텍스트 엔지니어링</b> · 프롬프트 한 줄을 잘 쓰는 것을 넘어, AI가 일할 때 볼 규칙·절차·자료·도구를 어디에 어떻게 둘지 설계하는 일이에요.</li><li><b>점진적 공개</b> · 스킬은 이름과 설명(description)만 늘 실리고, 본문은 그 일을 할 때, 딸린 파일은 필요할 때 읽혀요. 그래서 절차를 스킬로 옮기면 매번 읽는 양이 줄어요.</li><li><b>@import</b> · CLAUDE.md 안에 "@team/CLAUDE.md"처럼 적어 다른 파일을 불러오는 방법이에요. 불러온 파일은 통째로 실려서 읽는 양이 줄지 않아요. 늘 함께 실어야 하는 것(예: 조 규칙)에만 써요.</li><li><b>훅</b> · 정해진 순간(도구를 쓰기 전·후 등)에 Claude Code가 내 컴퓨터에서 자동으로 돌리는 명령이에요. 그만큼 무엇을 돌리는지 알고 써야 해요.</li><li><b>공급망 점검</b> · 남이 만든 스킬·코드를 들이기 전에 무엇을 실행하고, 어디에 접근하고, 어떤 라이선스인지 확인하는 것이에요.</li><li><b>JSON 계약(스키마)</b> · 한 단계가 다음 단계에 넘기는 결과의 모양(필수 칸, 타입, 허용 값)을 미리 정한 것이에요.</li><li><b>호출 정확도</b> · 불러야 할 말에서 그 스킬을, 안 될 말에서 다른 것을 고르는 비율이에요. description이 좌우해요.</li><li><b>최소 권한</b> · 에이전트에게 그 일에 꼭 필요한 도구만 주는 원칙이에요.</li><li><b>[실측]과 [어림]</b> · 도구가 보여 준 값·직접 센 값과 짐작한 값을 나누는 꼬리표예요.</li></ul></div></details>
</section>

<section id="s1">
<span class="eyebrow">① 규칙 정리 · 09:00–09:10 · 준비</span>
<h2>고치기 전 규칙을 남겨 두고 시작해요</h2>
<p class="why"><b>왜 해요?</b> 오늘은 내 AI의 규칙 파일(CLAUDE.md)을 크게 정리해요. 고치기 전 판을 남겨 두면 전후를 견줄 수 있고, 마음에 안 들면 한 줄로 되돌려요. 회사에서 문서를 고치기 전에 "v1"을 따로 저장해 두는 것과 같아요.</p>
<div class="card soft"><p><b>메인 대화의 모델은 Sonnet으로 두세요</b>(앱의 모델 선택, 터미널은 /model). P4·P5가 작은 모델(Haiku)로 시험을 여러 번 돌려요. P0 보고에 <b>파이썬 버전이 "없음"</b>으로 나오면 09:10 설명 시간에 강사님과 설치해요.</p></div>
<div class="card" id="profileCard">
<h3>레벨과 나와 회사</h3>
<div class="field"><label for="v-level">오늘 레벨 · 기본 / 표준 / 심화</label><input id="v-level" data-in="level" type="text" maxlength="10" placeholder="비워 두면: 표준" autocomplete="off"></div>
<p class="sub">이번 주에 P0을 보낸 폴더라면 아래 네 칸은 비워 둬도 돼요. 칸에 적은 것만 새 값으로 바뀌어요. 하고 싶은 일에 적을 말: 콘텐츠·브랜드 / MD·영업 / CX·서비스 기획 / 운영 / 데이터·개발(테크 트랙).</p>
<div class="field"><label for="v-role">내가 하고 싶은 일</label><input id="v-role" data-in="role" type="text" maxlength="40" placeholder="비워 두면: 아직 모름 (CLAUDE.md에 있으면 그대로)" autocomplete="off"></div>
<div class="field"><label for="v-brand">회사(브랜드) 이름</label><input id="v-brand" data-in="brand" type="text" maxlength="40" placeholder="비워 두면: 라라스윗" autocomplete="off"></div>
<div class="field"><label for="v-product">제품·서비스 한 줄</label><input id="v-product" data-in="product" type="text" maxlength="60" placeholder="비워 두면: 저당 아이스크림" autocomplete="off"></div>
<div class="field"><label for="v-customer">그 회사의 고객 한 줄</label><input id="v-customer" data-in="customer" type="text" maxlength="90" placeholder="비워 두면: 다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인" autocomplete="off"></div>
<button class="ghost" id="resetProfile" type="button">처음 값으로 되돌리기</button>
</div>
<p class="sub"><b>붙여 넣으면</b> 지금 규칙을 CLAUDE_v1.md로 남기고, 오늘 규칙을 더하고, 내 결정을 적어 둘 decisions.md를 만들어요. 약 30초. <b>끝나면 볼 것:</b> 보고의 파이썬 버전.</p>
'''+box('p00','P0 · 준비 (꼭)',PR['p00'])+'''
<div class="card warn"><h3>오늘 뜨는 허락 창 · 시킨 일이면 Yes</h3><p>파일·폴더 만들기, 웹에서 공개 스킬 받기, 보조 AI(서브에이전트) 실행, 파이썬(python3), 설정 파일(.claude/settings.json) 고치기, .claude 폴더 안의 파일 쓰기("민감한 파일"이라고 나와도 시킨 일이면 Yes), git(선택 C).</p><p><b>No를 누르는 두 가지:</b> ① 지우는 명령(rm, delete)이 뜨면 No를 누르고 "지우지 말고 이름 끝에 _old를 붙여줘"라고 보내요. ② P3에서 받은 공개 스킬의 프로그램을 실행하겠다고 하면 점검표를 보기 전에는 No.</p></div>
<h3 class="gap" id="remote">리모컨 · 필요할 때만</h3>
'''+box('r1','되물을 때',R['r1'])+'\n'+box('r2','말이 길 때',R['r2'])+'\n'+box('f9','답이 어려울 때',F['f9'])+'\n'+box('r3','자료가 없다고 멈췄을 때',R['r3'])+'\n'+box('r6','방금 만든 파일 보기',R['r6'])+'''
</section>

<section id="s2">
<span class="eyebrow">① 규칙 정리 · 09:10–10:30 · 1~2교시</span>
<h2>내 AI가 매번 읽는 규칙을 가볍게 정리해요</h2>
<p class="why"><b>왜 해요?</b> 매일 아침 P0이 규칙을 한 덩어리씩 더해서, 여러분의 CLAUDE.md는 열흘 치 공지가 겹겹이 붙은 게시판이 됐어요. AI는 이 게시판을 일할 때마다 처음부터 끝까지 읽어요. 지난 공지와 서로 다른 말이 섞여 있으면 사람 신입처럼 AI도 헷갈려서 결과가 흔들려요.</p>
<p class="sub"><b>회사에서는</b> 신입에게 사규집 전체를 매번 읽히지 않아요. 늘 지킬 것만 벽에 붙이고, 일마다 필요한 것은 매뉴얼로 빼 둬요. 오늘 하는 일이 그 정리예요.</p>
<span class="pill">강사님 설명 20분</span>
<div class="card" style="margin-top:12px"><h3>AI가 일할 때마다 읽는 것</h3>
<ol class="steps"><li><b>Claude Code의 기본 설명서</b> · 내가 바꿀 수 없어요</li><li><b>CLAUDE.md</b> · 매번 통째로 읽어요. 길면 매번 무거워요</li><li><b>스킬과 에이전트의 표지</b>(이름과 한 줄 설명) · 본문은 그 일을 할 때만 펴요</li><li><b>지금까지의 대화</b> · 계속 쌓여요</li></ol>
<p>그래서 벽(CLAUDE.md)에는 늘 필요한 것만 두고, 나머지는 서랍(스킬)으로 옮겨요. 서랍의 표지(설명)가 흐리면 엉뚱한 매뉴얼을 꺼내요.</p></div>
<div class="card"><h3>규칙의 다섯 자리</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">벽에 붙임</span><span class="w"><b>모든 일에 매번 필요한 것만</b><small>루트 CLAUDE.md. 나와 회사, 숫자·출처 규칙 같은 것. 오늘 기준 60줄 안</small></span></div>
<div class="row"><span class="k">서랍 속 매뉴얼</span><span class="w"><b>특정 일을 할 때만 필요한 순서와 예시</b><small>스킬. 상세페이지 쓰는 순서, 조사 표 칸 규칙 같은 것</small></span></div>
<div class="row"><span class="k">그 방에만, 자료실</span><span class="w"><b>특정 폴더에서만 쓰는 규칙, 가끔 보는 긴 참고 자료</b><small>그 폴더의 CLAUDE.md, docs/ 폴더</small></span></div>
<div class="row"><span class="k">자동 잠금</span><span class="w"><b>꼭 지켜야 하는데 말로는 못 막는 것</b><small>훅·권한. 지우기 금지, 저장 뒤 검사 같은 것. 오후에 만들어요</small></span></div>
<div class="row"><span class="k">버림</span><span class="w"><b>지난 공지, 겹치는 말, 서로 다른 말</b><small>서로 다른 두 규칙이 함께 있으면 AI가 그때그때 하나를 골라 결과가 흔들려요</small></span></div>
</div></div>
<details><summary>공식 일정표의 "프롬프트 기본 구조"는 어디에 있나요</summary><div class="body">
<p>공식 일정표의 프롬프트 기본 구조(역할, 맥락, 과업, 제약, 출력 형식, 예시)는 프롬프트 한 장에 다 적는 것이 아니에요. 오래 쓸 것은 제자리에 두고, 프롬프트에는 그날 할 일만 남겨요.</p>
<ul><li><b>역할</b> → 에이전트 파일, 스킬의 설명("너는 검수 담당이다")</li><li><b>맥락</b> → CLAUDE.md, 스킬의 참고 자료(나와 회사, 우리 회사 기준)</li><li><b>할 일(과업)</b> → 그날 보내는 프롬프트</li><li><b>제약</b> → CLAUDE.md 규칙, 꼭 막아야 하면 자동 잠금</li><li><b>출력 형식</b> → 정해진 양식(표 칸, 파일 이름)</li><li><b>예시</b> → 스킬의 예시 폴더</li></ul>
<p>오늘의 P1 상자를 뜯어 보면 할 일(점검해서 파일로), 맥락(내가 붙인 /context), 제약(되묻지 말고), 출력 형식(다섯 자리 표)이 한 장에 있어요. 역할과 회사 맥락은 CLAUDE.md에 있어서 적지 않았어요.</p></div></details>
<span class="pill">실습</span>
<div class="card soft"><p><b>(선택) P1 전에 /context를 쳐 보세요.</b> 메인 대화에서 /context를 보내면 AI가 지금 무엇을 얼마나 읽고 있는지 보여 줘요. 출력을 복사해 아래 칸에 붙여요. 안 되면 비워 두고 넘어가요.</p></div>
'''+fieldwide('ctx','/context 출력 (붙여 넣기 · 비워 둬도 돼요)','비워 두면: 적지 않음')+'''
<p class="sub"><b>붙여 넣으면</b> 내 규칙을 한 줄씩 읽어 다섯 자리로 나누고, 서로 다른 말을 하는 규칙을 찾아요. 약 1분. <b>끝나면 볼 것:</b> 자리별 줄 수, 부딪히는 규칙.</p>
'''+box('p01','P1 · 내 AI가 매번 읽는 규칙 점검하기 (꼭)',PR['p01'],TOP)+'''
<p class="sub"><b>붙여 넣으면</b> 점검한 대로 규칙을 옮겨요. 벽에는 늘 필요한 것만 남고, 일마다의 순서는 매뉴얼(스킬)로 가요. 약 1~2분. <b>끝나면 볼 것:</b> 전후 줄 수.</p>
'''+box('p02','P2 · 규칙 정리하기: 늘 볼 것만 남기고 나머지는 제자리로 (꼭)',PR['p02'],TOP)+'''
<div class="card"><h3>10:05 · 새 대화로 확인</h3><p>같은 폴더에서 <b>새 대화</b>를 열고 아래 한 줄을 보내요. 새로 온 신입에게 "규칙 말해 봐"라고 물어보는 것과 같아요. 중요한 규칙이 빠지지 않았는지 봐요. 확인한 뒤에는 <b>아침 대화로 돌아가</b>(앱은 대화 목록, 터미널은 /resume) 내 결정 1과 P3부터 이어서 보내요.</p></div>
'''+box('check','새 대화에서 · 규칙이 읽히는지 확인',CHECK)+'''
'''+box('pick1','내 결정 1 · 벽에 남길 규칙 (○○를 고쳐서 아침 대화로 보내요)',PICK1)+'''
'''+box('e1','잘 모르겠으면 · Claude 판단을 받고 이유 듣기',EASY1)+'''
<div class="card checks"><div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="b1"><span>CLAUDE.md 전후 줄 수와 부딪히던 규칙을 봤어요</span></label>
<label class="check"><input type="checkbox" data-k="b2"><span>새 대화에서 규칙이 제대로 읽히는지 확인했어요</span></label>
<label class="check"><input type="checkbox" data-k="b3"><span><b>내 결정 1</b> · 벽에 남길 규칙을 정했어요</span></label>
</div>
<p class="sub">정리한 결과가 마음에 안 들면 <a href="#m7">막히면 7번</a>, 답이 어려우면 리모컨 "답이 어려울 때".</p>
</section>

<section id="s3">
<span class="eyebrow">② 매뉴얼 만들기 · 10:30–11:40 · 2~3교시</span>
<h2>남이 만든 매뉴얼(공개 스킬)을 안전하게 들여와 우리 회사용으로 고쳐요</h2>
<p class="why"><b>왜 해요?</b> 회사에서도 양식을 처음부터 만들지 않아요. 잘 만든 것을 가져와 우리 회사에 맞게 고쳐요. 다만 스킬에는 내 컴퓨터에서 돌아가는 프로그램이 들어 있을 수 있어서, 들이기 전에 무엇을 하는지 읽어요. 회사에서 새 프로그램을 깔 때 보안 점검을 거치는 것과 같아요.</p>
<p class="sub"><b>면접에서는</b> "공개된 것을 그냥 깔지 않고, 무엇을 실행하는지와 라이선스를 점검한 뒤 들였다"는 말이 신뢰를 줘요.</p>
<span class="pill">강사님 설명 15분</span>
<div class="card" style="margin-top:12px"><h3>잘 만든 매뉴얼(스킬)의 모양</h3>
<ol class="steps"><li><b>표지</b>(description) · 가장 중요해요. 언제 쓰고 언제 쓰지 않는지. AI는 표지만 보고 꺼낼지 정해요</li><li><b>본문</b>(SKILL.md) · 짧게, 순서와 판단 기준만</li><li><b>부록</b>(references/) · 우리 회사 기준처럼 길지만 가끔 필요한 자료</li><li><b>계산기</b>(scripts/) · 매번 똑같아야 하는 계산과 검사. AI가 머리로 하면 흔들려요</li><li><b>모범 답안</b>(examples/) · 무엇이 잘한 결과인지</li></ol></div>
<div class="card"><h3>들이기 전 점검 여섯 줄</h3>
<ol class="steps"><li>무슨 프로그램을 실행하나</li><li>허락 창 없이 쓰는 도구가 적혀 있나(SKILL.md 맨 위의 allowed-tools)</li><li>무엇을 읽고 쓰나, 인터넷에 접근하나</li><li>무엇을 설치하게 하나</li><li>라이선스가 무엇이고 고쳐서 다시 내도 되나</li><li>어디서 언제 받았나</li></ol>
<p>이 점검은 P3이 대신 해서 표로 보여 줘요. 여러분은 표를 읽고 들일지 정해요. 그래서 P3은 받기만 하고(_incoming/ 폴더), 설치는 내 결정 2 뒤에 해요.</p></div>
<span class="pill">실습</span>
'''+field('pub','들일 공개 스킬 2개. 예: brand-guidelines, internal-comms','비워 두면: 네가 정해줘 (직무에 맞게 골라 줘요)')+'''
<p class="sub"><b>붙여 넣으면</b> Anthropic 공식 저장소에서 내 직무에 맞는 스킬 2개를 받아 점검표(supply_check.md)를 써요. 아직 설치하지 않아요. 약 1~2분. <b>끝나면 볼 것:</b> 스킬마다 판단 한 줄과 위험. "열리지 않음"이 나오면 <a href="#m5">막히면 5번</a>.</p>
'''+box('p03','P3 · 남이 만든 매뉴얼(공개 스킬) 받아서 점검하기 (꼭)',PR['p03'],TOP)+'''
'''+box('pick2','내 결정 2 · 무엇을 들일지 (○○를 고쳐서 보내요)',PICK2)+'''
'''+box('e2','잘 모르겠으면 · Claude 판단대로 들이고 이유 듣기',EASY2)+'''
<p class="sub"><b>붙여 넣으면</b> 들인 스킬 하나를 우리 회사용으로 고치고, 세 가지를 같은 과제로 견줘요: (가) 원본 그대로 / (나) 원본 + 우리 회사 기준 / (다) 고친 판 + 우리 회사 기준. 약 3~4분. <b>끝나면 볼 것:</b> 무엇이 효과를 냈는지 두 줄.</p>
'''+box('p04','P4 · 받은 매뉴얼을 우리 회사용으로 고치고 효과 재기 (꼭)',PR['p04'],TOP)+'''
<div class="card checks"><div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="c1"><span><b>내 결정 2</b> · 점검표를 읽고 들일 것을 정했어요</span></label>
<label class="check"><input type="checkbox" data-k="c2"><span>P4 표에서 "우리 회사 기준을 준 효과"(가 → 나)와 "매뉴얼을 고친 효과"(나 → 다)를 봤어요</span></label>
</div>
</section>

<section id="s4">
<span class="eyebrow">② 매뉴얼 만들기 · 11:40–13:00 · 4교시</span>
<h2>내 일의 매뉴얼(내 스킬)을 만들고, 정말 도움이 되는지 시험해요</h2>
<p class="why"><b>왜 해요?</b> 매뉴얼을 만들었다고 일이 나아지는 건 아니에요. 매뉴얼 없이 한 답과 매뉴얼을 보고 한 답을 같은 문제로 견줘야 알아요. 그래서 시험 문제를 먼저 내고, 매뉴얼을 만들기 <b>전에</b> "없이 한 답"부터 받아 둬요. 신입 교육을 하기 전에 수료 시험지부터 만들어 두는 것과 같아요.</p>
<p class="sub"><b>취업에는</b> 여기서 나오는 숫자("없이 ○건 → 있을 때 ○건")가 포트폴리오와 면접의 증거예요. 공식 일정표의 트랙 과제(크리에이티브: 브랜드 톤 카피·콘텐츠 캘린더, 데이터·서비스: 상품 정보 → JSON 변환·리뷰 분류)가 기본값이에요.</p>
'''+field('skills','만들 매뉴얼(스킬). 예: 브랜드 톤 카피, 콘텐츠 캘린더','비워 두면: 네가 정해줘 (직무에 맞게 골라 줘요)')+'''
<p class="sub"><b>붙여 넣으면</b> 시험 문제 5개 → 매뉴얼 없이 한 답 → 매뉴얼 만들기 → 매뉴얼 보고 한 답 → 채점 순서로 스킬을 하나씩 만들어요. 스킬 하나에 약 3~5분. <b>끝나면 볼 것:</b> 없음/있음 통과 수 표. 한도 메시지가 뜨면 <a href="#m1">막히면 1번</a>.</p>
'''+box('p05','P5 · 내 일의 매뉴얼(내 스킬) 만들기 · 시험 문제 먼저 (꼭)',PR['p05'],TOP)+'''
'''+box('pick3','내 결정 3 · 떨어진 문제로 매뉴얼 고치기 (○○를 고쳐서 보내요)',PICK3)+'''
'''+box('e3','잘 모르겠으면 · 왜 떨어졌는지 설명 듣고 고르기',EASY3)+'''
<div class="card checks"><div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="d1"><span>없음/있음 통과 수를 봤어요. 문제 5개를 한 번 푼 것이라 1개 차이는 "비슷함"이에요</span></label>
<label class="check"><input type="checkbox" data-k="d2"><span><b>내 결정 3</b> · 떨어진 문제 하나의 원인을 내 말로 정해 고치고 다시 시험했어요</span></label>
</div>
<div class="card soft"><p><b>12:20</b> · 첫 스킬의 시험이 끝났는지 봐요. 두 번째 스킬이 13:00까지 안 끝나면 오후 선택 시간에 이어서 해요.</p><p><b>12:40 · 조 안 1분씩:</b> CLAUDE.md 전후 줄 수, 들인 공개 스킬과 이유, 내 스킬의 없음/있음 통과 수. 그리고 내 새 CLAUDE.md에서 조가 함께 지킬 만한 규칙 다섯 줄을 골라 조 단톡방에 올려 둬요(나와 회사 칸은 빼고). 오후 P8에 써요.</p></div>
</section>

<section id="s5">
<span class="eyebrow">③ 양식·잠금·조 규칙 · 14:00–15:10 · 오후</span>
<h2>넘기는 양식을 정하고, 꼭 지킬 규칙에는 자동 잠금을 걸어요</h2>
<p class="why"><b>왜 해요?</b> 일은 혼자 끝나지 않아요. 조사한 쪽이 만든 표를 글 쓰는 쪽이 받아요. 양식이 어긋나면 받는 쪽에서 조용히 틀려요. 그래서 넘기는 양식을 미리 정하고, 받을 때 검사해요. 그리고 "지우지 마" 같은 규칙은 부탁만으로는 가끔 어겨져요. 정말 중요한 규칙은 시스템이 막게 해요.</p>
<p class="sub"><b>회사에서는</b> 부서 사이의 결재 양식과 출입 카드가 이 일을 해요. 양식에 빈칸이 있으면 반려되고, 권한이 없으면 문이 안 열려요.</p>
<span class="pill">강사님 설명 15분</span>
<div class="card" style="margin-top:12px"><h3>양식과 잠금</h3>
<div class="pairs" style="padding:0;margin:0">
<div class="row"><span class="k">넘기는 양식</span><span class="w"><b>결과의 모양을 미리 정하고 검사해요</b><small>JSON 계약. 꼭 있어야 하는 칸, 숫자의 단위, 출처와 조사일. 받는 쪽은 먼저 검사하고, 틀리면 만들지 않고 이유를 알려요</small></span></div>
<div class="row"><span class="k">권한</span><span class="w"><b>AI 팀원마다 쓸 수 있는 도구를 정해요</b><small>검수 담당에게 쓰기 도구를 주지 않으면 고칠 수 없어요. 선택 A에서 해요</small></span></div>
<div class="row"><span class="k">자동 잠금</span><span class="w"><b>정해진 순간에 자동으로 도는 검사</b><small>훅. 도구를 쓰기 전이면 막을 수 있고, 쓴 뒤면 검사할 수 있어요. 내 컴퓨터에서 자동으로 도는 것이라, 남이 만든 훅은 공개 스킬처럼 읽고 들여요</small></span></div>
</div></div>
<p class="sub"><b>붙여 넣으면</b> 내 일에서 한 단계가 다음 단계로 넘기는 결과의 양식과 검사기를 만들고, 좋은 예 1개와 나쁜 예 2개로 돌려 봐요. 약 1분. <b>끝나면 볼 것:</b> 나쁜 예가 걸리는지.</p>
'''+box('p06','P6 · 넘기는 양식 정하기 (꼭)',PR['p06'],TOP)+'''
<p class="sub"><b>붙여 넣으면</b> 아침에 적어 둔 후보(hooks_todo.md)에서 하나를 골라 자동 잠금으로 만들고 시험해요. 약 1분. <b>끝나면 볼 것:</b> 걸리는 경우와 안 걸리는 경우. 잠금 때문에 일이 막히면 <a href="#m4">막히면 4번</a>.</p>
'''+box('p07','P7 · 꼭 지킬 규칙에 자동 잠금 걸기 (꼭)',PR['p07'],TOP)+'''
<div class="card checks"><div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="e1"><span>나쁜 예가 검사에서 걸리는 것을 봤어요</span></label>
<label class="check"><input type="checkbox" data-k="e2"><span>hook_test.md 맨 위의 "자동으로 돌리는 명령"을 읽었어요</span></label>
</div>
</section>

<section id="s6">
<span class="eyebrow">③ 양식·잠금·조 규칙 · 15:10–15:50 · 조</span>
<h2>우리 조의 공통 규칙을 만들어요</h2>
<p class="why"><b>왜 해요?</b> 회사에서는 한 폴더를 여러 사람이 함께 써요. 사람마다 규칙이 다르면 결과물을 합칠 때 문제가 생겨요. 서로 다른 규칙을 찾아 하나로 정하는 일이 협업이고, 면접에서 "의견이 달랐을 때 어떻게 정했나요"에 답할 수 있는 장면이에요.</p>
<div class="card"><h3>15:10 · 이렇게 해요</h3><ol class="steps"><li>12:40에 단톡방에 올린 조원들의 규칙 다섯 줄을 복사해 아래 칸에 붙여요. 조원마다 "조원 1:"처럼 앞에 적어요. 15:25까지 안 온 조원이 있으면 온 것만 붙여 보내요.</li><li>P8을 보내 초안을 만들고, 부딪힌 규칙 하나를 조원과 정해 내 결정 4로 보내요.</li><li>조장이 최종 조 규칙을 단톡방에 올리면, 조원은 "최종 조 규칙 저장" 상자 밑에 그 글을 붙여 보내요. 조원 모두의 조 규칙이 같아져요.</li></ol></div>
'''+fieldwide('team','조원 규칙 (붙여 넣기)','비워 두면: 적지 않음')+'''
<p class="sub"><b>붙여 넣으면</b> 조원들의 규칙과 내 규칙을 합쳐 조 규칙 초안을 만들고, 서로 부딪히는 곳을 표로 보여 줘요. 약 1분.</p>
'''+box('p08','P8 · 우리 조의 공통 규칙 만들기 (꼭)',PR['p08'],TOP)+'''
'''+box('pick4','내 결정 4 · 부딪힌 규칙에서 고른 쪽 (○○를 고쳐서 보내요)',PICK4)+'''
'''+box('e4','잘 모르겠으면 · 고를 수 있는 쪽과 장단점 보기',EASY4)+'''
'''+box('teamsave','최종 조 규칙 저장 (조장이 올린 글을 붙여서)',TEAMSAVE)+'''
<div class="card checks"><div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="f1"><span><b>내 결정 4</b> · 부딪힌 규칙 가운데 하나를 조원과 정해 보냈어요</span></label>
</div>
</section>

<section id="s7">
<span class="eyebrow">③ 양식·잠금·조 규칙 · 15:50–17:20 · 선택</span>
<h2>선택에서 하나 이상 골라요</h2>
<p class="sub"><b>테크 트랙은 선택 D를 꼭 해요</b>(공식 일정표 데이터·서비스 트랙: 상품 정보 → JSON 변환, 구조화 출력). 에이전트 팀이 있으면 A, 에이전트가 없고 결과가 표·JSON이면 D, 매뉴얼끼리 하는 일이 비슷하면 B, 조 매뉴얼을 공개하고 싶으면 C. P5의 두 번째 스킬이 남았으면 그것부터 끝내요.</p>
<div class="card path"><span class="pill">선택 A · 권한 줄이기</span><h3>내 AI 팀원마다 꼭 필요한 도구와 맞는 모델만</h3><p>회사에서 신입에게 모든 시스템 권한을 주지 않는 것과 같아요. <b>끝나면 보이는 것:</b> agents_report.md(표와 전후 [실측]), 바뀐 에이전트 파일(고치기 전 판은 _backup/) · 30분</p>'''+box('xa','선택 A · 권한과 모델 다시 정하기',PR['xa'])+'''</div>
<div class="card path"><span class="pill">선택 B · 매뉴얼이 제때 불리게</span><h3>표지(설명) 세 가지를 견줘 가장 정확한 것으로</h3><p>서랍의 표지가 흐리면 엉뚱한 매뉴얼을 꺼내요. <b>끝나면 보이는 것:</b> trigger_report.md(표지별 맞은 수, 두 번씩, 처음 보는 말로 한 번 더) · 30분</p>'''+box('xb','선택 B · 표지 고치기(호출 정확도)',PR['xb'])+'''</div>
<div class="card path"><span class="pill">선택 C · 조 매뉴얼 공개 준비</span><h3>조 스킬을 GitHub에 낼 준비</h3><p>공개 저장소는 포트폴리오 링크로 쓸 수 있어요. 개인정보·키·라이선스 점검표를 만들고 첫 커밋까지 해요. 올리기는 Fork 실습 때처럼 직접 해요. <b>끝나면 보이는 것:</b> team-skills/, publish_check.md · 30분</p>'''+box('xc','선택 C · 조 스킬 저장소 준비',PR['xc'])+'''</div>
<div class="card path"><span class="pill">선택 D · 양식 검사와 다시 하기 · 테크 트랙은 꼭</span><h3>양식이 정말 지켜지는지 재고, 틀리면 스스로 다시 하게</h3><p>사람이 일일이 확인하지 않아도 되는 자동화의 기본이에요. <b>끝나면 보이는 것:</b> structured_report.md(1차·2차 통과 수, 늘어난 토큰), 고친 SKILL.md · 35분</p>'''+box('xd','선택 D · 구조화 출력과 검사 뒤 다시 하기',PR['xd'])+'''</div>
</section>

<section id="s8">
<span class="eyebrow">③ 양식·잠금·조 규칙 · 17:20–18:00 · 마무리</span>
<h2>오늘을 포트폴리오 한 장과 면접 세 문장으로 남겨요</h2>
<p class="why"><b>왜 해요?</b> 오늘 만든 것은 폴더 안에 있어서 남에게 안 보여요. 채용 담당자가 1분 안에 읽을 수 있는 한 장으로 바꿔야 취업에 쓸 수 있어요.</p>
<div class="card soft"><p>오늘 내 결정 1~4는 decisions.md에 쌓였어요. W2는 decisions.md를 읽으니 <b>어느 대화에서 보내도 돼요</b>. 대화가 길어 느리면 새 대화에서 보내요.</p></div>
<p class="sub"><b>붙여 넣으면</b> 오늘의 파일들을 읽어 포트폴리오 한 장을 만들고, 면접에서 말할 세 문장을 써 줘요. 약 2분. <b>끝나면 볼 것:</b> 세 문장과 [내가 적을 곳].</p>
'''+box('w2','W2 · 포트폴리오 한 장 portfolio_1120.html (꼭)',PR['w2'])+'''
<div class="card checks"><div class="progress"><i></i></div>
<label class="check"><input type="checkbox" data-k="g1"><span>portfolio_1120.html의 [내가 적을 곳]을 채웠어요</span></label>
<label class="check"><input type="checkbox" data-k="g2"><span>실습시트 오늘 칸에 링크를 적었어요(발행하려면 "portfolio_1120.html을 아티팩트로 발행하고 링크를 알려줘")</span></label>
<label class="check"><input type="checkbox" data-k="g3"><span>회고 4줄: CLAUDE.md 전후 줄 수 / 들인 공개 스킬과 이유 / 내 스킬 없음·있음 통과 수 / 자동 잠금으로 막은 것</span></label>
</div>
<div class="card soft"><h3>다음 수업(11/23 월)</h3><p>오늘 만든 규칙, 매뉴얼, 양식이 산업 리포트를 자동으로 만드는 부품이 돼요. 폴더를 그대로 두세요.</p></div>
</section>

<section id="s9">
<span class="eyebrow">막히면</span>
<h2>이런 메시지가 뜨면 이 한 줄을 보내요</h2>
<p class="sub">메시지의 글자는 조금씩 다를 수 있어요. 비슷한 말이 보이면 그 칸을 펴고, 상자를 복사해 보내요. 오늘은 Claude도 막히면 "다음에 보낼 한 줄"을 알려 주게 해 뒀어요(P0).</p>
<details id="m1"><summary>1. "…limit… resets…"처럼 한도와 시각이 적힌 메시지</summary><div class="body"><p><b>뜻:</b> 정해진 시간 동안 쓸 수 있는 양을 다 썼어요. 적힌 시각에 풀려요. 고장이 아니에요.</p><p><b>할 일:</b> 기다리는 동안 조원 노트북에서 P8을 함께 하고, 내 supply_check.md와 skills_report.md를 읽어 둬요. 풀리면 아래 한 줄을 보내요. 다음부터는 레벨을 기본으로 두면 덜 써요.</p>'''+box('f1','멈춘 곳부터 이어서',F['f1'])+'''</div></details>
<details id="m2"><summary>2. 허락 창에서 No를 잘못 눌렀어요 / Claude가 "권한이 없어 못 했다"고 해요</summary><div class="body"><p><b>뜻:</b> 내가 허락하지 않아서 그 일을 건너뛴 거예요.</p>'''+box('f2','거절한 것을 다시',F['f2'])+'''<p>다시 뜬 허락 창에서 Yes를 눌러요. ".claude" 폴더나 "민감한 파일"이라는 말이 나와도 오늘 시킨 일이면 Yes예요.</p></div></details>
<details id="m3"><summary>3. "python3: command not found", "Python was not found" 같은 말</summary><div class="body"><p><b>뜻:</b> 이 컴퓨터에 파이썬(검사기를 돌리는 프로그램)이 없어요.</p><p><b>할 일:</b> 강사님에게 알려 설치해요. 설치 전까지는 아래 한 줄로 계속해요. 그동안의 채점 결과에는 [어림]이 붙어요. P7 자동 잠금은 "등록 안 함"으로 남아요.</p>'''+box('f3','파이썬 없이 계속',F['f3'])+'''</div></details>
<details id="m4"><summary>4. "hook"이라는 말과 함께 명령이 막혀요 / "막음:"으로 시작하는 말</summary><div class="body"><p><b>뜻:</b> P7에서 만든 자동 잠금이 일하고 있어요. 지우기처럼 막으려던 것이 막혔으면 정상이에요.</p><p><b>평범한 일까지 막히면</b> 아래 한 줄을 보내요. Claude도 아무것도 못 하면 메모장 같은 편집기로 .claude/settings.json을 열어 "hooks" 부분을 지우고 저장한 뒤 새 대화를 열어요.</p>'''+box('f4','오늘 더한 잠금만 빼기',F['f4'])+'''</div></details>
<details id="m5"><summary>5. 공개 스킬을 받다가 "열리지 않음", 403, 404가 나와요</summary><div class="body"><p><b>뜻:</b> 지금 쓰는 인터넷에서 그 주소가 막혔거나 주소가 달라요.</p><p><b>할 일:</b> 내 브라우저로 github.com/anthropics/skills를 열어 그 스킬 폴더의 SKILL.md 내용을 복사하고, 아래 상자 밑에 붙여 보내요.</p>'''+box('f11','복사한 글로 점검하기',F['f11'])+'''</div></details>
<details id="m6"><summary>6. "API Error", "Overloaded", "Connection error" 같은 말 / 답이 중간에 끊겨요</summary><div class="body"><p><b>뜻:</b> 서버가 잠깐 바쁘거나 인터넷이 끊겼어요. 내 잘못이 아니에요.</p><p><b>할 일:</b> 1분 기다렸다가 1번의 "멈춘 곳부터 이어서"를 보내요.</p></div></details>
<details id="m7"><summary>7. 정리한 CLAUDE.md가 마음에 안 들어요 / 규칙이 너무 많이 사라졌어요</summary><div class="body">'''+box('f5','아침 규칙으로 되돌리기',F['f5'])+'''<p>되돌린 뒤 P2를 다시 보내거나, 내 결정 1로 필요한 규칙만 다시 넣어요.</p></div></details>
<details id="m8"><summary>8. 대화가 길어져 느려요 / "compact", "압축"이라는 말이 보여요</summary><div class="body"><p><b>뜻:</b> 대화가 길어져 앞 내용을 요약하고 있어요. 오늘 내 결정은 decisions.md에 적혀 있어서 사라지지 않아요.</p><p><b>할 일:</b> 지금 대화에서 첫 상자를 보내고, 새 대화를 열어 둘째 상자를 보내요.</p>'''+box('f7','지금 대화에서 · 남은 일 정리',F['f7'])+'\n'+box('f8','새 대화에서 · 이어서 하기',F['f8'])+'''</div></details>
<details id="m9"><summary>9. 보조 AI가 "haiku 모델을 쓸 수 없다"고 해요</summary><div class="body">'''+box('f6','다른 모델로 같은 시험',F['f6'])+'''</div></details>
<details id="m10"><summary>10. 지우겠다는 허락 창이 떴어요(rm, delete)</summary><div class="body"><p>No를 누르고 아래 한 줄을 보내요.</p>'''+box('f10','지우지 말고 이름만 바꾸기',F['f10'])+'''</div></details>
<details id="m11"><summary>11. 스킬 없음과 있음의 통과 수가 같아요 / 0건 대 5건처럼 너무 크게 벌어져요</summary><div class="body"><p><b>둘 다 다 맞혔으면</b> 문제가 쉬운 거예요. <b>둘 다 틀렸으면</b> 우리 회사 기준이 매뉴얼에 안 들어간 거예요. "통과 조건을 우리 회사만의 기준(분류 기준, 계산 규칙, 말투, 금지어)으로 바꾼 케이스 3개를 더하고 기준선부터 다시 시험해줘."</p><p><b>0건 대 5건이면</b> 답의 모양(칸 이름)을 매뉴얼 쪽만 알았을 수 있어요. "cases.json의 과제 글에 출력 형식이 들어 있는지 보고, 없으면 넣어서 기준선부터 다시 시험해줘."</p></div></details>
<details id="m12"><summary>12. Claude가 내 폴더 밖의 파일을 고친 것 같아요</summary><div class="body">'''+box('f12','고친 파일 확인하고 되돌리기',F['f12'])+'''</div></details>
<details id="m13"><summary>13. Claude가 자꾸 되물어요 / 답이 길고 어려워요</summary><div class="body"><p>맨 위 <a href="#remote">리모컨</a>의 "되물을 때", "말이 길 때", "답이 어려울 때"를 보내요. 그래도 물으면 새 대화를 열고 하던 P부터 보내요.</p></div></details>
<details id="m14"><summary>14. 사용량이 걱정돼요</summary><div class="body"><p>레벨을 기본으로 두고, 선택은 C처럼 보조 AI를 안 쓰는 것으로 해요.</p></div></details>
</section>
</div>

<button class="theme" id="themeBtn" type="button">다크 모드</button>
<div class="toast" id="toast" role="status" aria-live="polite">복사됐어요</div>
'''
body=expand_mvp_html(body)
out=build_page('Day 20 · AI 업무 매뉴얼 만들기',body,
  {'role':'아직 모름','level':'표준','ctx':'적지 않음','pub':'네가 정해줘','skills':'네가 정해줘','team':'적지 않음'},'l20-')
write_page(out,PATH)
