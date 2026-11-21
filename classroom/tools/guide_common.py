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
    print('written',dest,len(out),'boxes',out.count('class="copy"'))

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
