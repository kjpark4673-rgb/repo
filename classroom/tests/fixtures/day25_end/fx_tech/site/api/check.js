// Vercel 서버 함수: 화면에서 보낸 글과 기준 사실을 Gemini로 확인한다. 키는 환경 변수 GEMINI_API_KEY에만 둔다.
// 틀(PROMPT)은 화면(index.html)의 id="aic-prompt"(v2)와 같은 글이다. 한쪽을 고치면 다른 쪽도 고친다.
// 키와 받은 글은 로그에 남기지 않는다.
const PROMPT = "너는 꼼꼼한 검수 담당이야. 아래 글을 보내기 전에 기준대로 확인해 줘. 답은 한국어로 쉽게 써 줘.\n\n[회사·고객] 컬리 / 새벽배송 식료품 / 장 볼 시간이 없는 맞벌이 직장인\n\n[참고 자료]\n- 이번 주 패턴: 지금·오늘 첫 문장 / 이미지 한 장 / 구체적 혜택 자리\n- 고객에게 할 말: \"퇴근하고 장 볼 시간 없어도, 밤에 담으면 아침에 문 앞에 와 있어요.\"\n\n[기준 여섯 개]\n① 첫 문장에 무엇의 요약인지(대상·조사 날짜)가 보인다.\n② 두 문장 안, 쉬운 말이라 폰에서 한눈에 읽힌다.\n③ 이번 주 패턴(지금·오늘 첫 문장 / 이미지 한 장 / 구체적 혜택 자리) 가운데 하나가 글의 말이나 내용으로 나온다. 경쟁사 소식으로 나와도 된다.\n④ 문구에 넣지 않는 말(최고·1위·100%·완벽·무조건·최저가·역대급·단독·완치·부작용 없음)과 경쟁사 이름, 효능을 암시하는 말(살 안 찌는·다이어트·체중·혈당·피부 재생 같은 것)이 없다.\n⑤ 숫자는 출처와 조사일이 글에 함께 있거나 숫자가 없고(조사 날짜와 \"경쟁 5곳\"처럼 조사 범위를 말하는 수는 숫자로 세지 않는다), 오늘만·품절 임박은 실제 행사가 적혀 있을 때만 있으며, 우리 행사 숫자는 [할인율](가정) 같은 자리 표시로 둔다. 기준 사실이 있으면 글의 날짜·시간·장소·수량·가격이 기준 사실과 같은지 본다.\n⑥ 컬리 이름은 글자로만 쓰고, 다른 회사 문구를 그대로 옮기지 않았고 실제 로고·포장 흉내가 없다.\n\n[답 모양]\n1. 잘된 점 한 줄을 먼저 써.\n2. 기준마다 \"① ✓\" 또는 \"① 고칠 것: 한 줄\"로 ①부터 ⑥까지 써.\n3. 고칠 것이 있으면 고친 글을 한 번 써.\n4. 마지막 줄은 셋 중 하나만 써: \"판정: 보내도 돼요\"(모두 ✓) / \"판정: 고쳐서 다시\"(글만 고치면 되는 것) / \"판정: 보류(사람 확인)\".\n- 보류가 먼저야: 출처 없는 숫자, 효능·건강을 암시하는 말, 실제 행사인지 모르는 기간·수량 한정(오늘만·품절 임박), [할인율](가정) 같은 자리 표시처럼 사람이 사실을 확인해야 하는 것이 하나라도 있으면 보류야.\n- 보류는 위에 적은 경우만이야. 금지어나 길이처럼 글만 고치면 되는 것만 있으면 \"판정: 고쳐서 다시\"야.\n- 판정은 아래 붙여 준 글만 보고 정해. 네가 고친 글은 판정에 넣지 마.\n- 글의 날짜·시간·장소·수량·가격이 기준 사실에 있고 같으면 ✓야(출처가 있는 것으로 봐).\n- 기준 사실과 다르면 \"고칠 것: 글의 값 → 기준 사실의 값\"으로 적고 판정은 \"고쳐서 다시\"야.\n- 기준 사실에 없는 숫자·기간이나 수량 한정·효능은 위처럼 \"보류(사람 확인)\"야. 기준 사실이 (없음)이면 모두 위 규칙대로만 봐.\n\n기준 사실:\n{{사실}}\n\n확인할 글:\n{{글}}";
const MAX = 2000;
const FACTS_MAX = 1000;

// 같은 주소(IP)에서 1분에 10번까지만 받는다.
// 서버 메모리에 세는 간단한 방식이라, 서버가 새로 뜨면(배포·잠든 뒤 다시 깨어남) 0부터 다시 센다.
// Vercel은 서버를 여러 개 띄울 수 있어서 정확한 한도가 아니라 지나친 호출을 막는 울타리다.
const WINDOW_MS = 60 * 1000;
const LIMIT = 10;
const hits = new Map();

function clientIp(req) {
  const fwd = req.headers['x-forwarded-for'];
  if (typeof fwd === 'string' && fwd) return fwd.split(',')[0].trim();
  return (req.socket && req.socket.remoteAddress) || 'unknown';
}

function tooMany(ip, now) {
  if (hits.size > 5000) {
    for (const [k, v] of hits) { if (now - v.start >= WINDOW_MS) hits.delete(k); }
  }
  let h = hits.get(ip);
  if (!h || now - h.start >= WINDOW_MS) { h = { start: now, count: 0 }; hits.set(ip, h); }
  h.count += 1;
  return h.count > LIMIT;
}

function send(res, code, obj) {
  res.statusCode = code;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.end(JSON.stringify(obj));
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return send(res, 405, { error: 'POST로만 쓸 수 있어요' });
  }

  const origin = req.headers.origin;
  if (origin) {
    let same = false;
    try { same = new URL(origin).host === req.headers.host; } catch (e) { same = false; }
    if (!same) return send(res, 403, { error: '이 사이트에서만 쓸 수 있어요' });
  }

  if (tooMany(clientIp(req), Date.now())) {
    res.setHeader('Retry-After', '60');
    return send(res, 429, { error: '잠시 뒤에 다시 해요' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = null; }
  }
  if (!body || typeof body !== 'object') body = {};
  if (body.text !== undefined && body.text !== null && typeof body.text !== 'string') {
    return send(res, 400, { error: '확인할 글(text)은 글자로 보내요' });
  }
  if (body.facts !== undefined && body.facts !== null && typeof body.facts !== 'string') {
    return send(res, 400, { error: '기준 사실(facts)은 글자로 보내요' });
  }
  const text = typeof body.text === 'string' ? body.text.trim() : '';
  const facts = typeof body.facts === 'string' ? body.facts.trim() : '';
  if (!text) return send(res, 400, { error: '확인할 글을 먼저 붙여요' });
  if (text.length > MAX) return send(res, 400, { error: '글이 너무 길어요. 2,000자 안으로 줄여요' });
  if (facts.length > FACTS_MAX) return send(res, 400, { error: '기준 사실이 너무 길어요. 1,000자 안으로 줄여요' });

  const key = process.env.GEMINI_API_KEY;
  if (!key) return send(res, 500, { error: '서버에 키가 없어요' });
  const model = process.env.GEMINI_MODEL || 'gemini-flash-latest';

  // 붙인 글이 다시 바뀌지 않게: 틀을 {{글}}로 먼저 나누고, 조각마다 {{사실}}을 바꾼 뒤 글로 잇는다(화면 버튼과 같은 방식).
  const pieces = PROMPT.split('{{글}}').map(p => p.split('{{사실}}').join(facts || '(없음)'));
  const prompt = pieces.join(text);
  let r;
  try {
    r = await fetch('https://generativelanguage.googleapis.com/v1beta/models/' + encodeURIComponent(model) + ':generateContent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
      body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
    });
  } catch (e) {
    return send(res, 502, { error: 'AI에 연결하지 못했어요' });
  }
  if (r.status === 429) return send(res, 429, { error: '하루 쓸 수 있는 양을 다 썼어요' });
  if (!r.ok) return send(res, 502, { error: 'AI가 답하지 못했어요(' + r.status + ')' });

  let data;
  try { data = await r.json(); } catch (e) { data = null; }
  const parts = data && data.candidates && data.candidates[0] && data.candidates[0].content && data.candidates[0].content.parts;
  const answer = Array.isArray(parts) ? parts.map(p => (p && typeof p.text === 'string' ? p.text : '')).join('') : '';
  if (!answer.trim()) return send(res, 502, { error: 'AI 답이 비었어요' });
  return send(res, 200, { answer });
};
