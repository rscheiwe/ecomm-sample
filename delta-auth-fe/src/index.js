import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, RouterProvider } from "react-router-dom";
import { Provider } from "react-redux";
import { store } from "./@redux/store";

import { AuthProvider } from "./hooks/useAuth";
import App from "./App";

import "./styles/globals.css";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
  <StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <Provider store={store}>
          {/* <ThemeProvider theme={theme}> */}
          <App />
          {/* </ThemeProvider> */}
        </Provider>
      </AuthProvider>
    </BrowserRouter>
  </StrictMode>
);
