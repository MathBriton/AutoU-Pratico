import os
import openai

# Defina sua chave de API como variável de ambiente
# Ex: export OPENAI_API_KEY="sua_chave"
openai.api_key = os.getenv("OPENAI_API_KEY")

def classificar(texto: str):
    """
    Recebe o texto pré-processado e retorna:
    - categoria: "Produtivo" ou "Improdutivo"
    - confianca: estimativa de confiança (0 a 1)
    """
    try:
        prompt = f"""
        Você é um assistente que classifica emails em duas categorias:
        - Produtivo: emails que requerem ação ou resposta.
        - Improdutivo: emails que não requerem ação imediata.

        Classifique o seguinte email e responda apenas com o nome da categoria:

        {texto}
        """

        resposta = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=10,
            temperature=0
        )

        categoria = resposta.choices[0].text.strip()
        # Ajuste simples para confiança
        confianca = 0.95 if categoria.lower() in ["produtivo", "improdutivo"] else 0.5

        return categoria, confianca

    except Exception as e:
        print("Erro ao classificar:", e)
        return "Indefinido", 0.0

def gerar_resposta(categoria: str):
    """
    Gera uma resposta automática baseada na categoria
    """
    try:
        if categoria.lower() == "produtivo":
            prompt = "Gere uma resposta educada e útil para um email produtivo."
        elif categoria.lower() == "improdutivo":
            prompt = "Gere uma resposta breve indicando que não é necessária ação."
        else:
            prompt = "Gere uma resposta padrão indicando que o email não pôde ser classificado."

        resposta = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            temperature=0.7
        )

        return resposta.choices[0].text.strip()

    except Exception as e:
        print("Erro ao gerar resposta:", e)
        return "Não foi possível gerar uma resposta."
