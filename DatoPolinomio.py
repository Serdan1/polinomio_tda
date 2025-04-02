class DatoPolinomio:
    """Clase DatoPolinomio para almacenar el valor y el término del polinomio."""
    def __init__(self, valor=0, termino=0):
        self.valor = valor  # Coeficiente del término
        self.termino = termino  # Grado del término (xn, xn-1, ..., x0)