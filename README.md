# polinomio_tda

https://github.com/Serdan1/polinomio_tda.git


Documentación del Repositorio: Manipulación de Polinomios

Este repositorio contiene una implementación en Python para trabajar con polinomios, utilizando diferentes enfoques para su representación y operaciones. A continuación, se describe el propósito de cada fichero del proyecto.
Ficheros del Proyecto
1. Nodo.py
Este fichero define la clase Nodo, que representa un nodo básico en una lista enlazada. Cada nodo almacena un dato (en este caso, un término del polinomio) y un enlace al siguiente nodo. Es una pieza fundamental para la implementación de polinomios basada en listas enlazadas.
2. DatoPolinomio.py
Contiene la clase DatoPolinomio, que modela un término individual de un polinomio. Un término se define por su coeficiente (el valor numérico) y su exponente (el grado del término). Hay dos versiones: una más genérica con nombres como valor y termino, y otra más específica con coeficiente y exponente, que incluye una representación legible del término.
3. Polinomio.py (Versión con Lista Enlazada)
Este fichero implementa la clase Polinomio usando una lista enlazada. El polinomio se representa como una secuencia de nodos ordenados por exponente (de mayor a menor). Incluye métodos para:
Agregar un término en la posición correcta según su grado.

Modificar el coeficiente de un término existente.

Consultar el valor de un término específico (devolviendo 0 si no existe).

4. Polinomio.py (Versión con Lista Simple)
Otra implementación de la clase Polinomio, pero usando una lista simple de términos en lugar de una lista enlazada. Los términos no están necesariamente ordenados, y se proporcionan funciones para:
Agregar términos al final de la lista.

Evaluar el polinomio para un valor dado de x, calculando el resultado de la suma de los términos.

5. lanzador.py
Este fichero contiene funciones para realizar operaciones con polinomios y una interfaz básica para interactuar con el usuario. Incluye:
Funciones para sumar y multiplicar polinomios usando la clase Polinomio (versión con lista simple).

Funciones alternativas para sumar y restar polinomios representados como listas de coeficientes, ajustando los tamaños con ceros si es necesario.

Una función para pedir al usuario que ingrese un polinomio como una lista de coeficientes.

6. main.py
El punto de entrada del programa. Solicita al usuario que introduzca dos polinomios como listas de coeficientes, realiza las operaciones de suma y resta utilizando las funciones definidas en lanzador.py, y muestra los resultados en pantalla.



Resumen del Proyecto

Este repositorio implementa un sistema para manipular polinomios en Python mediante dos enfoques principales: una representación basada en listas enlazadas (ordenada y estructurada) y otra basada en listas simples (más sencilla y directa). El proyecto permite agregar términos a un polinomio, modificarlos, evaluarlos para un valor dado de x, y realizar operaciones como suma, resta y multiplicación. Además, incluye un programa interactivo que pide polinomios al usuario y muestra los resultados de las operaciones básicas. Es una herramienta útil para explorar conceptos de álgebra y estructuras de datos, con un diseño modular que facilita la extensión o comparación de diferentes implementaciones.




Diagrama de Dependencias del Repositorio

```mermaid
graph TD
    A[main.py] --> B[lanzador.py]
    B --> C[Polinomio.py - Lista Simple]
    C --> D[DatoPolinomio.py - Versión 2]
    B --> E[sumar_polinomios restar_polinomios pedir_polinomio multiplicar_polinomios]
    F[Polinomio.py - Lista Enlazada] --> G[Nodo.py]
    F --> H[DatoPolinomio.py - Versión 1]
    F --> I[agregar_termino modificar_termino obtener_valor]
    C --> J[agregar_termino obtener_valor]

Explicación del Diagrama


main.py:
Es el punto de entrada del programa.

Depende de lanzador.py para importar las funciones de operaciones y la interacción con el usuario.

Ejecuta un flujo interactivo que pide polinomios y muestra resultados.


lanzador.py:
Actúa como un módulo de utilidades.

Importa la versión de Polinomio.py basada en listas simples para realizar operaciones como suma y multiplicación.

Define funciones independientes para suma y resta usando listas de coeficientes.

Incluye pedir_polinomio para la entrada del usuario.


Polinomio.py (Lista Enlazada):
Representa polinomios como una lista enlazada ordenada.

Depende de Nodo.py para la estructura de nodos y de DatoPolinomio.py (Versión 1) para los términos.

No es usado directamente por main.py o lanzador.py en el flujo principal, pero está disponible como implementación alternativa.


Polinomio.py (Lista Simple):
Representa polinomios como una lista simple de términos.

Depende de DatoPolinomio.py (Versión 2) para los términos.

Es usado por lanzador.py para las operaciones de suma y multiplicación.


Nodo.py:
Define la clase Nodo, usada exclusivamente por la versión de lista enlazada de Polinomio.py.


DatoPolinomio.py:
    Tiene dos versiones:
Versión 1: Usada por la lista enlazada (Polinomio.py).

Versión 2: Usada por la lista simple (Polinomio.py), con una representación legible.

