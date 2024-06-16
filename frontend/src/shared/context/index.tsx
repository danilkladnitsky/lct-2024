import {
  ComponentType,
  ReactNode,
  createContext,
  useContext,
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
  setFormIsVisible: (value: boolean) => void;
  registerField: UseFormRegister<UploadSettingsFormFields>;
  getFields: () => UseFormGetValues<UploadSettingsFormFields>;
  watch: () => UploadSettingsFormFields;
  setPolygon: (value: UploadSettingsFormFields["polygon_points"]) => void;
  generateScene: () => void;
}

const AppContext = createContext<AppContextProps>({} as AppContextProps);

export const useAppContext = () => useContext(AppContext) as AppContextProps;

export const AppContextProvider: ComponentType<{ children: ReactNode }> = ({
  children,
}) => {
  const [renderLink, setRenderLink] = useState("");
  const [formIsVisible, setFormIsVisible] = useState(true);
  const [polygon, setPolygon] = useState<
    UploadSettingsFormFields["polygon_points"]
  >([]);
  const { register, getValues, watch } = useForm<UploadSettingsFormFields>({
    defaultValues: DEFAULT_UPLOAD_FORM_SETTINGS,
    mode: "onChange",
  });

  const generateScene = () => {
    const baseLink = `${API_HOST}/get_rendered_object?`;
    const queryParams = new URLSearchParams();

    const fields = getValues();

    Object.entries(fields).forEach(([key, value]) => {
      queryParams.append(key, value.toString());
    });

    queryParams.append("polygon_points", polygon.toString());

    setRenderLink(`${baseLink}${queryParams.toString()}`);
  };

  return (
    <AppContext.Provider
      value={{
        polygon,
        formIsVisible,
        renderLink,
        setPolygon,
        registerField: register,
        getFields: getValues,
        watch,
        setFormIsVisible,
        generateScene,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};