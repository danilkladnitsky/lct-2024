import classNames from "classnames";

import { Card, Text } from "@gravity-ui/uikit";
import styles from "./BuildingMetrics.module.scss";

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
  return (
    <Card className={classNames(styles.card, className)}>
      <Text variant="subheader-2">Технико-экономические показатели</Text>
      <div className={styles.metrics}>
        <Metric label="Количество этажей:" />
        <Metric label="Количество мест:" />
        <Metric label="Площадь участка (Га):" />
        <Metric label="Высота здания, (м.):" />
      </div>
    </Card>
  );
};
