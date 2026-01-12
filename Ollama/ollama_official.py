import ollama

# Asegurarnos de que Ollama esté corriendo

def chat_with_ollama(prompt, model="llama3.2"):
    print(f"Conectado a Ollama (Modelo: {model})...")

    stream = ollama.chat(
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
        stream=True
    )

    for chunk in stream:
        print(chunk['message']['content'], end="", flush=True)

    print('\n')



if __name__ == "__main__":
    pregunta = "Explícame brevemente el concepto de 'Prompt Engineering'"
    chat_with_ollama(pregunta, model="deepseek-r1:1.5b")
    
