import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    )

def chat_with_groq(model, prompt):

    print("Conectado a Groq...")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system", 
                "content": "Eres un asistente experto en Pytho y LLMs."
            },
            {
                "role": "user", 
                "content": prompt}
            ],
            temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    model = "llama-3.3-70b-versatile"
    respuesta = chat_with_groq(model, "Explicame que es la inferencia en un LLM")
    print("\n--- Respuesta de Groq ---\n")
    print(respuesta)