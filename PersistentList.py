from Nodo import Nodo


def crear_nodo(auto, siguiente=None):
    return Nodo(auto, siguiente)


def agregar_al_principio(lista, nodo):
    return crear_nodo(nodo.auto, lista)


def mostrar_autos(lista):
    if lista is None:
        return

    print("Número de Serie:", lista.auto.num_serie)
    print("Marca:", lista.auto.marca)
    print("Modelo:", lista.auto.modelo)
    print("Año de Fabricación:", lista.auto.anio_fabricacion)
    print("Tarifa Diaria:", lista.auto.tarifa_diaria)
    print()
    mostrar_autos(lista.siguiente)


def buscar_auto_por_numero_serie(lista, num_serie):
    if lista is None:
        return None
    if lista.auto.num_serie == num_serie:
        return lista
    return buscar_auto_por_numero_serie(lista.siguiente, num_serie)


def eliminar_auto_por_numero_serie(lista, num_serie):
    if lista is None:
        return None
    if lista.auto.num_serie == num_serie:
        return lista.siguiente
    lista.siguiente = eliminar_auto_por_numero_serie(lista.siguiente, num_serie)
    return lista


def agregar_al_final(lista, nodo):
    if lista is None:
        return nodo
    else:
        if lista.siguiente is None:
            lista.siguiente = nodo
        else:
            agregar_al_final(lista.siguiente, nodo)
        return lista


def iterar_lista(nodo):
    while nodo is not None:
        yield nodo

        nodo = nodo.siguiente
