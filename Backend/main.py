from fastapi import FastAPI
from api import routes

app = FastAPI(title="Email classificer API")

app.include_router(routes.router)

@app.get("/")
def root():
    return{"message":"API de classificação de Emails rodando!"}