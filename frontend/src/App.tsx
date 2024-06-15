import { ThemeProvider } from "@gravity-ui/uikit";

import { UploadSettingsForm } from "./modules";

import "./App.css";

function App() {
  return (
    <ThemeProvider>
      <UploadSettingsForm />
    </ThemeProvider>
  );
}

export default App;
