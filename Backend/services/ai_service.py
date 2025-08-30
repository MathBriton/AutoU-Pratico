import os
from openai import OpenAI

# Pega a chave da variável de ambiente
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("A variável de ambiente OPENAI_API_KEY não está definida!")

client = OpenAI(api_key=api_key)

def classificar(texto: str):
    prompt = (
        "Classifique o seguinte email em 'Produtivo' ou 'Improdutivo':\n\n"
        f"{texto}\n\n"
        "Retorne apenas a categoria e uma confiança estimada de 0 a 1."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    content = response.choices[0].message.content.strip()
    if "produtivo" in content.lower():
        return "Produtivo", 0.95
    else:
        return "Improdutivo", 0.95

def gerar_resposta(categoria: str):
    if categoria == "Produtivo":
        prompt = "Crie uma resposta educada e útil para um email produtivo."
    else:
        prompt = "Crie uma resposta breve e cortês para um email improdutivo."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    return response.choices[0].message.content.strip()
