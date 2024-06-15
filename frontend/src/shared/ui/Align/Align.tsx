import { CSSProperties, ComponentType, ReactNode } from "react";

import styles from "./Align.module.scss";

export const Align: ComponentType<{
  children: ReactNode;
  css?: CSSProperties;
  gap?: number;
}> = ({ children, css, gap }) => {
  return (
    <div className={styles.align} style={{ ...css, gap }}>
      {children}
    </div>
  );
};
