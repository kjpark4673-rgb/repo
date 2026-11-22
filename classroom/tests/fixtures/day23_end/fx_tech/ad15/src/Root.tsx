import React from 'react';
import {Composition} from 'remotion';
import {Ad15, Ad15Props} from './Ad15';
import {PatternBrief, PatternBriefProps} from './PatternBrief';

const emptyAd: Ad15Props = {image: '', hook: '', headline: '', desc: '', button: '', brand: ''};
const emptyBrief: PatternBriefProps = {topLine: '', title: '', patterns: [], rows: 0, collectedAt: '', source: '', basis: ''};

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="Ad15" component={Ad15} width={1080} height={1920} fps={30} durationInFrames={450} defaultProps={emptyAd} />
    <Composition id="PatternBrief" component={PatternBrief} width={1080} height={1920} fps={30} durationInFrames={450} defaultProps={emptyBrief} />
  </>
);
