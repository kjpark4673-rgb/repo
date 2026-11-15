// 가이드를 글로 옮기기 (수강생 눈 검토용): node classroom/tools/guide_to_text.js <가이드.html> <출력.txt>
// 접는 칸을 모두 펴고, 입력 칸은 [입력 칸 · 흐린 글씨: …], 그림은 [그림: …], 복사 상자는 <<<복사 상자 시작>>> … <<<복사 상자 끝>>>으로 적는다.
// 검토하는 서브에이전트에게 이 글 파일 경로를 주면 이미지(base64)를 읽느라 토큰을 쓰지 않는다.
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  if (!src || !out) { console.log('쓰는 법: node guide_to_text.js <가이드.html> <출력.txt>'); process.exit(1); }
  const b = await chromium.launch();
  const p = await (await b.newContext({ viewport: { width: 1280, height: 900 } })).newPage();
  await p.goto('file://' + require('path').resolve(src)); await p.waitForTimeout(500);
  const t = await p.evaluate(() => {
    document.querySelectorAll('details').forEach(d => { d.open = true; });
    document.querySelectorAll('[data-in]').forEach(i => { const s = document.createElement('span'); s.textContent = ' [입력 칸 · 흐린 글씨: ' + i.placeholder + '] '; i.after(s); });
    document.querySelectorAll('img').forEach(i => { const s = document.createElement('span'); s.textContent = ' [그림: ' + i.alt + '] '; i.after(s); });
    document.querySelectorAll('svg').forEach(v => { const s = document.createElement('div'); s.textContent = '[그림(SVG) 안의 글자: ' + [...v.querySelectorAll('text')].map(x => x.textContent).join(' / ') + ']'; v.after(s); });
    document.querySelectorAll('pre').forEach(pr => { pr.textContent = '<<<복사 상자 시작: 누르면 이 글이 복사됨>>>\n' + pr.textContent + '\n<<<복사 상자 끝>>>'; });
    return document.body.innerText;
  });
  require('fs').writeFileSync(out, t);
  console.log(out, t.length + '자');
  await b.close();
})();
