# 서버 함수 올리기 안내 (내가 할 일)
1. aistudio.google.com에서 API 키를 만든다(키는 채팅·화면·GitHub에 붙이지 않는다).
2. vercel.com에 가입한다.
3. 터미널에서 site 폴더로 가서 `npx vercel`을 실행한다(처음 묻는 것은 기본값).
4. Vercel 화면 Settings → Environment Variables에 `GEMINI_API_KEY`(값은 1번 키)를 넣는다. 모델을 바꾸고 싶으면 `GEMINI_MODEL`도 넣는다(없으면 gemini-flash-latest).
5. 터미널에서 `npx vercel --prod`를 실행한다.
6. 받은 주소를 폰에서 열어 "AI에게 바로 확인"을 눌러 본다.

- 무료 등급은 하루에 쓸 수 있는 양이 정해져 있고, 넣은 글이 구글의 서비스 개선에 쓰일 수 있어서 개인정보와 회사 기밀은 넣지 않아요.
- 결제를 연결한 키는 쓰지 않아요.
- 키가 새면(채팅·GitHub에 붙였으면) aistudio.google.com에서 그 키를 지우고 새로 만들어 Vercel 환경 변수를 바꾼 뒤 다시 올려요. 파일에서 지우는 것만으로는 안 돼요.
