// 수업 가이드 화면 점검 (모든 날짜에 쓴다): node classroom/tools/check_guide.js <가이드.html>
// 폰 폭(390, 밝은 화면)과 PC(1280, 어두운 화면)에서 본다.
// - 옆으로 넘치는 요소, 복사 상자 수와 겹치는 이름, 메뉴 링크가 가리키는 곳, 처음 열었을 때 입력 칸이 비었는지
// - 체크 칸 저장 키가 겹치는지, 화면 오류
// - 입력 칸마다 글자를 넣으면 프롬프트 안의 파란 글자(같은 이름의 data-v)가 바뀌는지, 지우면 처음 값으로 돌아가는지
const { chromium } = require('playwright');
(async () => {
  const file = process.argv[2];
  if (!file) { console.log('쓰는 법: node check_guide.js <가이드.html>'); process.exit(1); }
  const b = await chromium.launch();
  let bad = 0;
  for (const [w, h, scheme] of [[390, 844, 'light'], [1280, 900, 'dark']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: scheme });
    const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + require('path').resolve(file)); await p.waitForTimeout(500);
    await p.evaluate(() => document.querySelectorAll('details').forEach(d => { d.open = true; }));
    const r = await p.evaluate(() => {
      const ids = [...document.querySelectorAll('.copy')].map(x => x.dataset.copy);
      const wide = [...document.querySelectorAll('.wrap *')].filter(e => { const q = e.getBoundingClientRect(); return q.width > 0 && q.right > window.innerWidth + 1 && !e.closest('.tablewrap,nav'); }).slice(0, 5).map(e => e.tagName + '.' + e.className);
      const keys = [...document.querySelectorAll('.check input')].map(i => i.dataset.k);
      return {
        scrollW: document.documentElement.scrollWidth, wide, copies: ids.length,
        dupCopies: ids.filter((x, n) => ids.indexOf(x) !== n),
        missingPre: ids.filter(x => !document.getElementById(x)),
        badLinks: [...document.querySelectorAll('nav a, .map a')].filter(a => a.getAttribute('href').startsWith('#') && !document.querySelector(a.getAttribute('href'))).map(a => a.getAttribute('href')),
        filledInputs: [...document.querySelectorAll('[data-in]')].filter(i => i.value !== '').map(i => i.dataset.in),
        dupKeys: keys.filter((k, n) => keys.indexOf(k) !== n),
        inputs: [...document.querySelectorAll('[data-in]')].map(i => i.dataset.in),
      };
    });
    const tokenProblems = [];
    for (const k of r.inputs) {
      const before = await p.evaluate(k => [...document.querySelectorAll('[data-v="' + k + '"]')].map(e => e.textContent), k);
      if (!before.length) { tokenProblems.push(k + ': 이 칸을 쓰는 파란 글자가 없음'); continue; }
      await p.fill('[data-in="' + k + '"]', '점검값' + k); await p.waitForTimeout(60);
      const after = await p.evaluate(k => [...document.querySelectorAll('[data-v="' + k + '"]')].map(e => e.textContent), k);
      if (!after.every(t => t.includes('점검값' + k))) tokenProblems.push(k + ': 넣은 글자가 파란 글자에 안 들어감');
      await p.fill('[data-in="' + k + '"]', ''); await p.waitForTimeout(60);
      const back = await p.evaluate(k => [...document.querySelectorAll('[data-v="' + k + '"]')].map(e => e.textContent), k);
      if (back.join('|') !== before.join('|')) tokenProblems.push(k + ': 지워도 처음 값으로 안 돌아감');
    }
    const problems = [];
    if (r.scrollW > w || r.wide.length) problems.push('옆으로 넘침 ' + JSON.stringify(r.wide));
    if (r.dupCopies.length) problems.push('복사 상자 이름 겹침 ' + r.dupCopies.join(','));
    if (r.missingPre.length) problems.push('복사 상자에 글 없음 ' + r.missingPre.join(','));
    if (r.badLinks.length) problems.push('메뉴 링크가 가리키는 곳 없음 ' + r.badLinks.join(','));
    if (r.filledInputs.length) problems.push('처음부터 글자가 든 입력 칸 ' + r.filledInputs.join(','));
    if (r.dupKeys.length) problems.push('체크 저장 키 겹침 ' + r.dupKeys.join(','));
    problems.push(...tokenProblems);
    if (errs.length) problems.push('화면 오류 ' + JSON.stringify(errs));
    bad += problems.length;
    console.log(`${w} ${scheme}: 복사 상자 ${r.copies}개, 입력 칸 ${r.inputs.length}개 → ${problems.length ? '걸린 것 ' + problems.length + '개' : '통과'}`);
    problems.forEach(x => console.log('  - ' + x));
    await ctx.close();
  }
  await b.close();
  process.exit(bad ? 1 : 0);
})();
