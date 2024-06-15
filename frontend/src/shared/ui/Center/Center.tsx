import { ComponentType, ReactNode } from "react";

export const Center: ComponentType<{ children: ReactNode }> = ({
  children,
}) => {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: "inherit",
      }}
    >
      {children}
    </div>
  );
};
