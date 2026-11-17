import numpy as np;from os import system;system('cls')
A=np.array([
    [1,1,1],
    [1,1,1]
])
B=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

filas_A,columnas_A= A.shape
filas_B,columnas_B= B.shape

if columnas_A!=filas_B:
    print("No se pueden multiplicar, dimensiones no compatibles")
else:
    producto= np.zeros((filas_A,columnas_B),dtype=int)

for i in range(filas_A):
    for j in range(columnas_B):
        for k in range(columnas_A):
            producto[i,j] +=A[i,k]*B[k,j]
print(producto)