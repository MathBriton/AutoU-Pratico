# services/mock_service.py

def classificar(texto: str):
    # Retorna mock para classificação
    if "importante" in texto.lower():
        return "Produtivo", 0.95
    return "Improdutivo", 0.90

def gerar_resposta(categoria: str):
    if categoria == "Produtivo":
        return "Obrigado pelo email, vamos tratar com prioridade."
    else:
        return "Recebido, obrigado pelo contato."
    
def treinar():
    # Mock para endpoint de treino
    return {"status": "mock_trained"}
