from fastapi import FastAPI
from api.routes import router as email_router  # import mais explícito

app = FastAPI(title="Email Classifier API")

# Registrar rotas
app.include_router(email_router)

@app.get("/")
def root():
    return {"message": "API de classificação de Emails rodando!"}
