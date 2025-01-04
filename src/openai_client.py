import os
from openai import OpenAI
from dotenv import load_dotenv
from utils import manejar_error

load_dotenv()

client=OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

def createHilo(tema):
    """
    Esta wea crea hilos para twitter / X usando GPT para la generacion automatica de texto
    parametros:
    tema > el tema del hijo que prefieres hacer

    returna < Una lista de tweets que confirman todo el hilo generado
    
    """
    messages = [
    {"role": "system", "content": "Eres un asistente que genera contenido interesante y claro para Twitter."},
    {"role": "user", "content": f" Crea un hilo de Twitter sobre el tema {tema} con el siguiente formato: 1. Introducción breve y llamativa 2. Cuerpo con lista numerada: [Número]. [Item]: [Explicación breve] 3. Conclusión que fomente interacción."},
    ]
    try:
        response= client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        texto=response.choices[0].message.content
        lineas=texto.split("\n")
        lineas = [linea.strip() for linea in lineas if linea.strip()]
        # print(texto)
        return lineas;
    except Exception as e:
        manejar_error(e)
        return []