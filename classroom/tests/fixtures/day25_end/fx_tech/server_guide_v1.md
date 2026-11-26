# 서버 올리기 안내 (내가 할 일)

AI 버튼이 화면에서 바로 답하게 하려면, 키를 서버(Vercel)에만 두고 site 폴더를 올려요. 키는 채팅·화면·GitHub에 붙이지 않아요.

1. aistudio.google.com에서 Gemini API 키를 만들어요. 복사한 키는 아무 데도 붙이지 말고 3번까지 들고 있어요. (결제를 연결하지 않은 무료 등급 키)
2. vercel.com에 가입해요.
3. 터미널에서 site 폴더로 가서 `npx vercel`을 실행해요. 처음 묻는 것은 모두 기본값(엔터)으로 답해요.
4. Vercel 화면에서 이 프로젝트의 Settings → Environment Variables에 이름 `GEMINI_API_KEY`, 값은 1번의 키로 넣고 저장해요. (모델을 바꾸고 싶을 때만 `GEMINI_MODEL`도 넣어요. 안 넣으면 gemini-flash-latest)
5. 터미널에서 `npx vercel --prod`를 실행해요.
6. 받은 주소를 폰에서 열고, 글을 붙여 "AI에게 바로 확인"을 눌러요. 답이 안 오면 "AI 확인 글 복사"를 써요.

참고: 올리는 것은 site 폴더뿐이에요(index.html, api/check.js). decisions.md·research.csv 같은 작업 파일은 올리지 않아요. 올리기 전에 `node scripts/test_check.mjs`가 모두 ✓인지 봐요.

## 꼭 지켜요
- 무료 등급은 하루에 쓸 수 있는 양이 정해져 있고, 넣은 글이 구글의 서비스 개선에 쓰일 수 있어서 개인정보와 회사 기밀은 넣지 않아요.
- 결제를 연결한 키는 쓰지 않아요.
- 키가 새면(채팅·GitHub에 붙였으면) aistudio.google.com에서 그 키를 지우고 새로 만들어 Vercel 환경 변수를 바꾼 뒤 다시 올려요. 파일에서 지우는 것만으로는 안 돼요.
