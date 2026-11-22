import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';

export type Ad15Props = {image: string; hook: string; headline: string; desc: string; button: string; brand: string};

const font = '"Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", "WenQuanYi Zen Hei", sans-serif';

export const Ad15: React.FC<Ad15Props> = ({image, hook, headline, desc, button, brand}) => {
  const f = useCurrentFrame();
  const scale = interpolate(f, [0, 450], [1, 1.12]);
  const x = interpolate(f, [0, 450], [0, -30]);
  const show = (s: number) => ({opacity: interpolate(f, [s, s + 12], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}), transform: `translateY(${interpolate(f, [s, s + 12], [30, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}px)`});
  return (
    <AbsoluteFill style={{background: '#222', fontFamily: font, wordBreak: 'keep-all', color: '#fff'}}>
      {image ? <Img src={staticFile(image)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${scale}) translateX(${x}px)`}} /> : null}
      <AbsoluteFill style={{background: 'linear-gradient(to bottom, rgba(0,0,0,.65), rgba(0,0,0,0) 55%, rgba(0,0,0,.6))'}} />
      <div style={{position: 'absolute', top: 160, left: 80, right: 80, fontSize: 64, fontWeight: 900, ...show(0)}}>{hook}</div>
      <div style={{position: 'absolute', top: 420, left: 80, right: 80, fontSize: 96, fontWeight: 900, lineHeight: 1.2, ...show(60)}}>{headline}</div>
      <div style={{position: 'absolute', top: 700, left: 80, right: 80, fontSize: 44, ...show(120)}}>{desc}</div>
      <div style={{position: 'absolute', bottom: 220, left: 80, right: 80, ...show(390)}}>
        <div style={{fontSize: 44, fontWeight: 800, marginBottom: 28}}>{brand}</div>
        <span style={{display: 'inline-block', background: '#fff', color: '#3b0a55', fontSize: 44, fontWeight: 800, padding: '22px 52px', borderRadius: 999}}>{button}</span>
      </div>
      <div style={{position: 'absolute', right: 30, bottom: 24, fontSize: 24, opacity: 0.85}}>수업용 시안</div>
    </AbsoluteFill>
  );
};
