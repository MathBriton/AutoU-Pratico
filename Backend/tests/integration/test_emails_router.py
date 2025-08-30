from fastapi.testclient import TestClient
from main import app  # sua aplicação FastAPI

client = TestClient(app)

def test_health_check():
    response = client.get("/emails/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_listar_categorias():
    response = client.get("/emails/categorias")
    assert response.status_code == 200
    assert "Produtivo" in response.json()["categorias"]

def test_processar_email_texto(monkeypatch):
    # Mock da AI para não depender de chave real
    from services import ai_service

    class MockResponse:
        class Choice:
            message = type("obj", (), {"content": "Produtivo"})
        choices = [Choice()]

    monkeypatch.setattr(ai_service.client.chat.completions, "create", lambda **kwargs: MockResponse())
    
    payload = {"texto": "Reunião importante amanhã"}
    response = client.post("/emails/processar", data=payload)
    
    assert response.status_code == 200
    body = response.json()
    assert body["categoria"] == "Produtivo"
    assert "resposta" in body
    assert "conteudo" in body
