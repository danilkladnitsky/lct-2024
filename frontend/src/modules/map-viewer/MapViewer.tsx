import { Card } from "@gravity-ui/uikit";
import classNames from "classnames";

import { Map } from "react-map-gl";
import styles from "./MapViewer.module.scss";

interface Props {
  className?: string;
}

export const MapViewer = ({ className }: Props) => {
  return (
    <Card className={classNames(styles.mapViewer, className)}>
      <Map
        initialViewState={{
          longitude: -91.874,
          latitude: 42.76,
          zoom: 12,
        }}
        mapStyle="mapbox://styles/mapbox/satellite-v9"
      ></Map>
    </Card>
  );
};
