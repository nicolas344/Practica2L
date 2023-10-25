from Car import Auto
from PersistentList import *
from functools import reduce
import random

class Rent:
    def __init__(self):
        self.autos_disponibles = None
        self.autos_alquilados = None
        self.dias_transcurridos = 0

        marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan']
        modelos = ['Corolla', 'Civic', 'Focus', 'Cruze', 'Sentra']
        anios_fabricacion = ['2015', '2016', '2017', '2018', '2019']
        tarifas_diarias = [100, 200, 300, 400, 500]

        for i in range(10):
            num_serie = str(i)
            marca = random.choice(marcas)
            modelo = random.choice(modelos)
            anio_fabricacion = random.choice(anios_fabricacion)
            tarifa_diaria = random.choice(tarifas_diarias)
            auto_predeterminado = Auto(num_serie, marca, modelo, anio_fabricacion, tarifa_diaria)
            self.autos_disponibles = agregar_al_principio(self.autos_disponibles, crear_nodo(auto_predeterminado))
    def registrar_auto(self):
        num_serie = input("Número de Serie: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        anio_fabricacion = input("Año de Fabricación: ")
        tarifa_diaria = float(input("Tarifa Diaria: "))

        nuevo_auto = Auto(num_serie, marca, modelo, anio_fabricacion, tarifa_diaria)

        self.autos_disponibles = agregar_al_principio(self.autos_disponibles, crear_nodo(nuevo_auto))

    def ver_autos_disponibles(self):
        print("Autos Disponibles:")
        mostrar_autos(self.autos_disponibles)

    def alquilar_auto(self):
        num_serie = input("Ingrese el número de serie del auto que desea alquilar: ")

        auto_nodo = buscar_auto_por_numero_serie(self.autos_disponibles, num_serie)

        if auto_nodo is not None:
            self.autos_disponibles = eliminar_auto_por_numero_serie(self.autos_disponibles, num_serie)
            self.autos_alquilados = agregar_al_final(self.autos_alquilados, auto_nodo)
            print("Auto alquilado con éxito.")
            self.dias_transcurridos += 1
        else:
            print("Auto no encontrado en la lista de autos disponibles.")

    def devolver_auto(self):
        num_serie = input("Ingrese el número de serie del auto que desea devolver: ")

        auto_nodo = buscar_auto_por_numero_serie(self.autos_alquilados, num_serie)

        if auto_nodo is not None:
            self.autos_alquilados = eliminar_auto_por_numero_serie(self.autos_alquilados, num_serie)
            self.autos_disponibles = agregar_al_final(self.autos_disponibles, auto_nodo)
            print("Auto devuelto con éxito.")
        else:
            print("Auto no encontrado en la lista de autos alquilados.")

    def ver_autos_alquilados(self):
        print("Autos Alquilados:")
        mostrar_autos(self.autos_alquilados)

    def calcular_ingreso_total(self):
        ingreso_total = reduce(lambda acum, auto: acum + auto.auto.tarifa_diaria * self.dias_transcurridos, iterar_lista(self.autos_alquilados), 0)
        print(f"Ingreso Total hasta el momento: ${ingreso_total:.2f}")

    def intercambiar_autos(self):
        num_serie_alquilado = input("Ingrese el número de serie del auto alquilado: ")
        num_serie_disponible = input("Ingrese el número de serie del auto disponible para intercambiar: ")

        auto_alquilado = buscar_auto_por_numero_serie(self.autos_alquilados, num_serie_alquilado)
        auto_disponible = buscar_auto_por_numero_serie(self.autos_disponibles, num_serie_disponible)

        if auto_alquilado is not None and auto_disponible is not None:
            self.autos_disponibles = agregar_al_principio(self.autos_disponibles, auto_alquilado)
            self.autos_disponibles = eliminar_auto_por_numero_serie(self.autos_disponibles, num_serie_disponible)
            self.autos_alquilados = agregar_al_final(self.autos_alquilados, auto_disponible)
            self.autos_alquilados = eliminar_auto_por_numero_serie(self.autos_alquilados, num_serie_alquilado)
            print("Intercambio realizado con éxito.")
        else:
            print("Uno o ambos autos no se encontraron en las listas correspondientes.")
