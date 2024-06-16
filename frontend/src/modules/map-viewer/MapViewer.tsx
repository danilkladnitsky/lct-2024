import { Card, Loader, Spin } from "@gravity-ui/uikit";
import classNames from "classnames";

import styles from "./MapViewer.module.scss";
import { useEffect, useRef, useState } from "react";
import { useAppContext } from "@/shared/context";

interface Props {
  className?: string;
}

export const MapViewer = ({ className }: Props) => {
  const { formIsVisible } = useAppContext();
  const [isLoading, setIsLoading] = useState(true);
  const iFrameRef = useRef<HTMLIFrameElement>(null);

  const iframeCurrent = iFrameRef.current;
  useEffect(() => {
    iframeCurrent?.addEventListener("load", () => setIsLoading(false));
    return () => {
      iframeCurrent?.removeEventListener("load", () => setIsLoading(true));
    };
  }, [iframeCurrent]);

  return (
    <Card className={classNames(styles.mapViewer, className)}>
      {isLoading && (
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
        src="https://api-lct-2024.kladnitsky.ru/render"
      />
    </Card>
  );
};
