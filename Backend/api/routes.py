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
    conteudo = ""

    if file:
        raw = await file.read()
        print(f"[INFO] Recebido arquivo: {file.filename}, tamanho: {len(raw)} bytes")
        conteudo = file_parser.parse_file(file.filename, raw)
        print(f"[INFO] Conteúdo extraído (primeiros 200 caracteres): {conteudo[:200]}")

    elif texto:
        conteudo = texto
        print(f"[INFO] Texto recebido direto: {conteudo[:200]}")

    if not conteudo:
        return JSONResponse(status_code=400, content={"erro": "Nenhum conteúdo válido encontrado."})

    # Pré-processamento NLP
    texto_limpo = nlp_service.preprocessar(conteudo)

    # Classificação via AI
    categoria, confianca = ai_service.classificar(texto_limpo)

    # Geração de resposta via AI
    resposta = ai_service.gerar_resposta(categoria)

    return {
        "conteudo": conteudo,
        "categoria": categoria,
        "confianca": confianca,
        "resposta": resposta
    }
