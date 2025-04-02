class DatoPolinomio:
    """
    Representa un término del polinomio.
    """
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente  # Valor del coeficiente
        self.exponente = exponente      # Exponente del término

    def __repr__(self):
        return f"{self.coeficiente}x^{self.exponente}"


class Polinomio:
    """
    Representa un polinomio como una lista enlazada de términos.
    """
    def __init__(self):
        self.grado = 0                  # Grado del polinomio
        self.terminos = []              # Lista de términos (DatoPolinomio)

    def __repr__(self):
        return " + ".join([str(termino) for termino in self.terminos])


def agregar_termino(polinomio, coeficiente, exponente):
    """
    Agrega un término al polinomio.
    """
    nuevo_termino = DatoPolinomio(coeficiente, exponente)
    polinomio.terminos.append(nuevo_termino)
    polinomio.grado = max(polinomio.grado, exponente)


def obtener_valor(polinomio, x):
    """
    Evalúa el polinomio para un valor dado de x.
    """
    resultado = 0
    for termino in polinomio.terminos:
        resultado += termino.coeficiente * (x ** termino.exponente)
    return resultado