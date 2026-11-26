# aibutton 현장 조사 (11/26, 1단계)

## 1. 요청 조건 (그대로)
- 버튼이 하는 일: 사람이 보내기 전의 글을 화면에 붙이고 버튼을 누르면 "기준대로 확인해 줘"라는 글이 만들어져 복사되고, 그 글을 AI(Claude나 ChatGPT) 새 채팅에 붙이면 기준마다 ✓ 또는 "고칠 것"과 판정이 온다.
- 계획 모드로 만든다. API 키는 화면에 넣지 않는다. 원래 화면의 글·기능·스크립트는 그대로 둔다.
- 조사 보고서에 꼭 적을 것: 버튼을 넣을 화면 파일(CLAUDE.md의 MVP 줄에 적힌 화면, 없으면 mvp.html)과 그 안의 스크립트 변수·함수·id·스타일 이름(새 칸과 부딪힐 것), 이 화면을 읽거나 링크하는 파일(loop.html, weekly.html 같은 것), review_1125.md의 기준이 그림을 보는지 글을 보는지, 내 컴퓨터 파일(file://)로 열 때 복사가 막힐 수 있는 곳, 이름에 _v가 붙은 지난 판.
- 설계서 파일: 이 폴더의 spec.md (지금 없음). 이름: aibutton.

## 2. 읽은 파일과 거기서 안 것
- CLAUDE.md: MVP 줄은 `mvp.html / 조사형 / 따라잡기 원본: 없음`. 그래서 버튼을 넣을 화면은 **mvp.html**. 오늘 규칙: 화면은 더하기만, 스크립트는 함수 하나로 감싸기, top·name·status·parent 변수 금지, 390px에서 옆으로 안 밀리기, 키는 화면에 넣지 않고 AI 버튼은 "글 만들어 복사"까지, spec.md를 먼저 읽고 다르면 같이 고치기.
- mvp.html (3.4KB):
  - **스크립트 없음**(`<script>` 0개). 변수·함수 이름은 비어 있음.
  - id 없음. class: `top`, `sub`(p.sub), `scroll`, `note`. 요소: h1, table(thead·tbody), a.
  - CSS 변수: `--bg --fg --mute --line --accent --warn --warnfg`. 다크 모드 있음(prefers-color-scheme).
  - 스타일 규칙: `*`, `body`(padding 0 16px), `.top`, `h1`, `p.sub`, `.scroll`, `table`(min-width 720px), `th,td`, `th`, `tr:last-child td`, `a`, `.note`.
  - 표는 `.scroll` 안에서만 옆으로 밀림(min-width 720px). 칸 밖은 폰 폭에서 안 밀림.
  - 내용: 컬리 새벽배송 경쟁사 5곳 소식 표, 조사일 2026-11-22.
- review_1125.md: 기준 ①~⑥은 weekly-create 스킬 6번(심사)에서 온 것이고 **시안 그림(ad_MMDD_*.png)을 보고** 판정함. 글만 보는 게 아님.
  - ① 첫 1초에 무엇을 파는지 보인다 ② 헤드라인이 폰에서 한눈에 읽힌다 ③ brief의 패턴이 보인다 ④ 문구에 넣지 않는 말이 없다 ⑤ 실제 피드에 섞여도 어색하지 않다 ⑥ 회사 이름과 "수업용 시안", 실제 로고 흉내 없음.
  - 글만 붙여 넣는 "보내기 전 확인"에는 **① ⑤처럼 그림을 봐야 하는 기준을 그대로 쓸 수 없음.** ② 일부, ④, ⑥ 일부는 글로 판정 가능.
- spec.md: 없음. brief_1125.md, patterns_1125.md: 이번 조사에서는 훑지 않음(기준 출처는 SKILL.md와 review_1125.md로 충분).

## 3. 이미 있는 것 (다시 만들지 않을 것)
- 문구에 넣지 않는 말 목록과 숫자·효능 규칙: CLAUDE.md "오늘 규칙 (11/26 AI 버튼)"에 있음 → 버튼이 만드는 글에 그대로 가져다 씀.
- 6개 기준의 틀(✓ 또는 "고칠 것: 한 줄", 잘된 점 한 줄): weekly-create SKILL.md 6번.
- 다크 모드와 CSS 변수(--accent 등): 새 칸이 그대로 씀.

## 4. 벽 속 수도관
- **mvp.html 읽는 파일**: loop.html(46·57·69·77·96줄)이 글로 "mvp.html"을 적음. `href="mvp.html"` 링크는 loop.html·weekly.html 모두 없음. 제목 "컬리 새벽배송 경쟁사 동향"과 표 5곳·날짜 칸을 설명하므로 **제목·표 칸 이름(회사·최근 소식 한 줄·날짜)을 바꾸면 안 됨**(loop.html 69줄 통과 기준).
- weekly-research 스킬이 CLAUDE.md의 "MVP: 파일 / 갈래" 줄을 읽음 → **그 줄 모양을 바꾸지 말 것**. weekly-create 스킬은 "나와 회사"와 맨 아래 "# 오늘 규칙 (…)"을 읽음 → 제목 모양 유지.
- 새 칸과 부딪힐 이름(mvp.html 안): class `top` `sub` `scroll` `note`, 태그 규칙 `table` `th` `td` `a` `h1` `body`, CSS 변수 `--bg --fg --mute --line --accent --warn --warnfg`. 새 칸 class·id는 `ab-`처럼 접두어를 붙여 피할 것. 스크립트가 없으니 변수 충돌은 없지만, 새로 넣을 스크립트는 함수 하나로 감싸고 top·name·status·parent 금지.
- 지난 판: `mvp_v*.html` 없음. 이름에 _v가 붙은 것은 CLAUDE_v1·v2·v3.md, loop_v1.html, weekly-create/SKILL_v1.md. mvp.html을 고치기 전에 **mvp_v1.html**로 남겨야 함. spec.md도 이미 있으면 spec_v번호로 남김(지금은 없음).
- 파일 `file://` 복사: `navigator.clipboard.writeText`는 보안 문맥(https·localhost)에서만 되고, 내 컴퓨터에서 파일을 바로 열면(file://) 브라우저에 따라 막히거나 거부될 수 있음(Chrome은 file://을 대체로 허용하나 확실하지 않음, 못 확인). 폰이나 메신저 앱 안 브라우저에서 열 때도 막힐 수 있음. 막히면 `textarea` 선택 + `document.execCommand('copy')`로 물러나고, 그것도 안 되면 만든 글을 상자에 보여 주며 "직접 길게 눌러 복사" 안내를 둠.
- 규칙 부딪힘: 설계서 위치는 요청의 spec.md(폴더 바로 아래), 스킬 기본은 docs/design/(이름)_설계서.md. 요청이 먼저이므로 spec.md.

## 5. 정할 것 (보기와 추천)
1. 기준 내용
   - A. 6개 기준에서 글로 되는 것만 골라 새 기준을 씀(문구 금지어·숫자 출처·효능 암시·경쟁사 이름·기간 한정·[자리](가정) 표시) — **추천**
   - B. review_1125의 ①~⑥ 그대로 → 그림 기준이 글에는 맞지 않음
   - C. 사람이 화면에서 기준을 직접 입력
2. 새 칸 위치
   - A. 표 아래, `.note` 다음 — 원래 화면을 안 건드림 **추천**
   - B. 제목 아래(표 위) — 표가 밀려 loop.html 69줄 "바로 보인다"가 흔들림
3. 복사 방식
   - A. clipboard API → 안 되면 execCommand → 안 되면 상자에서 직접 복사 안내 **추천**
   - B. clipboard API만
4. 키·서버: 화면에서 답을 받는 일은 이번에 하지 않음(글 만들어 복사까지). 서버 함수는 나중 보기.

## 6. 아직 못 한 것
- brief_1125.md, patterns_1125.md 본문은 읽지 않음. 제작 단계 전에 spec.md를 쓸 때 필요하면 읽음.
