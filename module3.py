from module2 import searchByModel


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
            game = searchByModel(
                db, input("Ingrese el modelo del juego \n -->"))

            print(game)
        elif option == "2":
            pass
        elif option == "3":
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")
