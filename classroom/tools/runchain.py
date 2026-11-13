# 수업 프롬프트를 실제로 돌려 보는 시험기. 사용: python3 runchain.py <guide.html> <작업폴더> <결과.json> <단계...>
# 단계 표기: p01 (새 대화) / p02+ (앞 대화에 이어서)
import sys,re,json,html,subprocess,os,time
guide,work,outp=sys.argv[1],sys.argv[2],sys.argv[3]; steps=sys.argv[4:]
src=open(guide,encoding='utf-8').read()
prompts={m.group(1):html.unescape(re.sub(r'<[^>]+>','',m.group(2))) for m in re.finditer(r'<pre id="([a-z]+\d*)">(.*?)</pre>',src,flags=re.S)}
os.makedirs(work,exist_ok=True)
def tree():
    out={}
    for r,d,f in os.walk(work):
        if '/.git' in r: continue
        for x in f:
            p=os.path.join(r,x); out[os.path.relpath(p,work)]=os.path.getsize(p)
    return out
ASK=re.compile(r'\?|알려\s*주|말씀해\s*주|골라\s*주|선택해\s*주|정해\s*주|확인해\s*주시|할까요|원하시면|필요하시면|올려\s*주')
log=[]
for st in steps:
    cont=st.endswith('+'); pid=st.rstrip('+'); pr=prompts[pid]
    before=tree(); t0=time.time()
    cmd=['claude']+(['-c'] if cont else [])+['-p',pr,'--permission-mode','acceptEdits','--allowedTools','WebSearch,WebFetch,Read,Write,Edit,Glob,Grep','--max-turns','40','--output-format','json']
    try:
        r=subprocess.run(cmd,cwd=work,capture_output=True,text=True,timeout=540)
        try: d=json.loads(r.stdout)
        except Exception: d={'subtype':'not_json','result':(r.stdout or r.stderr)[-600:]}
    except subprocess.TimeoutExpired:
        d={'subtype':'timeout','result':''}
    after=tree()
    new=sorted(k for k in after if k not in before); changed=sorted(k for k in after if k in before and after[k]!=before[k])
    res=d.get('result') or ''
    rec={'step':st,'subtype':d.get('subtype'),'sec':round(time.time()-t0),'turns':d.get('num_turns'),'cost':d.get('total_cost_usd'),
         'denials':[x.get('tool_name') for x in (d.get('permission_denials') or [])],'new':new,'changed':changed,
         'reply_len':len(res),'ask_hits':ASK.findall(res),'reply':res}
    log.append(rec); json.dump(log,open(outp,'w'),ensure_ascii=False,indent=1)
    print(f"[{st}] {rec['subtype']} {rec['sec']}s turns={rec['turns']} new={new} changed={changed} denials={rec['denials']} len={len(res)} ask={rec['ask_hits'][:4]}",flush=True)
    print('   답:',res[:420].replace('\n',' / '),flush=True)
print('DONE',outp)
