import React from "react";
import EmailForm from "./EmailForm";
import "./index.css"; // CSS global/Tailwind

const App: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-start py-10 bg-gray-100">
      <h1 className="text-3xl font-bold mb-8 text-center text-gray-800">
        Classificador de Emails
      </h1>
      <EmailForm />
    </div>
  );
};

export default App; // export default
