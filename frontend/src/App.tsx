import React from "react";
import {EmailForm} from "./components/EmailForm";
import "./styles/css";

const App: React.FC = () => {
    return (
        <div className="App">
            <h1>Classificador de Emails</h1>
            <EmailForm/>
        </div>
    );
};

export default App;