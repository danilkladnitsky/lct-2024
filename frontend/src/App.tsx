import { Text, ThemeProvider } from "@gravity-ui/uikit";

import { BuildingMetrics, MapViewer, UploadSettingsForm } from "@/modules";

import { ArrowShapeUpFromLine } from "@gravity-ui/icons";
import { useState } from "react";
import { ButtonIcon, Group } from "./shared/ui";

import styles from "./App.module.scss";

function App() {
  const [formIsVisible, setFormIsVisible] = useState(true);

  return (
    <ThemeProvider>
      <div className={styles.app}>
        <div className={styles.header}>
          <Group
            css={{ justifyContent: "space-between", alignItems: "center" }}
          >
            <Text variant="header-1">Проектировщик зданий | Южане 2</Text>
            <ButtonIcon
              isLoading={formIsVisible}
              onClick={() => setFormIsVisible(true)}
              icon={ArrowShapeUpFromLine}
              title="Загрузить конфигурацию"
            />
          </Group>
        </div>
        <div className={styles.layout}>
          {formIsVisible && (
            <div className={styles.left}>
              <UploadSettingsForm
                close={() => setFormIsVisible(false)}
                className={styles.settingsForm}
              />
            </div>
          )}
          <div className={styles.right}>
            <MapViewer className={styles.mapViewer} />
            <BuildingMetrics className={styles.metrics} />
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
