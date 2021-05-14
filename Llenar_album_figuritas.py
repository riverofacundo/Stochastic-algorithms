"""
Estima la probabilidad de completar un álbum de 670 figuritas
comprando 850 paquetes o menos. 
"""

import matplotlib.pyplot as plt
import random
import numpy as np

def album_incompleto(A):
    return 0 in A
    
def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album

def comprar_paquetes(figus_total, figus_paquete):
    a = np.array([random.randint(0,figus_total-1)])
    for i in range(4):
        a = np.concatenate((a, np.array([random.randint(0,figus_total-1)])))     
    return a

def cuantos_paquetes(figus_total, figus_paquete):
    cantidad = 0
    album = crear_album(figus_total)
    while cantidad != 850: 
        h = comprar_paquetes(figus_total, figus_paquete)
        for i in range(5):
            album[h[i-1]] += 1
        cantidad += 1
    return not album_incompleto(album)

figus_total = 670
figus_paquete = 5
n = 1000

x = sum([(cuantos_paquetes(figus_total, figus_paquete)) for i in range(n)])
print(x)

prob = x/n
print(f'Probe {100} veces, de las cuales {x} llene el album')
print(f'Probabilidad de llenar con 850 paquetes: {prob:.6f}.')
