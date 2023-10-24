from Car import Auto

class Nodo:
    def __init__(self, auto, siguiente=None):
        self.auto = auto
        self.siguiente = siguiente
