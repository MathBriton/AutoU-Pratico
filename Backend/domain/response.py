from pydantic import BaseModel

class ResponseMessage(BaseModel):
    mensagem: str