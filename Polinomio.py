from typing import Optional
from dataclasses import dataclass
from Nodo import Nodo
from DatoPolinomio import DatoPolinomio
@dataclass

class Polinomio:
    """Clase Polinomio para representar un polinomio."""
    def __init__(self):
        self.grado = 0  # Grado del polinomio
        self.termino_mayor = None  # Puntero al término de mayor grado

    # Interfaz (Comportamiento)

def agregar_termino(polinomio, valor, termino):
    """Agrega un término al polinomio."""
    nuevo_nodo = Nodo(DatoPolinomio(valor, termino))
    if polinomio.termino_mayor is None or termino > polinomio.termino_mayor.dato.termino:
        nuevo_nodo.siguiente = polinomio.termino_mayor
        polinomio.termino_mayor = nuevo_nodo
    else:
        actual = polinomio.termino_mayor
        while actual.siguiente is not None and actual.siguiente.dato.termino > termino:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
    polinomio.grado = max(polinomio.grado, termino)

def modificar_termino(polinomio, valor, termino):
    """Modifica el valor de un término existente en el polinomio."""
    actual = polinomio.termino_mayor
    while actual is not None and actual.dato.termino != termino:
        actual = actual.siguiente
    if actual is not None:
        actual.dato.valor = valor
    else:
        raise ValueError("El término no existe en el polinomio.")

def obtener_valor(polinomio, termino):
    """Obtiene el valor de un término específico del polinomio."""
    actual = polinomio.termino_mayor
    while actual is not None and actual.dato.termino != termino:
        actual = actual.siguiente
    if actual is not None:
        return actual.dato.valor
    else:
        return 0  # Si el término no existe, se asume que su valor es 0