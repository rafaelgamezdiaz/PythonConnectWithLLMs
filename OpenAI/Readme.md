# Conectando con el SDK oficial de OpenAI

Este proyecto muestra cómo utilizar el SDK oficial de OpenAI para interactuar con sus modelos (como GPT-4o, GPT-4o-mini, etc.).

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
Para este módulo utilizamos la librería oficial de OpenAI:
```bash
pip install openai python-dotenv
```

### 3. Configuración de Variables de Entorno
Crea un archivo llamado `.env` dentro de la carpeta `OpenAI/` y añade tu clave de API:
```env
OPENAI_API_KEY=tu_api_key_de_openai_aqui
```

## 💻 Ejecución
Para ejecutar el script de ejemplo:
```bash
python openai_example.py
```

## 🛠️ Notas Técnicas
- A diferencia de Groq, aquí no especificamos un `base_url` ya que el SDK apunta por defecto a los servidores de OpenAI.
- El modelo configurado por defecto es `gpt-4o-mini` (económico y rápido).
- El código sigue la estructura oficial de la v1+ del SDK de OpenAI.
