// 시험에서 나온 화면(mvp.html 같은 것)을 갤러리용으로 폰 폭에서 찍기: node classroom/tools/shot_screen.js <화면.html> <출력.jpg>
// 390x700, 밝은 화면, JPEG 품질 72(한 장 30KB 안팎). 가로 넘침과 화면 오류도 같이 알려 준다.
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  if (!src || !out) { console.log('쓰는 법: node shot_screen.js <화면.html> <출력.jpg>'); process.exit(1); }
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 700 }, colorScheme: 'light', deviceScaleFactor: 1 });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(src)); await p.waitForTimeout(800);
  const info = await p.evaluate(() => ({ scrollW: document.documentElement.scrollWidth, title: document.title }));
  await p.screenshot({ path: out, type: 'jpeg', quality: 72 });
  console.log(out, JSON.stringify(info), errs.length ? '화면 오류 ' + JSON.stringify(errs) : '');
  await b.close();
})();
