// 쪽 길이 재기(얼마나 접었나): node classroom/tools/measure_blocks.js <가이드.html> <출력.txt>
// 폰 폭(390)에서 섹션마다 덩어리(카드·접는 칸·복사 상자·문단)의 높이를 큰 순서로 적는다. 접는 칸은 닫힌 채로 잰다.
// 폰 폭(390)에서 섹션마다 덩어리(카드·접는 칸·복사 상자·문단)의 높이와 첫 줄을 잰다. 접는 칸은 닫힌 채로.
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 390, height: 900 }, deviceScaleFactor: 1 });
  await p.goto('file://' + src);
  await p.waitForTimeout(500);
  const r = await p.evaluate(() => {
    const res = [];
    document.querySelectorAll('section').forEach(sec => {
      const sh = Math.round(sec.getBoundingClientRect().height);
      const items = [];
      [...sec.children].forEach(c => {
        const h = Math.round(c.getBoundingClientRect().height);
        if (h < 60) return;
        let label = '';
        const hd = c.querySelector('h3, h2, summary, h4');
        if (c.tagName === 'DETAILS') label = '[접힘] ' + (c.querySelector('summary') || {}).textContent;
        else if (hd) label = hd.textContent;
        else label = c.textContent.trim();
        const pres = c.querySelectorAll('pre').length + (c.tagName === 'PRE' ? 1 : 0);
        const dets = c.querySelectorAll('details').length;
        items.push({ h, tag: c.tagName + (c.className ? '.' + c.className.split(' ').join('.') : ''), id: c.id || '', pres, dets, label: label.replace(/\s+/g, ' ').slice(0, 70) });
      });
      res.push({ id: sec.id, h: sh, title: (sec.querySelector('h2') || {}).textContent, items });
    });
    return { total: Math.round(document.body.scrollHeight), res };
  });
  const lines = ['전체 높이 ' + r.total + 'px'];
  r.res.forEach(s => {
    lines.push(`\n== ${s.id} (${s.h}px) ${s.title}`);
    s.items.sort((a, b2) => b2.h - a.h).forEach(i => lines.push(`  ${String(i.h).padStart(5)}  ${i.tag}${i.id ? '#' + i.id : ''} 상자${i.pres} 접힘${i.dets} | ${i.label}`));
  });
  require('fs').writeFileSync(out, lines.join('\n'));
  console.log(out, r.total);
  await b.close();
})();
