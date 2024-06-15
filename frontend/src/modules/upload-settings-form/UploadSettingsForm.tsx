import { useForm } from "react-hook-form";

import { DEFAULT_UPLOAD_FORM_SETTINGS } from "@/shared/const";
import { UploadSettingsFormFields } from "@/shared/types";
import { Checkbox, SectionLabel, Stack, TextField } from "@/shared/ui";
import { Button, Card, RadioButton } from "@gravity-ui/uikit";

import styles from "./UploadSettingsForm.module.scss";

export const UploadSettingsForm = () => {
  const {
    register,
    handleSubmit,
    watch,
    getValues,
    formState: { errors },
  } = useForm<UploadSettingsFormFields>({
    defaultValues: DEFAULT_UPLOAD_FORM_SETTINGS,
    mode: "onChange",
  });

  const onSubmit = () => {
    console.log(getValues());
  };

  return (
    <Card className={styles.form}>
      <Stack className={styles.fields} gap={16}>
        <Stack>
          <SectionLabel>Технико-экономические характеристики</SectionLabel>
          <TextField label="Высота этажа" {...register("level_height")} />
          <TextField label="Количество этажей" {...register("levels_num")} />
          <TextField label="Площадь" {...register("square_size")} />
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
              label="Наличие корпуса младших классов"
              {...register("has_junior")}
            />
            <Checkbox
              label="Корпус старших и младших классов соединены"
              {...register("has_junior_hight_connection")}
            />
            <Checkbox
              label="Наличие отдельного актового зала в младшей школе"
              {...register("has_junior_assembly_hall")}
            />
            <Checkbox
              label="Наличие отдельной столовой в младшей школе"
              {...register("has_junior_dining_room")}
            />
            <Checkbox
              label="Наличие отдельного спортзала в младшей школе"
              {...register("has_junior_gym")}
            />
          </Stack>
          <Stack css={{ marginLeft: 16, marginTop: 8 }}>
            <SectionLabel>Настройки спорт-зоны</SectionLabel>
            <Checkbox
              label="Наличие бассейна"
              {...register("has_swimming_pool")}
            />
            <Checkbox
              label="Наличие волейбольной площадки"
              {...register("has_volleyball_court")}
            />
            <Checkbox
              label="Наличие баскетбольной площадки"
              {...register("has_basketball_court")}
            />
            <Checkbox
              label="Наличие турниковой зоны"
              {...register("has_additional_sport_square")}
            />
          </Stack>
          <Stack css={{ marginLeft: 16, marginTop: 8 }}>
            <SectionLabel>Прочее</SectionLabel>
            <Checkbox
              label="Наличие зоны отдыха"
              {...register("has_relax_zone")}
            />
            <Checkbox
              label="Наличие хозяйственной зоны"
              {...register("has_additional_ground_zone")}
            />
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
