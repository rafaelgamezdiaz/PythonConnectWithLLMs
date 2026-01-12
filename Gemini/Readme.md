# Python IA Connect to Gemini

Este proyecto muestra cómo conectar una aplicación de Python con los modelos de inteligencia artificial de Google Gemini utilizando el SDK más reciente.

## 🚀 Configuración del Proyecto

### 1. Crear entorno virtual
```bash
python -m venv .venv
```

### 2. Activar entorno virtual
- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar dependencias
Para este proyecto necesitamos el nuevo SDK de Google y `python-dotenv` para manejar variables de entorno:
```bash
pip install google-genai python-dotenv
```

> [!NOTE]
> Aunque existe la librería `google-generativeai`, este proyecto utiliza `google-genai`, que es el SDK más moderno y simplificado de Google para Gemini y Vertex AI.

### 4. Configuración de Variables de Entorno
Crea un archivo llamado `.env` en la raíz del proyecto y añade tu API Key:
```env
GEMINI_API_KEY=tu_api_key_aqui
```

## 💻 Ejecución
Para ejecutar el script principal:
```bash
python gemini_oficial.py
```

## 🛠️ Notas Técnicas
- El script utiliza `asyncio` para llamadas asíncronas.
- El modelo configurado por defecto es `gemini-2.0-flash-exp` (o el que desees ajustar en el código).
- La API Key se lee de forma segura desde el entorno a través de `os.getenv()`.