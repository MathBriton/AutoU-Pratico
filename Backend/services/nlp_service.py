# services/nlp_service.py

import spacy
import re

# Carregar modelo em português
# Você pode usar "pt_core_news_sm" ou instalar com:
# python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

def preprocessar(texto: str) -> str:
    """
    Pré-processa o texto:
    - Remove caracteres especiais
    - Remove múltiplos espaços
    - Remove stop words
    - Aplica lematização
    """
    # 1. Normalização básica
    texto = texto.lower()
    texto = re.sub(r"\s+", " ", texto)  # remover múltiplos espaços
    texto = re.sub(r"[^\w\s]", "", texto)  # remover pontuação

    # 2. Processar com spaCy
    doc = nlp(texto)
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and token.lemma_.strip() != ""
    ]

    # 3. Reconstruir texto limpo
    texto_limpo = " ".join(tokens)
    return texto_limpo
