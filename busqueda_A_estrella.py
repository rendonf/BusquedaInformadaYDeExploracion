import numpy
import random

#        Se llena v[] con un camino inicial siguiendo la estrategia de el Primero
#        mejor o estrategia de linea recta, en donde muestra el camino más rapido
#        para llegar a nuestro destino pero el menos eficiente, demostrando que
#        este tipo de estrategia es incompleta y poco optima
def caminoInicial():
    global suma

    s1 = 0
    s2 = 0
    for i in range(n):
        v[i] = i
    v[n] = 0
    for j in range(n):
        s1 = v[j]
        s2 = v[j+1]
        suma += a[s1][s2]
    print("\n---------- Primer Camino -----------")
    imprimir()
    cambio()


def cambio():
    global u
    u = v
    nuevoCamino()
#      Se genera un nuevo camino apartir del inicial, intecambiando
#      solo dos nodos de los grafos de forma aletoria
def nuevoCamino():
    global u
    s1 = 0
    s2 = 0
    temp = 0
    s1 = int(random.randrange(1,n + 1))     # Posiciones a intercambiar
    s2 = int(random.randrange(1,n + 1))
    # validacion de posiciones distintas
    if s1 != s2:
#       Dado que el nodo inicial y final son el mismo se verifica las posiciones
#       para que siga manteniendo se asi, aun en la
#       aleatoriedad del cambio del nuevo camino
        if (u[s1] == u[0]) or (u[s1] == u[n]):
            temp = u[s1]
            u[0] = u[s2]
            u[n] = u[s2]
            u[s2] = temp
            valorCamino()
        elif (u[s2] == u[0]) or (u[s2] == u[n]):
            temp = u[s2]
            u[0] = u[s1]
            u[n] = u[s1]
            u[s1] = temp
            valorCamino()
        else:
            temp= u[s1]
            u[s1]= u[s2]
            u[s2]= temp
            valorCamino()
    else:
        nuevoCamino()


#         Se obtiene el peso del camino alternativo u[]
#        aux: peso del camino alternativo
def valorCamino():
    global per
    global p
    aux = 0
    s1 = 0
    s2 = 0
    j = 1
    while j < n:
       s1 = u[j]
       s2 = u[j+1]
       aux += a[s1][s2]
       j += 1
    per += 1
    p += 1
#    print(u)   # Caminos avaluados para obtener el mejor camino
    mejorCamino(aux)


#        Se compara el peso de v[] y u[], y el de menor valor se selecciona como
#        el mejor camino, asignandose en v[]. Se realiza el conteo de la persistencia
#        para indicar una condición de parada.
def mejorCamino(aux):
    global per
    global suma
    global v
#       A mayor número de persistencias menor número de grafos, dado que la estrategia
#       A* tiende a profundizar mucho en el camino que facilmente puede desbordar la
#       memoria
    if per < n:
        if aux < suma:
            j = 0
            while j <= n:
                v[j]= u[j]
                j += 1
            suma = aux
            per = 0  # Se reinicia la persistencia cada vez que se obtenga un nuevo camino
        nuevoCamino()
    else:
        print("\n---------- Mejor Camino -----------")
        imprimir()
        print("\n Número de evaluaciones: ", p)


def imprimir():
    print(v)
    print(" Peso: ", suma, "\n")


n =  int(input("Ingrese tamañao del grafo:\n  -- "))     #  n: número de grafos
a = a = numpy.zeros(shape = (n,n),dtype=int)             #  a[][]: matriz de adyacencia
for i in range(n):
    for j in range(n):
        if i != j:
            a[i][j] = random.randrange(1,10)
        else:          # Se matiene la diagonal de ceros
            a[i][j] = 0

print("\n---------- Matriz de adyacencia -----------")
print(a)

v = numpy.zeros(n + 1, dtype=int)    #  v[]: el mejor camino
u = numpy.zeros(n + 1, dtype=int)    #  u[]: alternativa del mejor camino (no siempre es el mejor)
suma = 0      #  suma: el peso del mejor camino
per = 0       #  per: persistencia de la busqueda del mejor camino (contador que se reinicia con cada nuevo camino)
p = 0         #  p: número de caminos evaluados (contador), es diferente a la persistencia

caminoInicial()
