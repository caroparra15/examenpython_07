import os


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pausar():
    """
    Pausa el programa hasta que el usuario presione Enter.
    """

    input("\nPresione Enter para continuar...")


