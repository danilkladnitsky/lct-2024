import { ComponentType, ReactNode, createContext, useContext } from "react";
import { UploadSettingsFormFields } from "../types";
import { UseFormGetValues, UseFormRegister, useForm } from "react-hook-form";
import { DEFAULT_UPLOAD_FORM_SETTINGS } from "../const";

interface AppContextProps {
  registerField: UseFormRegister<UploadSettingsFormFields>;
  getFields: () => UseFormGetValues<UploadSettingsFormFields>;
  watch: () => UploadSettingsFormFields;
}

const AppContext = createContext<AppContextProps>({} as AppContextProps);

export const useAppContext = () => useContext(AppContext) as AppContextProps;

export const AppContextProvider: ComponentType<{ children: ReactNode }> = ({
  children,
}) => {
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
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
