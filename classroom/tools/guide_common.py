# 수업 가이드 빌더의 공통 부분 (Day 17부터). Day 16 빌더(build_day16.py)의 바탕을 그대로 옮겼다.
# 쓰는 법: from guide_common import *  → PR, body를 만든 뒤 write_page(...)
import re, os, sys
TOOLS=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(os.path.dirname(TOOLS))
_src=open(os.path.join(TOOLS,'guide_base.html'),encoding='utf-8').read()
BASE_STYLE=re.search(r'<style>.*?</style>',_src,flags=re.S).group(0)
BASE_SCRIPT=re.search(r'<script>.*?</script>',_src,flags=re.S).group(0)
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
def tok(k,d): return '<b data-v="%s">%s</b>'%(k,d)
def box(pid,title,text,style_attr=''):
    return ('<button class="copy" type="button" data-copy="%s"%s><div class="hd"><b>%s</b><span class="btn">눌러서 복사</span></div>\n<pre id="%s">%s</pre></button>'%(pid,style_attr,title,pid,text))
def field(k,label,ph=''):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><input id="v-%s" data-in="%s" type="text" maxlength="90" placeholder="%s" autocomplete="off"></div></div>'%(k,label,k,k,ph)
def fieldwide(k,label,ph='',n=1500):
    return '<div class="card"><div class="field" style="margin:0"><label for="v-%s">%s</label><textarea id="v-%s" data-in="%s" rows="4" maxlength="%d" placeholder="%s" autocomplete="off"></textarea></div></div>'%(k,label,k,k,n,ph)

# MVP 표기(강사 지시): 프롬프트는 줄마다 처음 한 번 "MVP(Minimum Viable Product)", 본문은 문단(블록)마다 처음 한 번, 괄호 부분은 흐리게
def expand_mvp_plain(t):
    out=[]
    for ln in t.split('\n'):
        if 'Minimum Viable Product' not in ln:
            ln=re.sub(r'MVP(?!\s*\()','MVP(Minimum Viable Product)',ln,count=1)
        out.append(ln)
    return '\n'.join(out)
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


def build_page(title,body,defaults,prefix,extra_css='',extra_js=''):
    """defaults: 입력 칸이 비었을 때 프롬프트에 들어갈 처음 값(dict). prefix: 이 기기 저장 키 앞머리(예: 'l17-')."""
    style=BASE_STYLE.replace('</style>',EXTRA_CSS+extra_css+'</style>')
    script=BASE_SCRIPT
    _f="i.value=f[i.getAttribute('data-in')]"
    assert script.count(_f)==1
    script=script.replace(_f,"i.value=val(prof[i.getAttribute('data-in')])")
    _d="var DEF={brand:'라라스윗',product:'저당 아이스크림',customer:'다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인',moment:'밤에 죄책감 없는 디저트·간식을 찾을 때',ind:'식품'};"
    assert script.count(_d)==1
    d=dict(brand='라라스윗',product='저당 아이스크림',customer='다이어트 중이지만 밤마다 디저트가 당기는 2534 직장인',moment='밤에 죄책감 없는 디저트·간식을 찾을 때',ind='식품'); d.update(defaults)
    js='var DEF={'+','.join("%s:%s"%(k,repr(v)) for k,v in d.items())+'};'
    script=script.replace(_d,js)
    assert script.count("'l16-")==4
    script=script.replace("'l16-","'"+prefix)
    return ('<meta name="claude:viewport-fit-sides" content="cover">\n<title>%s</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap">\n'%title
            +style+'\n'+body+'\n'+script+'\n'+extra_js+'\n')
def write_page(out,default_path):
    dest=sys.argv[1] if len(sys.argv)>1 else default_path
    open(dest,'w',encoding='utf-8').write(out)
    print('written',dest,len(out),'boxes',len(re.findall(r'class="copy[ "]',out)),'clipped',out.count('class="copy clip"'))

# 쪽 번호(11/21 강사 지시 "페이지 넘버 나오게끔, 몇 페이지 헷갈려"): 섹션마다 차례로 "N/총쪽"을 머리 칩·위 메뉴·오늘 순서 줄에 붙인다.
PAGE_CSS='''
.pg{display:inline-block;background:var(--ink);color:var(--bg);border-radius:8px;padding:1px 10px;margin-right:10px;font-size:16px;font-weight:800;vertical-align:1px}
nav a .pgn{font-weight:800;margin-right:6px;opacity:.8}
.pgtag{display:inline-block;font-size:15px;font-weight:800;color:var(--blue);background:var(--blue-soft);border-radius:8px;padding:0 8px;margin-left:8px;vertical-align:2px;white-space:nowrap}
.what{color:var(--sub);font-size:19px;line-height:1.6;margin:18px 0 10px}
.what p{margin:4px 0}
.what b{color:var(--ink)}
.card li{margin:10px 0}
.card p + p,.card p + ul,.card p + ol,.card ul + p,.card ol + p{margin-top:14px}
.sub{line-height:1.75}
'''
def number_pages(body):
    """<section id> 순서대로 쪽 번호를 매기고, 머리 칩·메뉴·오늘 순서 줄에 표시한다. 상자(pre) 글은 건드리지 않는다."""
    pos=[(m.start(),m.group(1)) for m in re.finditer(r'<section id="([^"]+)">',body)]
    total=len(pos); page={sid:i+1 for i,(p,sid) in enumerate(pos)}
    owner={}
    for m in re.finditer(r'\bid="([^"]+)"',body):
        cur=None
        for p,sid in pos:
            if p<=m.start(): cur=sid
        if cur: owner[m.group(1)]=page[cur]
    body=re.sub(r'(<section id="([^"]+)">\s*<span class="eyebrow">)',lambda m:m.group(1)+'<span class="pg">%d/%d쪽</span>'%(page[m.group(2)],total),body)
    nav=re.search(r'<nav id="nav".*?</nav>',body,flags=re.S).group(0)
    nav2=re.sub(r'<a href="#([^"]+)">([^<]+)</a>',lambda m:('<a href="#%s"><b class="pgn">%d</b>%s</a>'%(m.group(1),page[m.group(1)],m.group(2)) if m.group(1) in page else m.group(0)),nav)
    body=body.replace(nav,nav2,1)
    body=re.sub(r'(<a class="row" href="#([^"]+)"><span class="t">[^<]*</span><span class="w"><b>)(.*?)(</b>)',lambda m:m.group(1)+m.group(3)+('<span class="pgtag">%d쪽</span>'%owner[m.group(2)] if m.group(2) in owner else '')+m.group(4),body)
    return body

# ── 직무별 병목 증상 20가지 (11/21 강사 지시 "업무 직무마다 병목 증상 20가지 추려서 추가해")
# Day 21 2교시 카드와 Day 22 B 카드에서 같이 쓴다. (칸, 증상, AI 신입에게 맡길 첫 일)
BN20 = [
    ('콘텐츠·브랜드 마케터', [
        ('① 리서치하기', '경쟁 브랜드의 SNS와 광고를 매주 하나씩 열어 캡처하고 표에 옮겨 적어요', '정해 둔 계정·광고를 같은 칸(날짜·브랜드·문구·링크)으로 모아 표에 쌓기'),
        ('② 분석하기', '모은 자료는 많은데 요즘 무엇이 먹히는지는 감으로 골라요', '지난주보다 새로 늘어난 문구·이미지 Top 5를 근거 링크와 함께 뽑기'),
        ('③ 만들기', '같은 카피를 채널마다 길이와 말투만 바꿔 처음부터 다시 써요', '브랜드 말투 규칙으로 인스타·블로그·문자용 시안을 한 번에 만들기'),
        ('⑤ 반응 보기', '올린 뒤 숫자를 보려고 채널마다 따로 들어가 엑셀에 옮겨요', '채널별 조회·저장·클릭을 한 표로 모아 지난주와 견주기')]),
    ('퍼포먼스 마케터', [
        ('② 분석하기', '클릭률이 떨어진 광고를 늦게 알아채 예산이 새요', '어제보다 클릭률이 크게 떨어진 광고를 아침마다 골라 알리기'),
        ('③ 만들기', '광고 문구를 조금씩 바꾼 시안 수십 개를 손으로 만들어요', '잘된 문구를 바탕으로 길이·혜택·말투를 바꾼 시안 20개 만들기'),
        ('⑤ 반응 보기', '광고 매체마다 성과 리포트를 날마다 내려받아 한 시트로 합쳐요', '매체별 파일을 같은 칸으로 합쳐 날짜순으로 쌓기')]),
    ('MD(상품기획)', [
        ('① 리서치하기', '경쟁 상품의 가격·프로모션·증정품을 날마다 판매처를 돌며 옮겨 적어요', '정해 둔 상품 페이지의 가격·혜택을 조사일·출처와 함께 표에 쌓기'),
        ('② 분석하기', '판매 파일과 재고 파일을 맞춰 품절 위험 상품을 찾느라 오전이 다 가요', '판매 속도와 남은 재고로 품절 위험 상품을 아침마다 골라내기'),
        ('③ 만들기', '비슷한 상품도 상세페이지 문구를 상품마다 새로 써요', '상품 정보표로 특징·사용법·주의 문구 초안 만들기'),
        ('⑤ 반응 보기', '리뷰가 쌓이는데 다 못 읽어서 공통 불만을 늦게 알아요', '별점 낮은 리뷰의 공통 불만 3가지와 예시 리뷰 뽑기')]),
    ('운영 매니저(교육·매장·물류)', [
        ('① 리서치하기', '출석부·신청서·단톡방을 보고 현황을 한 표로 다시 옮겨 적어요', '흩어진 기록을 같은 칸(날짜·사람·상태)으로 모아 한 표에 쌓기'),
        ('② 분석하기', '빠진 사람·늦은 일을 표를 훑으며 손으로 골라내요', '미제출·결석·지연을 규칙대로 골라 급한 순서로 보여 주기'),
        ('④ 내보내기', '이름과 날짜만 다른 안내문을 한 사람씩 고쳐 보내고, 보냈는지도 손으로 확인해요', '명단으로 안내문 초안을 만들고, 사람이 확인한 뒤 보낸 기록 남기기')]),
    ('CX(고객 경험) 기획자', [
        ('② 분석하기', '상담 기록을 읽고 문의 유형을 손으로 나눠 주간 보고를 만들어요', '문의를 유형별로 나누고 지난주보다 늘어난 유형 알리기'),
        ('③ 만들기', '비슷한 문의가 대부분인데 답을 매번 새로 써요', '자주 묻는 문의별 답변 초안 만들기(보내기 전 사람 확인)'),
        ('④ 내보내기', '반복되는 불만을 상품·개발팀에 넘기기까지 한 주가 걸려요', '반복 불만을 한 장으로 묶어 담당 팀별로 보내기')]),
    ('데이터 분석가·개발(테크)', [
        ('① 리서치하기', '팀마다 엑셀 칸 이름과 날짜 모양이 달라 정리부터 오래 걸려요', '들어온 파일을 정해 둔 칸 이름·날짜 모양으로 맞춰 쌓기'),
        ('② 분석하기', '숫자가 이상해도 아무도 모르고 지나가다 나중에 우연히 발견해요', '빠진 날짜·튀는 값을 날마다 검사하고 이상하면 멈추고 알리기'),
        ('③ 만들기', '매주 같은 조회와 같은 차트를 다시 돌려 보고서에 붙여요', '같은 순서로 표·차트·한 줄 요약이 든 주간 보고 만들기')]),
]
assert sum(len(r) for _, r in BN20) == 20

BN20_DECODER = ('<p class="sub"><b>말버릇으로 칸 찾기</b> · "옮겨 적어요" → ① 리서치하기 · "감으로 골라요", "늦게 알아요" → ② 분석하기 · '
                '"처음부터 다시 써요" → ③ 만들기 · "한 사람씩 보내요", "넘기기까지 오래 걸려요" → ④ 내보내기 · '
                '"따로 들어가 봐요", "다 못 읽어요" → ⑤ 반응 보기</p>')

# 폰 폭에서 두 칸으로 나누면 글이 한두 글자씩 끊겨서(11/21 화면 점검), 칸 이름은 작은 표시로 글 위에 올리고 글은 폭 전체를 쓴다
BN20_CSS = '''
.bn{list-style:none;padding:0;margin:6px 0 18px}
.bn li{padding:14px 0;border-top:1px solid var(--line)}
.bn li:first-child{border-top:0}
.bn .cell{display:inline-block;font-size:15px;font-weight:800;color:var(--blue);background:var(--blue-soft);border-radius:8px;padding:0 8px;margin-bottom:6px}
.bn b{display:block;line-height:1.6}
.bn small{display:block;color:var(--sub);margin-top:6px;line-height:1.65}
'''

def bn20_rows():
    out, n = [], 0
    for role, rows in BN20:
        out.append('<h4>%s</h4><ol class="bn">' % role)
        for cell, sym, task in rows:
            n += 1
            out.append('<li><span class="cell">%s</span><b>%d. %s</b><small>AI 신입에게 맡길 첫 일 · %s</small></li>' % (cell, n, sym, task))
        out.append('</ol>')
    return '\n'.join(out)

# ── 형광펜과 접기 (11/21 강사 지시 "중요 강조점. 형광펜 쳐줘. 그리고 너무 많은 내용 접어")
# 쓰는 법(빌더 끝): body=finish(number_pages(expand_mvp_html(body)), FOLDS, HL)  /  extra_css에 FOLD_CSS, extra_js=FOLD_JS
#  - 형광펜(HL): 쪽마다 꼭 기억할 문장 1~3개. 본문(상자 밖)에서 정확히 한 번 나오는 글자만 칠한다.
#  - 접기(FOLDS): 지금 할 일·상자 제목과 설명·내 결정·입력 칸은 펴 두고, 예시·자세한 설명·고르는 카드·선택 활동을 접는다.
#  - 긴 상자: 앞 몇 줄만 보이고 "상자 글 전체 보기"로 편다. 복사는 전체 글 그대로(innerText는 잘린 글도 읽는다).
FOLD_CSS = '''
:root{--hl:#ffe45c}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--hl:rgba(255,214,10,.34)}}
:root[data-theme="dark"]{--hl:rgba(255,214,10,.34)}
mark.hl{background:linear-gradient(transparent 36%,var(--hl) 36%);color:inherit;padding:0 2px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
details.fold>.body,details.more>.body{color:var(--ink)}
details.fold>.body>*:first-child,details.more>.body>*:first-child{margin-top:0}
.card details.more{margin:12px 0 4px}
.copy.clip pre{max-height:11.5em;overflow:hidden;-webkit-mask-image:linear-gradient(#000 62%,transparent);mask-image:linear-gradient(#000 62%,transparent)}
.copy pre[id]{scroll-margin-top:150px}
.peek{display:block;margin:-4px 0 20px auto;background:none;border:0;color:var(--blue);font:inherit;font-weight:800;font-size:17px;cursor:pointer;padding:8px 4px}
'''
FOLD_JS = '''<script>
(function(){
  function openTo(id){var e=document.getElementById(id);for(var p=e;p;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true}}
  function fromHash(){var h=location.hash.slice(1);if(h){try{openTo(decodeURIComponent(h))}catch(e){}}}
  document.addEventListener('click',function(ev){var a=ev.target.closest&&ev.target.closest('a[href^="#"]');if(a){try{openTo(decodeURIComponent(a.getAttribute('href').slice(1)))}catch(e){}}},true);
  window.addEventListener('hashchange',fromHash);fromHash();
  [].forEach.call(document.querySelectorAll('.peek'),function(b){b.addEventListener('click',function(){
    var c=b.previousElementSibling,on=c.classList.toggle('clip');b.textContent=on?'상자 글 전체 보기':'상자 글 접기';b.setAttribute('aria-expanded',on?'false':'true')})});
})();
</script>'''

_VOID = {'br', 'img', 'input', 'hr', 'meta', 'link', 'source', 'wbr'}

def _end_of(h, i):
    """h[i]이 '<tag'인 요소의 끝(닫는 태그 다음 자리)을 돌려준다. 같은 이름 태그의 겹침을 센다."""
    m = re.match(r'<([a-zA-Z][a-zA-Z0-9]*)', h[i:])
    name = m.group(1).lower()
    gt = h.index('>', i)
    if name in _VOID or h[gt - 1] == '/':
        return gt + 1
    depth, k = 1, gt + 1
    pat = re.compile(r'<(/?)%s\b[^>]*>' % name, re.I)
    while depth:
        mm = pat.search(h, k)
        if not mm:
            raise ValueError('닫는 태그 없음: ' + name)
        depth += -1 if mm.group(1) else 1
        k = mm.end()
    return k

def _children(h, start, end):
    """h[start:end] 안의 바로 아래 자식 요소들 [(시작, 끝, 태그)]"""
    out, k = [], start
    while True:
        j = h.find('<', k, end)
        if j < 0:
            break
        if h.startswith('</', j):
            raise ValueError('뜻밖의 닫는 태그: ' + h[j:j + 30])
        e = _end_of(h, j)
        out.append((j, e, re.match(r'<([a-zA-Z0-9]+)', h[j:]).group(1).lower()))
        k = e
    return out

def _protected(h):
    """상자(pre)·그림(svg)·스크립트·스타일 자리"""
    return [(m.start(), m.end()) for m in re.finditer(r'<(pre|svg|script|style)\b.*?</\1>', h, flags=re.S)]

def _find_text(h, text):
    """태그 밖·보호 자리 밖에서 text가 정확히 한 번 나오는 자리"""
    prot = _protected(h)
    hits = []
    for m in re.finditer(re.escape(text), h):
        s = m.start()
        if any(a <= s < b for a, b in prot):
            continue
        lt, gt = h.rfind('<', 0, s), h.rfind('>', 0, s)
        if lt > gt:
            continue   # 태그 안
        hits.append(s)
    if len(hits) != 1:
        raise ValueError('"%s" 가 본문에 %d번' % (text[:40], len(hits)))
    return hits[0]

def _card(h, locator):
    """locator 글자를 품은 가장 안쪽 카드(div class="card…")의 (시작, 여는 태그 끝, 닫는 태그 시작, 끝)"""
    pos = _find_text(h, locator)
    k = pos
    while True:
        s = h.rfind('<div class="card', 0, k)
        if s < 0:
            raise ValueError('카드 없음: ' + locator[:40])
        e = _end_of(h, s)
        if e > pos:
            return s, h.index('>', s) + 1, h.rindex('</div>', s, e), e
        k = s

def _wrap(inner, summary, cls, ident=''):
    return '<details class="%s"%s><summary>%s</summary><div class="body">%s</div></details>' % (cls, (' id="%s"' % ident) if ident else '', summary, inner)

def fold_range(h, locator, i, j, summary):
    """locator가 든 카드의 자식 i~j번(0부터, 둘 다 포함)을 접는 칸 하나로"""
    s, o, c, e = _card(h, locator)
    kids = _children(h, o, c)
    j = len(kids) - 1 if j is None else j
    if not (0 <= i <= j < len(kids)):
        raise ValueError('자식 번호 밖: %s %d~%d / %d' % (locator[:30], i, j, len(kids)))
    a, b = kids[i][0], kids[j][1]
    return h[:a] + _wrap(h[a:b], summary, 'more') + h[b:]

def fold_whole(h, locator, summary):
    """locator가 든 카드 전체를 접는 칸으로(첫 h3는 접는 칸의 제목이 된다)"""
    s, o, c, e = _card(h, locator)
    tag = h[s:o]
    ident = (re.search(r'\bid="([^"]+)"', tag) or [None, ''])[1]
    kids = _children(h, o, c)
    inner = ''.join(h[a:b] for a, b, t in kids if not (t == 'h3' and (a, b, t) == kids[0]) and not (t == 'h3' and kids[0][2] == 'span' and (a, b, t) == kids[1]))
    return h[:s] + _wrap(inner, summary, 'fold', ident) + h[e:]

def clip_boxes(h, min_chars=330):
    """긴 복사 상자는 앞 몇 줄만 보이게. 학생이 고칠 ○○가 든 상자는 그대로 펴 둔다."""
    def rep(m):
        txt = re.sub(r'<[^>]+>', '', m.group(3))
        if len(txt) < min_chars or '○○' in txt:
            return m.group(0)
        return m.group(1).replace('class="copy"', 'class="copy clip"', 1) + m.group(2) + m.group(3) + m.group(4) + '<button type="button" class="peek" aria-expanded="false">상자 글 전체 보기</button>'
    return re.sub(r'(<button class="copy"[^>]*>)(.*?<pre id="[^"]+">)(.*?)(</pre></button>)', rep, h, flags=re.S)

def highlight(h, phrases):
    for t in phrases:
        p = _find_text(h, t)
        h = h[:p] + '<mark class="hl">' + t + '</mark>' + h[p + len(t):]
    return h

def finish(h, folds=(), hl=()):
    """folds: ('range', 찾을 글자, i, j, 제목) 또는 ('whole', 찾을 글자, 제목)"""
    for f in folds:
        h = fold_range(h, f[1], f[2], f[3], f[4]) if f[0] == 'range' else fold_whole(h, f[1], f[2])
    return highlight(clip_boxes(h), hl)

# ── 맨 앞 "오늘 만들 결과물" 예시 카드 (11/22 강사 지시 "결과물이 어떤 형태인지 예시로 보여 주고, 어떻게 활용될지 안내")
# 예시 그림은 classroom/tools/day21_gallery/에 둔다(수업 예시 회사로 같은 상자를 돌려 만든 화면, 마스터프롬프트-결과물예시.md).
EX_CSS = '''
.card details .excode{background:var(--card)}
.shot{margin:16px 0 8px}
.shot img{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--line);background:#fff}
.shot figcaption{color:var(--sub);font-size:16px;line-height:1.6;margin-top:8px}
.excode{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:15px;line-height:1.6;white-space:pre-wrap;word-break:keep-all;overflow-wrap:anywhere;background:var(--code);border-radius:12px;padding:14px 16px;margin:8px 0 14px;color:var(--ink)}
'''
def gallery_img(name):
    import base64, os
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'day21_gallery', name)
    return 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def shot(name, alt, caption):
    return '<figure class="shot"><img src="%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (gallery_img(name), alt, caption)
