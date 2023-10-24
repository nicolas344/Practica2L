from Rent import *
from PersistentList import *


def menu():
    while True:

        print("Menú:")

        print("1. Registrar un nuevo auto")

        print("2. Ver la lista de autos disponibles")

        print("3. Alquilar un auto")

        print("4. Devolver un auto")

        print("5. Ver la lista de autos alquilados")

        print("6. Calcular el ingreso total")

        print("7. Intercambiar autos")

        print("8. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_auto()

        elif opcion == "2":
            mostrar_autos(autos_disponibles)

        elif opcion == "3":
            alquilar_auto()

        elif opcion == "4":
            devolver_auto()

        elif opcion == "5":
            mostrar_autos(autos_alquilados)

        elif opcion == "6":
            calcular_ingreso_total()

        elif opcion == "7":
            intercambiar_autos()

        elif opcion == "8":
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")
