from pydantic import BaseModel

class Classification(BaseModel):
    categoria: str
    confianca: float