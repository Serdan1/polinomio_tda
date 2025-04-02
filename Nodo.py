class Nodo:
    """Clase Nodo para representar un nodo en una lista enlazada."""
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente