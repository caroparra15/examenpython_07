from tabulate import tabulate # type: ignore
from archivo_json import guardar_datos


def agregar_elemento(coleccion):
    """
    Permite agregar un nuevo elemento.
    """

    print("\n===== AGREGAR ELEMENTO =====")

    titulo = input("Título: ").strip()

    if titulo == "":
        print("El título no puede estar vacío.")
        return

    # Verificar duplicados
    for elemento in coleccion:

        if elemento["titulo"].lower() == titulo.lower():
            print("Ya existe un elemento con ese título.")
            return

    tipo = input(
        "Tipo (Libro/Película/Música): "
    ).strip()

    responsable = input(
        "Autor/Director/Artista: "
    ).strip()

    genero = input("Género: ").strip()

    try:

        valoracion = int(
            input("Valoración (1-5): ")
        )

        if valoracion < 1 or valoracion > 5:
            print(
                "La valoración debe estar entre 1 y 5."
            )
            return

    except ValueError:
        print("Debe ingresar un número.")
        return

    nuevo_elemento = {
        "titulo": titulo,
        "tipo": tipo,
        "responsable": responsable,
        "genero": genero,
        "valoracion": valoracion
    }

    coleccion.append(nuevo_elemento)

    guardar_datos(coleccion)

    print("Elemento agregado correctamente.")


def listar_elementos(coleccion):
    """
    Lista elementos utilizando filtros.
    """

    if len(coleccion) == 0:
        print("No hay elementos registrados.")
        return

    print("\n===== LISTAR ELEMENTOS =====")
    print("1. Mostrar todos")
    print("2. Mostrar libros")
    print("3. Mostrar películas")
    print("4. Mostrar música")
    print("5. Mostrar por género")

    opcion = input("Seleccione una opción: ")

    resultados = []

    if opcion == "1":

        resultados = coleccion

    elif opcion == "2":

        for elemento in coleccion:

            if elemento["tipo"].lower() == "libro":
                resultados.append(elemento)

    elif opcion == "3":

        for elemento in coleccion:

            if elemento["tipo"].lower() == "película":
                resultados.append(elemento)

    elif opcion == "4":

        for elemento in coleccion:

            if elemento["tipo"].lower() in [
                "música",
                "musica"
            ]:
                resultados.append(elemento)

    elif opcion == "5":

        genero = input(
            "Ingrese el género: "
        ).lower()

        for elemento in coleccion:

            if elemento["genero"].lower() == genero:
                resultados.append(elemento)

    else:
        print("Opción no válida.")
        return

    if len(resultados) == 0:
        print("No se encontraron resultados.")
        return

    tabla = []

    for elemento in resultados:
        tabla.append([
        elemento["titulo"],
        elemento["tipo"],
        elemento["responsable"],
        elemento["genero"],
        elemento["valoracion"]
        ])
        print(tabulate)
        print(type(tabulate))

    print(
        tabulate(
            tabla,
            headers=[
                "Título",
                "Tipo",
                "Responsable",
                "Género",
                "Valoración"
            ],
            tablefmt="grid"
        )
    )


def buscar_elemento(coleccion):
    """
    Busca elementos por título,
    responsable o género.
    """

    print("\n===== BUSCAR ELEMENTO =====")
    print("1. Buscar por título")
    print("2. Buscar por responsable")
    print("3. Buscar por género")

    opcion = input("Seleccione una opción: ")

    criterio = input(
        "Ingrese el dato a buscar: "
    ).strip().lower()

    resultados = []

    for elemento in coleccion:

        if opcion == "1":

            if criterio in elemento["titulo"].lower():
                resultados.append(elemento)

        elif opcion == "2":

            if criterio in elemento["responsable"].lower():
                resultados.append(elemento)

        elif opcion == "3":

            if criterio in elemento["genero"].lower():
                resultados.append(elemento)

    if len(resultados) == 0:
        print("No se encontraron resultados.")
        return

    tabla = []

    for elemento in resultados:

        tabla.append([
            elemento["titulo"],
            elemento["tipo"],
            elemento["responsable"],
            elemento["genero"],
            elemento["valoracion"],
        ])

    print(
        tabulate(
            tabla,
            headers=[
                "Título",
                "Tipo",
                "Responsable",
                "Género",
                "Valoración"
            ],
            tablefmt="grid"
        )
    )


def editar_elemento(coleccion):
    """
    Permite modificar un elemento.
    """

    titulo = input(
        "Ingrese el título a editar: "
    ).strip().lower()

    for elemento in coleccion:

        if elemento["titulo"].lower() == titulo:

            print(
                "Deje vacío un campo para mantenerlo."
            )

            nuevo_titulo = input(
                f"Título ({elemento['titulo']}): "
            ).strip()

            nuevo_responsable = input(
                f"Responsable ({elemento['responsable']}): "
            ).strip()

            nuevo_genero = input(
                f"Género ({elemento['genero']}): "
            ).strip()

            nueva_valoracion = input(
                f"Valoración ({elemento['valoracion']}): "
            ).strip()

            if nuevo_titulo:
                elemento["titulo"] = nuevo_titulo

            if nuevo_responsable:
                elemento["responsable"] = nuevo_responsable

            if nuevo_genero:
                elemento["genero"] = nuevo_genero

            if nueva_valoracion:

                try:

                    valoracion = int(
                        nueva_valoracion
                    )

                    if 1 <= valoracion <= 5:
                        elemento["valoracion"] = valoracion

                except ValueError:
                    print(
                        "Valoración inválida."
                    )

            guardar_datos(coleccion)

            print(
                "Elemento actualizado correctamente."
            )
            return

    print("Elemento no encontrado.")


def eliminar_elemento(coleccion):
    """
    Elimina un elemento por título.
    """

    titulo = input(
        "Ingrese el título a eliminar: "
    ).strip().lower()

    for i, elemento in enumerate(coleccion):

        if elemento["titulo"].lower() == titulo:

            confirmar = input(
                "¿Seguro que desea eliminarlo? (s/n): "
            ).lower()

            if confirmar == "s":

                coleccion.pop(i)

                guardar_datos(coleccion)

                print(
                    "Elemento eliminado correctamente."
                )

            return

    print("Elemento no encontrado.")


def mostrar_recomendados(coleccion):
    """
    Muestra los elementos con valoración 5.
    """

    recomendados = []

    for elemento in coleccion:

        if elemento["valoracion"] == 5:

            recomendados.append([
                elemento["titulo"],
                elemento["tipo"],
                elemento["responsable"],
                elemento["genero"],
                elemento["valoracion"],
            ])

    if len(recomendados) == 0:
        print(
            "No hay elementos recomendados."
        )
        return

    print(
        tabulate(
            recomendados,
            headers=[
                "Título",
                "Tipo",
                "Responsable",
                "Género",
                "Valoración"
            ],
            tablefmt="grid"
        )
    )
