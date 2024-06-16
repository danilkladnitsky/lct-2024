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

interface AppContextProps {
  formIsVisible: boolean;
  setFormIsVisible: (value: boolean) => void;
  registerField: UseFormRegister<UploadSettingsFormFields>;
  getFields: () => UseFormGetValues<UploadSettingsFormFields>;
  watch: () => UploadSettingsFormFields;
}

const AppContext = createContext<AppContextProps>({} as AppContextProps);

export const useAppContext = () => useContext(AppContext) as AppContextProps;

export const AppContextProvider: ComponentType<{ children: ReactNode }> = ({
  children,
}) => {
  const [formIsVisible, setFormIsVisible] = useState(true);
  const { register, getValues, watch } = useForm<UploadSettingsFormFields>({
    defaultValues: DEFAULT_UPLOAD_FORM_SETTINGS,
    mode: "onChange",
  });

  return (
    <AppContext.Provider
      value={{
        registerField: register,
        getFields: getValues,
        watch,
        formIsVisible,
        setFormIsVisible,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
