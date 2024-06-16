import { configure } from "@gravity-ui/uikit";
import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App.tsx";

configure({
  lang: "ru",
});

import "@gravity-ui/uikit/styles/fonts.css";
import "@gravity-ui/uikit/styles/styles.css";
import { QueryClient, QueryClientProvider } from "react-query";
import "./index.css";
import { AppContextProvider } from "./shared/context/index.tsx";

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <AppContextProvider>
        <App />
      </AppContextProvider>
    </QueryClientProvider>
  </React.StrictMode>,
);
