# Projeto Gysin IA

## Descrição
Gysin IA é uma assistente virtual humanizada integrada ao ChatGPT, com capacidade de memória para aprender sobre o usuário e se comunicar de forma natural.

## Novas Funcionalidades
- Sistema de aprendizagem por consulta
- Mapa mental para armazenamento de conhecimento
- Interface gráfica aprimorada com design futurista
- Processamento de linguagem natural avançado
- Sistema de logging para monitoramento

## Requisitos
- Python 3.8+
- Bibliotecas listadas em `requirements.txt`

## Instalação
1. Clone o repositório:git clone github.com2. Instale as dependências:
pip install -r requirements.txt3. Configure as variáveis de ambiente no arquivo `.env`

## Uso
Execute o arquivo principal:
python src/main.py
## Contribuição
Contribuições são bem-vindas! Por favor, leia o guia de contribuição antes de submeter pull requests.

## Licença
Este projeto está licenciado sob a MIT License.

Arquivos para .gitignore:
# Adicionar ao .gitignore
data/knowledge_base.db
.env
__pycache__/
*.pyc

Novas bibliotecas para requirements.txt:
spacy==3.5.0
transformers==4.28.1
torch==1.13.1
kivy==2.1.0
pyttsx3==2.90
SpeechRecognition==3.9.0
loguru==0.6.0
sqlite3==3.36.0


