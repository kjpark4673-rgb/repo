// 가상 학생 시험에서 나온 화면(HTML)을 브라우저로 실제로 열어, 스크립트 오류와 폰 폭 넘침이 없는지 본다.
// 사용: node classroom/tools/check_outputs.js <화면.html> [화면2.html ...]
// 왜: 프롬프트가 "코드를 읽고" 점검하거나 고친 화면은 문법 오류 하나로 빈 화면이 될 수 있고, 시험기(runchain.py)는 파일이 생겼는지만 본다.
//     Day 17 시험에서 한 갈래의 mvp.html이 정규식 오류로 빈 화면이었는데 자동 점검 프롬프트가 두 번 놓쳤다.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); let bad = 0;
  for (const f of process.argv.slice(2)) {
    const pg = await b.newPage({ viewport: { width: 390, height: 800 } }); const errs = [];
    pg.on('pageerror', e => errs.push(String(e.message).slice(0, 100)));
    await pg.goto('file://' + path.resolve(f)); await pg.waitForTimeout(400);
    const r = await pg.evaluate(() => ({ over: document.documentElement.scrollWidth - window.innerWidth, btn: document.querySelectorAll('button').length, txt: document.body.innerText.trim().length }));
    const n = Math.min(r.btn, 8); for (let i = 0; i < n; i++) { try { await pg.locator('button').nth(i).click({ timeout: 800 }); } catch (e) {} }
    await pg.waitForTimeout(200);
    const ok = !errs.length && r.over <= 0 && r.txt > 0; if (!ok) bad++;
    console.log((ok ? '통과' : '걸림'), f.split('/').slice(-2).join('/'), '| 넘침', r.over, '| 버튼', r.btn, '| 글자', r.txt, '|', errs[0] || '오류 없음');
    await pg.close();
  }
  await b.close(); process.exit(bad ? 1 : 0);
})();
