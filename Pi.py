"""
Es interesante ver cómo los algoritmos estocásticos (basados en elecciones
aleatorias) también sirven para resolver problemas que no tienen nada de
estocásticos. En este ejercicio vas a usar el generador random() 
para aproximar pi. 
"""



import random
import matplotlib.pyplot as plt


"""
Por definición pi es el área del círculo de radio uno. 
Si generamos puntos (x,y) con: 
"""
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

"""
Tendremos puntos dentro del cuadrado [0, 1]x[0, 1]. Algunos de estos puntos del
cuadrado caerán dentro del círculo unitario (los que cumplan que x^2 + y^2 < 1) y
otros puntos caerán afuera. La proporción de puntos que caigan dentro del cuarto
de círculo guardará relación con la proporción entre el área del cuarto de círculo y el
área del cuadrado. Obviamente hay una componente aleatoria, pero a medida que
la cantidad de puntos crece, la proporción de puntos se acercará a la proporción
entre las dos áreas.
"""

N = 100000
Xi = []
Yi = []
Xo = []
Yo = []
M = 0

for i in range(N):
    x, y = generar_punto()
    if x**2 + y**2 < 1:
        Xi.append(x)
        Yi.append(y)
        M += 1
    else:
        Xo.append(x)
        Yo.append(y)

"""
Si el área del círculo completo es pi, el área de nuestro cuarto de círculo es pi/4. Por
otro lado el área del cuadrado unitario es 1. Por lo tanto, si generamos N puntos con
una distribución uniforme en el cuadrado unitario, esperamos que pi/4 de estos N
puntos caigan dentro del cuarto del círculo y el resto afuera. Es decir que, si
llamamos M al número de puntos que caen dentro del círculo, esperamos que 
M~(pi/4 * N)
"""

print(f"pi: {4*M/N}")

plt.clf()
plt.scatter(Xi, Yi, s= 0.5, c="m", alpha = 0.1)
plt.scatter(Xo, Yo, s= 0.05, c ="c")


    