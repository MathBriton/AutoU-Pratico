import random

def classificar(texto: str):
    if "problema" in texto or "suporte" in texto or "ajuda" in texto:
        return "Produtivo", random.uniform(0.8, 0.95)
    else:
        return "Improdutivo", random.uniform(0.7, 0.9)

def gerar_resposta(categoria: str):
    if categoria == "Produtivo":
        return "Obrigado pelo contato, nossa equipe retornará em breve."
    else:
        return "Agradecemos sua mensagem! Tenha um ótimo dia."
