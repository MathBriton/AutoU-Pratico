from services import ai_service

def test_classificar_mock(monkeypatch):
    # Mockar a resposta do client OpenAI
    class MockResponse:
        class Choice:
            message = type("obj", (), {"content": "Produtivo"})
        choices = [Choice()]
    
    monkeypatch.setattr(ai_service.client.chat.completions, "create", lambda **kwargs: MockResponse())
    
    categoria, confianca = ai_service.classificar("Teste de email")
    assert categoria == "Produtivo"
    assert 0 <= confianca <= 1

def test_gerar_resposta_produtivo(monkeypatch):
    class MockResponse:
        class Choice:
            message = type("obj", (), {"content": "Obrigado pelo envio do email"})
        choices = [Choice()]

    monkeypatch.setattr(ai_service.client.chat.completions, "create", lambda **kwargs: MockResponse())
    
    resposta = ai_service.gerar_resposta("Produtivo")
    assert "Obrigado" in resposta or len(resposta) > 0
