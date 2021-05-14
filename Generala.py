#%% 4.7 Generala no necesariamente servida

"""
Estima la probabilidad de obtener una generala en las tres 
tiradas de una mano 
"""

import random

caras = [1, 2, 3, 4, 5, 6]

def es_generala(tirada):
    return max(tirada) == min(tirada)

def filtrorepe(lista):
    repeticiones = 0
    repes = set([x for x in lista if lista.count(x) > 1])
    for numero in repes:
        if lista.count(numero) > repeticiones:
            repeticiones = lista.count(numero)
            repetido = [numero]
    if not repes:
        repeticiones = 1
        repetido = [1]
    tirada = repetido*repeticiones
    return tirada

def jugar2():
    i = 0
    for i in range(3):
        
        if i == 0:
            tirada = random.choices(caras, k=5)
            #print(f"1ra tirada: {tirada}")
        elif not es_generala(tirada):
            tirada = filtrorepe(tirada).copy()
            for i in range(5-len(tirada)):
                tirada.append(random.randint(1,6))
            #print(f"2 o 3ra tirada: {tirada}")
    return tirada

N = 100000
G = sum([es_generala(jugar2()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante: {prob:.6f}.')



