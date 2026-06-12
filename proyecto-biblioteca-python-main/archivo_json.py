import json

ARCHIVO = "coleccion.json"


def cargar_datos():
    """
    Carga la información almacenada en el archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.
    """

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: el archivo JSON está dañado.")
        return []


def guardar_datos(coleccion):
    """
    Guarda la colección en el archivo JSON.
    """

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(
            coleccion,
            archivo,
            indent=4,
            ensure_ascii=False
        )
