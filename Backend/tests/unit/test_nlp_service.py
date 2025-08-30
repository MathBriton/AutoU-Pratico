from services import nlp_service

def test_preprocessar_texto():
    texto = "Olá, este é um email de teste!"
    resultado = nlp_service.preprocessar(texto)
    # O texto deve estar em minúsculo, sem pontuação e sem stopwords
    assert "email" in resultado
    assert "teste" in resultado
