import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el cliente oficial de OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def chat_with_openai(prompt, model="openai/gpt-oss-20b"):
    """
    Función para interactuar con los modelos oficiales de OpenAI.
    """
    print(f"Conectado a OpenAI (Modelo: {model})...")

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": "Eres un asistente experto en Python y LLMs."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al conectar con OpenAI: {e}"

if __name__ == "__main__":
    pregunta = "Explícame brevemente el concepto de 'Prompt Engineering'"
    respuesta = chat_with_openai(pregunta)
    
    print("\n--- Respuesta de OpenAI ---")
    print(respuesta)
