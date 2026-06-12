import json


def promedio_valoraciones(coleccion):

    libros = []
    peliculas = []
    musica = []

    for elemento in coleccion:

        tipo = elemento["tipo"].lower()

        if tipo == "libro":
            libros.append(elemento["valoracion"])

        elif tipo == "película" or tipo == "pelicula":
            peliculas.append(elemento["valoracion"])

        elif tipo == "música" or tipo == "musica":
            musica.append(elemento["valoracion"])

    promedio_libros = (
        sum(libros) / len(libros)
        if len(libros) > 0 else 0
    )

    promedio_peliculas = (
        sum(peliculas) / len(peliculas)
        if len(peliculas) > 0 else 0
    )

    promedio_musica = (
        sum(musica) / len(musica)
        if len(musica) > 0 else 0
    )

    reporte = {
        "Libros": promedio_libros,
        "Peliculas": promedio_peliculas,
        "Musica": promedio_musica
    }

    print("\n===== PROMEDIOS =====")
    print(f"Libros: {promedio_libros:.2f}")
    print(f"Películas: {promedio_peliculas:.2f}")
    print(f"Música: {promedio_musica:.2f}")

    with open(
        "promedio_valoraciones.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            reporte,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print(
        "\nArchivo promedio_valoraciones.json generado correctamente."
    )
