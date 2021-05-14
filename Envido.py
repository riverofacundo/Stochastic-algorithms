
#%% Elecciones sin reposicion

"""
Teniendo en cuenta las reglas del Truco , estimá la probabilidad de 
obtener 31, 32 o 33 puntos de envido en una mano. 
¿Son iguales estas tres probabilidades? ¿Por qué?
Observación: como corresponde, en esta materia jugamos al truco sin flor.
"""

import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]


def tiene33(mano):
    palos = [palo for valor,palo in mano]    
    if len(palos) == len(set(palos)):
        return False
    else:
        repeticiones = 0
        for palo in palos:
            if palos.count(palo) > repeticiones:
                repetido = palo
                repeticiones = palos.count(palo)
        envido = sum([valor for valor, palo in mano if palo == repetido and valor not in [1,2,3,10,11,12] ])
        if envido in [11,12,13,16,17,18]:
            return True
        else:
            return False
    print(repetido)
    print(envido)

"""            
Claramente la probabilidad de sacar 31 es mayor pues tiene 2 combinaciones
posibles (4/7 y 5/6) mientras que las prob de sacar 32 es menor que la de
pacar 33 porque para ambos hay solo una combinacion pero para 32 ademas de
una sola combinacion esnecesario no tener la combinacion (7/6/5)
"""

# ya que solo tienen una posibilidad (5/7 y 7/6)
N = 1000000
G = sum([tiene33(random.sample(naipes,k=3)) for i in range(N)])
prob = G/N
print(f'Jugue {N} veces, de las cuales {G} hubo 33 de envido.')
print(f'Podemos estimar la probabilidad de sacar 33/32/31 en envido es: {prob:.6f}.')

