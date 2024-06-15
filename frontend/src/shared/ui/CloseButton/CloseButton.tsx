import { Xmark } from "@gravity-ui/icons";
import { Button, Icon } from "@gravity-ui/uikit";

interface Props {
  onClick: () => void;
  className?: string;
}

export const CloseButton = ({ onClick, className }: Props) => {
  return (
    <Button className={className} onClick={onClick}>
      <Icon data={Xmark} />
    </Button>
  );
};
