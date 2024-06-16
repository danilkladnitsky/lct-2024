import { Label, Text, ThemeProvider } from "@gravity-ui/uikit";

import { BuildingMetrics, MapViewer, UploadSettingsForm } from "@/modules";

import { ArrowShapeUpFromLine } from "@gravity-ui/icons";
import { useState } from "react";
import { ButtonIcon, Group } from "./shared/ui";

import styles from "./App.module.scss";
import { usePingBackend } from "./api/hooks/usePingBackend";
import { APP_VERSION, APP_VERSION_LINK } from "./shared/env";

function App() {
  const { data: isLive } = usePingBackend();
  const [formIsVisible, setFormIsVisible] = useState(true);

  return (
    <ThemeProvider>
      <div className={styles.app}>
        <div className={styles.systemInfo}>
          <div className={styles.releaseTag}>
            Версия:
            <a target="_blank" href={APP_VERSION_LINK}>
              <Label interactive theme="info">
                {APP_VERSION}
              </Label>
            </a>
          </div>
          <div className={styles.backendLiveness}>
            Сервер: {isLive ? "live" : "dead"}
          </div>
        </div>
        <div className={styles.header}>
          <Group
            css={{ justifyContent: "space-between", alignItems: "center" }}
          >
            <Text variant="header-1">Проектировщик зданий | Южане 2</Text>
            {!formIsVisible && (
              <ButtonIcon
                onClick={() => setFormIsVisible(true)}
                icon={ArrowShapeUpFromLine}
                title={formIsVisible ? "Закрыть окно" : "Добавить конфигурацию"}
              />
            )}
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
