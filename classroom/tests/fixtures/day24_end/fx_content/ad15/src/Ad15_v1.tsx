import React from "react";
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from "remotion";

export type Ad15Props = {
  bg: string;
  clip?: string;
  theme: "dark" | "light";
  accent: string;
  brand: string;
  tag: string;
  hook: string;
  headline: string;
  desc: string;
  cta: string;
  mark: string;
};

export const ad15Defaults: Ad15Props = {
  bg: "bg_1125_a.png",
  clip: "",
  theme: "dark",
  accent: "#ffffff",
  brand: "라네즈",
  tag: "라네즈 수분 크림",
  hook: "후킹 한 줄",
  headline: "헤드라인",
  desc: "설명 한 줄",
  cta: "자세히 보기",
  mark: "수업용 시안",
};

const FONT =
  '"Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", "WenQuanYi Zen Hei", sans-serif';

// [할인율](가정) 같은 자리 표시를 점선 상자로 바꾼다
const Rich: React.FC<{ text: string; color: string }> = ({ text, color }) => {
  const parts = text.split(/(\[[^\]]+\]\(가정\))/g).filter(Boolean);
  return (
    <>
      {parts.map((p, i) => {
        const m = p.match(/^\[([^\]]+)\]\(가정\)$/);
        if (!m) return <React.Fragment key={i}>{p}</React.Fragment>;
        return (
          <span
            key={i}
            style={{
              display: "inline-block",
              border: `0.06em dashed ${color}`,
              borderRadius: "0.18em",
              padding: "0 0.22em",
              margin: "0 0.08em",
              lineHeight: 1.15,
              whiteSpace: "nowrap",
            }}
          >
            {m[1]}
            <span style={{ fontSize: "0.45em", fontWeight: 600, marginLeft: "0.2em", verticalAlign: "middle" }}>
              (가정)
            </span>
          </span>
        );
      })}
    </>
  );
};

export const Ad15: React.FC<Ad15Props> = (p) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const dark = p.theme === "dark";
  const fg = dark ? "#ffffff" : "#1f1a2e";
  const sub = dark ? "rgba(255,255,255,0.92)" : "rgba(31,26,46,0.88)";

  // 사진: 천천히 확대·이동
  const scale = interpolate(frame, [0, durationInFrames], [1.05, 1.22], {
    easing: Easing.inOut(Easing.quad),
  });
  const tx = interpolate(frame, [0, durationInFrames], [-30, 30]);
  const ty = interpolate(frame, [0, durationInFrames], [20, -40]);

  // 한 줄씩 들어오기
  const enter = (start: number) => {
    const s = spring({ frame: frame - start, fps, config: { damping: 200 } });
    return { opacity: s, transform: `translateY(${(1 - s) * 60}px)` };
  };

  // 후킹: 0프레임부터 보이고 3초에 사라짐
  const hookOut = interpolate(frame, [80, 100], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const hookIn = interpolate(frame, [0, 8], [0.85, 1], { extrapolateRight: "clamp" });
  const endStart = durationInFrames - 60; // 마지막 2초
  const bodyOut = interpolate(frame, [endStart - 10, endStart], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  const veil = dark
    ? "linear-gradient(180deg, rgba(10,8,30,0.55) 0%, rgba(10,8,30,0.15) 22%, rgba(10,8,30,0.25) 45%, rgba(10,8,30,0.78) 100%)"
    : "linear-gradient(180deg, rgba(255,255,255,0.55) 0%, rgba(255,255,255,0.1) 22%, rgba(255,255,255,0.35) 45%, rgba(255,255,255,0.85) 100%)";

  return (
    <AbsoluteFill style={{ backgroundColor: "#000", fontFamily: FONT, wordBreak: "keep-all" }}>
      <AbsoluteFill style={{ transform: `scale(${scale}) translate(${tx}px, ${ty}px)` }}>
        {p.clip ? (
          <OffthreadVideo src={staticFile(p.clip)} muted style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        ) : (
          <Img src={staticFile(p.bg)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        )}
      </AbsoluteFill>
      <AbsoluteFill style={{ background: veil }} />

      {/* 위: 무엇을 파는지 (처음부터 끝까지) */}
      <div
        style={{
          position: "absolute",
          top: 150,
          left: 0,
          right: 0,
          textAlign: "center",
          color: fg,
          fontSize: 44,
          fontWeight: 700,
          letterSpacing: "0.02em",
        }}
      >
        <span
          style={{
            padding: "12px 30px",
            borderRadius: 999,
            border: `3px solid ${fg}`,
            background: dark ? "rgba(0,0,0,0.25)" : "rgba(255,255,255,0.55)",
          }}
        >
          {p.tag}
        </span>
      </div>

      {/* 첫 1초: 후킹 한 줄 */}
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", padding: "0 90px", opacity: hookOut }}>
        <div
          style={{
            color: fg,
            fontSize: 92,
            fontWeight: 800,
            lineHeight: 1.3,
            textAlign: "center",
            transform: `scale(${hookIn})`,
            textShadow: dark ? "0 4px 24px rgba(0,0,0,0.45)" : "0 2px 18px rgba(255,255,255,0.6)",
          }}
        >
          <Rich text={p.hook} color={fg} />
        </div>
      </AbsoluteFill>

      {/* 본문: 헤드라인·설명이 한 줄씩 */}
      <div style={{ position: "absolute", left: 90, right: 90, bottom: 520, opacity: bodyOut }}>
        <div style={{ ...enter(100), color: fg, fontSize: 120, fontWeight: 800, lineHeight: 1.2, marginBottom: 40 }}>
          <Rich text={p.headline} color={fg} />
        </div>
        <div style={{ ...enter(150), color: sub, fontSize: 52, fontWeight: 500, lineHeight: 1.5 }}>
          <Rich text={p.desc} color={sub} />
        </div>
      </div>

      {/* 마지막 2초: 행동 버튼과 회사 이름 */}
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", gap: 70 }}>
        <div style={{ ...enter(endStart), color: fg, fontSize: 130, fontWeight: 800, letterSpacing: "0.04em" }}>
          {p.brand}
        </div>
        <div style={{ ...enter(endStart + 4), color: sub, fontSize: 56, fontWeight: 600, marginTop: -40, textAlign: "center", padding: "0 90px", lineHeight: 1.35 }}>
          <Rich text={p.headline} color={sub} />
        </div>
        <div
          style={{
            ...enter(endStart + 8),
            background: dark ? "#ffffff" : "#1f1a2e",
            color: dark ? "#1f1a2e" : "#ffffff",
            fontSize: 60,
            fontWeight: 800,
            padding: "30px 90px",
            borderRadius: 999,
            boxShadow: "0 10px 30px rgba(0,0,0,0.25)",
          }}
        >
          {p.cta} ›
        </div>
      </AbsoluteFill>

      {/* 오른쪽 아래 작게 */}
      <div style={{ position: "absolute", right: 40, bottom: 40, color: fg, opacity: 0.8, fontSize: 30, fontWeight: 600 }}>
        {p.mark}
      </div>
    </AbsoluteFill>
  );
};
