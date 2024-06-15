import { Text } from "@gravity-ui/uikit";
import { ComponentType, ReactNode } from "react";

export const SectionLabel: ComponentType<{ children: ReactNode }> = ({
  children,
}) => {
  return (
    <Text variant="header-1" style={{ marginBottom: 8 }}>
      {children}
    </Text>
  );
};
