// 접힌 칸 안 복사 상자 점검: node classroom/tools/verify_box_copy.js <가이드.html> <상자 id>
// 상자가 든 접는 칸을 펴고 눌러서, 클립보드 글이 상자 전체 글과 같은지 보고, #fold·#r1 링크가 접힌 칸 안 상자로 가는지 본다.
const { chromium } = require('playwright');
(async () => {
  const [src, boxId] = process.argv.slice(2);
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 900 }, deviceScaleFactor: 1, permissions: ['clipboard-read', 'clipboard-write'] });
  const p = await ctx.newPage();
  await p.goto('file://' + src); await p.waitForTimeout(400);
  // 1) 접힌 칸 안 상자: 사람이 펴는 것처럼 그 칸을 펴고 눌러 복사
  await p.evaluate(i => { for (let q = document.getElementById(i); q; q = q.parentElement) if (q.tagName === 'DETAILS') q.open = true; }, boxId);
  await p.waitForTimeout(200);
  await p.click(`.copy[data-copy="${boxId}"]`); await p.waitForTimeout(300);
  const got = await p.evaluate(() => navigator.clipboard.readText());
  const full = await p.evaluate(i => document.getElementById(i).textContent, boxId);
  const same = got.replace(/\s+/g, '') === full.replace(/\s+/g, '');
  // 2) 링크로 접힌 칸 안 상자로 가기(부드러운 스크롤이 끝날 때까지 기다림)
  await p.goto('file://' + src); await p.waitForTimeout(400);
  const res = {};
  for (const id of ['fold', 'r1']) {
    const a = await p.$(`a[href="#${id}"]`);
    await a.evaluate(el => { for (let q = el; q; q = q.parentElement) if (q.tagName === 'DETAILS') q.open = true; });
    await a.click(); await p.waitForTimeout(2500);
    res[id] = await p.evaluate(i => { const e = document.getElementById(i); const r = e.getBoundingClientRect(); return { open: e.closest('details').open, top: Math.round(r.top) }; }, id);
  }
  console.log(boxId, '복사 같음', same, '글자', full.length, JSON.stringify(res));
  await b.close();
})();
