from Rent import Rent


class Menu:

    def __init__(self):
        self.rent = Rent()

    def menu(self):

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
                self.rent.registrar_auto()

            elif opcion == "2":
                self.rent.ver_autos_disponibles()

            elif opcion == "3":
                self.rent.alquilar_auto()

            elif opcion == "4":
                self.rent.devolver_auto()

            elif opcion == "5":
                self.rent.ver_autos_alquilados()

            elif opcion == "6":
                self.rent.calcular_ingreso_total()

            elif opcion == "7":
                self.rent.intercambiar_autos()

            elif opcion == "8":
                break

            else:
                print("Opción no válida. Por favor, elija una opción válida.")
