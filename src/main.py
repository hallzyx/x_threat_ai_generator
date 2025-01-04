from utils import eliminar_imagenes
from twitter import verificar_credenciales, publicar_hilo
from openai_client import createHilo
from bing_image_search import get_images_from_hilos

if __name__ == "__main__":
    #Se verifica las credenciales de twitter / X
    verificar_credenciales()

    #Se le pide al usuario el tema del hilo
    tema=input("Tema del hilo: ")

    #Se crea el hilo
    hilo=createHilo(tema)    

    #Se imprime el hilo [Preview en consola]
    for tweet in hilo:
        print(f"- {tweet}")
    
    #Se indica la carpeta donde se guardaran las imagenes
    carpeta_img="img_hilo"

    #Se obtienen las imagenes del hilo
    get_images_from_hilos(hilo,carpeta_img)

    #Se publica el hilo
    publicar_hilo(hilo,carpeta_img)

    eliminar_imagenes(carpeta_img)


    