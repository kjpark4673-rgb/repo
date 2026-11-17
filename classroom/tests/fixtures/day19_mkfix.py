# Day 18을 끝낸 학생 폴더를 흉내 낸 시험 출발점 (시험용 가짜 자료)
import os, sys
def write(d, name, text, bom=False):
    p = os.path.join(d, name); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8-sig' if bom else 'utf-8').write(text)
FIX = {
 'mk': dict(role='콘텐츠 마케터', brand='라라스윗', product='저당 아이스크림', cust='다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인', pick='광고 소재 리서치',
   csv='조사일,브랜드,광고 문구,형식,게재 시작일,출처\n2026-11-16,라라스윗,"밤 10시, 죄책감 없이 한 컵",릴스,2026-11-02,https://www.facebook.com/ads/library\n2026-11-16,요아정,"요거트 아이스크림, 토핑은 내 맘대로",이미지,2026-10-28,https://www.facebook.com/ads/library\n2026-11-16,널담,"당 0g 쫀득 디저트",릴스,못 찾음,https://www.instagram.com\n2026-11-16,랩노쉬,"단백질 20g 한 끼",이미지,2026-11-05,https://www.facebook.com/ads/library\n'),
 'md': dict(role='MD (온라인 영업)', brand='아비브', product='약산성 어성초 클렌저', cust='민감성 피부로 고민하는 2030 여성', pick='경쟁사 가격·증정품 프로모션 조사',
   csv='조사일,브랜드,제품,판매처,용량(ml),판매가(원),100ml당(원),증정품·프로모션,출처\n2026-11-16,아비브,어성초 클렌저,올리브영,200,18000,9000,"1+1 기획, 미니 토너 증정",https://www.oliveyoung.co.kr\n2026-11-16,라운드랩,독도 클렌저,올리브영,200,15000,7500,미니 크림 증정,https://www.oliveyoung.co.kr\n2026-11-16,토리든,다이브인 클렌저,쿠팡,150,16900,11267,못 찾음,https://www.coupang.com\n2026-11-16,마녀공장,퓨어 클렌징폼,무신사,300,13500,4500,"2개 이상 10% 할인",https://www.musinsa.com\n'),
 'cx': dict(role='CX(고객 경험) 기획자', brand='케이뱅크', product='모바일 비상금 대출', cust='급하게 소액이 필요한 사회초년생', pick='상세페이지 조사', csv=None),
 'tech': dict(role='데이터 분석가', brand='라라스윗', product='저당 아이스크림', cust='다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인', pick='경쟁사 가격 조사',
   csv='조사일,브랜드,제품,판매처,용량(ml),판매가(원),100ml당(원),프로모션,출처\n2026-11-16,라라스윗,바닐라 파인트,쿠팡,474,8900,1878,못 찾음,https://www.coupang.com\n2026-11-16,라라스윗,초코 미니컵,공식몰,120,2900,2417,"3+1",https://laranswee.com\n2026-11-16,널담,쫀득 아이스바,공식몰,70,2500,3571,"10개 묶음 15%",https://nuldam.com\n2026-11-16,요아정,요거트 아이스크림,배달앱,300,9900,3300,못 찾음,https://www.baemin.com\n2026-11-16,랩노쉬,프로틴 아이스,쿠팡,100,3300,3300,"정기배송 10%",https://www.coupang.com\n'),
}
def make(d, key, full=True):
    f = FIX[key]; os.makedirs(d, exist_ok=True)
    write(d, 'CLAUDE.md', f"# 수업 작업 규칙\n- 되묻지 않고 가정해서 끝까지 만든다 / 추측한 곳은 (가정) / 웹에서 찾은 값에는 조사일과 출처 링크, 못 찾은 값은 \"못 찾음\" / 끝나면 3줄로만 보고하고, 내용을 보여 달라고 하면 그대로 보여 준다 / 한국어로 쉽게\n\n# 나와 회사\n- 하고 싶은 일: {f['role']}\n- 회사: {f['brand']} ({f['product']})\n- 고객: {f['cust']}\n\n# 오늘 규칙 (11/18 피칭 데이)\n- 발표 화면의 숫자는 이 폴더의 파일에서만 가져오고, 어느 파일에서 왔는지 적는다. 없는 숫자는 [채울 곳], 어림셈은 (가정).\n")
    write(d, 'mvp.md', f"# 조사 도우미 설계서\n- 누구의 불편: {f['role']} 신입이 매일 손으로 하는 {f['pick']}\n- 손으로 하면 하루 60분 (가정)\n- 조사 칸: 아래 research.csv 참고\n- 성공 기준: 하루 10분 안에 확인\n")
    if not full: return
    if f['csv']: write(d, 'research.csv', f['csv'], bom=True)
    write(d, 'mvp.html', f"<!doctype html><meta charset=utf-8><title>{f['brand']} 조사 도우미</title><h1>{f['brand']} 경쟁사 한눈에</h1><p>오늘 바뀐 곳을 먼저 보여 줘요.</p><table><tr><th>브랜드</th><th>값</th></tr><tr><td>요아정</td><td>9,900원</td></tr></table><img src='https://example.com/competitor_ad.jpg' alt='경쟁사 광고 캡처'><footer>학습용 MVP이며 실제 회사와 관계없습니다</footer>")
    write(d, 'pitch.md', f"# 피치 일곱 칸\n- 문제: {f['role']} 신입이 매일 60분 (가정) 동안 {f['pick']}을 손으로 해요\n- 해결: 조사 도우미 한 화면\n- 시장: 같은 일을 하는 신입 [채울 곳]\n- BM: 회사 안 도구, 아끼는 시간\n- MVP: mvp.html, 데모 3단계\n- 함께 만든 것: 다른 조 학생 2명이 써 봄 / 내가 내린 결정: 비교 칸을 100ml당 가격으로 바꿈\n- 요청사항: 일주일 써 볼 동료 3명\n- 한 줄 약속: 매일 아침 10분이면 경쟁사가 한눈에\n")
    write(d, 'pitch.html', f"<!doctype html><meta charset=utf-8><title>{f['brand']} 피치</title><section><h1>매일 아침 10분이면 경쟁사가 한눈에</h1><p>발표자 홍길동</p><img src='images/kv.png'></section><section><h2>문제</h2><p>{f['brand']} 공식 로고를 표지에 넣음</p></section><footer>학습용 MVP 발표이며 실제 회사와 관계없습니다</footer>")
    write(d, 'test_report.md', "# 사용자 테스트 결과서\n- 다른 조 학생 2명 중 2명이 1번 일을 해냄\n- 고칠 순서: 1) 표 제목 2) 걸러 보기 버튼\n- 써 본 사람: 홍길동(010-0000-0000, 시험용 가짜)\n")
    write(d, 'next.md', "# 다음 할 일\n1. 걸러 보기 버튼\n2. 출처 링크 열기 버튼\n3. 매일 아침 자동 실행\n- 다음 주에 확인할 숫자: 하루 확인 시간\n")
    write(d, 'portfolio_1118.md', "# 11/18 피칭\n- 조 안에서 3분 발표\n")
if __name__ == '__main__':
    make(sys.argv[1], sys.argv[2], full=(len(sys.argv) < 4 or sys.argv[3] != 'partial'))
