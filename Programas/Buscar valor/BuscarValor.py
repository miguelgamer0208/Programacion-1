import numpy as np; from os import system
system('cls')

arreglo = np.array([10, 25, 30, 25, 50, 15, 25])
valor = 25

indices= np.where(arreglo==valor)[0]
indices= np.sort(indices)[::-1]
if indices.size==0: print("No se encontro el valor")
else: print(f"Encontrado en los indices {indices}")
