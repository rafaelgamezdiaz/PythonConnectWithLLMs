# Conectando Groq mediante el SDK de OpenAI

Este proyecto muestra cómo utilizar la API de Groq aprovechando la compatibilidad con el SDK de OpenAI, permitiendo una transición sencilla entre diferentes proveedores de LLM.

## 🚀 Configuración del Proyecto

### 1. Activar entorno virtual
Si ya tienes un entorno creado en la raíz:
- **Windows:**
  ```bash
  ..\.venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source ../.venv/bin/activate
  ```

### 2. Instalar dependencias
Para utilizar Groq con el SDK de OpenAI y manejar variables de entorno:
```bash
pip install openai python-dotenv
```

### 3. Configuración de Variables de Entorno
Crea un archivo llamado `.env` dentro de la carpeta `Groq/` y añade tu API Key de Groq:
```env
GROQ_API_KEY=tu_api_key_de_groq_aqui
```

## 💻 Ejecución
Para ejecutar el script de ejemplo:
```bash
python groq_openai.py
```

## 🛠️ Notas Técnicas
- El script utiliza la clase `OpenAI` pero apunta al `base_url` de Groq: `https://api.groq.com/openai/v1`.
- El modelo configurado por defecto es `llama3-70b-8192`.
- Permite mantener la misma estructura de código que usarías con los modelos de OpenAI (GPT-4, etc.) pero ejecutando en la infraestructura de Groq para mayor velocidad.
