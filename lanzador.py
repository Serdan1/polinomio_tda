from Polinomio import Polinomio

def sumar_polinomios(p1, p2):
    """Suma dos polinomios utilizando la clase Polinomio."""
    resultado = Polinomio()
    for termino in p1.terminos + p2.terminos:
        resultado.agregar_termino(termino.coeficiente, termino.grado)
    return resultado

def multiplicar_polinomios(p1, p2):
    """Multiplica dos polinomios utilizando la clase Polinomio."""
    resultado = Polinomio()
    for t1 in p1.terminos:
        for t2 in p2.terminos:
            coef = t1.coeficiente * t2.coeficiente
            grado = t1.grado + t2.grado
            resultado.agregar_termino(coef, grado)
    return resultado

def mostrar_polinomio(p):
    """Muestra un polinomio de forma legible utilizando la clase Polinomio."""
    return str(p)

def pedir_polinomio():
    polinomio = input("Introduce el polinomio (coeficientes separados por espacios, del mayor al menor grado): ")
    return list(map(float, polinomio.split()))

def sumar_polinomios(p1, p2):
    grado_max = max(len(p1), len(p2))
    p1 = [0] * (grado_max - len(p1)) + p1
    p2 = [0] * (grado_max - len(p2)) + p2
    return [a + b for a, b in zip(p1, p2)]

def restar_polinomios(p1, p2):
    grado_max = max(len(p1), len(p2))
    p1 = [0] * (grado_max - len(p1)) + p1
    p2 = [0] * (grado_max - len(p2)) + p2
    return [a - b for a, b in zip(p1, p2)]