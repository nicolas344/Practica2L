from Car import Auto
from PersistentList import *
from functools import reduce

autos_disponibles = None
autos_alquilados = None
dias_transcurridos = 0


def registrar_auto():
    num_serie = input("Número de Serie: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio_fabricacion = input("Año de Fabricación: ")
    tarifa_diaria = float(input("Tarifa Diaria: "))

    nuevo_auto = Auto(num_serie, marca, modelo, anio_fabricacion, tarifa_diaria)
    global autos_disponibles

    autos_disponibles = agregar_al_principio(autos_disponibles, crear_nodo(nuevo_auto))

def ver_autos_disponibles():
    print("Autos Disponibles:")
    mostrar_autos(autos_disponibles)

def alquilar_auto():
    global autos_disponibles, autos_alquilados

    num_serie = input("Ingrese el número de serie del auto que desea alquilar: ")

    auto_nodo = buscar_auto_por_numero_serie(autos_disponibles, num_serie)

    if auto_nodo is not None:

        autos_disponibles = eliminar_auto_por_numero_serie(autos_disponibles, num_serie)

        autos_alquilados = agregar_al_final(autos_alquilados, auto_nodo)

        print("Auto alquilado con éxito.")

        global dias_transcurridos

        dias_transcurridos += 1

    else:

        print("Auto no encontrado en la lista de autos disponibles.")


def devolver_auto():
    global autos_disponibles, autos_alquilados

    num_serie = input("Ingrese el número de serie del auto que desea devolver: ")

    auto_nodo = buscar_auto_por_numero_serie(autos_alquilados, num_serie)

    if auto_nodo is not None:

        autos_alquilados = eliminar_auto_por_numero_serie(autos_alquilados, num_serie)

        autos_disponibles = agregar_al_final(autos_disponibles, auto_nodo)

        print("Auto devuelto con éxito.")

    else:

        print("Auto no encontrado en la lista de autos alquilados.")

def ver_autos_alquilados():

    print("Autos Alquilados:")

    mostrar_autos(autos_alquilados)

def calcular_ingreso_total():
    ingreso_total = reduce(lambda acum, auto: acum + auto.auto.tarifa_diaria * dias_transcurridos, iterar_lista(autos_alquilados), 0)
    print(f"Ingreso Total hasta el momento: ${ingreso_total:.2f}")

def intercambiar_autos():
    global autos_disponibles, autos_alquilados

    num_serie_alquilado = input("Ingrese el número de serie del auto alquilado: ")

    num_serie_disponible = input("Ingrese el número de serie del auto disponible para intercambiar: ")

    auto_alquilado = buscar_auto_por_numero_serie(autos_alquilados, num_serie_alquilado)

    auto_disponible = buscar_auto_por_numero_serie(autos_disponibles, num_serie_disponible)

    if auto_alquilado is not None and auto_disponible is not None:

        autos_disponibles = agregar_al_principio(autos_disponibles, auto_alquilado)

        autos_disponibles = eliminar_auto_por_numero_serie(autos_disponibles, num_serie_disponible)

        autos_alquilados = agregar_al_final(autos_alquilados, auto_disponible)

        autos_alquilados = eliminar_auto_por_numero_serie(autos_alquilados, num_serie_alquilado)

        print("Intercambio realizado con exito.")

    else:

        print("Uno o ambos autos no se encontraron en las listas correspondientes.")
