from fastapi import APIRouter, UploadFile, Form
from services import nlp_service, ai_service
from infrastructure import file_parser

router = APIRouter()

@router.post("/processar-email")
async def processar_email(file: UploadFile = None, texto: str = Form(None)):
    # 1. Extrair conteúdo
    conteudo = ""
    if file:
        raw = await file.read()
        conteudo = file_parser.parse_file(file.filename, raw)
    elif texto:
        conteudo = texto

    # 2. Pré-processar
    texto_limpo = nlp_service.preprocessar(conteudo)

    # 3. Classificar
    categoria, confianca = ai_service.classificar(texto_limpo)

    # 4. Gerar resposta
    resposta = ai_service.gerar_resposta(categoria)

    return {
        "conteudo": conteudo,
        "categoria": categoria,
        "confianca": confianca,
        "resposta": resposta
    }
