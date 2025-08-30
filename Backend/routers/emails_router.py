from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.emails_router import router as email_router  # aponta direto para emails_router.py

app = FastAPI(title="Email Classifier API")

# Configuração CORS
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar router
app.include_router(email_router)

@app.get("/")
def root():
    return {"message": "API de classificação de Emails rodando!"}
