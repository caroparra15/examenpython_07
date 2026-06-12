# Importa la función para generar el reporte de promedios
from reportes import promedio_valoraciones 


from coleccion import (
    agregar_elemento,
    listar_elementos,
    buscar_elemento,
    editar_elemento,
    eliminar_elemento,
    mostrar_recomendados
)
# Importa la función para cargar los datos desde el archivo JSON

from archivo_json import cargar_datos

from utilidades import (
    limpiar_pantalla,
    pausar
)

# Muestra el menú principal del sistema

def mostrar_menu():

    print("\n" + "=" * 40)
    print("ADMINISTRADOR DE COLECCIÓN")
    print("=" * 40)
    print("1. Agregar elemento")
    print("2. Listar elementos")
    print("3. Buscar elemento")
    print("4. Editar elemento")
    print("5. Eliminar elemento")
    print("6. Mostrar recomendados")
    print("7. Promedio valoraciones")
    print("0. Salir")
    print("=" * 40)

# Carga la colección almacenada en el archivo JSON

coleccion = cargar_datos()
# contrla la ejecucion del programa 

ejecutando = True
#ciclo principal del sistema
while ejecutando:

# Limpia la pantalla antes de mostrar el menú
    limpiar_pantalla()

    mostrar_menu()

    opcion = input(
        "Seleccione una opción: "
    )
# Agregar un nuevo elemento
    if opcion == "1":

        agregar_elemento(coleccion)
        pausar()
#mostrar elementos registrados en la coleccion 
    elif opcion == "2":

        listar_elementos(coleccion)
        pausar()

        # Buscar elementos
    elif opcion == "3":

        buscar_elemento(coleccion)
        pausar()

        # Editar un elemento existente
    elif opcion == "4":

        editar_elemento(coleccion)
        pausar()

# Eliminar un elemento
    elif opcion == "5":

        eliminar_elemento(coleccion)
        pausar()

    elif opcion == "6":
# Mostrar elementos recomendados

        mostrar_recomendados(coleccion)
        pausar()

# Generar reporte de promedios
    elif opcion == "7":

      promedio_valoraciones(coleccion)
      pausar()
 #Finalizar el programa
    elif opcion == "0":

     print("Gracias por usar el sistema.")
     ejecutando = False

 #Manejo de opciones inválidas
    else:

     print("Opción no válida.")
pausar()
