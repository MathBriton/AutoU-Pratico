import React, { useState } from "react";
import axios, { AxiosError } from "axios";

interface ResultadoEmail {
  conteudo: string;
  categoria: string;
  confianca: number;
  resposta: string;
}

export const EmailForm: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [texto, setTexto] = useState("");
  const [resultado, setResultado] = useState<ResultadoEmail | null>(null);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErro("");
    setResultado(null);

    if (!file && !texto.trim()) {
      setErro("Insira um texto ou faça upload de um arquivo.");
      return;
    }

    const formData = new FormData();
    if (file) formData.append("file", file);
    if (texto.trim()) formData.append("texto", texto);

    try {
      setLoading(true);
      const response = await axios.post<ResultadoEmail>(
        "http://localhost:8000/emails/processar",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setResultado(response.data);
    } catch (err) {
      const axiosError = err as AxiosError<{ detail?: string }>;
      setErro(
        axiosError.response?.data?.detail || "Erro ao processar email."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="email-form">
      <h2>Processar Email</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Upload de arquivo (.txt ou .pdf):</label>
          <input
            type="file"
            accept=".txt,.pdf"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />
        </div>
        <div>
          <label>Ou insira o texto do email:</label>
          <textarea
            value={texto}
            onChange={(e) => setTexto(e.target.value)}
            rows={6}
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Processando..." : "Enviar"}
        </button>
      </form>

      {erro && <p style={{ color: "red" }}>{erro}</p>}

      {resultado && (
        <div className="resultado">
          <h3>Resultado</h3>
          <p>
            <strong>Categoria:</strong> {resultado.categoria}
          </p>
          <p>
            <strong>Confiança:</strong> {resultado.confianca}
          </p>
          <p>
            <strong>Resposta sugerida:</strong> {resultado.resposta}
          </p>
          <p>
            <strong>Conteúdo do email:</strong> {resultado.conteudo}
          </p>
        </div>
      )}
    </div>
  );
};
