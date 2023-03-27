from module1 import agregarJuego
from module3 import rentAGame
from txtModule import readDatabase


def main():
    db = readDatabase()
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
            agregarJuego(db)
        elif option == "2":
            pass
        elif option == "3":
            rentAGame(db)
        elif option == "4":
            pass
        elif option == "5":
            pass
        elif option == "6":
            break
        else:
            print("Ingreso incorrecto, vuelvalo a intentar.")


main()
