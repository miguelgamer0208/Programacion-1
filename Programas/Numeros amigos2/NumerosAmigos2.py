import os
os.system("cls")

print("De Miguel Angel Encinas Bustillos")

print("Este programa calcula los números amigos hasta un límite máximo.\n")

L = []
lm = int(input("Límite máximo: "))

#OK aqui capaz se vea raro, pero crea una lista de lm numeros, y todos seran 0 para evitar crear de mas.
L = [0] * lm

# aca tambien se ve raro, pero en vez de checar por divisores, recorre todos los multiplos de cada numero hasta el limite establecido.
for i in range(1, lm // 2 + 1):
    for n in range(i * 2, lm, i):
        L[n] += i

#Aca no ocupo explicar, solo es la imprimir los pares.
for n in range(2, lm):
    amigo = L[n]

    if n < amigo < lm and L[amigo] == n:
        print(f"{n} es amigo de {amigo}")
