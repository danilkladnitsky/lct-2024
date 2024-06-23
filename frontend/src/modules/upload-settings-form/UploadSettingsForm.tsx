import {
  Checkbox,
  CloseButton,
  SectionLabel,
  Stack,
  TextField,
} from "@/shared/ui";
import { Button, Card, RadioButton } from "@gravity-ui/uikit";
import classNames from "classnames";

import styles from "./UploadSettingsForm.module.scss";
import { useAppContext } from "@/shared/context";
import { SelectMapArea } from "../select-map-area/SelectMapArea";

interface Props {
  close: () => void;
  className?: string;
}

export const UploadSettingsForm = ({ close, className }: Props) => {
  const { registerField: register, generateScene } = useAppContext();

  const onSubmit = () => {
    generateScene();
  };

  return (
    <Card className={classNames(styles.form, className)}>
      <CloseButton onClick={close} className={styles.closeButton} />
      <SectionLabel>Технико-экономические показатели</SectionLabel>
      <Stack className={styles.fields} gap={16}>
        <Stack>
          <TextField label="Высота этажа (м)" {...register("level_height")} />
          <TextField label="Количество этажей" {...register("levels_num")} />
          <TextField label="Площадь (м2)" {...register("square_size")} />
          <TextField label="Вместимость" {...register("human_capacity")} />
        </Stack>
        <Stack>
          <SectionLabel>Конфигурация объекта</SectionLabel>
          <RadioButton
            size="l"
            value="school"
            options={[
              {
                value: "school",
                content: "Школа",
              },
              {
                value: "hospital",
                content: "Больница",
                disabled: true,
              },
              {
                value: "gym",
                content: "Центр физкультуры",
                disabled: true,
              },
            ]}
          />
          <Stack css={{ marginLeft: 16, marginTop: 8 }}>
            <SectionLabel>Настройки корпуса младшей школы</SectionLabel>
            <Checkbox
              label="Корпус младших классов"
              {...register("has_junior")}
            />
            <Checkbox
              label="Корпусы старших и младших классов соединены"
              {...register("has_junior_hight_connection")}
            />
            <Checkbox
              label="Отдельный актовый зал в младшей школе"
              {...register("has_junior_assembly_hall")}
            />
            <Checkbox
              label="Отдельная столовая в младшей школе"
              {...register("has_junior_dining_room")}
            />
            <Checkbox
              label="Отдельный спортзал в младшей школе"
              {...register("has_junior_gym")}
            />
          </Stack>
          <Stack css={{ marginLeft: 16, marginTop: 8 }}>
            <SectionLabel>Настройки спортивной зоны</SectionLabel>
            <Checkbox
              label="Бассейна"
              {...register("has_swimming_pool")}
            />
            <Checkbox
              label="Волейбольной площадка"
              {...register("has_volleyball_court")}
            />
            <Checkbox
              label="Баскетбольная площадка"
              {...register("has_basketball_court")}
            />
            <Checkbox
              label="Площадка с тренажёрами"
              {...register("has_additional_sport_square")}
            />
          </Stack>
          <Stack css={{ marginLeft: 16, marginTop: 8 }}>
            <SectionLabel>Прочее</SectionLabel>
            <Checkbox
              label="Зона отдыха"
              {...register("has_relax_zone")}
            />
            <Checkbox
              label="Учебно-опытная зона"
              {...register("has_additional_ground_zone")}
            />
          </Stack>
          <Stack css={{ marginLeft: 0, marginTop: 16 }}>
            <SectionLabel>Область</SectionLabel>
            <SelectMapArea />
          </Stack>
        </Stack>
      </Stack>
      <div>
        <Button
          style={{ marginTop: 16 }}
          view="action"
          size="l"
          width="max"
          onClick={onSubmit}
        >
          Отправить
        </Button>
      </div>
    </Card>
  );
};
