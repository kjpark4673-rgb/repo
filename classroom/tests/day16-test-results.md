# Day 16 프롬프트 시험 결과 (2판, 2026-11-13 밤)

가이드(`classroom/student-guide/day16.html`)의 복사 박스를 그대로 뽑아 Claude Code로 실행했습니다. 시험기는 `classroom/tools/runchain.py`입니다. `+`가 붙은 단계는 앞 대화에 이어서 넣은 것입니다.

- 실행 55회, 모델은 claude-sonnet-5-5(검색 요약에 claude-haiku-5-5), 도구가 계산한 사용량은 합계 약 $12.81입니다.
- **P와 T 박스 15개는 모두 최종 문구로 통과했습니다.** 통과 기준은 약속한 파일이 생긴다, 사용자에게 묻거나 자료를 달라고 하지 않는다, 답이 500자 안팎, 3분 안팎입니다.
- 리모컨 r1~r5는 한 번씩 돌려 답이 나오는 것까지 봤습니다. 시험에서는 Claude가 되묻는 상황이 한 번도 생기지 않아, 그 상황에서 리모컨이 듣는지는 확인하지 못했습니다.
- "브라우저로 열기"와 Claude Design에 보내는 한 줄은 이 환경에서 돌릴 수 없어 시험하지 않았습니다.
- 1판(11/13 낮)의 결과는 저장소 기록(커밋 ecea7f4)에 있습니다.

## 최종 문구로 돌린 결과

| 조건 | 단계 | 결과 | 걸린 시간(초) | 만들거나 고친 파일 | 마지막 답 글자 수 |
|---|---|---|---|---|---|
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p01 | success | 54 | benchmark.md | 311 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p02+ | success | 19 | benchmark.md | 317 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p03+ | success | 32 | mvp.md | 332 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p04+ | success | 16 | mvp.md | 373 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p05+ | success | 23 | plan.md | 337 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p06+ | success | 34 | landing.html | 352 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p07+ | success | 57 | landing.html | 425 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p08+ | success | 14 | .claude/skills/frontend-design/SKILL.md | 477 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p10+ | success | 38 | kv.md | 491 |
| 빈 폴더 · 테크 트랙 순서대로 | t1 | success | 22 | mvp.md | 282 |
| 빈 폴더 · 테크 트랙 순서대로 | t2+ | success | 45 | prototype.html | 329 |
| 빈 폴더 · 테크 트랙 순서대로 | t3+ | success | 173 | prototype.html, sample.csv | 429 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p03 | success | 26 | mvp.md | 315 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p05 | success | 25 | plan.md | 249 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p06 | success | 37 | landing.html | 406 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p07 | success | 39 | landing.html | 527 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p08 | success | 13 | .claude/skills/frontend-design/SKILL.md | 547 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p10 | success | 27 | kv.md | 471 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | t1 | success | 17 | mvp.md | 243 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | t3 | success | 37 | prototype.html, sample.csv | 460 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p00 | success | 12 | CLAUDE.md | 167 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p11 | success | 42 | kv.md, landing.html, sns.html | 389 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p09 | success | 50 | landing.html, landing_before.html | 320 |
| 다른 브랜드(뷰티) · 순서대로 | p03 | success | 25 | mvp.md | 308 |
| 다른 브랜드(뷰티) · 순서대로 | p05+ | success | 25 | plan.md | 269 |
| 다른 브랜드(뷰티) · 순서대로 | p06+ | success | 43 | landing.html | 414 |
| 다른 브랜드(뷰티) · 순서대로 | p10+ | success | 39 | kv.md | 429 |
| 다른 브랜드(뷰티) · 이미지 4장이 있는 폴더 | p11 | success | 48 | landing.html, sns.html | 517 |
| 금요일 규칙 파일이 남은 폴더 · 다른 브랜드로 바꾼 경우 | p00 | success | 22 | CLAUDE.md | 272 |
| 금요일 규칙 파일이 남은 폴더 · 다른 브랜드로 바꾼 경우 | p03 | success | 22 | mvp.md | 338 |
| 금요일 규칙 파일이 남은 폴더 · 다른 브랜드로 바꾼 경우 | p06+ | success | 29 | landing.html | 427 |
| 빈 폴더 · P0 → P6 → P8 → P9 | p00 | success | 15 | CLAUDE.md | 234 |
| 빈 폴더 · P0 → P6 → P8 → P9 | p06 | success | 39 | landing.html | 413 |
| 빈 폴더 · P0 → P6 → P8 → P9 | p08+ | success | 16 | .claude/skills/frontend-design/SKILL.md | 517 |
| 빈 폴더 · P0 → P6 → P8 → P9 | p09+ | success | 43 | landing.html, landing_before.html | 244 |
| 금요일 규칙만 있고 P0을 건너뛴 경우 | p03 | success | 30 | mvp.md | 380 |
| 금요일 규칙만 있고 P0을 건너뛴 경우 | r1+ | success | 39 | mvp.md | 393 |
| 금요일 규칙만 있고 P0을 건너뛴 경우 | p06 | success | 37 | landing.html | 247 |
| 금요일 규칙만 있고 P0을 건너뛴 경우 | r3+ | success | 8 | - | 382 |
| 리모컨(후속 한 줄) | p03 | success | 24 | mvp.md | 286 |
| 리모컨(후속 한 줄) | r4+ | success | 19 | mvp.md | 363 |
| 리모컨(후속 한 줄) | r5+ | success | 13 | mvp.md | 312 |
| 리모컨(후속 한 줄) | r2+ | success | 7 | - | 248 |
| 앱의 계획 모드에서 P6 | p06 | success | 26 | - | 369 |

## 고치기 전 문구로 돌린 기록

P0, P9, P11은 시험에서 걸려 문구를 고쳤습니다. 아래는 고치기 전 기록입니다.

| 조건 | 단계 | 결과 | 걸린 시간(초) | 만들거나 고친 파일 | 마지막 답 글자 수 |
|---|---|---|---|---|---|
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p00 | success | 18 | CLAUDE.md | 420 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p09+ | success | 48 | landing.html, landing_before.html | 573 |
| 금요일 규칙 파일이 남은 폴더 · 라라스윗 · 하루 순서대로 | p11+ | success | 49 | landing.html, sns.html | 543 |
| 빈 폴더 · 테크 트랙 순서대로 | p00 | success | 14 | CLAUDE.md | 263 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p09 | success | 40 | landing.html, landing_before.html | 812 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p11 | success | 36 | kv.md, landing.html, sns.html | 477 |
| 규칙 파일 없음 · 빈 폴더에서 이것 하나만 | p09 | success | 60 | landing.html, landing_before.html | 795 |
| 다른 브랜드(뷰티) · 순서대로 | p00 | success | 14 | CLAUDE.md | 254 |
| 다른 브랜드(뷰티) · 순서대로 | p09+ | success | 92 | landing.html, landing_before.html | 517 |
| 금요일 규칙 파일이 남은 폴더 · 다른 브랜드로 바꾼 경우 | p09+ | success | 71 | landing.html, landing_before.html | 687 |
| 리모컨(후속 한 줄) | p00 | success | 13 | CLAUDE.md | 296 |

## 시험에서 걸려 고친 것

| 프롬프트 | 걸린 것 | 고친 것 |
|---|---|---|
| P0 | 답이 420자였고 끝에 "~하려면 말씀해 주세요"가 붙음. 브랜드를 바꾼 학생은 금요일 브랜드 소개와 오늘 브랜드가 함께 남음 | 첫 줄에 "끝나면 3줄로만 알려줘"를 넣고, 브랜드 제목을 "기준 브랜드 (오늘은 이 브랜드로 작업한다)"로 바꿈. 다시 돌린 결과 다른 브랜드로 mvp.md와 landing.html이 나옴 |
| P9 | 답이 570~810자(글꼴 이름과 색 코드를 길게 나열). 빈 폴더에서는 랜딩페이지를 아주 얇게 만듦 | "바꾼 곳을 세 문장으로만", "글꼴 이름과 색 코드는 말하지 않아도 돼", "없으면 여덟 화면으로 먼저 만들고"를 넣음. 다시 돌린 결과 244자, 320자 |
| P11 | 빈 폴더에서 이미지 이름을 제각각 정함(kv.jpg, sns-1.jpg) | 이미지 이름 기준(kv.png, sns1~3.png)을 프롬프트에 적음 |

## 화면으로 확인한 것

- 순서대로 만든 landing.html: 폰 폭(400px)에서 옆으로 넘치지 않음, 이미지 4장이 보임, [채울 곳] 표시와 "학습용 가상 기획안" 문구가 있음.
- sns.html: 이미지 3장과 큰 카피가 함께 보임.
- 테크 트랙 prototype.html: 열면 샘플 30줄이 보이고, CSV 파일을 고르면 표가 그 데이터로 바뀜.
- P8이 저장한 SKILL.md는 원본 파일과 한 글자도 다르지 않음(두 번 확인).
- 금요일 규칙 파일이 남은 폴더에서 P0을 돌리면 "멈추고 묻기", "아카이브에 없는 광고 인용 금지" 두 줄만 지워지고 나머지는 남음.

## 이 시험이 보장하지 않는 것

- 시험은 이 저장소의 클라우드 작업 환경에서 돌렸습니다. 학생 노트북의 Claude Code와 모델·설정이 다를 수 있습니다.
- 허락 창은 시험에서 미리 허용해 두었습니다. 학생 화면에서는 파일 쓰기, 웹 검색, 파일 내려받기에 Yes를 눌러야 합니다. 시험에서는 명령 실행을 막아 둔 단계가 있어, 파일 복사에 시간이 더 걸린 경우가 있습니다(P9 92초, T3 173초).
- 이미지 만들기(GPT 에듀), 앱의 Plan 모드 화면, Claude Design 화면은 시험하지 못했습니다. 계획 모드는 명령줄에서 P6을 넣어 계획만 나오고 파일은 만들어지지 않는 것까지 확인했습니다.
