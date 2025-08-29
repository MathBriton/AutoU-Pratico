import re
import nltk

nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('portuguese'))

def preprocessar(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r'[^a-záéíóúãõç\s]', '', texto)
    tokens = [t for t in texto.split() if t not in stop_words]
    return " ".join(tokens)
