import { Text, ThemeProvider } from "@gravity-ui/uikit";

import { BuildingMetrics, UploadSettingsForm } from "@/modules";

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
          <Group css={{ alignItems: "center" }}>
            <Text variant="header-1" style={{ maxWidth: 374, width: "100%" }}>
              Проектировщик зданий | Южане 2
            </Text>
            <ButtonIcon
              isLoading={formIsVisible}
              onClick={() => setFormIsVisible(true)}
              icon={ArrowShapeUpFromLine}
              title="Загрузить конфигурацию"
            />
          </Group>
        </div>
        {formIsVisible && (
          <UploadSettingsForm
            close={() => setFormIsVisible(false)}
            className={styles.settingsForm}
          />
        )}
        <BuildingMetrics className={styles.metrics} />
      </div>
    </ThemeProvider>
  );
}

export default App;
