from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as email_router

app = FastAPI(title="Email Classifier API")

# Configuração CORS
origins = [
    "http://localhost:5173",  # endereço do seu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # lista de domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],     # permitir todos métodos (GET, POST, etc)
    allow_headers=["*"],     # permitir todos headers
)

# Registrar rotas
app.include_router(email_router)

@app.get("/")
def root():
    return {"message": "API de classificação de Emails rodando!"}
