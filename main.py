
from lanzador import sumar_polinomios, restar_polinomios, pedir_polinomio

if __name__ == "__main__":
    print("Operaciones con polinomios")
    polinomio1 = pedir_polinomio()
    polinomio2 = pedir_polinomio()

    suma = sumar_polinomios(polinomio1, polinomio2)
    resta = restar_polinomios(polinomio1, polinomio2)

    print("Suma de polinomios:", suma)
    print("Resta de polinomios:", resta)