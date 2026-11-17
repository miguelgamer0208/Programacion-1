import numpy as np;from os import system;system('cls')
invertido=False;Vacio=False
sim2="ø"
sim="*"
while 1:
    try:
        n=int(input("Que tan grande quieres tu figura?[Mayor a 3]\n>>"))
        if n<=3:print("Error:Porfavor elige un valor mayor a 3\n")
        else:break
    except ValueError:print("Error:Ingresa un numero entero, no decimal ni tampoco no numerico.")
while 1:
    try:
        i=int(input(f"Valor de i? [0,{n-1}]\n>>"))
        if i<0:print("Error:Porfavor elige un valor mayor a 3\n")
        else:break
    except ValueError:print("Error:Ingresa un numero entero, no decimal ni tampoco no numerico.")
while 1:
    try:
        j=int(input(f"Valor de j? [0,{n-1}]\n>>"))
        if j<0:print(f"Error:Porfavor elige un valor dentro del rango [0,{n-1}]\n")
        else:break
    except ValueError:print("Error:Ingresa un numero entero, no decimal ni tampoco no numerico.")

matriz=np.full((n,n)," ",np.dtype("U1"))
matriz2=np.full((n,n)," ",np.dtype("U1"))
matriz3=np.full((n,n)," ",np.dtype("U1"))
for fila in range(n):
    for columna in range(n):
        if fila-columna==i-j:
            matriz[fila,columna]="*"
for fila in range(n):
    for columna in range(n):
        if fila+columna==i+j:
            matriz2[fila,columna]="*"

matriz3[:,j]=sim
matriz3[i,:]=sim
for fila in range(n):
    for columna in range(n):
        if fila-columna==i-j or fila+columna ==i+j:
            matriz3[fila,columna]=sim
        if fila-columna==i-j and fila+columna ==i+j:
            matriz3[fila,columna]=sim2

for fila in matriz:
    print(" ".join(fila))

print(" ".join("-"*(n+7)))

for fila in matriz2:
    print(" ".join(fila))

print(" ".join("-"*(n+7)))

for fila in matriz3:
    print(" ".join(fila))

    

