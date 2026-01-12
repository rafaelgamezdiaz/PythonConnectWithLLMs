import os
import asyncio
from google import genai
from dotenv import load_dotenv

load_dotenv()

async def main():

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    model = "gemma-3-27b-it"
 
    print('Conectado a Gemini. Escribe "salir" para terminar.')
 
    while True:
        promt = input("\nPregunta: ")
        
        if promt.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break

        print("Generando respuesta...")

        try:
            response = await client.aio.models.generate_content(
                model = model, 
                contents = promt)

            print("\nRespuesta:")
            print(response.text)
        except Exception as e:
            print(f"Error al generar respuesta: {e}")

if __name__ == "__main__":
    asyncio.run(main())
