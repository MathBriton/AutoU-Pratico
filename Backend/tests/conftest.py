# conftest.py
import pytest
from fastapi.testclient import TestClient
from services import ai_service
from main import app

# Fixture: cliente de teste FastAPI
@pytest.fixture
def client():
    """
    Retorna um TestClient do FastAPI para realizar chamadas HTTP simuladas.
    """
    return TestClient(app)
# Fixture: mock de AI
@pytest.fixture
def mock_ai(monkeypatch):
    """
    Mocka os métodos classificar e gerar_resposta do ai_service,
    para que os testes não precisem de uma chave real da OpenAI.
    """
    def mock_classificar(texto: str):
        # Sempre retorna 'Produtivo' com confiança 0.95
        return "Produtivo", 0.95

    def mock_gerar_resposta(categoria: str):
        return "Esta é uma resposta simulada."

    monkeypatch.setattr(ai_service, "classificar", mock_classificar)
    monkeypatch.setattr(ai_service, "gerar_resposta", mock_gerar_resposta)
