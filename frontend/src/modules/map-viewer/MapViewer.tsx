import { Card } from "@gravity-ui/uikit";
import classNames from "classnames";

import styles from "./MapViewer.module.scss";

interface Props {
  className?: string;
}

export const MapViewer = ({ className }: Props) => {
  return (
    <Card className={classNames(styles.mapViewer, className)}>MapViewer</Card>
  );
};
