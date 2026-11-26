// 키 없이 site/api/check.js를 직접 불러 가짜 req·res로 시험한다.
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire(import.meta.url);
const handler = require('../site/api/check.js');
delete process.env.GEMINI_API_KEY;

function run(req) {
  return new Promise((resolve) => {
    const res = {
      statusCode: 200, headers: {},
      setHeader(k, v) { this.headers[k] = v; },
      end(b) { resolve({ code: this.statusCode, body: b }); }
    };
    handler(req, res);
  });
}
const host = 'my-site.vercel.app';
const cases = [
  ['GET은 405', { method: 'GET', headers: { host } }, 405],
  ['다른 사이트 Origin은 403', { method: 'POST', headers: { host, origin: 'https://other.example' }, body: { text: '시험 글' } }, 403],
  ['빈 글은 400', { method: 'POST', headers: { host }, body: { text: '   ' } }, 400],
  ['2,001자는 400', { method: 'POST', headers: { host }, body: { text: 'ㄱ'.repeat(2001) } }, 400],
  ['키 없음은 500', { method: 'POST', headers: { host, origin: 'https://' + host }, body: { text: '시험 글' } }, 500],
  // v2 (11/27)
  ['facts가 숫자면 400', { method: 'POST', headers: { host }, body: { text: '시험 글', facts: 123 } }, 400],
  ['facts 1,001자는 400', { method: 'POST', headers: { host }, body: { text: '시험 글', facts: 'ㄱ'.repeat(1001) } }, 400],
];
const rows = [];
async function add(name, req, want) {
  const r = await run(req);
  let msg = ''; try { msg = JSON.parse(r.body).error || ''; } catch (e) {}
  rows.push([name, want, r.code, r.code === want ? '✓' : '✗', msg]);
}
for (const [name, req, want] of cases) await add(name, req, want);
// 같은 주소에서 11번 부르기: 1~10번째는 한도 안(키 없음 500), 11번째는 429. 다른 시험과 섞이지 않게 따로 주소를 씀.
const ipReq = () => ({ method: 'POST', headers: { host, 'x-forwarded-for': '203.0.113.7' }, body: { text: '시험 글', facts: '일정표: 시험용' } });
let under = true;
for (let i = 0; i < 10; i++) { const r = await run(ipReq()); if (r.code === 429) under = false; }
rows.push(['같은 주소 1~10번째는 한도 안', '429 아님', under ? '429 아님' : '429', under ? '✓' : '✗', '']);
await add('같은 주소 11번째는 429', ipReq(), 429);
// 틀이 화면(index.html)의 aic-prompt와 같은지
const html = readFileSync(new URL('../site/index.html', import.meta.url), 'utf8');
const tpl = html.match(/<script type="text\/plain" id="aic-prompt">([\s\S]*?)<\/script>/)[1].replace(/^\n+|\n+$/g, '');
const src = readFileSync(new URL('../site/api/check.js', import.meta.url), 'utf8');
const same = src.includes('const PROMPT = ' + JSON.stringify(tpl) + ';');
console.log('| 시험 | 기대 | 실제 | 결과 | 메시지 |\n|---|---|---|---|---|');
for (const r of rows) console.log('| ' + r.join(' | ') + ' |');
console.log('| 틀이 화면과 같음 | 같음 | ' + (same ? '같음' : '다름') + ' | ' + (same ? '✓' : '✗') + ' | |');
process.exit(rows.every(r => r[3] === '✓') && same ? 0 : 1);
