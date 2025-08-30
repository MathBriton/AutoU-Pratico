import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // import default do App
import "./index.css"; // CSS global/Tailwind

const root = document.getElementById("root");
if (!root) throw new Error("Elemento raiz #root não encontrado no HTML");

ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
