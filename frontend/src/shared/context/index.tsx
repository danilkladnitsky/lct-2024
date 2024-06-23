import {
  ComponentType,
  ReactNode,
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";
import { UploadSettingsFormFields } from "../types";
import { UseFormGetValues, UseFormRegister, useForm } from "react-hook-form";
import { DEFAULT_UPLOAD_FORM_SETTINGS } from "../const";
import { API_HOST } from "../env";

interface AppContextProps {
  formIsVisible: boolean;
  polygon: UploadSettingsFormFields["polygon_points"];
  renderLink: string;
  sceneIsLoading: boolean;
  setFormIsVisible: (value: boolean) => void;
  registerField: UseFormRegister<UploadSettingsFormFields>;
  getFields: () => UseFormGetValues<UploadSettingsFormFields>;
  watch: () => UploadSettingsFormFields;
  setPolygon: (value: UploadSettingsFormFields["polygon_points"]) => void;
  generateScene: () => void;
  setSceneIsLoading: (value: boolean) => void;
}

const AppContext = createContext<AppContextProps>({} as AppContextProps);

export const useAppContext = () => useContext(AppContext) as AppContextProps;

export const AppContextProvider: ComponentType<{ children: ReactNode }> = ({
  children,
}) => {
  const [sceneIsLoading, setSceneIsLoading] = useState(false);
  const [attempts, setAttempts] = useState(0);
  const [renderLink, setRenderLink] = useState("");
  const [formIsVisible, setFormIsVisible] = useState(true);
  const [polygon, setPolygon] = useState<
    UploadSettingsFormFields["polygon_points"]
  >([]);
  const { register, getValues, watch } = useForm<UploadSettingsFormFields>({
    defaultValues: DEFAULT_UPLOAD_FORM_SETTINGS,
    mode: "onChange",
  });

  const form = watch();

  const generateScene = () => {
    setSceneIsLoading(true);
    const baseLink = `${API_HOST}/get-rendered-object`;
    const { level_height, ...fields } = getValues();

    const payload = {
      ...fields,
      level_height: Math.floor(level_height / 100),
      polygon_points: polygon,
      attempts: attempts + 1,
    };

    setRenderLink(`${baseLink}?json=${JSON.stringify(payload)}`);
    setAttempts((attempts) => attempts + 1);
  };

  return (
    <AppContext.Provider
      value={{
        polygon,
        formIsVisible,
        renderLink,
        sceneIsLoading,
        setPolygon,
        registerField: register,
        getFields: getValues,
        watch,
        setFormIsVisible,
        generateScene,
        setSceneIsLoading,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
