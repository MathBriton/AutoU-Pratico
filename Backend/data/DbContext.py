# Mock de banco de dados em memória (apenas para teste técnico)

_historico = []


def salvar(conteudo: str, categoria: str, confianca: float, resposta: str):
    """
    Salva um registro de email processado no histórico.
    """
    _historico.append({
        "conteudo": conteudo,
        "categoria": categoria,
        "confianca": confianca,
        "resposta": resposta
    })


def listar():
    """
    Lista todos os emails processados no histórico.
    """
    return {"historico": _historico}
