import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Certifique-se de baixar as stopwords
nltk.download('stopwords')

# Carregar stopwords e stemmer
STOP_WORDS = set(stopwords.words('portuguese'))
STEMMER = SnowballStemmer('portuguese')

def preprocessar(texto: str) -> str:
    """
    Pré-processa o texto do email para NLP:
    - converte para minúsculas
    - remove caracteres especiais
    - tokeniza
    - remove stopwords
    - aplica stemming
    Retorna o texto processado pronto para classificação.
    """
    # 1. Converter para minúsculas
    texto = texto.lower()
    
    # 2. Remover caracteres especiais (mantendo letras e números)
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
    
    # 3. Tokenizar por espaço
    tokens = texto.split()
    
    # 4. Remover stopwords
    tokens = [t for t in tokens if t not in STOP_WORDS]
    
    # 5. Aplicar stemming
    tokens = [STEMMER.stem(t) for t in tokens]
    
    # 6. Reconstruir texto
    texto_processado = ' '.join(tokens)
    
    return texto_processado
