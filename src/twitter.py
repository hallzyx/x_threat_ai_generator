import os
import tweepy
from dotenv import load_dotenv
from utils import manejar_error

load_dotenv()

api_key=os.getenv("X_API_KEY")
api_secret=os.getenv("X_API_KEY_SECRET")


twitter_auth=tweepy.OAuthHandler(
    os.getenv("X_API_KEY"),
    os.getenv("X_API_KEY_SECRET")
)

twitter_auth.set_access_token(
    os.getenv("X_ACCESS_TOKEN"),
    os.getenv("X_ACCESS_TOKEN_SECRET")
)

x_api=tweepy.API(twitter_auth)

def verificar_credenciales():
    """
    Verifica si las credenciales de twitter son correctas
    """

    try:
        user=x_api.verify_credentials()
        if user:
            print(f"Las credenciales de @{user.screen_name} son correctas.")
        else:
            print("Las credenciales de x no son correctas.")

    except Exception as e:
        manejar_error(e)

def publicar_hilo(hilo, carpeta_imagenes):
    """
    Publica un hilo en twitter con imagenes
    hilo > lista de tweets
    carpeta_imagenes > carpeta donde se encuentran las imagenes

    devuelve < confirmación si se publico el hilo
    """

    try:
        tweet_previo=None
        for i, tweet in enumerate(hilo):
            media_id=None
            ruta_imagen=f"{carpeta_imagenes}/{i+1}.jpg"   
            if os.path.exists(ruta_imagen):
                media=x_api.media_upload(ruta_imagen)
                media_id=media.media_id

            if tweet_previo is None:
                tweet_previo=x_api.update_status(tweet,media_ids=[media_id] if media_id else None) 
            else:
                tweet_previo=x_api.update_status(

                    tweet,
                    in_reply_to_status_id=tweet_previo.id,
                    auto_populate_reply_metadata=True,
                    media_ids=[media_id] if media_id else None
                )

            print("Tu hilo se ha publicado correctamente ctm.")

    except Exception as e:
        manejar_error(e)