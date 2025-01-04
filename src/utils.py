import os


def manejar_error(e):
    """
    Maneja los errores de una manera más amigable para el usuario y centralizada.
    parametro > e < Exception-error: excepción que se quiere manejar.
    """
    print(f"Se ha producido un error: {e}")


def manejar_error_per_line(index,e):
 
    """
    Maneja los errores de una manera más amigable para el usuario y centralizada por linea.
    parametro > e < Exception-error: excepción que se quiere manejar.
    parametro > index < Elemento de la lista que se esta iterando.
    """
    print(f"Se ha producido un error en la iteración {index}: {e}")


def eliminar_imagenes(carpeta_imagenes):
    """
    Elimina las imagenes de una carpeta
    """

    try:
        for archivo in os.listdir(carpeta_imagenes):
            ruta_archivo=os.path.join(carpeta_imagenes,archivo)
            if os.path.isfile(ruta_archivo):   # Si es un archivo como por ejemplo .jpg, no borra la carpetas dentro de la carpeta
                os.remove(ruta_archivo)
        print(f"Las imagenes se han eliminado correctamente en {carpeta_imagenes}")
            
    except Exception as e:
        manejar_error(e)