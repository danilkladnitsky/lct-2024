import classnames from "classnames";
import { CSSProperties, ComponentType, ReactNode } from "react";

import styles from "./Stack.module.scss";

export const Stack: ComponentType<{
  children: ReactNode;
  css?: CSSProperties;
  gap?: number;
  align?: CSSProperties["textAlign"];
  className?: string;
}> = ({ children, css, gap = 8, align = "unset", className }) => {
  return (
    <div
      className={classnames(styles.stack, className)}
      style={{
        ...css,
        gap,
        textAlign: align,
      }}
    >
      {children}
    </div>
  );
};
