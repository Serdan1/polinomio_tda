class Nodo:
    """
    Representa un nodo en una lista enlazada.
    """
    def __init__(self, dato=None, siguiente=None):
        """
        Inicializa un nodo con un dato y un puntero al siguiente nodo.
        :param dato: El dato almacenado en el nodo.
        :param siguiente: Referencia al siguiente nodo en la lista.
        """
        self.dato = dato
        self.siguiente = siguiente

    def __repr__(self):
        """
        Representación en cadena del nodo.
        """
        return f"Nodo({self.dato})"