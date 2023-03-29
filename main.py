

def codigoUnico(db: list, modelo: str) -> bool:
    for juego in db:
        if juego["modelo"] == modelo:
            return False
    return True

def mostrar_juego(game):
        print(f'''
    ================ {game["titulo"]} ===================

    Modelo --> {game["modelo"]}  
    Nombre del juego --> {game["titulo"]}
    Precio de alquiler --> {game["precio"]}Bs
    Estatus del juego --> {game["status"]}
    Codigo Hash --> 

    =====================================================
        ''')

def agregar_juego(db: list):
    
    titulo = input("Ingrese el nombre del juego \n -->")

    while len(titulo) > 10:
        titulo = input("Ingrese el nombre del juego otra vez (SOLO MAXIMO 10 CARACTERES) \n -->")

    modelo = input("Ingrese el modelo (Formato = AAAAAA00) \n -->")

    while (
            not modelo[:6].isalpha() or
            not modelo[6:].isnumeric() or
            len(modelo) != 8 or
            not codigoUnico(db, modelo)
    ):
        modelo = input(
            "Ingrese el modelo otra vez (Formato = AAAAAA00) \n -->")

    precio = input("Ingrese el precio del juego (Monto ENTERO hasta 999bs) \n -->")
    
    while (
        not precio.isnumeric() or
        int(precio) <= 0 or
        int(precio) > 999
    ):
        precio = input("Ingrese el precio del juego otra vez (Monto ENTERO hasta 999bs) \n -->")

    db.append(
        {
            "titulo": titulo,
            "modelo": modelo,
            "precio": int(precio),
            "status": "EN STOCK"
        }
    )
    print("Juego agregado correctamente")

def searchByModel(db: list, model: str) -> dict:
    for game in db:
        if game["modelo"] == model:
            return game
    return {}


def searchByTitle(db: list, title: str) -> dict:
    for game in db:
        if game["titulo"] == title:
            return game
    return {}

def rentAGame(db: list):
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
            game = searchByModel(db, input("Ingrese el modelo del juego \n -->"))
            mostrar_juego(game)
        elif option == "2" :
            game = searchByTitle(db, input("Ingrese el titulo del juego \n -->"))
            mostrar_juego(game)
        elif option == "3":
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")

def eliminar_juego(db: list):
    print("Eliminar un juego")
    modelo = input("Ingrese el modelo del juego \n -->")
    for juego in db:
        if juego["modelo"] == modelo:
            db.remove(juego)
            print("Juego eliminado correctamente")
            return
    print("No se encontro el juego")

def main():
    
    db = [ ]
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
            agregar_juego(db)
        elif option == "2":
            pass
        elif option == "3":
            rentAGame(db)
        elif option == "4":
            pass
        elif option == "5":
            eliminar_juego(db)
        elif option == "6":
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")


main()
