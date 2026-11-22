#!/bin/bash
# 11/24(Day 22)를 끝낸 시험용 폴더 네 개를 처음부터 다시 만든다(가이드가 바뀌어 출발점이 낡았을 때).
# 사용: classroom/tests/fixtures/day22_end/make_day22_end.sh <출력 폴더>   (한 줄에 10~15분, 네 갈래를 한꺼번에, 약 4~5달러)
# 학생 작업물은 쓰지 않는다. 조사형 셋은 빈 폴더에서 "따라잡기(원본 없음)" 길로, 운영형은 _starts/ops의 가짜 기록으로 시작한다.
# 길: 11/23 가이드 P0 → (따라잡기) → P1 → P3 → P4, 11/24 가이드 P0 → P5 → P6 → P7. 그 뒤 아래 save 방법으로 이 폴더에 다시 저장한다.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$HERE/../../../.." && pwd)"
OUT="${1:?출력 폴더를 적어 주세요}"; mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
R="$REPO/classroom/tools/runchain.py"
export TOOLS='Bash,WebSearch,WebFetch,Read,Write,Edit,Glob,Grep,Skill' MAXT=60 TLIM=1200 ANTHROPIC_MODEL="${ANTHROPIC_MODEL:-claude-sonnet-5-5}"
cp "$REPO/classroom/student-guide/day21.html" "$OUT/g21.html"; cp "$REPO/classroom/student-guide/day22.html" "$OUT/g22.html"
run(){ g="$1"; b="$2"; shift 2; for st in "$@"; do ( cd "$OUT/$b" && APPEND=1 python3 "$R" "$g" . "../$b.json" "$st" >> "../$b.log" 2>&1 ); done; echo "$b $(basename "$g") done" >> "$OUT/limits.txt"; }
make(){ b="$1"; shift; mkdir -p "$OUT/$b"; ( export TOK="$(cat "$HERE/$b/persona.json")"; "$@" ) & }
chain_research(){ run "$OUT/g21.html" "$1" p00 cu+ p01+ p03+ pchk+; run "$OUT/g22.html" "$1" p00 p05+ p06+ p07+; }
chain_ops(){ run "$OUT/g21.html" "$1" p00 p01+ p03+ pchk+; run "$OUT/g22.html" "$1" p00 p05+ p06+ p07+; }
make fx_md chain_research fx_md
make fx_content chain_research fx_content
make fx_tech chain_research fx_tech
mkdir -p "$OUT/fx_ops"; cp "$HERE/_starts/ops/mvp.html" "$HERE/_starts/ops/records.csv" "$OUT/fx_ops/"
make fx_ops chain_ops fx_ops
wait; echo "끝: $OUT (결과는 <이름>.json, 만든 폴더는 <이름>/)"
