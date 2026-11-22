import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const require = createRequire(import.meta.url);
const here = path.dirname(fileURLToPath(import.meta.url));
const handler = require(path.join(here, '..', 'site', 'api', 'check.js'));

function fakeRes() {
  const r = { code: 200, body: null, headers: {} };
  r.setHeader = (k, v) => { r.headers[k] = v; };
  r.status = (c) => { r.code = c; return r; };
  r.json = (b) => { r.body = b; return r; };
  return r;
}
delete process.env.GEMINI_API_KEY;
const cases = [
  ['GET은 405', { method: 'GET', headers: {}, body: null }, 405, null],
  ['다른 사이트 Origin은 403', { method: 'POST', headers: { origin: 'https://other.example', host: 'mine.example' }, body: { text: '글' } }, 403, 'KEY'],
  ['빈 글은 400', { method: 'POST', headers: { host: 'mine.example' }, body: { text: '   ' } }, 400, 'KEY'],
  ['2,001자는 400', { method: 'POST', headers: { host: 'mine.example' }, body: { text: 'ㄱ'.repeat(2001) } }, 400, 'KEY'],
  ['키 없음은 500', { method: 'POST', headers: { host: 'mine.example' }, body: { text: '확인할 글' } }, 500, null],
];
const rows = [];
for (const [label, req, want] of cases) {
  const res = fakeRes();
  await handler(req, res);
  rows.push({ 시험: label, 기대: want, 실제: res.code, 결과: res.code === want ? '✓' : '✗', 이유: res.body && res.body.error });
}
delete process.env.GEMINI_API_KEY;
console.table(rows);
process.exit(rows.every((r) => r.결과 === '✓') ? 0 : 1);
