// Vercel 서버 함수: 확인할 글을 Gemini에 보내 답을 돌려준다. 키는 환경 변수 GEMINI_API_KEY에만 둔다.
const TEMPLATE = "너는 꼼꼼한 검수 담당이야. 아래 글을 보내기 전에 기준대로 확인해 줘.\n\n회사·고객: 컬리 / 새벽배송 식료품 / 장 볼 시간이 없는 맞벌이 직장인\n\n참고 자료:\n- 이번 주 패턴: ① 첫 문장에 '지금·오늘' ② 이미지 한 장·메시지 하나 ③ 구체적 혜택 자리\n- 고객에게 할 말: \"퇴근하고 장 볼 시간 없어도, 밤에 담으면 아침에 문 앞에 와 있어요.\"\n\n기준 여섯 개:\n① 첫 문장만 읽어도 무슨 소식(어떤 종류·무엇이 달라졌나)인지 보인다.\n② 2~3문장, 문장마다 소식 하나, 쉬운 말이라 한눈에 읽히고 실제 주간 리포트에 섞여도 어색하지 않다.\n③ 이번 주 패턴 가운데 하나(지금·오늘 첫 문장 / 한 가지 메시지 / 구체적 혜택 자리)가 보인다.\n④ 문구에 넣지 않는 말이 없다: 최고·1위·100%·완벽·무조건·최저가·역대급·단독·완치·부작용 없음, 경쟁사 이름(요약에는 \"경쟁 한 곳\"처럼 쓴다), 효능·건강을 암시하는 말(살 안 찌는·다이어트·체중·혈당·피부 재생 등).\n⑤ 숫자와 날짜마다 바로 뒤에 출처와 조사일이 붙어 있고, [할인율](가정) 같은 자리 표시는 지우거나 채우지 않고 사람이 확인할 칸으로 남아 있다.\n⑥ 우리 회사 이름(컬리)은 글자로만 쓰고 글 앞에 \"수업용\" 표시가 있으며, 실제 사람 이름·계정·연락처가 없다.\n\n답 모양:\n1. 잘된 점 한 줄\n2. 기준마다 \"① ✓\" 또는 \"① 고칠 것: 한 줄\" (①~⑥)\n3. 고칠 것이 있으면 고친 글 한 번\n4. 마지막 줄은 셋 중 하나:\n   - \"판정: 보내도 돼요\" — 모두 ✓\n   - \"판정: 고쳐서 다시\" — 글만 고치면 되는 것\n   - \"판정: 보류(사람 확인)\" — 출처 없는 숫자, 효능·건강을 암시하는 말, 실제 행사인지 모르는 기간·수량 한정(오늘만·품절 임박), 자리 표시처럼 사람이 사실을 확인해야 하는 것이 하나라도 있으면. 이것이 먼저.\n판정은 붙여 준 글만 보고 정해. 네가 고친 글은 판정에 넣지 마.\n\n확인할 글:\n{{글}}\n";

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'POST로만 보낼 수 있어요' });
  }
  const origin = req.headers.origin;
  if (origin) {
    let originHost = '';
    try { originHost = new URL(origin).host; } catch (e) { originHost = ''; }
    if (originHost !== req.headers.host) {
      return res.status(403).json({ error: '이 사이트에서만 쓸 수 있어요' });
    }
  }
  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = {}; }
  }
  const text = body && typeof body.text === 'string' ? body.text.trim() : '';
  if (!text) {
    return res.status(400).json({ error: '확인할 글을 먼저 붙여요' });
  }
  if (text.length > 2000) {
    return res.status(400).json({ error: '글은 2,000자까지만 확인할 수 있어요' });
  }
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    return res.status(500).json({ error: '서버에 키가 없어요' });
  }
  const model = process.env.GEMINI_MODEL || 'gemini-flash-latest';
  const prompt = TEMPLATE.split('{{글}}').join(text);
  let reply;
  try {
    reply = await fetch(
      'https://generativelanguage.googleapis.com/v1beta/models/' + encodeURIComponent(model) + ':generateContent',
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-goog-api-key': apiKey },
        body: JSON.stringify({ contents: [{ role: 'user', parts: [{ text: prompt }] }] }),
      }
    );
  } catch (e) {
    return res.status(502).json({ error: 'AI에 연결하지 못했어요' });
  }
  if (reply.status === 429) {
    return res.status(429).json({ error: '하루 쓸 수 있는 양을 다 썼어요' });
  }
  if (!reply.ok) {
    return res.status(502).json({ error: 'AI가 답하지 못했어요(' + reply.status + ')' });
  }
  let data;
  try { data = await reply.json(); } catch (e) { data = null; }
  const parts = data && data.candidates && data.candidates[0] && data.candidates[0].content && data.candidates[0].content.parts;
  const answer = Array.isArray(parts) ? parts.map((p) => (p && typeof p.text === 'string' ? p.text : '')).join('') : '';
  if (!answer.trim()) {
    return res.status(502).json({ error: 'AI가 빈 답을 보냈어요' });
  }
  return res.status(200).json({ answer: answer });
};
