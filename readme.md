# Proyecto: Generador de Hilos para Twitter

Este proyecto automatiza la generación, descarga de imágenes relacionadas y publicación de hilos en Twitter/X utilizando la API de OpenAI, la API de Bing Image Search y la API de Twitter. Es ideal para crear contenido atractivo, completo y automatizado en formato de hilos.

---

## Características

- **Generación de contenido:** Usa OpenAI para generar un hilo basado en un tema proporcionado.
- **Descarga de imágenes:** Busca y descarga imágenes relacionadas con cada tweet del hilo utilizando Bing Image Search API.
- **Publicación en Twitter:** Publica el hilo completo en Twitter con las imágenes correspondientes.
- **Limpieza automática:** Elimina las imágenes descargadas una vez que el hilo ha sido publicado.

---

## Requisitos

1. **Python 3.8 o superior**.
2. Dependencias de Python:
   - `tweepy`
   - `requests`
   - `python-dotenv`
3. Claves de API:
   - **OpenAI API Key:** Para la generación de texto.
   - **Bing API Key:** Para la búsqueda de imágenes.
   - **Twitter API Keys:** Para la publicación del hilo.

---

## Instalación

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/hallzyx/x_threat_ai_generator.git
cd x_threat_ai_generator
```

### Paso 2: Crear y activar un entorno virtual
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requeriments.txt
```

### Paso 4: Configurar las variables de entorno
Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes claves:
```plaintext
# Claves de OpenAI
OPENAI_KEY=

# Claves de Bing
BING_API_KEY_1=
URL_BING_API=https://api.bing.microsoft.com

# Claves de Twitter
X_API_KEY=
X_API_KEY_SECRET=
X_ACCESS_TOKEN=
X_ACCESS_TOKEN_SECRET=
```

---

## Estructura del Proyecto

```plaintext
├── LICENSE               # Licencia del proyecto
├── requeriments.txt      # Dependencias del proyecto
├── readme.md             # Documentación principal
├── img_hilo/             # Carpeta para almacenar imágenes temporales
├── src/                  # Código fuente del proyecto
│   ├── bing_image_search.py   # Maneja la búsqueda y descarga de imágenes
│   ├── main.py                # Punto de entrada principal
│   ├── openai_client.py       # Genera el hilo usando OpenAI
│   ├── twitter.py             # Publica hilos en Twitter
│   ├── utils.py               # Funciones auxiliares (ej: eliminar imágenes)
│   └── __init__.py            # Define la carpeta como paquete de Python
└── .env                  # Configuración con claves de API (ignorado por Git)
```

---

## Uso

1. **Ejecutar el programa**:
   ```bash
   python src/main.py
   ```

2. **Flujo del programa**:
   - Ingresa un tema para el hilo.
   - OpenAI generará un hilo estructurado basado en el tema.
   - Bing buscará y descargará imágenes relacionadas para cada tweet.
   - Publicará el hilo en Twitter con las imágenes correspondientes.
   - Finalmente, se eliminarán las imágenes temporales.

3. **Ejemplo de Ejecución**:
```plaintext
Tema del hilo: "Avances en Inteligencia Artificial en 2023"
Hilo generado:
- Introducción: "2023 marcó un antes y un después en la Inteligencia Artificial. ¡Descubre cómo! 🦝🔌"
- 1. GPT-4: OpenAI lanzó este modelo, transformando la forma en que interactuamos con IA.
    [imagen 1]
- 2. Medicina: IA ayudó a identificar nuevas terapias para enfermedades raras.
    [imagen 2]
- 3. Energía limpia: Modelos predictivos mejoraron la eficiencia solar.
    [imagen 3]
...
- Conclusión: "¿Y tu que opinas? Dejame tu respuesta en los comentarios..."

Publicando...
¡Hilo publicado exitosamente!
```

---

## Funciones Clave

### 1. **Generar Hilos**
Archivo: `openai_client.py`
```python
def createHilo(tema):
    # Genera un hilo en formato estructurado basado en un tema.
```

### 2. **Buscar y Descargar Imágenes**
Archivo: `bing_image_search.py`
```python
def get_images_from_hilos(hilo, carpeta):
    # Descarga imágenes relacionadas con cada tweet.
```

### 3. **Publicar Hilos en Twitter**
Archivo: `twitter.py`
```python
def publicar_hilo(hilo, carpeta_imagenes):
    # Publica cada tweet con su imagen correspondiente.
```

### 4. **Eliminar Imágenes**
Archivo: `utils.py`
```python
def eliminar_imagenes(carpeta):
    # Elimina todas las imágenes descargadas.
```

---

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por usar este generador de hilos! ¡Comparte tus mejoras y resultados! 🚀

