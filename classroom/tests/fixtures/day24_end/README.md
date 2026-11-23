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

## 11/23에 더한 것 · 설계 먼저 스킬

- 네 폴더의 `_claude/skills/design-first/SKILL.md`에 학생용 스킬 원본(`classroom/student-kit/design-first/SKILL.md`)을 넣었어요. 11/24 설치 상자를 보낸 학생 폴더와 같아요.
- 이 폴더들은 11/22에 "설계 먼저" 전의 Day 24 상자로 만든 것이라 `docs/design/aibutton_조사.md`가 없고, spec.md에 기능 태그·바꿀 파일·위험 칸이 없어요. 11/23 판 Day 24 상자로 돌린 폴더 모습은 `classroom/tests/design-first-test-results.md` 2차 표에 있어요. 11/27 상자가 이 칸들을 읽게 되면 Day 24의 P13-1·P13-2를 먼저 한 번 돌리고 시작해요.

## 쓰는 법

```bash
classroom/tests/fixtures/day24_end/restore.sh fx_md /경로/시험폴더/fx_md
export TOK="$(cat classroom/tests/fixtures/day24_end/fx_md/persona.json)"   # 칸을 비운 학생이면 TOK 없이
cd /경로/시험폴더/fx_md && python3 <저장소>/classroom/tools/runchain.py <새 가이드.html> . ../결과.json p00 ...
```

- 시험 기록은 `classroom/tests/day24-test-results.md`, 버튼 점검은 `node classroom/tools/check_aibutton.js <폴더>/mvp.html`이에요.
