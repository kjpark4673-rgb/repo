# AX 수업 용어 사전 (Day 1~21) 빌더
# 출처: 공식 일정표 "상세 커리큘럼_최종" 탭의 10/26~11/23 행, Day 14·15·16 수업 가이드의 용어 칸.
# "수업에서" 줄은 위 두 출처에 적힌 것만 옮긴다. 강사의 말로 꾸미지 않는다.
import html, re

OUT = '/home/user/repo/classroom/student-guide/glossary.html'

DAYS = {
 1:('10/26(월)','온보딩'), 2:('10/27(화)','Local 오리엔테이션'), 3:('10/28(수)','지역 자산 조사 Ⅰ'),
 4:('10/29(목)','지역 자산 조사 Ⅱ'), 5:('10/30(금)','콘텐츠 아카이빙'), 6:('11/2(월)','지역 자산 인벤토리'),
 7:('11/3(화)','페르소나와 세계관'), 8:('11/4(수)','스토리보드'), 9:('11/5(목)','산업 구조와 기업 리서치'),
 10:('11/6(금)','밸류체인'), 11:('11/9(월)','페인포인트'), 12:('11/10(화)','AX 이해'),
 13:('11/11(수)','AX 비즈니스 모델'), 14:('11/12(목)','서비스 시나리오와 스펙'), 15:('11/13(금)','시장 검증'),
 16:('11/16(월)','콘텐츠·서비스 제작 Ⅰ'), 17:('11/17(화)','제작 Ⅱ와 사용자 테스트'), 18:('11/18(수)','피칭 데이'),
 19:('11/19(목)','AI 이해'), 20:('11/20(금)','컨텍스트 엔지니어링'), 21:('11/23(월)','산업 리포트 자동 생성'),
}
UPCOMING_FROM = 17

CATS = [
 ('course','과정과 수업'), ('research','리서치와 자료'), ('customer','고객과 브랜드'), ('biz','사업과 기획'),
 ('mkt','마케팅과 콘텐츠'), ('ai','AI 기본'), ('tools','Claude와 도구'), ('marks','가이드 표시'),
]

E = []
def add(id, t, en, cat, days, d, c, r=(), e=''):
    E.append(dict(id=id, t=t, en=en, cat=cat, days=sorted(set(days)), d=d, e=e, c=c, r=list(r)))

# ── 과정과 수업
add('onboarding','온보딩','Onboarding','course',[1],
    '과정을 시작할 때 운영 방식, 일정, 규칙을 안내하고 서로 인사하는 첫 시간이에요.',
    '일정표 Day 1 · 커리큘럼 안내, 직무 선호도 조사, 학습 계획 세우기, 자기소개, 팀 정하기.',
    ['track','team'])
add('track','트랙','Track','course',[2,16],
    '같은 과정 안에서 관심 분야에 따라 나눈 길이에요. 이 과정에는 AX 크리에이티브 트랙과 AX 데이터·서비스 트랙이 있어요.',
    '일정표 · 날마다 [공통] 실습과 트랙별 실습이 함께 있어요. Day 16 가이드는 개발·데이터 쪽 학생이 따라가는 길을 "테크 트랙"이라고 불러요.',
    ['team'])
add('team','팀(조)','Team','course',[1,2,16],
    '함께 과제를 하는 4~5명의 모둠이에요. 가이드에서는 "조", 이끄는 사람은 "조장"이라고 불러요.',
    '일정표 Day 1 · 팀장과 팀 이름 정하기. Day 2 · 트랙 안에서 4~5명, 6주 동안 같은 팀.',
    ['track'])
add('portfolio','포트폴리오','Portfolio','course',[16],
    '내가 만든 결과물과, 그것을 만들며 내린 결정을 모아 남에게 보여 주는 자료예요.',
    'Day 16 가이드 · 하루를 정리한 "포트폴리오 한 장"(portfolio_1116.md)을 W2로 남겨요.',
    ['mydecision'])
add('pitching','피칭 데이','Pitching day','course',[18],
    '팀별로 만든 것을 사람들 앞에서 짧게 발표하고 질문을 받는 날이에요.',
    '일정표 Day 18 · 팀별 5분 발표, 라이브 데모, 3분 질문. 발표 자료는 브라우저에서 열리는 HTML 피치덱이에요.',
    ['pitchdeck','livedemo'])
add('pitchdeck','피치덱','Pitch deck','course',[17,18],
    '아이디어를 짧은 시간에 설득하려고 만든 발표 자료예요.',
    '일정표 Day 18 · 순서는 문제 → 해결 → 시장 → BM → MVP → 팀 → 요청사항. Day 17 오후부터 뼈대를 만들어요.',
    ['pitching','bm','mvp'],
    '가게를 차리기 전에 투자자에게 보여 주는 얇은 설명서예요.')
add('livedemo','라이브 데모','Live demo','course',[18],
    '발표하면서 만든 것을 실제로 눌러 보이며 보여 주는 시연이에요.',
    '일정표 Day 18 · 5분 발표 안에 라이브 데모를 넣어요.',
    ['pitching','prototype'])

# ── 리서치와 자료
add('localresearch','로컬 리서치','Local research','research',[2],
    '한 지역의 장소, 사람, 가게, 이야기, 데이터를 조사하는 일이에요.',
    '일정표 Day 2 · 로컬 리서치 → 콘텐츠 아카이빙 → AI 서비스·콘텐츠 기획 순서로 Local 모듈을 시작해요.',
    ['localasset','archive','keywordmap'])
add('keywordmap','키워드 맵','Keyword map','research',[2],
    '한 주제와 관련된 낱말들을 묶어서 지도처럼 펼쳐 놓은 것이에요. 무엇을 더 조사할지 한눈에 보여요.',
    '일정표 Day 2 · 지역 키워드 맵을 만들고, 주제별 노트를 research 폴더에 쌓아요.',
    ['localresearch'])
add('localasset','지역 자산','Local asset','research',[3,6],
    '그 지역만 가진 자원이에요. 자연, 역사, 문화, 인물, 산업, 커뮤니티로 나눠 봐요.',
    '일정표 Day 3 · 지역 자산 분류 체계. Day 6 · 지역 자산 인벤토리 30개 가운데 핵심 자산 3개를 골라요.',
    ['inventory','localresearch'])
add('primarysecondary','1차 자료와 2차 자료','Primary / secondary data','research',[3,4],
    '1차 자료는 내가 직접 모은 자료(리뷰, 영상, 사진, 인터뷰)이고, 2차 자료는 남이 이미 정리해 둔 자료(통계, 공공데이터, 보고서)예요.',
    '일정표 Day 3 · 2차 자료(공공데이터포털, 지자체 통계, 한국관광 데이터랩). Day 4 · 1차 자료를 모을 곳(유튜브, 인스타그램, 블로그, 지도 리뷰).',
    ['publicdata','fieldwork'])
add('publicdata','공공데이터포털과 KOSIS','Public data','research',[3,15],
    '공공데이터포털은 공공기관이 공개한 데이터를 모아 둔 곳이고, KOSIS는 나라의 통계를 모아 둔 국가통계포털이에요.',
    '일정표 Day 3 · 공공데이터포털, 한국관광 데이터랩, KOSIS에서 자료를 찾아요. Day 15에도 KOSIS가 나와요.',
    ['primarysecondary','csv'])
add('crosscheck','교차검증','Cross-check','research',[3],
    '한 출처만 믿지 않고, 다른 출처로 같은 사실을 한 번 더 확인하는 일이에요.',
    '일정표 Day 3 · 교차검증과 출처 기록 원칙. 출처와 검증 결과를 표로 모아요.',
    ['source','hallucination'],
    '길을 물을 때 한 사람 말만 믿지 않고 두 사람에게 더 묻는 것과 같아요.')
add('source','출처 기록','Source','research',[2,3,5],
    '자료를 어디서 가져왔는지(사이트, 주소, 날짜)를 남기는 일이에요. 출처가 없으면 맞는지 확인할 수 없어요.',
    '일정표 Day 2 · 출처와 할루시네이션 점검. Day 5 · 파일마다 소스, 주소, 일시, 저작권을 적어요.',
    ['crosscheck','metadata','hallucination'])
add('fieldwork','디지털 필드워크','Digital fieldwork','research',[4,5],
    '현장에 직접 가는 대신, 영상, SNS, 지도 리뷰, 로드뷰처럼 온라인에서 현장 자료를 모으는 조사예요.',
    '일정표 Day 4 · 팀별 필드워크 계획서. Day 5 · 강의장에서 팀별로 자료를 20건 이상 모아요.',
    ['primarysecondary','archive','sociallistening'])
add('sociallistening','소셜 리스닝','Social listening','research',[4],
    'SNS, 리뷰, 댓글에서 사람들이 실제로 하는 말을 모아 듣는 일이에요.',
    '일정표 Day 4 · 리뷰 100건 안팎을 분석해 차트와 인사이트 3가지를 뽑아요.',
    ['voc','fieldwork'])
add('archive','아카이빙과 아카이브','Archiving / archive','research',[2,5,15],
    '아카이빙은 자료를 정해진 규칙으로 모아 두는 일이고, 아카이브는 그렇게 모아 둔 보관함이에요.',
    '일정표 Day 5 · archive 폴더와 메타데이터 CSV. Day 15 가이드 · 경쟁사 광고를 archive.csv로 모아요.',
    ['metadata','benchmarking'],
    '요리사의 맛집 노트예요. 잘되는 집이 무엇을, 어떻게, 얼마나 오래 파는지 적어 둬요.')
add('metadata','메타데이터','Metadata','research',[5],
    '자료에 붙이는 설명 정보예요. 파일 이름, 출처 주소, 날짜, 저작권, 태그 같은 것이에요.',
    '일정표 Day 5 · 아카이빙 규칙: 파일명, 태그, 메타데이터(소스, URL, 일시, 저작권).',
    ['archive','csv'],
    '도서관 책 등에 붙은 분류 스티커예요. 책을 다 읽지 않아도 무엇인지 알 수 있어요.')
add('copyright','저작권과 공공누리','Copyright / KOGL','research',[4,5,19],
    '저작권은 만든 사람이 자기 작품의 쓰임을 정할 권리예요. 공공누리는 공공기관의 사진이나 자료를 어떤 조건으로 써도 되는지 표시한 제도예요.',
    '일정표 Day 4 · 이용약관, 개인정보, 저작권 유의. Day 5 · 공공누리로 저작권 확인. Day 19 · AI 결과물의 저작권 문제.',
    ['airisk','source'])
add('inventory','인벤토리','Inventory','research',[2,6],
    '가진 것을 빠짐없이 적은 목록이에요. 이 과정에서는 지역 자산을 한 표에 정리한 것이에요.',
    '일정표 Day 6 · 자산명, 유형, 스토리성, 시장성, 데이터 가용성, 연계 사업을 적어 30개 항목을 만들어요.',
    ['localasset','scoring'])
add('scoring','스코어링과 가중치','Scoring / weight','research',[6],
    '기준마다 점수를 매겨 고르는 방법이에요. 가중치는 기준마다 다르게 주는 중요도예요.',
    '일정표 Day 6 · 평가 매트릭스로 핵심 자산 3개를 골라요. 크리에이티브 트랙은 스토리성, 데이터·서비스 트랙은 데이터 가용성에 가중치를 줘요.',
    ['inventory','opportunitymatrix'],
    '같은 시험이라도 국어 점수를 두 배로 쳐 주는 학과가 있는 것과 같아요.')
add('csv','CSV','Comma-Separated Values','research',[3,4,5,16],
    '쉼표로 칸을 나눈 표 파일이에요. 엑셀이나 구글 시트에서 열려요.',
    '일정표 Day 3 · 공공데이터를 CSV로 정리해요. Day 16 가이드 · 테크 트랙이 sample.csv를 만들어요.',
    ['metadata','dataspec'])
add('dataspec','데이터 명세','Data specification','research',[3],
    '데이터의 각 열이 무엇을 뜻하는지, 단위와 형식은 무엇인지 적은 설명서예요.',
    '일정표 Day 3 · 데이터·서비스 트랙이 공공데이터셋의 구조(CSV, API, 데이터 명세)를 읽어요.',
    ['csv','api'])
add('trendtools','네이버 데이터랩과 구글 트렌드','Search trends','research',[4],
    '사람들이 어떤 말을 얼마나 검색했는지 시간에 따라 보여 주는 무료 도구예요.',
    '일정표 Day 4 · 국내는 네이버 데이터랩, 해외와 외국인 관광 수요는 구글 트렌드로 봐요.',
    ['sociallistening'])
add('disclosure','공시와 IR','Disclosure / Investor Relations','research',[9],
    '공시는 회사가 경영 정보를 법에 따라 공개하는 것이고, IR은 투자자에게 회사를 설명하는 자료와 활동이에요. DART는 금융감독원의 전자공시 사이트예요.',
    '일정표 Day 9 · 공시와 보도자료를 AI로 요약하고 비교해서, 관심 기업 1곳의 산업 리서치 원페이지를 만들어요.',
    ['onepager','subagent'])
add('onepager','한 장 기획서(원페이지)','One-pager','research',[7,9],
    '핵심만 한 장에 담은 문서예요. 읽는 사람이 1~2분 안에 무엇을, 왜 하는지 알 수 있어요.',
    '일정표 Day 7 · AI 서비스·콘텐츠 한 장 기획서. Day 9 · 산업 리서치 원페이지.',
    ['spec','mvpdoc'])

# ── 고객과 브랜드
add('persona','페르소나(퍼소나)','Persona','customer',[2,7,14],
    '우리가 겨냥하는 사람을 실제 한 사람처럼 구체적으로 그린 인물이에요. 고객 페르소나는 고객을, 브랜드 페르소나는 브랜드를 한 사람처럼 그려요.',
    '일정표 Day 7 · 브랜드 페르소나와 고객 페르소나. Day 14 가이드 · 퍼소나와 고객 여정 지도를 스킬로 만들어요. 가이드에서는 "퍼소나"라고 써요.',
    ['segment','cjm','worldview'],
    '단골손님 일기장이에요. "25~34세 여성"이 아니라 "밤 10시 냉동실 앞에서 10분째 서성이는 29살"처럼 장면이 보여야 해요.')
add('segment','고객 세그먼트','Customer segment','customer',[7,13],
    '나이, 상황, 행동이 비슷한 고객끼리 묶은 무리예요.',
    '일정표 Day 7 · 데이터·서비스 트랙이 행동 데이터로 세그먼트를 정해요. Day 13 · BM 캔버스의 한 칸이에요.',
    ['persona','bmcanvas'])
add('worldview','세계관과 세계관 바이블','Worldview / bible','customer',[7],
    '세계관은 브랜드나 캐릭터가 사는 세상의 설정(배경, 인물, 갈등, 가치, 톤앤매너)이에요. 세계관 바이블은 그 설정을 한 문서에 모아 둔 기준서예요.',
    '일정표 Day 7 · 세계관 바이블을 브랜드 스킬 파일로 저장해요.',
    ['tone','skill','persona'])
add('tone','톤앤매너','Tone & manner','customer',[7,20],
    '말투와 분위기의 규칙이에요. 예: 존댓말, 짧은 문장, 이모지 쓰지 않기. "브랜드 보이스"라고도 해요.',
    '일정표 Day 7 · 브랜드 스킬 파일에 톤, 금칙어, 핵심 메시지를 적어요. Day 20 · 브랜드 보이스 공개 스킬.',
    ['forbidden','worldview'])
add('forbidden','금칙어','Forbidden words','customer',[7],
    '브랜드가 쓰지 않기로 정한 말이에요.',
    '일정표 Day 7 · 브랜드 스킬 파일에 들어가요.',
    ['tone'])
add('storytelling','스토리텔링 구조','Storytelling structure','customer',[8],
    '이야기를 전하는 순서예요. 일정표에는 훅 → 전개 → 전환 → 행동 유도 순서가 나와요.',
    '일정표 Day 8 · 숏폼, 카드뉴스, 웹페이지, 앱 화면마다 이 구조로 이야기를 짜요.',
    ['hook','cta','storyboard'])
add('storyboard','스토리보드','Storyboard','customer',[2,8],
    '영상이나 화면을 장면별로 그림과 글로 미리 짜 놓은 것이에요.',
    '일정표 Day 8 · 6~8컷짜리 스토리보드(장면, 카메라 무빙, 대사)를 만들어요.',
    ['shotlist','storytelling'],
    '영화를 찍기 전에 그리는 만화 콘티예요.')
add('shotlist','샷 리스트','Shot list','customer',[8],
    '찍을 장면(컷)을 순서대로 적은 목록이에요. 장면마다 무엇을, 어떤 각도로 찍을지 적어요.',
    '일정표 Day 8 · 샷 리스트를 바탕으로 스토리보드를 만들어요.',
    ['storyboard'])
add('cjm','고객 여정 지도(CJM)','Customer Journey Map','customer',[11,14],
    '고객이 문제를 느끼는 순간부터 찾아보고, 사고, 쓰고, 다시 사기까지 거치는 단계를 순서대로 그린 지도예요.',
    '일정표 Day 11 · 고객 여정 지도로 페인포인트 3가지를 찾아요. Day 14 가이드 · 6단계(문제 자각, 탐색, 비교·의심, 구매 결심, 첫 사용, 자랑·재구매).',
    ['painpoint','churn','persona'],
    '지하철 노선도예요. 손님이 1호역에서 타서 6호역(재구매)까지 가요. 중간에 내리는 게 이탈이에요.')
add('churn','이탈','Drop-off','customer',[14],
    '고객이 여정 중간에 떠나는 것이에요. 사지 않거나, 다시 오지 않아요.',
    'Day 14 가이드 · 단계마다 손님이 내리려는 이유와, 그 이유를 붙잡는 훅 카피를 적어요.',
    ['cjm','hook'])
add('painpoint','페인포인트','Pain point','customer',[11],
    '고객이 불편하거나 짜증 나는 지점이에요.',
    '일정표 Day 11 · 리뷰, 댓글 같은 VOC로 근거를 만들고 빈도, 강도, 해결 가능성으로 우선순위를 정해요.',
    ['voc','cjm','jtbd'])
add('voc','VOC','Voice of Customer','customer',[11],
    '고객의 목소리예요. 리뷰, 문의, 댓글처럼 고객이 직접 한 말이에요.',
    '일정표 Day 11 · VOC를 분류해서 페인포인트의 근거로 써요.',
    ['painpoint','sociallistening'])
add('jtbd','JTBD','Jobs To Be Done','customer',[11,12],
    '고객이 제품을 사서 끝내고 싶은 "일"이에요. 사람들은 제품 자체보다 그 일을 해결하려고 사요.',
    '일정표 Day 12 · JTBD에서 출발해 AI를 쓸 기회를 찾아요.',
    ['painpoint','opportunitymatrix'],
    '드릴을 사는 사람은 드릴보다 벽에 난 구멍을 원해요.')
add('fivewhys','5-Whys','Five Whys','customer',[14,16],
    '"왜?"를 반복해서 겉으로 보이는 행동 밑의 진짜 이유까지 내려가는 방법이에요.',
    'Day 14 가이드 · 퍼소나의 속마음 찾기. Day 16 가이드 · P2에서 경쟁사의 훅이 왜 통하는지 다섯 번 파고들어요.',
    ['persona','hook'],
    '양파 껍질 벗기기예요. 마지막 답이 감정이면 성공이에요. 꼭 다섯 번일 필요는 없어요.')

# ── 사업과 기획
add('valuechain','밸류체인','Value chain','biz',[10],
    '제품이 만들어져 고객에게 닿기까지 가치가 더해지는 단계를 사슬처럼 이은 것이에요. 단계마다 누가 일하고, 돈과 데이터가 어떻게 흐르는지 봐요.',
    '일정표 Day 10 · 팀별 밸류체인 맵. 크리에이티브 예: 로컬 IP → 콘텐츠 → 캠페인 → 뷰티 커머스 기획전 → 구매.',
    ['bottleneck','stakeholder','opportunitymatrix'],
    '빵 한 개가 밀밭에서 빵집 진열대까지 오는 길이에요. 길목마다 누가 무엇을 더했는지 봐요.')
add('bottleneck','병목','Bottleneck','biz',[10],
    '흐름이 막혀 전체 속도를 늦추는 한 지점이에요.',
    '일정표 Day 10 · 밸류체인 단계별로 병목, 비용, 기회를 찾아요.',
    ['valuechain'],
    '병의 좁은 목처럼, 거기서 막히면 병이 아무리 커도 천천히 나와요.')
add('stakeholder','이해관계자','Stakeholder','biz',[10],
    '그 일에 영향을 주거나 받는 사람과 조직이에요. 고객, 직원, 협력사, 지역 주민이 모두 해당할 수 있어요.',
    '일정표 Day 10 · 밸류체인 분석 틀에 들어가요.',
    ['valuechain'])
add('dxax','DX와 AX','Digital / AI Transformation','biz',[12],
    'DX(디지털 전환)는 종이와 손으로 하던 일을 디지털로 옮기는 것이고, AX(AI 전환)는 일하는 방식 자체를 AI 중심으로 바꾸는 것이에요.',
    '일정표 Day 12 · 2026년의 AX는 챗봇 하나에서 에이전트, 여러 에이전트로 넘어가고, 사람이 결과를 검토해요.',
    ['agent','humanloop'])
add('opportunitymatrix','기회 매트릭스','Opportunity matrix','biz',[12],
    '가로와 세로에 기준을 놓고 칸마다 기회를 적어, 어디에 힘을 쓸지 고르는 표예요.',
    '일정표 Day 12 · 밸류체인 단계 × AI 역량(생성, 예측, 추천, 자동화, 에이전트)으로 AX 기회 10개를 찾고, 임팩트와 실현성으로 평가해요.',
    ['valuechain','scoring','jtbd'])
add('bm','비즈니스 모델(BM)','Business model','biz',[9,13,18],
    '회사가 누구에게, 무엇을 주고, 어떻게 돈을 버는지의 구조예요.',
    '일정표 Day 9 · 대표 기업의 사업 모델. Day 13 · BM 캔버스. Day 18 · 피치 구조의 한 칸.',
    ['bmcanvas','revenuemodel'])
add('bmcanvas','BM 캔버스','Business Model Canvas','biz',[13],
    '비즈니스 모델을 9칸(고객 세그먼트, 가치 제안, 채널, 고객 관계, 수익원, 핵심 자원, 핵심 활동, 핵심 파트너, 비용 구조)에 나눠 한 장에 그리는 틀이에요.',
    '일정표 Day 13 · AX BM 캔버스는 여기에 AI 역할, 데이터 원천, 학습 루프 칸을 더해요.',
    ['bm','vpc','segment'])
add('revenuemodel','수익모델','Revenue model','biz',[13],
    '돈을 받는 방식이에요. 구독, 수수료, 광고, 라이선스, 데이터 같은 유형이 있어요.',
    '일정표 Day 13 · 수익모델 유형. 크리에이티브 트랙은 로컬 IP 라이선싱과 기획전 수익 구조를 봐요.',
    ['bm'])
add('vpc','가치 제안과 가치 제안 캔버스','Value proposition','biz',[13],
    '가치 제안은 고객이 왜 우리를 골라야 하는지 말하는 약속이에요. 가치 제안 캔버스는 고객의 할 일, 불편, 기대를 우리 제품이 무엇으로 채우는지 맞춰 보는 표예요.',
    '일정표 Day 13 · 가치 제안 캔버스로 BM이 앞뒤가 맞는지 점검해요.',
    ['bmcanvas','promise'])
add('redteam','레드팀','Red team','biz',[13],
    '일부러 반대편에 서서 계획의 허점을 찾는 검토예요.',
    '일정표 Day 13 · 투자자, 고객, 경쟁사 입장의 서브에이전트로 BM을 검증해요.',
    ['subagent','bmcanvas'],
    '시합 전에 우리 팀 약점만 노리는 연습 상대예요.')
add('scenario','서비스 시나리오(As-Is → To-Be)','Service scenario','biz',[14],
    '서비스를 쓰는 장면을 이야기처럼 적은 것이에요. As-Is는 지금의 모습, To-Be는 바뀐 뒤의 모습이에요.',
    '일정표 Day 14 · To-Be 시나리오, 유저 플로우, spec.md를 만들어요.',
    ['userstory','userflow','spec'])
add('userstory','유저 스토리','User story','biz',[14],
    '"(누구)로서 (무엇)을 하고 싶다. 왜냐하면 (이유)"처럼 사용자 입장에서 쓴 기능 한 줄이에요.',
    '일정표 Day 14 · 서비스 시나리오와 함께 써요.',
    ['scenario','spec'])
add('userflow','유저 플로우','User flow','biz',[14],
    '사용자가 목적을 이루려고 화면을 어떤 순서로 지나가는지 그린 흐름이에요.',
    '일정표 Day 14 · 유저 플로우와 정보 구조(IA).',
    ['ia','scenario'])
add('ia','정보 구조(IA)','Information Architecture','biz',[14],
    '서비스 안의 정보와 메뉴를 어떻게 나누고 묶을지 정한 구조예요.',
    '일정표 Day 14 · 유저 플로우와 함께 나와요.',
    ['userflow'],
    '마트의 코너 배치예요. 손님이 우유를 어디서 찾을지 미리 정해 두는 일이에요.')
add('spec','스펙(spec.md, PRD)','Specification','biz',[14],
    '무엇을 만들지 적은 설계 문서예요. 목표, 사용자, 기능, 제약, 완료 기준을 적어요. 회사에서는 PRD(제품 요구사항 문서)라고도 해요.',
    '일정표 Day 14 · Claude Code가 질문하고 내가 답하는 인터뷰 방식으로 spec.md를 써요. 일정표는 "프롬프트에서 스펙으로"를 2026년의 흐름으로 소개해요.',
    ['mvpdoc','scenario'])
add('kpi','KPI','Key Performance Indicator','biz',[14],
    '목표를 얼마나 이뤘는지 재는 핵심 숫자예요.',
    '일정표 Day 14 · 콘텐츠 기획안은 목적, 타깃, 메시지, 채널, KPI로 짜요.',
    ['ctr','cvr'])
add('marketvalidation','시장 검증','Market validation','biz',[15],
    '이 아이디어를 살 사람이 충분한지, 팔수록 남는지를 경쟁과 숫자로 확인하는 일이에요.',
    '일정표 Day 15 · 경쟁 분석, 포지셔닝 맵, 시장 규모, 단위 경제성 시뮬레이션.',
    ['positioning','tamsamsom','uniteconomics'])
add('substitute','경쟁재와 대체재','Competitor / substitute','biz',[15],
    '경쟁재는 같은 종류의 다른 제품이고, 대체재는 종류는 달라도 같은 필요를 채우는 제품이에요.',
    '일정표 Day 15 · 경쟁·대체재 분석.',
    ['benchmarking','positioning'],
    '저당 아이스크림의 경쟁재는 다른 저당 아이스크림이고, 대체재는 같은 순간에 손이 가는 다른 간식이에요.')
add('positioning','포지셔닝 맵','Positioning map','biz',[15],
    '두 가지 기준(예: 가격, 맛)으로 축을 그리고 경쟁 브랜드의 위치를 찍은 그림이에요.',
    '일정표 Day 15 · 경쟁사 비교표와 포지셔닝 맵.',
    ['substitute','marketvalidation'],
    '동네 지도예요. 가게들이 어디에 몰려 있는지 그려 보면 아무도 없는 빈 땅이 보여요.')
add('tamsamsom','TAM·SAM·SOM','Total / Serviceable / Obtainable Market','biz',[15],
    '시장 크기를 세 겹으로 보는 방법이에요. TAM은 전체 시장, SAM은 우리가 닿을 수 있는 시장, SOM은 실제로 차지할 수 있는 몫이에요.',
    '일정표 Day 15 · 시장 규모 추정.',
    ['fermi','marketvalidation'],
    '피자 한 판이에요. 피자 전체(TAM), 우리 배달 구역 안의 조각(SAM), 올해 실제로 먹을 수 있는 조각(SOM).')
add('fermi','페르미 추정','Fermi estimate','biz',[15],
    '모르는 큰 숫자를 아는 작은 숫자들로 쪼개서 대략 계산하는 방법이에요.',
    'Day 15 가이드 · 시장 규모를 추정할 때 써요.',
    ['tamsamsom'],
    '수박씨 세기예요. 씨를 다 세지 않고, 한 조각의 씨를 세고 조각 수를 곱해요.')
add('revenueformula','매출 공식(매출 인수분해)','Revenue formula','biz',[15],
    '매출을 곱셈 조각으로 나눠 보는 방법이에요. 온라인 판매는 노출 수 × 클릭률 × 구매 전환율 × 객단가예요.',
    'Day 15 가이드 · 파는 방식(온라인, 오프라인, 앱, 예약, B2B)마다 조각의 이름만 달라요.',
    ['ctr','cvr','aov'],
    '찌개를 재료별로 맛보기예요. 맛이 이상하면 재료를 하나씩 맛보듯, 매출이 이상하면 조각을 하나씩 봐요.')
add('aov','객단가','Average order value','biz',[15],
    '고객 한 명이 한 번 살 때 쓰는 평균 금액이에요.',
    '일정표 Day 15 · 단위 경제성(객단가, 전환율, CAC).',
    ['revenueformula','uniteconomics'])
add('uniteconomics','단위 경제성','Unit economics','biz',[15],
    '고객 한 명이나 주문 한 건을 기준으로, 팔수록 남는지 손해인지 따져 보는 계산이에요.',
    '일정표 Day 15 · 객단가, 전환율, CAC로 시뮬레이션을 만들어요.',
    ['aov','caclv','xlsx'])
add('caclv','CAC와 LTV','Customer Acquisition Cost / Lifetime Value','biz',[15],
    'CAC는 고객 한 명을 데려오는 데 드는 돈이고, LTV는 그 고객이 관계를 이어 가며 남겨 주는 돈이에요. LTV가 CAC보다 커야 남아요.',
    'Day 15 가이드 · 테크 트랙과 심화 내용으로 나와요.',
    ['uniteconomics'],
    '전단지 값과 단골이 남기는 돈이에요.')
add('hypothesis','가설','Hypothesis','biz',[15,16],
    '"이렇게 하면 이렇게 될 것이다, 왜냐하면"처럼 근거를 붙인 추측이에요. 틀릴 수 있고, 시험해서 확인해요.',
    'Day 15 가이드 · 가설 v1, v2. Day 16 가이드 · P1이 시험해 볼 소재 가설 3개를 써요.',
    ['corehypothesis','usertest'],
    '일기예보예요. 틀릴 수 있지만 근거가 있어야 해요.')
add('mvp','MVP','Minimum Viable Product (최소 기능 제품)','biz',[16,17,18],
    '고객 반응을 보려고 꼭 필요한 것만 넣어 가장 작게 만든 첫 버전이에요. 다 만든 뒤에 반응을 보는 대신, 작게 내놓고 반응을 본 뒤 고쳐요.',
    '일정표 Day 16 · MVP 범위 정하기(핵심 가설, 필수 기능). Day 17 · MVP 고도화와 사용자 테스트. Day 18 · 피치 구조의 한 칸.',
    ['mvpdoc','corehypothesis','mustfeature','prototype'],
    '시식 코너예요. 가게를 다 짓기 전에 한 입만 내놓고 반응을 봐요. Day 16의 한 입은 랜딩페이지 한 장이에요.')
add('mvpdoc','MVP 정의서','MVP definition','biz',[16],
    'MVP를 만들기 전에 무엇을, 누구에게, 왜 만드는지 한 장으로 정리한 문서예요.',
    'Day 16 가이드 · 기획전 주제, 누구에게(고객 한 명의 장면), 사지 않는 이유 3가지, 핵심 가설, 약속 한 줄, 꼭 넣을 것 5가지, 만들지 않을 것 3가지, 성공 기준(처음 보는 사람이 첫 화면을 5초 보고 알아보는가)을 적어요. 파일 이름은 mvp.md예요.',
    ['mvp','spec','onepager'])
add('corehypothesis','핵심 가설','Core hypothesis','biz',[16],
    '"첫 화면에서 이걸 보여 주면 산다"는 우리의 가장 중요한 추측이에요. 아직 맞는지 몰라요.',
    'Day 16 가이드 · 핵심 가설은 우리끼리 보는 추측이고, 약속 한 줄은 고객이 보는 문장이에요. 맞는지는 Day 17에 사람에게 보여 주고 확인해요.',
    ['hypothesis','promise','usertest'])
add('mustfeature','필수 기능과 만들지 않을 것','Must-have / out of scope','biz',[16],
    '이번 버전에 반드시 넣을 것과, 이번에는 빼기로 정한 것이에요. 뺄 것을 정해야 끝낼 수 있어요.',
    'Day 16 가이드 · 꼭 넣을 것 5가지, 만들지 않을 것 3가지.',
    ['mvp','mvpdoc'])
add('prototype','프로토타입','Prototype','biz',[16,17],
    '버튼이 눌리고 결과가 바뀌는, 시험용으로 만든 화면이에요. 진짜 제품 전에 써 보게 하려고 만들어요.',
    '일정표 Day 16 · Claude Design 시안을 Claude Code로 넘겨 동작하는 프로토타입을 만들어요. Day 16 가이드 · 테크 트랙이 prototype.html을 만들어요.',
    ['mvp','sampledata','handoff'])
add('sampledata','샘플 데이터','Sample data','biz',[16,17],
    '진짜 데이터 대신 넣어 보는 예시 데이터예요. 데이터를 넣었을 때 화면이 제대로 도는지 볼 수 있어요.',
    'Day 16 가이드 · T5가 샘플 30줄과 sample.csv를 만들고, 화면에 "샘플 데이터"라고 표시해요.',
    ['prototype','csv'])
add('usertest','사용자 테스트','User test','biz',[17],
    '실제 사용자에게 과제를 주고 써 보게 하면서, 어디서 막히는지 관찰하는 시험이에요.',
    '일정표 Day 17 · 과업, 질문, 관찰 지표를 설계하고 팀끼리 서로 테스트한 뒤 고칠 순서를 정해요.',
    ['mvp','hypothesis','chrome'])

# ── 마케팅과 콘텐츠
add('benchmarking','벤치마킹','Benchmarking','mkt',[15,16],
    '앞서가는 곳이 어떻게 하는지 보고 배울 점을 찾는 일이에요.',
    'Day 15 가이드 · 경쟁사 광고를 아카이브로 모아요. Day 16 가이드 · P1이 한 걸음 앞선 브랜드 3곳의 벤치마킹 한 장(benchmark.md)을 만들어요.',
    ['archive','winningad','substitute'],
    '앞서 달리는 선수의 경기 영상이에요. 나보다 한 걸음 앞선 선수의 영상을 돌려 봐요.')
add('winningad','승부 소재','Winning creative','mkt',[15],
    '한 브랜드가 오래 틀고, 모양만 바꿔 여러 벌 만드는 광고예요. 그 브랜드가 지금 가장 믿는 카드예요.',
    'Day 15 가이드 · 승부 소재를 뜯어보며 왜 잘 팔리는지 봐요.',
    ['adcreative','benchmarking'],
    '상대 팀의 에이스예요.')
add('adcreative','광고 소재','Ad creative','mkt',[15,16],
    '광고에 쓰는 이미지, 영상, 문구 한 벌이에요.',
    'Day 16 가이드 · P1이 우리가 시험해 볼 소재 가설 3개를 써요.',
    ['winningad','hook','copy'])
add('hook','훅','Hook','mkt',[8,14,16],
    '첫 몇 초나 첫 줄에서 눈길을 붙잡는 장면이나 문장이에요.',
    '일정표 Day 8 · 훅 → 전개 → 전환 → 행동 유도. Day 14 가이드 · 훅 카피. Day 16 가이드 · 인스타그램 시안 3장은 훅을 서로 다르게(문제 공감, 반전, 결과 먼저) 써요.',
    ['storytelling','copy','churn'],
    '낚싯바늘의 미끼예요. 손님이 내리려는 이유에 직접 답하는 문장이 좋은 훅이에요.')
add('copy','카피','Copy','mkt',[14,16],
    '광고나 웹페이지에 들어가는 글이에요. 가장 크게 보이는 한 줄을 "큰 카피"라고 해요.',
    'Day 16 가이드 · 랜딩페이지 칸마다 큰 카피를 쓰고, 이미지 위에 얹을 카피를 따로 써요.',
    ['hook','promise'])
add('cta','CTA(행동 유도)','Call To Action','mkt',[8,16],
    '"지금 사기", "신청하기"처럼 다음 행동을 하게 만드는 문구나 버튼이에요.',
    '일정표 Day 8 · 스토리텔링의 마지막 단계(행동 유도). Day 16 가이드 · 랜딩페이지의 마지막 칸 "지금 사기"(물건을 팔지 않으면 예약, 신청, 방문).',
    ['landing','storytelling'])
add('pdp','상세페이지','Product Detail Page (PDP)','mkt',[15,16],
    '쇼핑몰에서 제품 하나를 자세히 설명하는 웹페이지예요. 사람들이 살지 말지 정하는 곳이에요.',
    'Day 15 가이드 · "구매는 상세페이지에서 일어나요." 광고와 상세페이지를 한 세트로 봐요(pdp_v2.html).',
    ['landing','cvr'])
add('landing','랜딩페이지','Landing page','mkt',[16,17],
    '광고를 누른 사람이 처음 도착하는 웹페이지예요. 상세페이지가 제품 하나를 설명한다면, 랜딩페이지는 행사 하나로 설득해서 구매나 상세페이지로 보내요.',
    'Day 16 가이드 · 위에서 아래로 여덟 칸(문제 → 공감 → 제품 → 근거 → 남의 말 → 쓰는 장면 → 걱정 풀기 → 지금 사기). 파일 이름은 landing.html이에요.',
    ['pdp','firstscreen','promise','cta'],
    '가게 쇼윈도예요. 지나가던 사람이 멈추고, 들어오고, 사게 만드는 한 장이에요.')
add('promo','기획전','Promotion','mkt',[10,13,14,16],
    '한 가지 주제로 상품을 묶어서 파는 행사예요. 예: 여름 한정, 첫 구매 세트.',
    '일정표 Day 10 · 크리에이티브 밸류체인의 한 단계. Day 14 · 기획전 캠페인 기획안. Day 16 가이드 · 물건을 파는 곳이 아니면 "이벤트 페이지"로 읽어요.',
    ['landing','keyvisual'])
add('promise','약속 한 줄','One-line promise','mkt',[16],
    '고객에게 보여 줄 한 문장이에요. 광고와 랜딩페이지의 첫 화면이 똑같이 말해요.',
    'Day 16 가이드 · P4가 후보 5개를 쓰고, 학생이 고르거나 바꿔요(내 결정 2).',
    ['corehypothesis','firstscreen','vpc'])
add('firstscreen','첫 화면','First screen','mkt',[16],
    '폰에서 웹페이지를 열었을 때, 내리지 않고 맨 처음 보이는 맨 위 칸이에요.',
    'Day 16 가이드 · 첫 화면은 제품보다 고객의 짜증 나는 순간 한 장면으로 시작해요(P7).',
    ['landing','keyvisual'])
add('keyvisual','키비주얼','Key visual','mkt',[16],
    '기획전이나 캠페인을 대표하는 이미지 한 장이에요. 광고, SNS, 웹페이지가 이 분위기를 따라가요.',
    'Day 16 가이드 · 랜딩페이지 첫 화면의 장면을 세로로 그려 kv.png로 저장해요.',
    ['firstscreen','draft','imageai'])
add('draft','시안','Draft','mkt',[7,8,14,16],
    '확정하기 전에 보여 주는 밑그림이에요. 여러 개를 보고 하나를 골라요.',
    '일정표 Day 8 · 장면 시안. Day 14 · 핵심 화면 시안. Day 16 가이드 · 인스타그램 시안 3장.',
    ['keyvisual','moodboard','claudedesign'])
add('moodboard','무드보드','Mood board','mkt',[7],
    '원하는 분위기의 사진, 색, 글꼴을 한 판에 모아 놓은 것이에요. 말로 설명하기 어려운 느낌을 맞출 때 써요.',
    '일정표 Day 7 · 캐릭터 외형을 고정하고 무드보드를 만들어요.',
    ['draft','keyvisual'])
add('shortform','숏폼과 티저','Short-form / teaser','mkt',[8,17],
    '숏폼은 1분 안팎의 세로 영상(릴스, 쇼츠, 틱톡)이에요. 티저는 본편이나 출시 전에 궁금하게 만드는 짧은 예고예요.',
    '일정표 Day 8 · 채널별 이야기 구성. Day 17 · 15초 숏폼 티저(Google Flow, Kling).',
    ['videoai','storyboard'])
add('cardnews','카드뉴스','Card news','mkt',[8],
    '여러 장의 이미지에 짧은 글을 얹어 옆으로 넘겨 보게 만든 콘텐츠예요.',
    '일정표 Day 8 · 채널별 이야기 구성의 한 형식.',
    ['storytelling'])
add('ctr','클릭률(CTR)','Click-Through Rate','mkt',[15],
    '광고나 링크를 본 사람 가운데 누른 사람의 비율이에요.',
    'Day 15 가이드 · 매출 공식의 한 조각.',
    ['cvr','revenueformula','kpi'],
    '가게 앞을 지나간 사람 가운데 들어온 사람의 비율이에요.')
add('cvr','구매 전환율','Conversion Rate','mkt',[15],
    '페이지에 들어온 사람 가운데 실제로 산(신청한) 사람의 비율이에요.',
    '일정표 Day 15 · 단위 경제성. Day 15 가이드 · 매출 공식의 한 조각.',
    ['ctr','pdp','landing'],
    '가게에 들어온 사람 가운데 물건을 산 사람의 비율이에요.')
add('metaadlib','메타 광고 라이브러리','Meta Ad Library','mkt',[15,16],
    '페이스북과 인스타그램에서 지금 집행 중인 광고를 누구나 찾아볼 수 있게 모아 둔 곳이에요.',
    'Day 15 가이드 · 경쟁사 광고 아카이빙. Day 16 가이드 · 먼저 끝난 사람은 실제 광고 3개를 찾아 benchmark.md에 넣어요.',
    ['snipit','archive'])
add('snipit','스니핏','Snipit','mkt',[15,16],
    '광고를 검색하고 저장해서 벤치마킹에 쓰는 AI 서비스예요.',
    'Day 15 가이드 · 광고 아카이빙에 쓰는 사이트로 나와요. Day 16 가이드 · 먼저 끝난 사람이 실제 광고를 찾을 때 써요.',
    ['metaadlib','benchmarking'])
add('aeo','AEO와 GEO','Answer / Generative Engine Optimization','mkt',[14,21],
    'ChatGPT나 검색 AI가 답할 때 내 글을 인용하게 만드는 글쓰기예요. 질문에 바로 답하는 문단, 질문과 답 단위로 써요.',
    '일정표 Day 14 · 크리에이티브 트랙의 콘텐츠 기획안. Day 21 · AEO 구조로 트렌드 리포트를 써요.',
    ['report'])

# ── AI 기본
add('genai','생성형 AI','Generative AI','ai',[12],
    '글, 이미지, 영상, 코드를 새로 만들어 내는 AI예요.',
    '일정표 Day 12 · AI 역량 다섯 가지(생성, 예측, 추천, 자동화, 에이전트) 가운데 하나.',
    ['llm','agent'])
add('llm','LLM(대규모 언어 모델)','Large Language Model','ai',[19],
    '아주 많은 글을 학습해서, 다음에 올 말을 예측하며 글을 만드는 AI 모델이에요. Claude, ChatGPT, Gemini가 LLM이에요.',
    '일정표 Day 19 · LLM의 원리(토큰, 컨텍스트, 확률적 생성)와 2026년 모델 지형.',
    ['token','context','model'])
add('model','AI 모델','AI model','ai',[19],
    'AI가 일을 하는 두뇌에 해당하는 프로그램이에요. 같은 회사에도 빠른 모델과, 답하기 전에 더 깊게 생각하는 추론 모델이 따로 있어요.',
    '일정표 Day 19 · 같은 과제를 Claude, ChatGPT, Gemini로 블라인드 비교하고, 작업마다 맞는 모델을 골라요.',
    ['llm','blindtest'])
add('token','토큰','Token','ai',[19],
    'AI가 글을 읽고 쓰는 단위예요. 낱말보다 작은 조각이에요. 사용량과 한도도 토큰으로 계산해요.',
    '일정표 Day 19 · LLM 원리에서 나와요.',
    ['llm','context'])
add('context','컨텍스트','Context','ai',[19,20],
    'AI가 지금 답할 때 참고하는 모든 내용이에요. 내 지시, 지금까지의 대화, 읽은 파일이 다 들어가요. 한 번에 담을 수 있는 양에 한계가 있어요.',
    '일정표 Day 19 · 긴 대화에서 성능이 떨어지는 이유. Day 20 · 컨텍스트 엔지니어링.',
    ['contextdecay','contexteng','token'])
add('contextdecay','컨텍스트 열화와 새 대화','Context degradation','ai',[16,19],
    '대화가 길어질수록 AI가 앞의 내용을 놓치거나 흐려지는 것이에요. 그래서 일이 크게 바뀔 때는 새 대화를 열어요.',
    '일정표 Day 19 · 컨텍스트 열화와 세션 관리. Day 16 가이드 · 작업 폴더를 열고 새 대화로 시작해요.',
    ['context','claudemd'])
add('contexteng','컨텍스트 엔지니어링','Context engineering','ai',[20],
    '프롬프트 한 줄을 잘 쓰는 것을 넘어, AI가 일할 때 볼 규칙과 자료(CLAUDE.md, 스킬, 파일)를 미리 갖춰 두는 일이에요.',
    '일정표 Day 20 · CLAUDE.md와 스킬 설계.',
    ['prompt','claudemd','skill'],
    '신입에게 매번 말로 설명하는 대신, 업무 매뉴얼과 자료철을 책상에 놓아 주는 것이에요.')
add('prompt','프롬프트','Prompt','ai',[14,20],
    'AI에게 보내는 지시문이에요.',
    'Day 14 가이드 · 프롬프트와 스킬의 차이. 일정표 Day 20 · 기본 구조(역할, 맥락, 과업, 제약, 출력 형식, 예시).',
    ['contexteng','skill','remote'],
    '식당에서 하는 주문 한 번이에요. 대화가 끝나면 사라져요. 스킬은 파일로 남아요.')
add('structuredoutput','구조화 출력과 JSON','Structured output / JSON','ai',[20],
    'AI의 답을 표나 JSON처럼 정해진 모양으로 받는 것이에요. JSON은 "이름: 값"을 짝지어 적는 데이터 형식이에요.',
    '일정표 Day 20 · 데이터·서비스 트랙은 상품 정보를 JSON으로 바꾸는 스킬을 만들어요.',
    ['csv','api'])
add('hallucination','할루시네이션','Hallucination','ai',[2,15,16],
    'AI가 사실이 아닌 내용을 그럴듯하게 지어내는 것이에요. 없는 숫자, 없는 후기, 없는 출처를 만들어 낼 수 있어요.',
    '일정표 Day 2 · 출처와 할루시네이션 점검. Day 15 · AI 리서치 숫자 검증법. Day 16 가이드 · 추측한 곳은 (가정), 지어내면 안 되는 곳은 [채울 곳]으로 남겨요.',
    ['crosscheck','assume','fillin'])
add('agent','AI 에이전트','AI agent','ai',[2,12],
    '목표를 주면 스스로 계획을 세우고, 검색, 파일, 프로그램 같은 도구를 써서 여러 단계의 일을 끝내는 AI예요. 챗봇은 대답하고, 에이전트는 일을 해요.',
    '일정표 Day 2 · 검색형 AI와 에이전트형 리서치의 차이. Day 12 · 실제 업무 하나를 에이전트에게 맡기는 라이브 데모.',
    ['subagent','claudecode','dxax'])
add('humanloop','사람 검토','Human in the loop','ai',[12,16],
    'AI가 만든 결과를 사람이 확인하고 고치는 단계를 일 안에 넣는 것이에요.',
    '일정표 Day 12 · 2026년 AX의 흐름. Day 16 가이드 · 초안은 Claude가 만들고, 결정은 내가 해요(내 결정 1~4).',
    ['mydecision','agent'])
add('airisk','AI 리스크','AI risks','ai',[12,19],
    'AI를 쓸 때 조심할 위험이에요. 개인정보 유출, 저작권 침해, 편향된 결과, 잘못됐을 때 누가 책임지는지가 대표적이에요.',
    '일정표 Day 12 · AI 도입 리스크. Day 19 · AI 결과물의 저작권, 개인정보, 상표.',
    ['copyright','hallucination'])
add('api','API','Application Programming Interface','ai',[3,19],
    '프로그램끼리 정해진 방식으로 데이터를 주고받는 창구예요.',
    '일정표 Day 3 · 공공데이터셋 구조(CSV, API). Day 19 · API로 모델을 부르는 구조.',
    ['dataspec','structuredoutput'],
    '식당의 주문 창구예요. 주방에 들어가지 않아도 정해진 방식으로 주문하면 음식이 나와요.')
add('blindtest','블라인드 비교','Blind comparison','ai',[19],
    '누가 만든 결과인지 가리고, 결과만 보고 비교하는 방법이에요. 이름 때문에 생기는 선입견을 줄여요.',
    '일정표 Day 19 · 같은 과제를 세 모델로 블라인드 비교해 평가 기준표를 만들어요.',
    ['model'])

# ── Claude와 도구
add('claude','Claude','Claude','tools',[1],
    'Anthropic이 만든 AI예요. 대화하며 글쓰기, 분석, 코딩, 자료 정리를 도와요.',
    '일정표 Day 1 · 학습 목표와 자기소개 문장을 다듬어요.',
    ['claudecode','llm'])
add('claudecode','Claude Code','Claude Code','tools',[2],
    '내 컴퓨터의 작업 폴더 안에서 파일을 읽고, 만들고, 고치며 일하는 Claude예요. 데스크톱 앱의 Code 탭이나 웹(claude.ai/code)에서 써요.',
    '일정표 Day 2 · 설치와 첫 실행, 리서치 결과를 "파일"로 쌓는 습관. 그 뒤 거의 모든 실습에서 써요.',
    ['claudemd','skill','subagent','planmode'])
add('claudemd','CLAUDE.md','CLAUDE.md','tools',[2,16,20],
    '작업 폴더에 두는 규칙 파일이에요. Claude가 그 폴더에서 일할 때마다 먼저 읽어요.',
    '일정표 Day 2 · 나는 누구, 목표, 선호를 적어요. Day 16 가이드 · P0이 오늘의 작업 규칙을 심어요. Day 20 · 팀 CLAUDE.md.',
    ['skill','contexteng'],
    '사무실 벽에 붙여 둔 업무 규칙표예요. 들어올 때마다 보고 일해요.')
add('skill','스킬(SKILL.md)','Skill','tools',[4,7,14,16,20],
    'Claude가 특정 일을 하는 방법을 적어 둔 파일(SKILL.md)이에요. 작업 폴더의 .claude/skills 안에 넣어 두면 그 일을 할 때 꺼내 써요. 남이 만들어 공개한 "공개 스킬"을 받아 쓸 수도 있어요.',
    '일정표 Day 4 · /dataviz 스킬 시연. Day 7 · 브랜드 스킬 파일. Day 14 가이드 · 퍼소나·고객 여정 지도 스킬. Day 16 가이드 · 공개 디자인 스킬 frontend-design. Day 20 · 스킬 만들기와 공개 스킬 설치.',
    ['claudemd','contexteng','prompt'],
    'Day 14 가이드는 "레시피 카드"로, Day 16 가이드는 "선배의 체크리스트"로 설명했어요. 한 번 써 두면 매번 설명하지 않아도 돼요.')
add('subagent','서브에이전트','Subagent','tools',[3,9,13,21],
    '메인 Claude가 일을 나눠 맡기는 보조 에이전트예요. 여러 개를 동시에 돌려 나란히 조사할 수 있어요. 여러 에이전트가 함께 일하는 방식을 멀티에이전트라고 해요.',
    '일정표 Day 3 · 병렬 리서치 시연. Day 9 · 기업별 병렬 리서치. Day 13 · 레드팀 서브에이전트. Day 21 · 리포트 자동화.',
    ['agent','redteam','report'],
    '팀장이 조사할 회사를 팀원 셋에게 나눠 주고, 보고를 모아 한 장으로 합치는 것이에요.')
add('chrome','Claude in Chrome','Claude in Chrome','tools',[3,4,5,9,17,21],
    '크롬 브라우저에서 Claude가 웹페이지를 직접 열고, 읽고, 누르며 일하게 해 주는 확장 프로그램이에요.',
    '일정표 Day 3 · 공공 사이트 탐색. Day 17 · 사용 흐름 자동 점검. Day 21 · 웹 수집.',
    ['claudecode','usertest'])
add('claudedesign','Claude Design','Claude Design','tools',[7,8,14,16],
    'Claude와 대화하면서 화면 시안과 움직이는 프로토타입을 만드는 도구예요. 만든 시안을 Claude Code로 넘길 수 있어요.',
    '일정표 Day 7 · 첫 사용 시연. Day 14 · 핵심 화면 시안. Day 16 · 시안을 Claude Code로 넘기기(핸드오프).',
    ['handoff','prototype','draft'])
add('handoff','핸드오프','Handoff','tools',[16],
    '만든 것을 다음 사람이나 다음 도구에 넘겨주는 일이에요.',
    '일정표 Day 16 · Claude Design 시안을 Claude Code로 넘겨 동작하는 프로토타입을 만들어요.',
    ['claudedesign','planmode'])
add('planmode','계획 모드','Plan mode','tools',[16],
    'Claude Code가 바로 만들지 않고, 먼저 계획을 보여 준 뒤 내가 승인하면 만드는 모드예요.',
    '일정표 Day 16 · 디자인 넘기기 → 계획 확인 → 구현. Day 16 가이드 · 같은 흐름을 P5(계획)와 P6(만들기)로 해요.',
    ['handoff','claudecode'],
    '공사 전 도면 확인이에요. 벽을 세운 뒤에 고치면 비싸요. 도면에서 고치면 한 줄이에요.')
add('artifact','아티팩트','Artifact','tools',[16],
    'Claude가 만든 결과물을 링크로 열어 볼 수 있게 올린 페이지예요. 처음에는 나만 볼 수 있고, 공유 설정을 바꿔야 남이 열 수 있어요.',
    'Day 16 가이드 · "화면을 링크로 만들기" 한 줄로 landing.html을 링크로 만들어 실습시트에 적어요.',
    ['deploy'])
add('permission','허락 창','Permission prompt','tools',[16],
    'Claude Code가 파일을 만들거나 웹을 검색하기 전에 "실행해도 될까요?"라고 묻는 창이에요. 되묻는 게 아니라 허락을 구하는 거예요.',
    'Day 16 가이드 · 파일 만들기, 웹 검색, 내려받기, 폴더 열기는 Yes. 무엇을 지우겠다고 하면 누르지 말고 강사를 불러요.',
    ['claudecode'])
add('schedule','예약 작업','Scheduled task','tools',[21],
    '정해 둔 시간마다 Claude가 같은 일을 자동으로 하도록 걸어 두는 기능이에요.',
    '일정표 Day 21 · 리포트 스킬과 예약 작업으로 주간 리포트를 자동 발행해요.',
    ['report','skill'])
add('report','인터랙티브 HTML 리포트','Interactive report','tools',[21],
    '문서 파일 대신, 스크롤하며 읽고 차트를 눌러 볼 수 있는 웹페이지 형태의 리포트예요.',
    '일정표 Day 21 · 질문 설계 → 병렬 조사 → 근거 정리 → 리포트 순서로 산업 리포트를 발행해요.',
    ['subagent','schedule','aeo'])
add('github','GitHub와 저장소','GitHub / repository','tools',[2,16,20],
    '코드와 파일을 저장하고, 바뀐 기록을 남기며 함께 작업하는 곳이에요. 저장소(repository)는 프로젝트 하나의 보관함이에요.',
    '일정표 Day 2 · GitHub 계정과 팀 저장소. Day 20 · 스킬 저장소.',
    ['deploy'])
add('deploy','배포와 Vercel','Deploy','tools',[17,18],
    '만든 웹페이지를 인터넷 주소(URL)로 올려 누구나 열 수 있게 하는 일이에요. Vercel, Netlify는 그 일을 해 주는 서비스예요.',
    '일정표 Day 18 · HTML 피치덱을 URL로 배포해요(Vercel).',
    ['artifact','github','html'])
add('html','HTML','HyperText Markup Language','tools',[14,16],
    '웹페이지를 만드는 언어이자 파일 형식(.html)이에요.',
    'Day 14 가이드에서 처음 설명했어요. Day 16 가이드 · landing.html, prototype.html.',
    ['markdown','deploy'],
    '웹용 PPT 파일이에요. 더블클릭하면 크롬으로 열려요. 코드를 몰라도 돼요.')
add('markdown','마크다운(.md)','Markdown','tools',[14,16],
    '"# 제목", "- 목록"처럼 간단한 기호로 쓰는 글 파일 형식이에요. Claude가 글 결과를 .md 파일로 저장해요.',
    'Day 16 가이드 · benchmark.md, mvp.md. 글 파일을 보려면 리모컨 "파일 내용 보기"를 보내요.',
    ['html','remote'])
add('xlsx','수식이 살아 있는 시트','Live-formula spreadsheet','tools',[15],
    '숫자를 바꾸면 결과가 다시 계산되도록 수식이 들어 있는 엑셀(xlsx)이나 구글 시트예요.',
    '일정표 Day 15 · 시장 규모와 수익성 시뮬레이션을 수식이 살아 있는 xlsx로 만들어요.',
    ['uniteconomics','tamsamsom'])
add('mermaid','Mermaid','Mermaid','tools',[10],
    '글로 적으면 흐름도 같은 다이어그램으로 그려 주는 표기법이에요.',
    '일정표 Day 10 · 밸류체인을 Mermaid나 HTML 다이어그램으로 만들어요.',
    ['valuechain'])
add('figjam','FigJam','FigJam','tools',[7,10],
    '여러 사람이 붙임쪽지를 붙이며 함께 생각을 펼치는 온라인 화이트보드예요. 피그마에서 만들었어요.',
    '일정표 Day 7 · 팀 발산 보드. Day 10 · 팀 토론 보드.',
    ['valuechain'])
add('imageai','ChatGPT 이미지 생성','Image generation','tools',[7,8,16],
    '글로 장면을 설명하면 그림을 만들어 주는 ChatGPT의 기능이에요.',
    '일정표 Day 7 · 캐릭터 기준 이미지. Day 16 · 키비주얼과 SNS 시안. Day 16 가이드에서는 "GPT 에듀"의 이미지 만들기라고 불러요.',
    ['keyvisual','videoai'])
add('videoai','영상 AI(Kling, Google Flow)','Video generation','tools',[7,8,17],
    '글이나 이미지를 넣으면 짧은 영상을 만들어 주는 AI 서비스예요. Kling이 있고, 구글의 영상 모델 Veo를 쓰는 Google Flow가 있어요.',
    '일정표 Day 8 · 카메라 무빙 테스트(Kling). Day 17 · 15초 숏폼 티저(Google Flow, Kling). 무료 크레딧 안에서 써요.',
    ['shortform','credit'])
add('credit','크레딧','Credit','tools',[7,17],
    'AI 서비스를 쓸 때마다 빠지는 사용권이에요. 무료 계정은 쓸 수 있는 크레딧이 정해져 있어요.',
    '일정표 Day 7 · Kling 무료 계정과 크레딧 확인. Day 17 · 무료 영상 AI 크레딧 계획.',
    ['videoai'])
add('notebooklm','NotebookLM','NotebookLM','tools',[18],
    '내가 올린 자료를 바탕으로 답하고 요약하는 구글의 AI 노트예요. 자료를 대화하듯 들려주는 "오디오 오버뷰" 기능이 있어요.',
    '일정표 Day 18 · 오디오 오버뷰로 발표 리허설을 해요.',
    ['pitching'])
add('chartjs','Chart.js','Chart.js','tools',[18],
    '웹페이지에 움직이는 차트를 그려 주는 도구(라이브러리)예요.',
    '일정표 Day 18 · 데이터·서비스 트랙이 라이브 차트로 숫자를 보여 줘요.',
    ['pitchdeck'])

# ── 가이드 표시
add('assume','(가정)','Assumption mark','marks',[14,15,16],
    'Claude가 확인하지 못하고 추측한 곳에 붙이는 표시예요. 내가 확인해요.',
    'Day 16 가이드 · (가정) 표시 한 곳을 공식몰이나 인스타그램에서 확인해요(내 결정 1).',
    ['fillin','hallucination'])
add('fillin','[채울 곳]과 [실데이터 입력]','Fill-in mark','marks',[14,16],
    'Claude가 지어내면 안 돼서 비워 둔 자리예요. 가격, 성분, 후기 같은 진짜 값을 내가 넣어요. Day 14 가이드의 [실데이터 입력]과 같은 뜻이에요.',
    'Day 16 가이드 · 랜딩페이지의 가격, 성분, 후기 자리.',
    ['assume','hallucination'])
add('remote','리모컨','Remote lines','marks',[16],
    'Claude가 마음에 안 들게 움직일 때, 긴 설명 대신 보내는 한 줄 프롬프트예요.',
    'Day 16 가이드 · 일곱 개: 되물을 때, 말이 길 때, 자료가 없다고 멈췄을 때, 한 단계 더 깊게, 장면으로 다시, 파일 내용 보기, 광고 규정 점검.',
    ['prompt'])
add('mydecision','내 결정','My decision','marks',[16],
    '가이드에서 Claude 대신 내가 판단하는 자리예요. 확인하기, 고르기, 고칠지 정하기, 다시 시킬지 정하기.',
    'Day 16 가이드 · 결정을 Claude에게 한 줄로 말해 두면 저녁의 포트폴리오 한 장에 남아요.',
    ['humanloop','portfolio'])
add('must','(꼭)','Required mark','marks',[16],
    '꼭 하는 프롬프트에 붙인 표시예요. (꼭)만 끝내도 그날은 통과예요.',
    'Day 16 가이드 · P0 → W1 → P1 → P3 → P5 → P6 → P10 → W2.',
    ['remote'])
add('bluetext','파란 글자와 입력 칸','Blue text','marks',[15,16],
    '프롬프트 안의 파란 글자는 페이지의 입력 칸에 적은 대로 바뀌는 자리예요. 내 브랜드로 바꿔서 쓸 수 있어요.',
    'Day 15·16 가이드 · 브랜드, 제품, 고객, 하고 싶은 일.',
    ['prompt'])

# ── 점검: 아이디 중복, 함께 보기 대상
ids=[x['id'] for x in E]
assert len(ids)==len(set(ids)), [i for i in ids if ids.count(i)>1]
for x in E:
    for r in x['r']:
        assert r in ids, (x['id'], r)
    assert re.fullmatch(r'[a-z0-9-]+', x['id']), x['id']
    assert all(1<=d<=21 for d in x['days']), x['id']
names={x['id']:x['t'] for x in E}

esc=html.escape
def day_label(days):
    return 'Day ' + ' · '.join(str(d) for d in days)

cat_count={k:0 for k,_ in CATS}
for x in E: cat_count[x['cat']]+=1

sections=[]
for key,label in CATS:
    items=[x for x in E if x['cat']==key]
    items.sort(key=lambda x:(x['days'][0], x['t']))
    arts=[]
    for x in items:
        up = x['days'][0] >= UPCOMING_FROM
        text=' '.join([x['t'],x['en'],x['d'],x['e'],x['c']]).lower()
        rel=' '.join('<a href="#%s">%s</a>'%(r,esc(names[r])) for r in x['r'])
        arts.append(
            '<article class="entry" id="%s" data-cat="%s" data-days="%s" data-t="%s" data-en="%s" data-text="%s">'
            '<div class="head"><h3>%s</h3><span class="en">%s</span></div>'
            '<p class="def">%s</p>%s'
            '<p class="cls"><b>수업에서</b> %s</p>'
            '<div class="meta"><span class="day">%s</span>%s%s</div></article>' % (
            x['id'], x['cat'], ' '.join(map(str,x['days'])), esc(x['t'].lower(), quote=True), esc(x['en'].lower(), quote=True), esc(text, quote=True),
            esc(x['t']), esc(x['en']), esc(x['d']),
            ('<p class="easy"><b>쉽게 말하면</b> %s</p>'%esc(x['e'])) if x['e'] else '',
            esc(x['c']), esc(day_label(x['days'])),
            '<span class="soon">예정</span>' if up else '',
            ('<span class="rel">함께 보기 %s</span>'%rel) if rel else ''))
    sections.append('<section class="cat" data-cat="%s"><h2>%s <span class="n">%d</span></h2>%s</section>'%(key,esc(label),len(items),'\n'.join(arts)))

chips=['<button type="button" class="chip" data-cat="all" aria-pressed="true">전체 <span>%d</span></button>'%len(E)]
for key,label in CATS:
    chips.append('<button type="button" class="chip" data-cat="%s" aria-pressed="false">%s <span>%d</span></button>'%(key,esc(label),cat_count[key]))
opts=['<option value="all">모든 날</option>']
for d,(date,name) in DAYS.items():
    opts.append('<option value="%d">Day %d · %s %s%s</option>'%(d,d,date,esc(name),' (예정)' if d>=UPCOMING_FROM else ''))

CSS='''
/* 레이아웃: 위에 찾기 막대(검색, 분류, 날짜)를 붙여 두고, 분류별로 사전 항목이 이어지는 한 줄 목록 */
:root{--bg:#f2f4f6;--card:#ffffff;--ink:#191f28;--sub:#6b7684;--blue:#3182f6;--blue-ink:#ffffff;--blue-soft:#e8f3ff;--line:#e5e8eb;--warn:#b26b00;--warn-soft:#fff6e0;--hit:#fff3c4;
--ui:'Noto Sans KR',-apple-system,BlinkMacSystemFont,'Apple SD Gothic Neo','Malgun Gothic',sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17171c;--card:#202027;--ink:#f2f4f6;--sub:#a1a9b4;--blue:#4593fc;--blue-ink:#0b1220;--blue-soft:#1c2b42;--line:#2e2e36;--warn:#f5b73b;--warn-soft:#352b14;--hit:#3a3214;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#17171c;--card:#202027;--ink:#f2f4f6;--sub:#a1a9b4;--blue:#4593fc;--blue-ink:#0b1220;--blue-soft:#1c2b42;--line:#2e2e36;--warn:#f5b73b;--warn-soft:#352b14;--hit:#3a3214;color-scheme:dark}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{background:var(--bg);color:var(--ink);font-family:var(--ui);font-size:19px;line-height:1.65;word-break:keep-all;overflow-wrap:break-word;padding-block:0 96px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);background:var(--bg);z-index:30}
.wrap{max-width:860px;margin:0 auto}
header.top{padding:48px 0 8px}
.eyebrow{display:inline-block;color:var(--blue);background:var(--blue-soft);font-weight:800;font-size:16px;border-radius:10px;padding:5px 12px}
h1{font-size:clamp(34px,6vw,54px);line-height:1.25;font-weight:800;letter-spacing:-0.03em;margin:16px 0 10px;text-wrap:balance}
.lead{font-size:clamp(19px,2.6vw,23px);color:var(--sub);margin:0 0 12px}
.note{font-size:16px;color:var(--sub);margin:0}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--bg);padding:14px 0 10px;display:grid;gap:10px}
.find{display:flex;gap:8px;align-items:center}
.find input{flex:1;min-width:0;font:inherit;font-size:20px;padding:14px 18px;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink)}
.find input:focus{outline:none;border-color:var(--blue)}
.find select{font:inherit;font-size:16px;padding:14px 12px;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);max-width:46%}
.chips{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
.chips::-webkit-scrollbar{display:none}
.chip{flex:none;font:inherit;font-size:16px;font-weight:700;padding:8px 14px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--sub);cursor:pointer}
.chip span{font-weight:500;margin-left:2px;font-variant-numeric:tabular-nums}
.chip[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.status{display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:16px;color:var(--sub);min-height:24px}
.status button{font:inherit;font-size:16px;color:var(--blue);background:none;border:0;padding:4px 0;cursor:pointer}
.today{font:inherit;font-size:16px;font-weight:700;color:var(--blue);background:var(--blue-soft);border:0;border-radius:12px;padding:8px 14px;cursor:pointer}
section.cat,#results{padding-top:28px}
section.cat h2,#results h2{font-size:clamp(24px,3.6vw,30px);font-weight:800;margin:0 0 12px;scroll-margin-top:170px}
section.cat h2 .n{font-size:18px;color:var(--sub);font-weight:600;font-variant-numeric:tabular-nums}
.entry{background:var(--card);border-radius:20px;padding:22px 24px;margin:0 0 12px;scroll-margin-top:180px;transition:background .3s}
.entry.hit{background:var(--hit)}
.entry .head{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;margin-bottom:6px}
.entry h3{font-size:clamp(22px,3vw,26px);font-weight:800;margin:0;line-height:1.35}
.entry .en{font-size:16px;color:var(--sub)}
.entry p{margin:0 0 8px}
.entry .def{font-weight:600}
.entry .easy b,.entry .cls b{display:inline-block;font-size:15px;font-weight:800;color:var(--blue);margin-right:6px}
.entry .cls{color:var(--sub)}
.entry .cls b{color:var(--sub)}
.meta{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:center;font-size:15px;margin-top:10px;padding-top:10px;border-top:1px solid var(--line)}
.meta .day{font-weight:800;color:var(--ink);font-variant-numeric:tabular-nums}
.meta .soon{font-weight:800;color:var(--warn);background:var(--warn-soft);border-radius:8px;padding:1px 8px}
.meta .rel{color:var(--sub)}
.meta .rel a{color:var(--blue);text-decoration:none;font-weight:700;margin-right:8px;white-space:nowrap}
.meta .rel a:hover{text-decoration:underline}
.empty{background:var(--card);border-radius:20px;padding:28px;text-align:center;color:var(--sub);margin-top:20px}
a:focus-visible,button:focus-visible,select:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
footer{margin-top:40px;font-size:15px;color:var(--sub)}
@media (max-width:520px){.find{flex-wrap:wrap}.find select{max-width:100%;width:100%}}
'''

JS=r'''
(function(){
  var q=document.getElementById('q'), day=document.getElementById('day');
  var chips=[].slice.call(document.querySelectorAll('.chip'));
  var entries=[].slice.call(document.querySelectorAll('.entry'));
  var cats=[].slice.call(document.querySelectorAll('section.cat'));
  var results=document.getElementById('results');
  var count=document.getElementById('count'), reset=document.getElementById('reset'), empty=document.getElementById('empty');
  var homes={}; cats.forEach(function(s){ homes[s.dataset.cat]=s; });
  entries.forEach(function(e,i){ e.dataset.idx=i; });
  var cat='all', moved=false;
  function norm(t){ return (t||'').toLowerCase().replace(/\s+/g,''); }
  function passes(e,d){ return (cat==='all'||e.dataset.cat===cat)&&(d==='all'||(' '+e.dataset.days+' ').indexOf(' '+d+' ')>-1); }
  function score(e,t){
    var h=norm(e.dataset.t), en=norm(e.dataset.en);
    if(h===t) return 100;
    if(h.indexOf(t)===0) return 80;
    if(h.indexOf(t)>-1) return 60;
    if(en.indexOf(t)>-1) return 40;
    if(norm(e.dataset.text).indexOf(t)>-1) return 10;
    return 0;
  }
  function goHome(){
    if(!moved) return;
    entries.slice().sort(function(a,b){ return a.dataset.idx-b.dataset.idx; }).forEach(function(e){ homes[e.dataset.cat].appendChild(e); });
    moved=false;
  }
  function apply(){
    var t=norm(q.value), d=day.value, shown=0;
    if(t){
      var hits=entries.map(function(e){ return {e:e, s:passes(e,d)?score(e,t):0}; }).filter(function(x){ return x.s>0; });
      hits.sort(function(a,b){ return b.s-a.s || a.e.dataset.idx-b.e.dataset.idx; });
      entries.forEach(function(e){ e.hidden=true; });
      hits.forEach(function(x){ x.e.hidden=false; results.appendChild(x.e); });
      moved=true; shown=hits.length;
      results.hidden=shown===0; cats.forEach(function(s){ s.hidden=true; });
    } else {
      goHome(); results.hidden=true;
      entries.forEach(function(e){ var ok=passes(e,d); e.hidden=!ok; if(ok) shown++; });
      cats.forEach(function(s){
        var n=s.querySelectorAll('.entry:not([hidden])').length;
        s.hidden=n===0; s.querySelector('.n').textContent=n;
      });
    }
    var filtered=t||d!=='all'||cat!=='all';
    count.textContent=filtered?(shown+'개 찾았어요'):('모두 '+entries.length+'개');
    reset.hidden=!filtered; empty.hidden=shown>0;
  }
  function setCat(c){ cat=c; chips.forEach(function(b){ b.setAttribute('aria-pressed', String(b.dataset.cat===c)); }); apply(); }
  function clearAll(){ q.value=''; day.value='all'; setCat('all'); }
  chips.forEach(function(b){ b.addEventListener('click', function(){ setCat(b.dataset.cat); }); });
  q.addEventListener('input', apply); day.addEventListener('change', apply);
  reset.addEventListener('click', function(){ clearAll(); q.focus(); });
  document.getElementById('today').addEventListener('click', function(){ q.value=''; setCat('all'); day.value='16'; apply(); });
  function show(id){
    var el=document.getElementById(id); if(!el||!el.classList.contains('entry')) return;
    if(el.hidden) clearAll();
    try{ el.scrollIntoView({block:'start',behavior:'instant'}); }catch(e){ el.scrollIntoView(true); }
    el.classList.add('hit'); setTimeout(function(){ el.classList.remove('hit'); }, 1600);
  }
  document.addEventListener('click', function(ev){
    var a=ev.target.closest('a[href^="#"]'); if(!a) return;
    var id=a.getAttribute('href').slice(1); var el=document.getElementById(id);
    if(el&&el.classList.contains('entry')){ ev.preventDefault(); history.replaceState(null,'','#'+id); show(id); }
  });
  window.addEventListener('hashchange', function(){ show(location.hash.slice(1)); });
  apply();
  if(location.hash){
    var h=location.hash.slice(1); show(h);
    if(document.fonts&&document.fonts.ready){ document.fonts.ready.then(function(){ show(h); }); }
    window.addEventListener('load', function(){ show(h); });
  }
})();
'''

page='''<meta name="claude:viewport-fit-sides" content="cover">
<title>AX 수업 용어 사전</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap">
<style>%s</style>
<div class="wrap">
<header class="top">
<span class="eyebrow">Day 1–21 · 52일 과정</span>
<h1>AX 수업 용어 사전</h1>
<p class="lead">Day 1부터 Day 21까지 수업에 나오는 말 %d개를 모았어요. 모르는 말은 검색창에 쳐 보세요.</p>
<p class="note">Day는 그 말이 공식 일정표나 수업 가이드에 나온 날이에요. 실제 수업 순서와 다를 수 있어요. "예정"은 아직 하지 않은 날이에요.</p>
</header>
<div class="bar">
<div class="find"><label for="q" class="sr">말 찾기</label><input id="q" type="search" placeholder="예: MVP, 페르소나, 스킬" autocomplete="off"><label for="day" class="sr">날짜</label><select id="day">%s</select></div>
<div class="chips" role="group" aria-label="분류">%s</div>
<div class="status"><span id="count"></span><span><button type="button" class="today" id="today">Day 16에 나오는 말</button> <button type="button" id="reset" hidden>처음으로</button></span></div>
</div>
<main>
<section id="results" hidden><h2>찾은 말</h2></section>
%s
<p class="empty" id="empty" hidden>찾는 말이 없어요. 다른 말로 쳐 보거나 "처음으로"를 눌러요.</p>
</main>
<footer>뜻은 쉬운 말로 옮긴 일반적인 정의예요. "수업에서"는 공식 일정표와 Day 14~16 수업 가이드에 적힌 내용이에요.</footer>
</div>
<script>%s</script>
''' % (CSS.replace('.status{','.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}\n.status{',1), len(E), '\n'.join(opts), '\n'.join(chips), '\n'.join(sections), JS)

open(OUT,'w',encoding='utf-8').write(page)
print('entries',len(E),'bytes',len(page.encode('utf-8')))
for k,_ in CATS: print(k,cat_count[k])
