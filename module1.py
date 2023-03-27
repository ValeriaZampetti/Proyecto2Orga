from txtModule import writeDatabase


def codigoUnico(db: list, modelo: str) -> bool:
    for juego in db:
        if juego["modelo"] == modelo:
            return False
    return True


def agregarJuego(db: list):
    print("Agregar un juego")
    titulo = input("Ingrese el nombre del juego \n -->")

    while len(titulo) > 10:
        titulo = input("Ingrese el nombre del juego otra vez \n -->")

    modelo = input("Ingrese el modelo (Formato = AAAAAA00) \n -->")

    while (
            not modelo[:6].isalpha() or
            not modelo[6:].isnumeric() or
            len(modelo) != 8 or
            not codigoUnico(db, modelo)
    ):
        modelo = input(
            "Ingrese el modelo otra vez (Formato = AAAAAA00) \n -->")

    precio = input("Ingrese el precio del juego \n -->")
    # Verify that is precio is a number and the values is between 0 and 999
    while (
        not precio.isnumeric() or
        int(precio) <= 0 or
        int(precio) > 999
    ):
        precio = input("Ingrese el precio del juego otra vez \n -->")

    db.append(
        {
            "titulo": titulo,
            "modelo": modelo,
            "precio": int(precio),
            "status": "EN STOCK"
        }
    )
    print("Juego agregado correctamente")
    writeDatabase(db)
