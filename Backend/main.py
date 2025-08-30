# Backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.emails_router import router as email_router  # importa o router principal

# Cria a instância do FastAPI
app = FastAPI(title="Email Classifier API")

# Configuração CORS para permitir frontend local
origins = [
    "http://localhost:5173",  # endereço do seu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],     # permitir todos os métodos (GET, POST, etc)
    allow_headers=["*"],     # permitir todos os headers
)

# Registrar o router de emails
app.include_router(email_router)

# Endpoint raiz para checagem simples da API
@app.get("/")
def root():
    return {"message": "API de classificação de Emails rodando!"}

# Entrypoint para rodar diretamente com Python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
