// Day 25 AI 버튼 둘째 판(v2, 기준 사실 칸) 점검: node classroom/tools/check_aibutton2.js <화면.html> [예시 글] [기준 사실] [찍을 그림.jpg]
// 시험에서 만들어진 화면을 폰 폭(390px) 브라우저로 열어 아래를 본다. 통과면 종료 코드 0.
//  1) #ai-check 칸, 고칠 수 있는 입력 칸 둘(글, 기준 사실), 버튼, 틀(script#aic-prompt, {{글}}과 {{사실}} 자리)이 있다
//  2) 글 칸이 빈 채로 누르면 복사하지 않는다
//  3) 글만 넣고 누르면 만들어진 글에 글이 들어가고, 기준 사실 자리에 "(없음)"이 들어가고, {{글}}·{{사실}}이 남지 않는다
//  4) 글과 기준 사실을 넣고 누르면 둘 다 들어간다
//  5) "v2" 표시와 사람 정보 안내(이름·연락처·출결)가 보이고, 저장·전송 코드(localStorage, fetch 등)가 없다
//  6) 화면 오류가 없고, 폰 폭에서 옆으로 밀리지 않는다
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const [src, sample = '시험 글 한 줄입니다. 12/5(토) 10시에 만나요.', facts = '일정표: 12/5(토) 9:30 집합', out] = process.argv.slice(2);
  if (!src) { console.log('쓰는 법: node check_aibutton2.js <화면.html> [예시 글] [기준 사실] [그림.jpg]'); process.exit(1); }
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, colorScheme: 'light', deviceScaleFactor: out ? 2 : 1 });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + path.resolve(src)); await p.waitForTimeout(600);
  const res = { file: src, ok: true, notes: [] };
  const bad = (m) => { res.ok = false; res.notes.push('✗ ' + m); };
  const has = await p.evaluate(() => {
    const sec = document.getElementById('ai-check');
    const tpl = document.getElementById('aic-prompt');
    const ta = sec ? [...sec.querySelectorAll('textarea, input[type=text]')] : [];
    return { sec: !!sec, tpl: !!tpl, slot: tpl ? tpl.textContent.includes('{{글}}') : false, slot2: tpl ? tpl.textContent.includes('{{사실}}') : false,
      inputs: ta.filter(t => !t.readOnly).map(t => t.id), outs: ta.filter(t => t.readOnly).length,
      btns: sec ? [...sec.querySelectorAll('button')].map(x => x.textContent.trim()) : [],
      text: sec ? sec.innerText : '', scrollW: document.documentElement.scrollWidth, ids: [...document.querySelectorAll('[id]')].map(e => e.id) };
  });
  if (!has.sec) bad('#ai-check 칸 없음');
  if (!has.tpl) bad('script#aic-prompt 틀 없음'); else { if (!has.slot) bad('틀에 {{글}} 자리 없음'); if (!has.slot2) bad('틀에 {{사실}} 자리 없음'); }
  if (has.inputs.length < 2) bad('고칠 수 있는 입력 칸이 둘보다 적음: ' + JSON.stringify(has.inputs));
  const dup = has.ids.filter((x, i) => has.ids.indexOf(x) !== i); if (dup.length) bad('겹치는 id: ' + [...new Set(dup)].join(', '));
  if (has.scrollW > 392) bad('폰 폭 넘침 ' + has.scrollW + 'px');
  if (!/v2/.test(has.text)) res.notes.push('? 버튼 칸에 "v2" 표시가 안 보임');
  if (!/(이름|연락처|출결)/.test(has.text)) res.notes.push('? 사람 정보 안내(이름·연락처·출결)가 안 보임');
  const code = fs.readFileSync(src, 'utf8');
  const leak = ['localStorage', 'sessionStorage', 'document.cookie', 'indexedDB', 'fetch(', 'XMLHttpRequest', 'sendBeacon'].filter(k => code.includes(k));
  if (leak.length) res.notes.push('? 저장·전송 코드가 화면 파일에 있음(원래 화면의 것일 수 있음): ' + leak.join(', '));
  res.buttons = has.btns; res.inputs = has.inputs;
  let copyBtn = has.btns.findIndex(t => /복사/.test(t) && !/기록/.test(t));
  if (copyBtn < 0 && has.btns.length) { copyBtn = has.btns.findIndex(t => /확인/.test(t)); if (copyBtn < 0) copyBtn = 0; res.notes.push('? "복사"가 든 버튼이 없어 "' + has.btns[copyBtn] + '"를 누름'); }
  if (has.sec && copyBtn < 0) bad('버튼 없음');
  const readOut = async () => p.evaluate(async () => {
    const sec = document.getElementById('ai-check');
    const o = [...sec.querySelectorAll('textarea')].find(t => t.readOnly);
    let clip = ''; try { clip = await navigator.clipboard.readText(); } catch (e) {}
    return { out: o ? o.value : '', clip, text: sec.innerText };
  });
  if (has.sec && copyBtn >= 0 && has.inputs.length >= 2) {
    const btn = p.locator('#ai-check button').nth(copyBtn);
    const ins = p.locator('#ai-check textarea:not([readonly]), #ai-check input[type=text]:not([readonly])');
    // 어느 칸이 기준 사실 칸인지: id나 라벨에 fact·사실이 든 것, 없으면 둘째
    const fi = await p.evaluate(() => { const sec = document.getElementById('ai-check'); const a = [...sec.querySelectorAll('textarea, input[type=text]')].filter(t => !t.readOnly);
      let k = a.findIndex(t => /fact|사실/i.test(t.id + ' ' + (t.getAttribute('aria-label') || '') + ' ' + (t.placeholder || ''))); return k < 0 ? 1 : k; });
    const ti = fi === 0 ? 1 : 0;
    await ins.nth(ti).fill(''); await ins.nth(fi).fill('');
    await btn.click(); await p.waitForTimeout(300);
    const e1 = await readOut();
    if (!/먼저/.test(e1.text)) res.notes.push('? 빈 칸 안내("먼저 붙여요")가 안 보임');
    if (e1.out && e1.out.includes('{{')) res.notes.push('? 빈 칸에서 누르면 글 상자에 자리 표시가 남음');
    // 3) 글만
    await ins.nth(ti).fill(sample); await btn.click(); await p.waitForTimeout(500);
    const e2 = await readOut(); const m2 = e2.out.includes(sample) ? e2.out : e2.clip;
    if (!m2.includes(sample)) bad('글만 넣었을 때 만들어진 글에 글이 없음');
    if (m2.includes('{{글}}') || m2.includes('{{사실}}')) bad('글만 넣었을 때 자리 표시가 남음');
    if (!m2.includes('(없음)')) bad('기준 사실이 비었을 때 "(없음)"이 안 들어감');
    // 4) 글 + 기준 사실
    await ins.nth(fi).fill(facts); await btn.click(); await p.waitForTimeout(500);
    const e3 = await readOut(); const m3 = e3.out.includes(sample) ? e3.out : e3.clip;
    if (!m3.includes(sample) || !m3.includes(facts)) bad('글과 기준 사실을 넣었을 때 둘 다 들어가지 않음');
    if (m3.includes('{{글}}') || m3.includes('{{사실}}')) bad('자리 표시가 남음');
    if (!/판정/.test(m3)) res.notes.push('? 만들어진 글에 "판정" 말이 없음');
    if (m3.indexOf(facts) > m3.lastIndexOf(sample)) res.notes.push('? 기준 사실이 확인할 글보다 뒤에 있음');
    res.made_len = m3.length; res.tail = m3.slice(-260).replace(/\n/g, ' / ');
  }
  if (errs.length) bad('화면 오류 ' + JSON.stringify(errs));
  if (out && has.sec) { await p.locator('#ai-check').screenshot({ path: out, type: 'jpeg', quality: 78 }); res.shot = out; }
  console.log(JSON.stringify(res, null, 1));
  await b.close(); process.exit(res.ok ? 0 : 2);
})();
