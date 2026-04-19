# Voice AI Customer Support Assistant

Simulador de atendimento ao cliente por voz utilizando inteligência artificial.

O sistema permite que o usuário fale com o microfone, transcreve o áudio, gera uma resposta com IA e retorna em áudio.

# Funções:

-Gravação de áudio em tempo real
-Transcrição de fala usando Whisper
-Geração de resposta com modelo de linguagem
-Conversão de texto para áudio (gTTS)

# Tecnologias utilizadas
Python
OpenAI API
Whisper
gTTS
sounddevice
FFmpeg

# Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

Python 3.10+
Git
FFmpeg (adicionado ao PATH)

# Como executar

1. Clonar o repositório
git clone https://github.com/MateusPeracoli/voice-ai-customer-support.git
cd voice-ai-customer-support
2. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate
3. Instalar dependências
pip install -r requirements.txt
4. Configurar variável de ambiente

Crie um arquivo .env:

OPENAI_API_KEY=sua_chave_aqui
5. Executar
python main.py


Qual o Fluxo esperado?

Usuário grava áudio
Áudio é transcrito (Whisper)
Texto é enviado para IA
IA gera resposta
Resposta é convertida em áudio
