import os
import requests
from utils import manejar_error_per_line

from dotenv import load_dotenv

load_dotenv()

BING_API_KEY = os.getenv("BING_API_KEY_1")
BING_SEARCH_ENDPOINT = os.getenv("URL_BING_API")+"/v7.0/images/search"


def get_images_from_hilos(hilo, carpeta="img"):
    """
    Esta funcion obtiene imagenes de bing para un hilo
    hilo > lista de tweets
    carpeta > carpeta donde se guardaran las imagenes

    returna < una lista de urls de imagenes
    """
    
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    for  i, tweet in enumerate(hilo):
        query = tweet.split(":")[0].strip()
        params = {"q": query, "count":1, "safeSearch":"Moderate"}
        headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}

        if tweet[0].isnumeric():
            try:
                response= requests.get(BING_SEARCH_ENDPOINT,headers=headers,params=params)
                response.raise_for_status()
                resultados=response.json().get("value",[])

                if resultados:
                    url_imagen=resultados[0]['contentUrl']
                    respuesta_imagen=requests.get(url_imagen)
                    respuesta_imagen.raise_for_status()

                    
                    # Guardar la imagen
                    ruta_imagen= f"{carpeta}/{i+1}.jpg"
                    with open(ruta_imagen,"wb") as f:
                        f.write(respuesta_imagen.content)
                        print(f"Imagen guardada en {ruta_imagen}")
                    
                else:
                    print(f"No se encontraron imagenes para {query}")

            except Exception as e:
                manejar_error_per_line(tweet,e)
        else:
            print(f"El tweet {tweet} no es una elemento del hilo correspondiente al cuerpo")

        