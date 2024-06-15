import { CSSProperties, ComponentType, ReactNode } from 'react';
import styles from './Group.module.scss';

export const Group: ComponentType<{ children: ReactNode; css?: CSSProperties; gap?: number }> = ({
  children,
  css,
  gap = 8,
}) => {
  return (
    <div
      className={styles.group}
      style={{
        ...css,
        gap,
      }}
    >
      {children}
    </div>
  );
};
