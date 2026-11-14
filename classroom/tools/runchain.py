# 수업 프롬프트를 실제로 돌려 보는 시험기. 사용: python3 runchain.py <guide.html> <작업폴더> <결과.json> <단계...>
# 단계 표기: p01 (새 대화) / p02+ (앞 대화에 이어서)
# 환경 변수: BRAND='브랜드|제품|고객' (다른 브랜드로 바꿔 시험), TOOLS='허용 도구 목록', PMODE='권한 모드(기본 acceptEdits, 계획 모드는 plan)'
#           FILL='{"p06":["계획에서 바꿀 것: 없음","계획에서 바꿀 것: 3번 칸은 빼줘"]}' (학생이 입력 칸을 채운 경우), 단계를 p05&p06처럼 쓰면 두 프롬프트를 한 번에 붙여 넣은 경우
#           한 프롬프트의 여러 칸: FILL='{"m1":[["옛1","새1"],["옛2","새2"]]}'
#           EXTRA='{"x1":"2번으로 바꿔줘. 이유는 ..."}' (가이드에 없는, 학생이 직접 친 한 줄. 단계에 x1+처럼 쓴다)
# BRAND는 페이지의 입력 칸과 똑같이 파란 글자(data-v) 자리만 바꾼다. 프롬프트 본문에 적힌 예시 브랜드 이름은 그대로 둔다.
import sys,re,json,html,subprocess,os,time
guide,work,outp=sys.argv[1],sys.argv[2],sys.argv[3]; steps=sys.argv[4:]
src=open(guide,encoding='utf-8').read()
raw={m.group(1):m.group(2) for m in re.finditer(r'<pre id="([a-z]+\d*)">(.*?)</pre>',src,flags=re.S)}
os.makedirs(work,exist_ok=True)
if os.environ.get('BRAND'):
    for key,val in zip(('brand','product','customer'),os.environ['BRAND'].split('|')):
        raw={k:re.sub(r'<b[^>]*data-v="%s"[^>]*>.*?</b>'%key,lambda m,val=val:html.escape(val),v,flags=re.S) for k,v in raw.items()}
prompts={k:html.unescape(re.sub(r'<[^>]+>','',v)) for k,v in raw.items()}
prompts.update(json.loads(os.environ.get('EXTRA','{}')))
FILL=json.loads(os.environ.get('FILL','{}'))
for k,v in FILL.items():
    pairs=v if v and isinstance(v[0],list) else [v]   # ["옛","새"] 하나 또는 [["옛","새"],["옛","새"]] 여러 개
    for old,new in pairs:
        assert old in prompts[k],('FILL 대상 없음',k,old); prompts[k]=prompts[k].replace(old,new)
def tree():
    out={}
    for r,d,f in os.walk(work):
        if '/.git' in r: continue
        for x in f:
            p=os.path.join(r,x); out[os.path.relpath(p,work)]=os.path.getsize(p)
    return out
ASK=re.compile(r'\?|알려\s*주|말씀해\s*주|골라\s*주|선택해\s*주|정해\s*주|확인해\s*주시|할까요|원하시면|필요하시면|올려\s*주')
TOOLS=os.environ.get('TOOLS','WebSearch,WebFetch,Read,Write,Edit,Glob,Grep'); PMODE=os.environ.get('PMODE','acceptEdits')
log=json.load(open(outp)) if os.environ.get('APPEND') and os.path.exists(outp) else []
for st in steps:
    cont=st.endswith('+'); pid=st.rstrip('+'); pr='\n\n'.join(prompts[x] for x in pid.split('&'))
    before=tree(); t0=time.time()
    cmd=['claude']+(['-c'] if cont else [])+['-p',pr,'--permission-mode',PMODE,'--allowedTools',TOOLS,'--max-turns','40','--output-format','json']
    try:
        r=subprocess.run(cmd,cwd=work,capture_output=True,text=True,timeout=540)
        try: d=json.loads(r.stdout)
        except Exception: d={'subtype':'not_json','result':(r.stdout or r.stderr)[-600:]}
    except subprocess.TimeoutExpired:
        d={'subtype':'timeout','result':''}
    after=tree()
    new=sorted(k for k in after if k not in before); changed=sorted(k for k in after if k in before and after[k]!=before[k])
    res=d.get('result') or ''
    rec={'step':st,'model':','.join(sorted((d.get('modelUsage') or {}).keys())),'subtype':d.get('subtype'),'sec':round(time.time()-t0),'turns':d.get('num_turns'),'cost':d.get('total_cost_usd'),
         'denials':[x.get('tool_name') for x in (d.get('permission_denials') or [])],'new':new,'changed':changed,
         'reply_len':len(res),'ask_hits':ASK.findall(res),'reply':res}
    log.append(rec); json.dump(log,open(outp,'w'),ensure_ascii=False,indent=1)
    print(f"[{st}] {rec['subtype']} {rec['sec']}s turns={rec['turns']} new={new} changed={changed} denials={rec['denials']} len={len(res)} ask={rec['ask_hits'][:4]}",flush=True)
    print('   답:',res[:420].replace('\n',' / '),flush=True)
print('DONE',outp)
