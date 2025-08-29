def parse_file(filename: str, raw_bytes: bytes) -> str:
    if filename.endswith(".txt"):
        return raw_bytes.decode("utf-8")
    elif filename.endswith(".pdf"):
        try:
            from PyPDF2 import PdfReader
            import io
            reader = PdfReader(io.BytesIO(raw_bytes))
            return " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
        except Exception:
            return ""
    return ""
