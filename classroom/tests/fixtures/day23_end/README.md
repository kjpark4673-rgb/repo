# 11/25(Day 23)를 끝낸 시험용 폴더 (11/26 이후 가이드 시험의 출발점)

> 11/22에 만들었어요. 학생 이름, 학생 작업물, 링크는 들어 있지 않아요. 시험 전용이에요.

## 왜 있나요

`../day22_end/`과 같은 까닭이에요. 새 날짜 가이드를 가상 학생으로 시험하려면 앞날을 끝낸 폴더가 필요한데, 시험 폴더는 그 세션의 임시 폴더라 새 창에는 없어요. 그래서 `day22_end`의 네 폴더에서 Day 23 가이드(5차 시험 판)를 끝까지 돌린 결과를 여기에 뒀어요.

## 네 폴더

| 이름 | 직무 · 회사 | 시안 모양 · 재료 | 11/25에 지난 길 | 끝난 상태 |
|---|---|---|---|---|
| `fx_md` | MD · 라라스윗 | 이미지 · 디저트 공통광고 표 | P0 → P8 → 쓸 패턴(내가 정함) → P9 → 사진 → P10 → P11 → E 카드(내 심사 vs AI 심사) → 새 대화 스킬 확인 | 시안 3개 통과, 변형 2개, weekly-create 스킬 |
| `fx_content` | 콘텐츠 마케터 · 라네즈 | 영상 · 스킨케어 표 | P0 → 영상 준비 → P8 → 잘 모르겠으면 → P9 → 사진 → P10 → P11 | 영상 시안 3개 보류(시험용 자리 사진이라), weekly-create 스킬 |
| `fx_ops` | 운영 매니저 · 예시 교육센터(가상) | 이미지 · 교육 표 | P0 → P8 → P9 → 사진 → P10 → 고치기 → P11 → 새 대화 스킬 확인 → 내 결정(내보낼 시안 A) → P12 | 시안 보류(자리 사진), 내보낼 시안 적힘, 루프 점검 다시 |
| `fx_tech` | 데이터 분석가 · 컬리 | 이미지 · 새벽배송 표 | P0 → P8 → P9 → 사진 → P10 → P11 → E 카드 ○○ 그대로(멈춤) → A 패턴 브리핑 영상 | 시안 보류(자리 사진), 브리핑 영상 스크립트(`scripts/`) |

폴더마다 11/24까지의 파일(`_CLAUDE.md`, `decisions.md`, `loop.html`, `weekly.html`, `research.csv` 또는 `records.csv`, `mvp.html`, `_claude/skills/weekly-research`)에 더해 이 파일들이 있어요: `patterns_1125.md`, `brief_1125.md`, `image_prompt_1125.md`, `bg_1125_a·b·c.png`, 시안(`ad_1125_*` 또는 `ad15_1125_*`), `review_1125.md`, `compare_1125.html`, `_claude/skills/weekly-create/SKILL.md`, `persona.json`.

## 저장소에 두면서 뺀 것과 바꾼 것

- **남의 광고 문구:** `공통광고_*.csv`와 `creatives_1125*.csv`는 뺐어요(다른 회사 광고 문구라 공개 저장소에 두지 않아요). patterns 등에 있던 광고 링크와 "대표 예" 줄은 지우고, 11/24 폴더에 없던 광고주 이름은 "(광고주)"로 바꿨어요. 그래서 P8을 다시 돌리려면 강사님의 공통광고 표를 넣어야 해요.
- **큰 파일:** 사진과 시안 PNG는 360×450으로 줄였고(이름은 그대로), 영상(mp4), `ad15/node_modules`, 심사용 컷 그림은 뺐어요. 영상을 다시 렌더하려면 `ad15`에서 `npm install`부터 해요.
- **사진:** `fx_md`의 사진은 강사님이 P9 그림 글로 만든 것을 줄인 것이고, 나머지 셋은 시험용 자리 사진(흐린 색 덩어리)이라 심사가 보류로 멈춘 상태예요. 다음 날 시험에서 "보류가 남은 학생"으로 쓰기 좋아요.
- `CLAUDE.md`는 `_CLAUDE.md`, `.claude`는 `_claude`로 이름을 바꿔 뒀어요. `restore.sh`가 되돌려요.

## 쓰는 법

```bash
classroom/tests/fixtures/day23_end/restore.sh fx_md /경로/시험폴더/fx_md
export TOK="$(cat classroom/tests/fixtures/day23_end/fx_md/persona.json)"
cd /경로/시험폴더/fx_md && python3 <저장소>/classroom/tools/runchain.py <새 가이드.html> . ../결과.json p00 ...
```

- 이 폴더들은 5차 시험 판으로 끝냈어요. 발행 판(6차)에서 바뀐 것은 P8·P9의 "운영 패턴은 시안 패턴에서 빼고 운영 메모로"와 P10 심사 ②의 "폰 크기(390px)로도 보기"뿐이라, 다음 날 시험의 출발점으로는 그대로 써도 돼요.
- 시험 기록은 `classroom/tests/day23-test-results.md`예요.
