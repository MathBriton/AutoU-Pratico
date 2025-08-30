from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
from services import nlp_service, ai_service, file_parser, mock_service
from data import DbContext as historico

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
        conteudo = file_parser.parse_file(file.filename, raw)
    elif texto:
        conteudo = texto

    if not conteudo:
        return JSONResponse(status_code=400, content={"erro": "Nenhum conteúdo válido encontrado."})

    # Pré-processamento NLP
    texto_limpo = nlp_service.preprocessar(conteudo)

    # Classificação via AI (ou mock se não houver chave)
    categoria, confianca = ai_service.classificar(texto_limpo)

    # Geração de resposta via AI
    resposta = ai_service.gerar_resposta(categoria)

    # Salva no histórico
    historico.salvar(conteudo, categoria, confianca, resposta)

    return {
        "conteudo": conteudo,
        "categoria": categoria,
        "confianca": confianca,
        "resposta": resposta
    }


@router.get("/categorias", summary="Lista categorias possíveis")
async def listar_categorias():
    """
    Retorna a lista de categorias suportadas pelo sistema.
    """
    return {"categorias": ["Produtivo", "Improdutivo"]}


@router.get("/historico", summary="Lista histórico de emails processados")
async def listar_historico():
    """
    Retorna os emails já processados (mock ou base real).
    """
    return historico.listar()


@router.post("/treinar", summary="Treina o modelo de IA (mock)")
async def treinar_modelo():
    """
    Simula um treinamento de modelo. Não executa IA de verdade.
    """
    resultado = mock_service.treinar()
    return {"mensagem": "Treinamento concluído (mock)", "detalhes": resultado}


@router.get("/health", summary="Health check do sistema")
async def health_check():
    """
    Verifica se a API está no ar.
    """
    return {"status": "ok"}
