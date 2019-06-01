import Matriz
import numpy as np
import numpy
import random

Matriz.inversa()
n = Matriz.n                        # Número de grafos
a = Matriz.a                        # Matriz de adyacencia
p = Matriz.p                        # Matriz de probabilidades
v = numpy.zeros(n + 1, dtype=int)   # El mejor camino
u = numpy.zeros(n + 1, dtype=int)   # Alternativa del mejor camino (no siempre es el mejor)
suma = 100
per = 0              # Persistencia de la busqueda del mejor camino (contador que se reinicia con cada nuevo camino)

z = int(input("Por favor ingrese el grafo inicial: \n1. A \n2. B \n3. C \n4. D  \n5. E  \n-- "))

#       Ya seleccionado el grafo inicial-final (z), se inicia la construcción del
#       nuevo camino. Esta construcción se guía por un random (s1) y dos
#       rangos(probabilidad b[][]),  los cuales toman la decisión del camino que
#       te tiene que seguir
def nuevoCamino():
    global u
    s1 = 0.0
    m1 = 0.0
    m2 = 0.0
    w = z - 1
    u[0] = w    # Nodo inicial
    for i in range(n):
        s1 = random.random()
        for j in range(n):
            m1 = p[w][j] + m2
            if (s1 > m2) and (s1 <= m1):   #  Rangos
                u[i + 1] = j               # Asignación de nodo
            m2 = p[w][j]
        w = u[i + 1]      # Nodo de camino
    u[n] = z - 1      # Nodo final
    valorCamino()


#       Se obtiene el peso del camino alternativo u[]
def valorCamino():
    global per

    aux = 0    # Peso del camino alternativo
    s1 = 0
    s2 = 0
    j = 1
    while j < n:
        s1 = u[j]
        s2 = u[j + 1]
        aux += a[s1][s2]
        j += 1
    per += 1
    mejorCamino(aux)


#       Se compara el peso de v[] y u[], y el de menor valor se selecciona como
#       el mejor camino, asignandose en v[]. Se realiza el conteo de la persistencia
#       para indicar una condición de parada.
#       suma: el peso del mejor camino
def mejorCamino(aux):
    global per
    global v
    global suma

#       La persistencia se maneja en tres tipos {2n, n^2, n}, para hallar la mejor
#       forma de encontrar el mejor camino
    if per < 2*n:
        if aux < suma:
            j = 0
            while j <= n:
                v[j] = u[j]
                j += 1
            suma = aux
            per = 0
        nuevoCamino()
    else:
        print("---------- Mejor Camino -----------")
        imprimir()


def imprimir():
    q =""
    for i in range(n + 1):
        if v[i] == 0:
            q += "A "
        elif v[i] == 1:
            q += "B "
        elif v[i] == 2:
            q += "C "
        elif v[i] == 3:
            q += "D "
        elif v[i] == 4:
            q += "E "
    print(q, "\n   Peso: ", suma, "\n")

nuevoCamino()
