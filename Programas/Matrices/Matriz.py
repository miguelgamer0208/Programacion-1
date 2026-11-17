import numpy as np;from os import system;system('cls')

matriz= np.array([
    [10,20,30],
    [40,50,60]
    ])

#print(matriz)

matriz2= np.zeros((3,4),dtype=int)

for fila in range(3):
    for columna in range(4):
        matriz2[fila,columna]= fila+columna

#print(matriz2)

A=np.array([
    [1,2],
    [3,4]
])
B=np.array([
    [5,6],
    [7,8]
])
C= A+B
D= A-B
k=3
print(C)
print(D)
print(A*k)
