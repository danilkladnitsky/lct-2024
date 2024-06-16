import classNames from "classnames";

import { Card, Text } from "@gravity-ui/uikit";
import styles from "./BuildingMetrics.module.scss";
import { useAppContext } from "@/shared/context";
import { UploadSettingsFormFields } from "@/shared/types";

interface Props {
  className?: string;
}

const Metric = ({
  label,
  value = 0,
}: {
  label: string;
  value?: string | number;
}) => {
  return (
    <div className={styles.metric}>
      <Text>{label} </Text>
      <Text>{value}</Text>
    </div>
  );
};

export const BuildingMetrics = ({ className }: Props) => {
  const { watch } = useAppContext();

  const { levels_num, level_height, square_size, human_capacity } =
    watch() as UploadSettingsFormFields;

  return (
    <Card className={classNames(styles.card, className)}>
      <Text variant="subheader-2">Технико-экономические показатели</Text>
      <div className={styles.metrics}>
        <Metric label="Количество этажей:" value={levels_num} />
        <Metric label="Количество мест:" value={human_capacity} />
        <Metric label="Площадь участка (Га):" value={square_size} />
        <Metric label="Высота здания, (м.):" value={level_height} />
      </div>
    </Card>
  );
};
