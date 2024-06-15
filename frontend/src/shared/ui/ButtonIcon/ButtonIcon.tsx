import { Button, Icon } from "@gravity-ui/uikit";

interface Props {
  icon: any;
  title?: string;
  onClick?: () => void;
  isLoading?: boolean;
}

export const ButtonIcon = ({ icon, title, onClick, isLoading }: Props) => {
  return (
    <Button size="l" view="outlined" onClick={onClick} loading={isLoading}>
      <Icon data={icon} />
      {title}
    </Button>
  );
};
