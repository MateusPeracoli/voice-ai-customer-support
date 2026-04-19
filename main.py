import whisper
from gtts import gTTS
import os
from config import OPENAI_API_KEY
from openai import OpenAI
import sounddevice as sd
from scipy.io.wavfile import write

# Inicializa cliente OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Configurações
LANGUAGE = "pt"
INPUT_AUDIO = "audio_input/input.wav"
OUTPUT_AUDIO = "audio_output/response.mp3"

# -------------------------
# 1. Gravar áudio
# -------------------------

def gravar_audio(duracao=5, arquivo="audio_input/input.wav"):
    print("🎤 Gravando... fale agora")

    fs = 44100  # taxa de amostragem
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()

    write(arquivo, fs, audio)

    print("✅ Gravação finalizada!")

gravar_audio()

# -------------------------
# 2. Transcrição de áudio
# -------------------------
def transcrever_audio(caminho_audio):
    print("🔄 Carregando modelo Whisper...")
    model = whisper.load_model("small")

    print("🎤 Transcrevendo áudio...")
    result = model.transcribe(caminho_audio, fp16=False, language=LANGUAGE)

    return result["text"]


# -------------------------
# 2. Gerar resposta com IA
# -------------------------
def gerar_resposta(texto):
    print("🧠 Gerando resposta com IA...")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # mais atual e barato
        messages=[
            {
                "role": "system",
                "content": "Você é um atendente de suporte de um banco digital. Responda de forma clara e objetiva."
            },
            {
                "role": "user",
                "content": texto
            }
        ]
    )

    return response.choices[0].message.content


# -------------------------
# 3. Converter texto em áudio
# -------------------------
def gerar_audio(texto, caminho_saida):
    print("🔊 Convertendo resposta em áudio...")

    tts = gTTS(text=texto, lang=LANGUAGE)
    tts.save(caminho_saida)

    print(f"✅ Áudio salvo em: {caminho_saida}")


# -------------------------
# FLUXO PRINCIPAL
# -------------------------
def main():
    if not os.path.exists(INPUT_AUDIO):
        print("❌ Arquivo de áudio não encontrado.")
        return

    transcricao = transcrever_audio(INPUT_AUDIO)
    print("\n🗣️ Usuário:", transcricao)

    resposta = gerar_resposta(transcricao)
    print("\n🤖 Assistente:", resposta)

    gerar_audio(resposta, OUTPUT_AUDIO)


if __name__ == "__main__":
    main()
