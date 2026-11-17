#!/bin/bash
# Day 19 2차 시험: 검토 반영 뒤, 바뀐 상자가 든 갈래를 처음부터
# 쓰는 법: 빈 작업 폴더 T를 정하고 이 폴더의 day19_mkfix.py를 T/mkfix.py로, day19_answers.py를 T에서 한 번 돌려 answers.json을 만든 뒤
#   T=/경로 REPO=/저장소 bash day19_run2.sh   (갈래는 백그라운드로 나란히 돌고, 결과는 T/r2/*.json, *.log)
# 세 AI의 답은 시험용으로 흉내 낸 글이에요(실제 ChatGPT·Gemini의 답이 아님).
T=${T:-.}
export ANS="$(cd "$T" && pwd)/answers.json"
R=${REPO:-$(git rev-parse --show-toplevel)}/classroom/tools/runchain.py
G=${REPO:-$(git rev-parse --show-toplevel)}/classroom/student-guide/day19.html
cd $T; rm -rf r2; mkdir -p r2
ex(){ python3 - "$1" <<'PY'
import json,sys
import os
A=json.load(open(os.environ['ANS']))
k=sys.argv[1]
print(json.dumps({'xa':A.get(k,''),'xag':A['again'],
 'xpick':'이 일엔 Claude를 쓸래. 이유는 1안이 시간과 장면이 가장 구체적이었어. compare.html과 eval.md에 적어줘.',
 'xpick1':'기준은 그대로 갈게. 이유는 우리 고객 말투가 가장 중요해서. task.md 맨 아래에 적어줘.',
 'xknown':'이름 알고 매김. eval.md에 적어줘.',
 'xdec':'오늘 정한 것: 점수 기준은 그대로(우리 고객 말투가 가장 중요해서) / 내 점수 A 4 4 5 4, B 4 5 4 4, C 2 2 3 2 / 이 일엔 Claude / 다짐: 숫자가 들어간 답은 출처 링크를 한 번 열어 본다'},ensure_ascii=False))
PY
}
( python3 mkfix.py r2/mk mk
  cd r2/mk && EXTRA="$(ex mk)" TOK='{"crit":"2534 직장인 말투인가","score":"A 4 4 5 4 / B 4 5 4 4 / C 2 2 3 2","key":"A=Claude 기본, B=Gemini 기본, C=ChatGPT 기본","rule":"숫자가 들어간 답은 출처 링크를 한 번 열어 본다"}' \
  python3 $R $G . ../mk.json p00 p01+ p02+ xpick1+ 'p03&xa+' critshow+ p04+ xpick+ p05+ fix+ 'p06&xag+' 'w2&xdec+' p11 > ../mk.log 2>&1 ) &
( python3 mkfix.py r2/md md
  cd r2/md && EXTRA="$(ex md)" TOK='{"crit":"마진 하한을 지켰나"}' python3 $R $G . ../md.json p00 p01+ p02+ 'p03&xa+' > ../md.log 2>&1
  EXTRA="$(ex md)" APPEND=1 TOK='{"crit":"마진 하한을 지켰나","score":"A 5 4 4 4 / B 4 4 5 3 / C 1 2 1 1","key":"A=Gemini 기본, B=ChatGPT 기본, C=Claude 기본"}' python3 $R $G . ../md.json p03+ p04+ p05+ p08+ p09+ w2+ >> ../md.log 2>&1 ) &
( python3 mkfix.py r2/cx cx partial
  cd r2/cx && EXTRA="$(ex cx)" TOK='{"score":"A 5 5 4 5 / B 2 2 3 1 / C 4 3 4 4","team":"MD · 프로모션 3안 · 1등 Gemini 16점, 2등 Claude 15점, 3등 ChatGPT 9점 / 콘텐츠 마케터 · 카피 3안 · 1등 Claude 18점, 2등 ChatGPT 14점, 3등 Gemini 13점"}' \
  python3 $R $G . ../cx.json p00 p01+ p02+ 'p03&xa+' xknown+ p04+ p05+ p07+ w2+ > ../cx.log 2>&1 ) &
( python3 mkfix.py r2/tech tech
  cd r2/tech && EXTRA="$(ex tech)" TOK='{"key":"A=ChatGPT 기본, B=Claude 기본, C=Gemini 기본"}' python3 $R $G . ../tech.json p00 p01+ p02+ 'p03&xa+' > ../tech.log 2>&1
  EXTRA="$(ex tech)" APPEND=1 TOOLS='WebSearch,WebFetch,Read,Write,Edit,Glob,Grep,Bash' python3 $R $G . ../tech.json code+ >> ../tech.log 2>&1
  EXTRA="$(ex tech)" APPEND=1 TOK='{"score":"A 4 5 4 4 / B 5 4 5 4 / C 2 1 2 2","key":"A=ChatGPT 기본, B=Claude 기본, C=Gemini 기본"}' python3 $R $G . ../tech.json p03+ p04+ p05+ p10+ w2+ >> ../tech.log 2>&1 ) &
( mkdir -p r2/empty; cd r2/empty && python3 $R $G . ../empty.json p00 p01+ p02+ p03+ p04+ p05+ w2+ > ../empty.log 2>&1 ) &
( mkdir -p r2/ops; cd r2/ops && BRAND='멋쟁이사자처럼|IT 부트캠프|취업을 준비하는 20대 수강생' TOK='{"role":"운영 매니저(교육 회사)"}' python3 $R $G . ../ops.json p00 p01+ p02+ > ../ops.log 2>&1 ) &
( python3 mkfix.py r2/roletyped tech && sed -i 's/하고 싶은 일: 데이터 분석가/하고 싶은 일: 아직 모름/' r2/roletyped/CLAUDE.md
  cd r2/roletyped && TOK='{"role":"데이터 분석가"}' python3 $R $G . ../roletyped.json p00 p01+ p02+ > ../roletyped.log 2>&1 ) &
( for b in p10 p08 fix; do mkdir -p r2/solo_$b; (cd r2/solo_$b && python3 $R $G . ../solo_$b.json $b > ../solo_$b.log 2>&1); done ) &
wait; echo ALLDONE
