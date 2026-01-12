# Conectando con Ollama (LLMs Locales)

Este proyecto muestra cómo utilizar **Ollama** para ejecutar y comunicarte con modelos de lenguaje de forma local (sin necesidad de internet ni API keys).

## 🚀 Configuración del Proyecto

### 1. Instalar Ollama
Primero, debes tener instalado Ollama en tu sistema. Puedes descargarlo desde [ollama.com](https://ollama.com/).

### 2. Descargar un Modelo
Para este ejemplo, estamos utilizando `deepseek-r1:1.5b`. Puedes descargarlo ejecutando el siguiente comando en tu terminal:
```bash
ollama run deepseek-r1:1.5b
```

### 3. Activar entorno virtual
Si ya tienes un entorno creado en la raíz:
- **Windows:**
  ```bash
  ..\.venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source ../.venv/bin/activate
  ```

### 4. Instalar la librería de Python
Necesitas instalar el paquete oficial de Ollama para Python:
```bash
pip install ollama
```

## 💻 Ejecución

### Opción A: Usando el SDK oficial (Recomendado)
Para ejecutar el script que utiliza la librería `ollama`:
```bash
python ollama_official.py
```

### Opción B: Usando peticiones HTTP Raw (Sin SDK)
Si prefieres usar la API REST directa con `requests` (ya instalada para los otros módulos):
```bash
python ollama_raw.py
```

## 🛠️ Notas Técnicas
- **ollama_official.py**: Utiliza el SDK oficial, ideal por su simplicidad.
- **ollama_raw.py**: Muestra cómo conectar directamente a la API REST de Ollama (Puerto 11434).
- Ambos scripts utilizan el modo **streaming** para respuestas en tiempo real.
- No requieren `.env` ni API keys, ya que el procesamiento es 100% local.