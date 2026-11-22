// 접기·형광펜 점검 (11/21부터 모든 가이드): node classroom/tools/verify_fold.js <가이드.html>
// 폰 폭(390)에서 쪽 높이, 형광펜 수(보이는 것), 잘린 긴 상자의 복사 글이 전체 글과 같은지(눌러서 클립보드로 확인), "상자 글 전체 보기" 단추, 화면 오류를 본다.
// 접힌 칸 안 상자는 verify_box_copy.js로 따로. 접힌 칸 안의 리모컨 링크(#fold, #r1)가 칸을 펴는지도 여기서 본다.
// 접기·형광펜 점검: 전체 높이, 형광펜 수, 잘린 상자의 복사 글이 전체 글과 같은지, 링크로 접힌 칸이 펴지는지
const { chromium } = require('playwright');
(async () => {
  const [src] = process.argv.slice(2);
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 900 }, deviceScaleFactor: 1, permissions: ['clipboard-read', 'clipboard-write'] });
  const p = await ctx.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + src);
  await p.waitForTimeout(500);
  const info = await p.evaluate(() => {
    const clipped = [...document.querySelectorAll('.copy.clip')];
    const bad = clipped.filter(c => { const pre = c.querySelector('pre'); return pre.innerText.replace(/\s+/g, '') !== pre.textContent.replace(/\s+/g, ''); }).map(c => c.dataset.copy);
    const hl = [...document.querySelectorAll('mark.hl')];
    const hlVisible = hl.filter(m => m.getClientRects().length > 0).length;
    const peeks = document.querySelectorAll('.peek').length;
    return { height: document.body.scrollHeight, clipped: clipped.map(c => c.dataset.copy), bad, hl: hl.length, hlVisible, peeks,
             folds: document.querySelectorAll('details.fold, details.more').length };
  });
  // 잘린 상자 하나를 실제로 눌러 클립보드 글이 전체 글과 같은지
  let clipOk = null;
  if (info.clipped.length) {
    const id = info.clipped[0];
    await p.click(`.copy[data-copy="${id}"]`);
    await p.waitForTimeout(300);
    const got = await p.evaluate(() => navigator.clipboard.readText());
    const full = await p.evaluate(i => document.getElementById(i).textContent, id);
    clipOk = got.replace(/\s+/g, '') === full.replace(/\s+/g, '');
  }
  // 펴기 단추
  let peekOk = null;
  if (info.peeks) {
    peekOk = await p.evaluate(() => { const b = document.querySelector('.peek'); const c = b.previousElementSibling; const h0 = c.getBoundingClientRect().height; b.click(); const h1 = c.getBoundingClientRect().height; const t = b.textContent; b.click(); const h2 = c.getBoundingClientRect().height; return { h0: Math.round(h0), h1: Math.round(h1), h2: Math.round(h2), label: t }; });
  }
  // 접힌 칸 안을 가리키는 링크를 누르면 펴지는지(#fold, #r1)
  const linkRes = {};
  for (const id of ['fold', 'r1']) {
    const a = await p.$(`a[href="#${id}"]`);
    if (!a) { linkRes[id] = 'no link'; continue; }
    await a.evaluate(el => { for (let q = el; q; q = q.parentElement) if (q.tagName === 'DETAILS') q.open = true; });
    await a.click(); await p.waitForTimeout(400);
    linkRes[id] = await p.evaluate(i => { const e = document.getElementById(i); const d = e.closest('details'); const r = e.getBoundingClientRect(); return { open: d ? d.open : 'not in details', inView: r.top >= 0 && r.top < window.innerHeight }; }, id);
  }
  console.log(JSON.stringify({ ...info, clipOk, peekOk, linkRes, errs }, null, 1));
  await b.close();
})();
