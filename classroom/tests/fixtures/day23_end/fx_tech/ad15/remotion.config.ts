import fs from 'fs';
import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');

// 렌더용 브라우저를 내려받을 수 없는 컴퓨터에서는 설치된 크롬을 쓴다(있을 때만).
const localChrome = process.env.REMOTION_CHROME || '/usr/bin/google-chrome';
if (fs.existsSync(localChrome)) {
  Config.setBrowserExecutable(localChrome);
}
