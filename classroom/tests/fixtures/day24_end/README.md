# 11/26(Day 24)를 끝낸 시험용 폴더 (11/27 이후 가이드 시험의 출발점)

> 11/22에 만들었어요. 학생 이름, 학생 작업물, 링크는 들어 있지 않아요. 시험 전용이에요.

## 왜 있나요

`../day23_end/`과 같은 까닭이에요. 새 날짜 가이드를 가상 학생으로 시험하려면 앞날을 끝낸 폴더가 필요한데, 시험 폴더는 그 세션의 임시 폴더라 새 창에는 없어요. 그래서 `day23_end`의 네 폴더에서 Day 24 가이드(3차 시험 판 = 발행 판)를 돌린 결과를 여기에 뒀어요.

## 네 폴더

| 이름 | 직무 · 회사 | 11/26에 지난 길 | 끝난 상태 |
|---|---|---|---|
| `fx_md` | MD · 라라스윗 (확인할 글 "기획전 배너와 상세페이지 첫 화면 문구", 내가 정함) | P0 → P13 → 설계서에서 바꿀 것(예시 2를 반려된 배너 문구로, 내가 정함) → P14(계획 모드) → 계획 승인 → "spec.md의 예시 2 글만 보여줘" → 되돌리기 연습 → 되돌리기 · 고치기 전 판으로 → P15 | 버튼 첫 판, 예시 3개 같음(고친 횟수 0), mvp_oops.html |
| `fx_content` | 콘텐츠 마케터 · 라네즈 | P0 → P13 → 설계서에서 바꿀 것(○○ 그대로 → 멈춤) → 잘 모르겠으면 → P14 → 계획 승인 → P15 | 버튼 첫 판, P15 1번 고침 뒤 세 예시 같음 |
| `fx_ops` | 운영 매니저 · 예시 교육센터(가상) (확인할 글 "수강생에게 보낼 휴강·보강 안내 문자", 원래 화면에 스크립트 있음) | P0 → P13 → P14 → 계획 승인 → 되돌리기 연습 → 되돌리기 · 고치기 전 판으로 → P15 | 버튼 첫 판(원래 스크립트 그대로), mvp_oops.html |
| `fx_tech` | 데이터 분석가 · 컬리 | P0 → P13 → P14 → 계획 승인 → P15 → D 서버 함수 | 버튼 첫 판, site 폴더(index.html, api/check.js), scripts/test_check.mjs, server_guide.md(키 없음, 배포 안 함) |

폴더마다 11/25까지의 파일(`day23_end`과 같음)에 더해 이 파일들이 있어요: `spec.md`(+ `spec_v번호.md`), AI 버튼이 든 `mvp.html`(+ `mvp_v번호.html`), `button_test_1126.md`와 `button_test_1126/예시1~3.txt`, 바뀐 `loop.html`·`run_log.md`·`decisions.md`·`CLAUDE.md`(오늘 규칙 "11/26 AI 버튼"). 11/27 "내일 고칠 것"(tomorrow_1127.md)은 이 폴더들에서 보내지 않았어요(1차 시험 MD·운영 갈래에서만 시험).

## 저장소에 두면서 뺀 것과 바꾼 것

- `day23_end`과 같이 남의 광고 문구(`공통광고_*.csv`, `creatives_1125*.csv`)는 없어요. 영상(mp4)과 node_modules도 뺐어요.
- 사진과 시안 PNG는 `day23_end`에서 줄인 그대로예요.
- `CLAUDE.md`는 `_CLAUDE.md`, `.claude`는 `_claude`로 이름을 바꿔 뒀어요. `restore.sh`가 되돌려요.

## 11/24 새벽에 다시 만듦 · "설계 먼저" 흐름

- 네 폴더를 `day23_end`에서 11/26 가이드(Version 4와 같은 상자)로 다시 돌려 만들었어요: P0 → (테크만 설계 먼저 설치, 나머지는 스킬 원본을 미리 넣음) → P13-1 현장 조사 → P13-2 설계서 → P14(계획 모드) → 계획 승인 → P15 → 내일 고칠 것(잘 모르겠으면) → (테크만 D 카드 서버 함수) → P16. 모두 끝까지 돌았고 네 화면 모두 `check_aibutton.js` 통과.
- 그래서 폴더마다 `_claude/skills/design-first/SKILL.md`, `docs/design/aibutton_조사.md`, 기능 표시([필수]/[선택]/[빼도 됨])·바꿀 파일·위험 칸이 든 `spec.md`, `button_test_1126.md`, `tomorrow_1127.md`가 있어요. 테크에는 `site/`(index.html, api/check.js)와 `scripts/test_check.mjs`도 있어요.
- 출발점이 옛 `day23_end`라 `weekly-research`·`weekly-create` 스킬의 머리말은 옛 꼴(큰따옴표로 시작)인 폴더가 있어요. 11/25 가이드의 "스킬 설명 줄 고치기" 상자를 보낸 학생을 흉내 내려면 되살린 뒤 그 상자를 한 번 보내요.

## 쓰는 법

```bash
classroom/tests/fixtures/day24_end/restore.sh fx_md /경로/시험폴더/fx_md
export TOK="$(cat classroom/tests/fixtures/day24_end/fx_md/persona.json)"   # 칸을 비운 학생이면 TOK 없이
cd /경로/시험폴더/fx_md && python3 <저장소>/classroom/tools/runchain.py <새 가이드.html> . ../결과.json p00 ...
```

- 시험 기록은 `classroom/tests/day24-test-results.md`, 버튼 점검은 `node classroom/tools/check_aibutton.js <폴더>/mvp.html`이에요.
