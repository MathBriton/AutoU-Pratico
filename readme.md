# Configuração da API Key
Antes de rodar, defina a variável de ambiente OPENAI_API_KEY com sua chave OpenAI. Porém, irei deixar também um arquivo mockado para testes sem necessidade de criação da API_KEY.

Exemplo:

Windows:
  setx OPENAI_API_KEY "SUA_CHAVE_AQUI"
Linux / MacOS:
  export OPENAI_API_KEY="SUA_CHAVE_AQUI"

Em seguida, rode:
  uvicorn main:app --reload
