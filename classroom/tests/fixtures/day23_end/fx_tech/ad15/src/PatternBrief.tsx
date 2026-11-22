import React from 'react';
import {AbsoluteFill, interpolate, Sequence, useCurrentFrame} from 'remotion';

export type BriefPattern = {name: string; longPct: number; restPct: number; longText: string; restText: string};
export type PatternBriefProps = {
  topLine: string; // 이번 주 고객에게 할 말
  title: string;
  patterns: BriefPattern[];
  rows: number; // 재료 줄 수
  collectedAt: string; // 수집일
  source: string; // 출처 파일 이름
  basis: string; // 성과 신호 기준
};

const font = '"Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", "WenQuanYi Zen Hei", sans-serif';
const C = {bg: '#17112a', fg: '#ffffff', mute: '#b9b1cc', long: '#c79bff', rest: '#6f6787', track: 'rgba(255,255,255,.12)'};
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

const FadeIn: React.FC<{at: number; children: React.ReactNode; style?: React.CSSProperties}> = ({at, children, style}) => {
  const f = useCurrentFrame();
  return (
    <div style={{opacity: interpolate(f, [at, at + 10], [0, 1], clamp), transform: `translateY(${interpolate(f, [at, at + 10], [24, 0], clamp)}px)`, ...style}}>{children}</div>
  );
};

const Bar: React.FC<{label: string; pct: number; color: string; start: number}> = ({label, pct, color, start}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [start, start + 30], [0, pct], clamp);
  return (
    <div style={{marginBottom: 44}}>
      <div style={{display: 'flex', justifyContent: 'space-between', fontSize: 44, fontWeight: 700, marginBottom: 16}}>
        <span>{label}</span>
        <span style={{fontVariantNumeric: 'tabular-nums'}}>{Math.round(p)}%</span>
      </div>
      <div style={{height: 56, borderRadius: 28, background: C.track, overflow: 'hidden'}}>
        <div style={{width: `${p}%`, height: '100%', borderRadius: 28, background: color}} />
      </div>
    </div>
  );
};

const PatternCut: React.FC<{p: BriefPattern; i: number; rows: number; source: string; basis: string}> = ({p, i, rows, source, basis}) => (
  <AbsoluteFill style={{padding: '260px 90px 0'}}>
    <FadeIn at={0}><div style={{fontSize: 40, fontWeight: 800, color: C.long, marginBottom: 20}}>패턴 {i + 1}</div></FadeIn>
    <FadeIn at={4}><div style={{fontSize: 76, fontWeight: 900, lineHeight: 1.25, marginBottom: 90}}>{p.name}</div></FadeIn>
    <FadeIn at={10}>
      <Bar label="오래 돈 묶음" pct={p.longPct} color={C.long} start={14} />
      <div style={{fontSize: 32, color: C.mute, margin: '-28px 0 56px'}}>{p.longText}</div>
      <Bar label="나머지 묶음" pct={p.restPct} color={C.rest} start={22} />
      <div style={{fontSize: 32, color: C.mute, margin: '-28px 0 56px'}}>{p.restText}</div>
    </FadeIn>
    <FadeIn at={30}><div style={{fontSize: 28, color: C.mute}}>출처: {source}({rows}줄, {basis})</div></FadeIn>
  </AbsoluteFill>
);

export const PatternBrief: React.FC<PatternBriefProps> = ({topLine, title, patterns, rows, collectedAt, source, basis}) => {
  const intro = 75;
  const outro = 75;
  const each = patterns.length ? Math.floor((450 - intro - outro) / patterns.length) : 0;
  return (
    <AbsoluteFill style={{background: C.bg, color: C.fg, fontFamily: font, wordBreak: 'keep-all'}}>
      <Sequence durationInFrames={intro}>
        <AbsoluteFill style={{padding: '0 90px', justifyContent: 'center'}}>
          <FadeIn at={0}><div style={{fontSize: 44, fontWeight: 800, color: C.long, marginBottom: 36}}>{title}</div></FadeIn>
          <FadeIn at={8}><div style={{fontSize: 80, fontWeight: 900, lineHeight: 1.3}}>{topLine}</div></FadeIn>
        </AbsoluteFill>
      </Sequence>
      {patterns.map((p, i) => (
        <Sequence key={i} from={intro + i * each} durationInFrames={each}>
          <PatternCut p={p} i={i} rows={rows} source={source} basis={basis} />
        </Sequence>
      ))}
      <Sequence from={intro + patterns.length * each}>
        <AbsoluteFill style={{padding: '0 90px', justifyContent: 'center'}}>
          <FadeIn at={0}><div style={{fontSize: 44, fontWeight: 800, color: C.long, marginBottom: 40}}>이번 주 쓸 패턴 <span style={{color: C.mute, fontSize: 32}}>(오래 돈 묶음 · 나머지 묶음)</span></div></FadeIn>
          {patterns.map((p, i) => (
            <FadeIn key={i} at={6 + i * 6}>
              <div style={{fontSize: 52, fontWeight: 800, lineHeight: 1.35, marginBottom: 30}}>{i + 1}. {p.name} <span style={{color: C.mute, fontSize: 40}}>{Math.round(p.longPct)}% · {Math.round(p.restPct)}%</span></div>
            </FadeIn>
          ))}
          <FadeIn at={30}><div style={{fontSize: 30, color: C.mute, marginTop: 40}}>재료 {rows}줄 · 수집일 {collectedAt} · 출처: {source}({basis})</div></FadeIn>
        </AbsoluteFill>
      </Sequence>
      <div style={{position: 'absolute', right: 30, bottom: 24, fontSize: 24, color: C.mute}}>수업용 시안</div>
    </AbsoluteFill>
  );
};
