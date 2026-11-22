// Day 24 AI 버튼(보내기 전 확인) 점검: node classroom/tools/check_aibutton.js <화면.html> [예시 글] [찍을 그림.jpg]
// 시험에서 만들어진 화면을 폰 폭(390px) 브라우저로 열어 아래를 본다. 통과면 종료 코드 0.
//  1) #ai-check 칸, 입력 칸(textarea), 버튼, 틀(script#aic-prompt, {{글}} 자리)이 있다
//  2) 입력 칸이 빈 채로 누르면 복사하지 않는다(글 상자가 비어 있거나 안내만 보인다)
//  3) 예시 글을 넣고 누르면 만들어진 글에 예시 글이 들어가고 {{글}}이 남지 않는다(클립보드나 읽기 전용 글 상자에서 읽음)
//  4) 화면 오류(pageerror)가 없고, 폰 폭에서 옆으로 밀리지 않는다
// 세 번째 인자를 주면 #ai-check 칸만 deviceScaleFactor 2로 찍는다(맨 앞 예시 카드용).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, sample = '시험 글 한 줄입니다. 지금 확인해 주세요.', out] = process.argv.slice(2);
  if (!src) { console.log('쓰는 법: node check_aibutton.js <화면.html> [예시 글] [그림.jpg]'); process.exit(1); }
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, colorScheme: 'light', deviceScaleFactor: out ? 2 : 1 });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + path.resolve(src)); await p.waitForTimeout(600);
  const res = { file: src, ok: true, notes: [] };
  const bad = (m) => { res.ok = false; res.notes.push('✗ ' + m); };
  const has = await p.evaluate(() => {
    const sec = document.getElementById('ai-check');
    const tpl = document.getElementById('aic-prompt');
    const ta = sec ? [...sec.querySelectorAll('textarea')] : [];
    return { sec: !!sec, tpl: !!tpl, tplType: tpl ? tpl.getAttribute('type') : '', slot: tpl ? tpl.textContent.includes('{{글}}') : false,
      inputs: ta.filter(t => !t.readOnly).length, outs: ta.filter(t => t.readOnly).length,
      btns: sec ? [...sec.querySelectorAll('button')].map(x => x.textContent.trim()) : [],
      scrollW: document.documentElement.scrollWidth, ids: [...document.querySelectorAll('[id]')].map(e => e.id) };
  });
  if (!has.sec) bad('#ai-check 칸 없음');
  if (!has.tpl) bad('script#aic-prompt 틀 없음'); else if (!has.slot) bad('틀에 {{글}} 자리 없음');
  if (has.inputs < 1) bad('입력 칸(textarea) 없음');
  const dup = has.ids.filter((x, i) => has.ids.indexOf(x) !== i); if (dup.length) bad('겹치는 id: ' + [...new Set(dup)].join(', '));
  if (has.scrollW > 392) bad('폰 폭 넘침 ' + has.scrollW + 'px');
  res.buttons = has.btns;
  let copyBtn = has.btns.findIndex(t => /복사/.test(t));
  if (copyBtn < 0 && has.btns.length) { copyBtn = has.btns.findIndex(t => /확인/.test(t)); if (copyBtn < 0) copyBtn = 0; res.notes.push('? "복사"가 든 버튼이 없어 "' + has.btns[copyBtn] + '"를 누름(학생이 이름을 바꿨을 수 있음)'); }
  if (has.sec && copyBtn < 0) bad('버튼 없음');
  const readOut = async () => p.evaluate(async () => {
    const sec = document.getElementById('ai-check');
    const o = [...sec.querySelectorAll('textarea')].find(t => t.readOnly);
    let clip = ''; try { clip = await navigator.clipboard.readText(); } catch (e) {}
    return { out: o ? o.value : '', clip, text: sec.innerText };
  });
  if (has.sec && copyBtn >= 0 && has.inputs) {
    const btn = p.locator('#ai-check button').nth(copyBtn);
    // 2) 빈 채로 누르기
    await p.locator('#ai-check textarea:not([readonly])').first().fill('');
    await btn.click(); await p.waitForTimeout(300);
    const e1 = await readOut();
    if (e1.out.includes('{{글}}') || (e1.out && !/먼저/.test(e1.text))) res.notes.push('? 빈 칸에서 누르면 글 상자: ' + e1.out.slice(0, 40));
    if (!/먼저/.test(e1.text)) res.notes.push('? 빈 칸 안내("먼저 붙여요")가 안 보임');
    // 3) 예시 글
    await p.locator('#ai-check textarea:not([readonly])').first().fill(sample);
    await btn.click(); await p.waitForTimeout(500);
    const e2 = await readOut();
    const made = e2.clip.includes(sample) ? e2.clip : e2.out;
    if (!made.includes(sample)) bad('만들어진 글에 예시 글이 없음');
    if (made.includes('{{글}}')) bad('만들어진 글에 {{글}}이 남음');
    if (!/판정/.test(made)) res.notes.push('? 만들어진 글에 "판정" 말이 없음');
    res.made_len = made.length; res.made_head = made.slice(0, 120).replace(/\n/g, ' / ');
    res.via = e2.clip.includes(sample) ? '클립보드' : '읽기 전용 글 상자';
  }
  if (errs.length) bad('화면 오류 ' + JSON.stringify(errs));
  if (out && has.sec) {
    await p.locator('#ai-check').screenshot({ path: out, type: 'jpeg', quality: 78 });
    res.shot = out;
  }
  console.log(JSON.stringify(res, null, 1));
  await b.close(); process.exit(res.ok ? 0 : 2);
})();
