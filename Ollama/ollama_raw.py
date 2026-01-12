import requests 
import json

OLLAMA_URL = "http://localhost:11434/api/chat"


def chat_local_raw():

    print("Conectado a Ollama via HTTP Raw")

    payload = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "user", 
                "content": "Explícame brevemente qué es una API REST"
            }
        ],
        "stream": True
    }

    try:
        # Importante: usar stream=True en la petición para procesar la respuesta por partes
        with requests.post(OLLAMA_URL, json=payload, stream=True) as response:
            response.raise_for_status()

            print("\n--- Respuesta de Ollama ---")

            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode('utf-8'))
                    # Ollama devuelve el contenido en ['message']['content'] cuando es /api/chat
                    if 'message' in data and 'content' in data['message']:
                        print(data['message']['content'], end='', flush=True)

            print('\n')
    except Exception as e:
        print(f"Error al conectar con Ollama: {e}")



if __name__ == "__main__":
    chat_local_raw()