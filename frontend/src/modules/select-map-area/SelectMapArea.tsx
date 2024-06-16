import { Layer, Map } from "react-map-gl";
import mapboxgl, { FillLayer } from "mapbox-gl";
import { MAPBOX_TOKEN } from "@/shared/env";
import { useCallback, useState } from "react";
import { DrawControl } from "./DrawControl";
import { ControlPanel } from "./ControlPanel";
import { useAppContext } from "@/shared/context";

mapboxgl.accessToken = MAPBOX_TOKEN;

const buildingsLayer: FillLayer = {
  id: "add-3d-buildings",
  source: "composite",
  "source-layer": "building",
  filter: ["==", "extrude", "true"],
  type: "fill-extrusion",
  minzoom: 15,
  paint: {
    "fill-extrusion-color": "#aaa",

    "fill-extrusion-height": [
      "interpolate",
      ["linear"],
      ["zoom"],
      15,
      0,
      15.05,
      ["get", "height"],
    ],
    "fill-extrusion-base": [
      "interpolate",
      ["linear"],
      ["zoom"],
      15,
      0,
      15.05,
      ["get", "min_height"],
    ],
    "fill-extrusion-opacity": 0.6,
  },
};

export const SelectMapArea = () => {
  const { setPolygon } = useAppContext();
  const [features, setFeatures] = useState({});

  const onUpdate = useCallback(
    (e) => {
      setFeatures((currFeatures) => {
        const newFeatures = { ...currFeatures };
        for (const f of e.features) {
          newFeatures[f.id] = f;
        }
        return newFeatures;
      });

      const polygons = Object.values(e.features).map(
        (f) => f.geometry.coordinates[0],
      );

      setPolygon(polygons[0]);
    },
    [setPolygon],
  );

  const onDelete = useCallback((e) => {
    setFeatures((currFeatures) => {
      const newFeatures = { ...currFeatures };
      for (const f of e.features) {
        delete newFeatures[f.id];
      }
      return newFeatures;
    });
  }, []);

  return (
    <div>
      <Map
        mapLib={import("mapbox-gl")}
        initialViewState={{
          longitude: 30.323304,
          latitude: 59.931658,
          zoom: 15,
          pitch: 45,
        }}
        style={{ width: "100%", height: 300 }}
        mapStyle="mapbox://styles/mapbox/dark-v11"
      >
        <Layer
          id="add-3d-buildings"
          sourceLayer="building"
          {...buildingsLayer}
        />
        <DrawControl
          position="top-left"
          displayControlsDefault={false}
          controls={{
            polygon: true,
            trash: true,
          }}
          defaultMode="draw_polygon"
          onCreate={onUpdate}
          onUpdate={onUpdate}
          onDelete={onDelete}
        />
      </Map>
    </div>
  );
};
