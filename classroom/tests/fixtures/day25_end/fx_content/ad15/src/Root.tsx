import { Composition } from "remotion";
import { Ad15, ad15Defaults } from "./Ad15";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Ad15"
        component={Ad15}
        durationInFrames={450}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={ad15Defaults}
      />
    </>
  );
};
