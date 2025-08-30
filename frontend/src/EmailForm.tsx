import React, { useState } from "react";
import axios, { AxiosError } from "axios";

interface ResultadoEmail {
  conteudo: string;
  categoria: string;
  confianca: number;
  resposta: string;
}

const EmailForm: React.FC = () => {
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
    <div className="w-full max-w-xl mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center">Processar Email</h2>

      <form onSubmit={handleSubmit} className="space-y-5">
        <div>
          <label className="block mb-2 font-medium text-gray-700">
            Upload de arquivo (.txt ou .pdf):
          </label>
          <input
            type="file"
            accept=".txt,.pdf"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />
        </div>

        <div>
          <label className="block mb-2 font-medium text-gray-700">
            Ou insira o texto do email:
          </label>
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

      {erro && <p className="mt-4 text-red-500 text-center">{erro}</p>}

      {resultado && (
        <div className="resultado">
          <h3 className="text-xl font-semibold mb-3 text-gray-800">Resultado</h3>
          <p><strong>Categoria:</strong> {resultado.categoria}</p>
          <p><strong>Confiança:</strong> {resultado.confianca}</p>
          <p><strong>Resposta sugerida:</strong> {resultado.resposta}</p>
          <p><strong>Conteúdo do email:</strong> {resultado.conteudo}</p>
        </div>
      )}
    </div>
  );
};

export default EmailForm;
