import { CheckboxProps, Checkbox as UICheckbox } from "@gravity-ui/uikit";
import { forwardRef } from "react";

interface Props
  extends Pick<CheckboxProps, "onChange" | "value" | "checked" | "name"> {
  label: string;
}

export const Checkbox = forwardRef<HTMLInputElement, Props>(
  ({ label, ...restProps }, ref) => {
    return <UICheckbox content={label} size="l" ref={ref} {...restProps} />;
  },
);
