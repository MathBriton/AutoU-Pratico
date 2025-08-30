from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
from services import nlp_service, ai_service
from infrastructure import file_parser

router = APIRouter(
    prefix="/emails",
    tags=["Emails"]
)

# 🔹 Armazena histórico simples em memória
historico = []

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
        conteudo = file_parser.parse_file(file.filename, raw)
    elif texto:
        conteudo = texto

    if not conteudo:
        return JSONResponse(status_code=400, content={"erro": "Nenhum conteúdo válido encontrado."})

    # Pré-processamento NLP
    texto_limpo = nlp_service.preprocessar(conteudo)

    # Classificação via AI
    categoria, confianca = ai_service.classificar(texto_limpo)

    # Geração de resposta via AI
    resposta = ai_service.gerar_resposta(categoria)

    resultado = {
        "conteudo": conteudo,
        "categoria": categoria,
        "confianca": confianca,
        "resposta": resposta
    }

    # Guarda no histórico (poderia ser BD no futuro)
    historico.append(resultado)

    return resultado


@router.get("/categorias", summary="Lista as categorias possíveis")
async def listar_categorias():
    """
    Retorna todas as categorias de classificação possíveis.
    """
    return {"categorias": ["Produtivo", "Improdutivo"]}


@router.get("/historico", summary="Lista o histórico de classificações")
async def listar_historico():
    """
    Retorna os últimos e-mails classificados durante a execução do servidor.
    """
    return {"historico": historico}


@router.post("/treinar", summary="Simula o re-treinamento do modelo com novos dados")
async def treinar_modelo(dados: dict):
    """
    Endpoint mockado para simular o re-treinamento de modelo.
    """
    return {"status": "treinamento iniciado", "dados_recebidos": len(dados)}


@router.get("/health", summary="Health check da API")
async def health_check():
    """
    Verifica se o serviço está online.
    """
    return {"status": "ok"}
