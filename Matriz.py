import numpy as np
import numpy

#       a[][]: matriz de adyacencia
#       b[]: matriz inversa
#       p[][]: matriz de adyacencia probabilidades (frecuencia relativa de la inversa)
#       n: número de nodos en cada grafo

a = np.array([(0, 10, 11, 6, 4),(10, 0, 5, 14, 8),(11, 5, 0, 16, 9),(6, 14, 16, 0, 8),(4, 8, 9, 8, 0)])
n = 5
p = numpy.zeros(shape = (n,n))
b = numpy.zeros(shape = (n,n))

#   La matriz de la inversa se obtiene gracias p=1/a, donde -p- se almacena en la inversa
def inversa():
    t = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                t = a[i][j]
                b[i][j] = 1/t
            else:          # Se matiene la diagonal de ceros
                b[i][j] = 0
    llenar()


#   Ya teniendo la matriz de la inversa, se puede obtener la matriz de las probabilidades
def llenar():
    suma = 0.0
    z = 0.0
    for i in range(n):
#             Cada cambio de fila (i) en la matriz de probabilidad, requiere la suma total de la
#             fila o grafos de la matriz de inversas, para asi lograr obtener los datos de la
#             matriz probabilidad
        for j in range(n):
            suma = suma + b[i][j]

        for j in range(n):
            if a[i][j] > 0:
#                    la probabildad se obtiene de z (inversa) y la división por la suma total
#                    de de la fila en cuestion  *
                z = b[i][j]
                p[i][j] = z/suma
            else:           # diagonal de ceros
                p[i][j] = 0


#   Cada vez que se evalua un nuevo, se realiza apartir de u[]
def suma(i):
    suma = 0.0
    for j in range(n):
        suma = suma + b[i][j]
    return suma


def imprimir():
        print("---------- Matriz de inversa -----------\n")
        print(b)

        print("\n---------- Matriz de adyacencía probabilidad-----------\n")
        print(p)

#inversa()
#imprimir()
