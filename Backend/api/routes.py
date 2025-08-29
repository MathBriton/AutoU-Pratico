from fastapi import APIRouter, UploadFile, Form
from services import nlp_service, ai_service
from infrastructure import file_parser
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/emails",
    tags=["Emails"]
)

@router.post("/processar", summary="Processa um email e retorna categoria e sugestão de resposta")
async def processar_email(file: UploadFile = None, texto: str = Form(None)):
    """
    Recebe um email em formato de arquivo (.txt ou .pdf) ou texto direto,
    realiza pré-processamento, classifica como Produtivo ou Improdutivo,
    e sugere uma resposta automática.
    """
    # 1. Extrair conteúdo
    conteudo = ""
    if file:
        raw = await file.read()
        conteudo = file_parser.parse_file(file.filename, raw)
    elif texto:
        conteudo = texto

    if not conteudo:
        return JSONResponse(status_code=400, content={"erro": "Nenhum conteúdo válido encontrado."})

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
