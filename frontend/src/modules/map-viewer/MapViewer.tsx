import { Card, Loader, Text } from "@gravity-ui/uikit";
import classNames from "classnames";

import styles from "./MapViewer.module.scss";
import { useEffect, useRef } from "react";
import { useAppContext } from "@/shared/context";

interface Props {
  className?: string;
}

export const MapViewer = ({ className }: Props) => {
  const { formIsVisible, renderLink, setSceneIsLoading, sceneIsLoading } =
    useAppContext();
  const iFrameRef = useRef<HTMLIFrameElement>(null);

  const iframeCurrent = iFrameRef.current;
  useEffect(() => {
    iframeCurrent?.addEventListener("load", () => setSceneIsLoading(false));
    return () => {
      iframeCurrent?.removeEventListener("load", () => setSceneIsLoading(true));
    };
  }, [iframeCurrent]);

  if (!renderLink) {
    return (
      <Card className={classNames(styles.mapViewer, className)}>
        <div className={styles.loader}>
          <Text variant="subheader-2">Заполните форму</Text>
        </div>
      </Card>
    );
  }

  return (
    <Card className={classNames(styles.mapViewer, className)}>
      {sceneIsLoading && (
        <div className={styles.loader}>
          <Loader size="l" />
        </div>
      )}
      <iframe
        key={formIsVisible}
        ref={iFrameRef}
        style={{
          outline: 0,
          border: "unset",
          height: "100%",
          width: "100%",
          opacity: isLoading ? "0" : "1",
        }}
        src={renderLink}
      />
    </Card>
  );
};
