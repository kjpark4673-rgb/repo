// 패턴 브리핑 영상 만들기: node scripts/make_brief_video.mjs 1125
// patterns_MMDD.md와 creatives_MMDD.csv를 읽어 ad15/props.json을 만들고 PatternBrief를 렌더한다.
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const day = process.argv[2];
if (!/^\d{4}$/.test(day || '')) {
  console.error('날짜를 월일 네 자리로 넣어 주세요. 예: node scripts/make_brief_video.mjs 1125');
  process.exit(1);
}
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = (name) => {
  const p = path.join(root, name);
  if (!fs.existsSync(p)) return null;
  return fs.readFileSync(p, 'utf8').replace(/^﻿/, '');
};

const md = read(`patterns_${day}.md`);
const csv = read(`creatives_${day}.csv`);
if (!md || !csv) {
  console.error(`patterns_${day}.md 또는 creatives_${day}.csv가 없어요.`);
  process.exit(1);
}

// creatives 줄 수(머리줄 빼고, 따옴표 안 줄바꿈은 한 줄로 침)
let rows = 0, inQ = false, cur = '';
for (const ch of csv) {
  if (ch === '"') inQ = !inQ;
  if (ch === '\n' && !inQ) { if (cur.trim()) rows++; cur = ''; } else cur += ch;
}
if (cur.trim()) rows++;
rows -= 1;

// 이번 주 쓸 패턴 3개(추천)
const rec = md.split(/^## .*이번 주 쓸 패턴/m)[1] || '';
const picks = [...rec.matchAll(/^\d+\.\s*\*\*패턴\s*(\d+)\s*([^*]+?)\*\*/gm)].slice(0, 3);
const patterns = picks.map(([, n, name]) => {
  const sec = md.split(new RegExp(`^### 패턴 ${n}\\.`, 'm'))[1] || '';
  const m = sec.match(/오래 돈 묶음\s*(\d+)개 중\s*(\d+)개\s*·\s*나머지 묶음\s*(\d+)개 중\s*(\d+)개/);
  if (!m) throw new Error(`패턴 ${n}의 묶음 숫자를 못 찾았어요.`);
  const [, lt, lh, rt, rh] = m.map(Number);
  return {
    name: name.trim(),
    longPct: Math.round((lh / lt) * 100),
    restPct: Math.round((rh / rt) * 100),
    longText: `${lt}개 중 ${lh}개`,
    restText: `${rt}개 중 ${rh}개`,
  };
});
if (patterns.length === 0) throw new Error('추천 패턴을 못 찾았어요.');

const collectedAt = (md.match(/수집일\s*(\d{4}-\d{2}-\d{2})/) || [, '못 찾음'])[1];

// 맨 위 한 줄: brief의 "이번 주 고객에게 할 말", 없으면 CLAUDE.md의 고객
const brief = read(`brief_${day}.md`) || '';
let topLine = (brief.match(/이번 주 고객에게 할 말:\s*\**["“]?([^"”*\n]+)["”]?/) || [])[1];
if (!topLine) topLine = ((read('CLAUDE.md') || '').match(/고객:\s*([^(\n]+)/) || [, '이번 주 무엇이 먹혔나'])[1];

const props = {
  topLine: topLine.trim(),
  title: `이번 주 무엇이 먹혔나 · ${day.slice(0, 2)}/${day.slice(2)}`,
  patterns,
  rows,
  collectedAt,
  source: `creatives_${day}.csv`,
  basis: '게재 일수 기준',
};
const ad15 = path.join(root, 'ad15');
fs.writeFileSync(path.join(ad15, 'props.json'), JSON.stringify(props, null, 2), 'utf8');
console.log('props.json:', JSON.stringify(props));

const r = spawnSync('npx', ['remotion', 'render', 'PatternBrief', `../pattern_brief_${day}.mp4`, '--props=props.json'], {
  cwd: ad15,
  stdio: 'inherit',
  shell: true,
});
process.exit(r.status ?? 1);
