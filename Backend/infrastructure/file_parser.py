import io
from typing import List

def parse_txt(raw_bytes: bytes) -> str:
    """Extrai texto de arquivos .txt"""
    try:
        return raw_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        print(f"[ERROR] Falha ao decodificar TXT: {e}")
        return ""

def extract_text_from_pdf(reader) -> List[str]:
    """Extrai texto de cada página de PDF usando PyPDF2"""
    conteudo = []
    for i, page in enumerate(reader.pages):
        texto = page.extract_text()
        if texto and texto.strip():
            conteudo.append(texto)
        else:
            print(f"[WARN] Página {i+1} sem texto legível.")
    return conteudo

def ocr_pdf(raw_bytes: bytes) -> str:
    """Extrai texto de PDF via OCR usando pytesseract"""
    try:
        from pdf2image import convert_from_bytes
        import pytesseract

        pages = convert_from_bytes(raw_bytes)
        ocr_text = ""
        for i, page_img in enumerate(pages):
            ocr_text += pytesseract.image_to_string(page_img)
        return ocr_text
    except Exception as e:
        print(f"[ERROR] OCR falhou: {e}")
        return ""

def parse_file(filename: str, raw_bytes: bytes) -> str:
    """
    Lê arquivos .txt ou .pdf e retorna o texto contido.
    Para PDFs, tenta extrair texto com PyPDF2; se falhar, usa OCR com pytesseract.
    """
    if filename.endswith(".txt"):
        return parse_txt(raw_bytes)

    elif filename.endswith(".pdf"):
        try:
            from PyPDF2 import PdfReader

            reader = PdfReader(io.BytesIO(raw_bytes))
            conteudo = extract_text_from_pdf(reader)
            final_text = " ".join(conteudo).strip()

            if not final_text:
                print("[INFO] Nenhum texto extraído via PyPDF2. Tentando OCR...")
                final_text = ocr_pdf(raw_bytes).strip()

            return final_text
        except Exception as e:
            print(f"[ERROR] Falha ao processar PDF: {e}")
            return ""

    else:
        print(f"[WARN] Formato não suportado: {filename}")
        return ""
