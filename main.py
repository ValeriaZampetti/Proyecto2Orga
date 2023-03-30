
def hash(modelo):
    suma = 0
    for i in modelo:
        suma += ord(i)
    div = suma % 3

    return div


def codigoUnico(db: list, modelo: str) -> bool:
    for juego in db:
        if juego["modelo"] == modelo:
            return False
    return True


def mostrar_juego(game):
    if game == {}:
        print("Ese juego no existe o ya esta alquilado")
        return
    print(f'''
    ================ {game["titulo"]} ===================

    Modelo --> {game["modelo"]}  
    Nombre del juego --> {game["titulo"]}
    Precio de alquiler --> {game["precio"]}Bs
    Estatus del juego --> {game["status"]}
    Codigo Hash --> {game["hash"]}

    =====================================================
        ''')


def titulo_unico(db, titulo):
    for juego in db:
        if juego["titulo"] == titulo:
            return False
    return True


def agregar_juego(db: list, buckets: list, overflows: list, index: dict):

    titulo = input("Ingrese el nombre del juego \n -->").upper()

    while len(titulo) > 10 or not titulo_unico(db, titulo):
        titulo = input(
            "Ingrese el nombre del juego otra vez (SOLO MAXIMO 10 CARACTERES) \n -->").upper()

    modelo = input("Ingrese el modelo (Formato = AAAAAA00) \n -->").upper()

    while (
            not modelo[:6].isalpha() or
            not modelo[6:].isnumeric() or
            len(modelo) != 8 or
            not codigoUnico(db, modelo)
    ):

        modelo = input(
            "Ingrese el modelo otra vez (Formato = AAAAAA00) \n -->").upper()

    precio = input(
        "Ingrese el precio del juego (Monto ENTERO hasta 999bs) \n -->")

    while (
        not precio.isnumeric() or
        int(precio) <= 0 or
        int(precio) > 999
    ):
        precio = input(
            "Ingrese el precio del juego otra vez (Monto ENTERO hasta 999bs) \n -->")

    hash_code = hash(modelo)
    game = {
        "titulo": titulo,
        "modelo": modelo,
        "precio": int(precio),
        "status": "EN STOCK",
        "hash": hash_code
    }

    db.append(
        game)

    index[titulo] = game

    bucket_actual = buckets[hash_code]
    if len(bucket_actual) < 3:
        bucket_actual.append(game)
    else:
        i = 0
        group_overflow = overflows[hash_code]

        while len(group_overflow[i]) >= 3:
            i += 1
            if i >= len(group_overflow):
                print("No hay espacio en el overflow")
                return
        overflow = group_overflow[i]
        overflow.append(game)

    print("Juego agregado correctamente")


def searchByModel(db: list, modelo: str, overflows: list, buckets: list) -> dict:
    hash_code = hash(modelo)
    bucket_actual = buckets[hash_code]

    for game in bucket_actual:
        if game["modelo"] == modelo:
            if game["status"] == "EN STOCK":
                return game
            else:
                print("Ese juego ya esta alquilado")
                return {}

    for overflow in overflows[hash_code]:
        for game in overflow:
            if game["modelo"] == modelo:
                if game["status"] == "EN STOCK":
                    return game
                else:
                    print("Ese juego ya esta alquilado")
                    return {}
    return {}


def searchByTitle(db: list, title: str, index: dict) -> dict:
    game = index.get(title)

    if game is None:
        return {}
    return game


def writeDataBase(db: list):
    with open("database.txt", "w") as file:
        for game in db:
            file.write(
                f"{game['titulo']},{game['modelo']},{game['precio']},{game['status']}")


def BuscarJuego(db: list, buckets: list, overflows: list, index: dict):
    while True:
        print(f"""
        ===========Buscar un juego============

        1. Buscar por Modelo.
        2. Buscar por Titulo.
        3. Regresar al menu principal.

        ======================================
        """)

        option = input("Ingrese la opción a realizar \n -->")

        game = {}
        if (option == "1"):
            game = searchByModel(
                db, input("Ingrese el modelo del juego \n -->").upper(), overflows, buckets)
            mostrar_juego(game)
        elif option == "2":
            game = searchByTitle(
                db, input("Ingrese el titulo del juego \n -->").upper(), index)
            mostrar_juego(game)
        elif option == "3":
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")


def rentAGame(db: list, buckets: list, overflows: list, index: dict):
    while True:
        print(f"""
        ===========Rentar un juego============

        1. Buscar por Modelo.
        2. Buscar por Titulo.
        3. Regresar al menu principal.

        =================================
        """)

        option = input("Ingrese la opción a realizar \n -->")

        game = {}
        if (option == "1"):
            game = searchByModel(
                db, input("Ingrese el modelo del juego \n -->").upper(), overflows, buckets)

            while game == {}:
                print("Ese juego no existe o ya esta alquilado")
                game = searchByModel(
                    db, input("Ingrese el modelo del juego otra vez \n -->").upper(), overflows, buckets)

            titulo = game["titulo"]

            q = input(
                f"Seguro que desea alquilar {titulo} por un precio de {game['precio']}Bs ?\n 1. SI\n 2. NO\n introduzca su seleccion:")
            if q == "1":
                game["status"] = "ALQUILADO"
                print(f"{titulo} ha sido alquilado con exito")

        elif option == "2":
            game = searchByTitle(
                db, input("Ingrese el titulo del juego \n -->").upper(), index)

            while game == {}:
                print("Ese juego no existe o ya esta alquilado")
                game = searchByTitle(
                    db, input("Ingrese el titulo del juego otra vez \n -->")).upper()

            titulo = game["titulo"]
            q = input(
                f"seguro que quiere alquilar {titulo} ?\n 1.Si\n 2.No\n Introduzca su seleccion: ")
            if q == "1":
                game["status"] = "ALQUILADO"
                print(f"{titulo} ha sido alquilado con exito")
        elif option == "3":
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")


def eliminar_juego(db: list, buckets: list, overflows: list, index: dict):
    modelo = input("Ingrese el modelo del juego \n -->").upper()
    for juego in db:
        if juego["modelo"] == modelo:
            db.remove(juego)
            print("Juego eliminado correctamente!")
            return
    print("No se encontro el juego!")


def devolver_juego(db: list, buckets: list, overflows: list, index: dict):
    modelo = input("Ingrese el modelo del juego \n -->").upper()
    for juego in db:
        if juego["modelo"] == modelo:
            if juego["status"] == "ALQUILADO":
                juego["status"] == "EN STOCK"
                print("juego devuelto exitosamente!")
                return
    print("Ese juego no se encuentra alquilado!")


def main():

    db = []
    buckets = [[], [], []]
    overflows = [[[], []], [[], []], [[], []]]
    index = {}

    while True:
        print(f"""
        ===========Rent-A-Game============

        1. Agregar un juego.
        2. Buscar un juego.
        3. Alquilar un juego.
        4. Devolver un juego.
        5. Eliminación de un juego.
        6. Cerrar sistema.

        =================================
        """)

        option = input("Ingrese la opción a realizar \n -->")
        if (option == "1"):
            agregar_juego(db, buckets, overflows, index)
        elif option == "2":
            BuscarJuego(db, buckets, overflows, index)
        elif option == "3":
            rentAGame(db, buckets, overflows,index)
        elif option == "4":
            devolver_juego(db, buckets, overflows, index)
        elif option == "5":
            eliminar_juego(db, buckets, overflows, index)
        elif option == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")


main()
