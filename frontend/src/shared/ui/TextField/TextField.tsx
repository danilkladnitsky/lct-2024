import { Spin, Text, TextInput, TextInputProps } from "@gravity-ui/uikit";
import { forwardRef } from "react";

interface Props
  extends Pick<TextInputProps, "value" | "placeholder" | "label" | "onChange"> {
  isLoading?: boolean;
}

export const TextField = forwardRef<HTMLInputElement, Props>(
  (
    {
      placeholder = "Введите значение...",
      isLoading = false,
      label,
      ...restProps
    },
    ref,
  ) => {
    return (
      <TextInput
        ref={ref}
        placeholder={placeholder}
        size="l"
        disabled={isLoading}
        hasClear
        startContent={
          <Text
            variant="body-1"
            style={{ width: 160, textAlign: "left", padding: "0px 12px" }}
          >
            {label}
          </Text>
        }
        endContent={
          isLoading ? <Spin size="xs" style={{ padding: 8 }} /> : null
        }
        {...restProps}
      />
    );
  },
);
