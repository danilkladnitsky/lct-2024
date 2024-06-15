import { CameraControls, Environment, useGLTF } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";

interface Props {
  sceneUrl: Url;
}

export const SceneViewer = ({ sceneUrl }: Props) => {
  const { nodes } = useGLTF(sceneUrl);

  return (
    <Canvas>
      <CameraControls minPolarAngle={0} maxPolarAngle={Math.PI / 1.6} />
      <primitive object={nodes.Scene} />
      <Environment preset="studio" background blur={0.5} />
    </Canvas>
  );
};
