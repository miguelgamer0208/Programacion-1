import numpy as np;from os import system
system('cls')

def algoritmo(x,y):
    c=0
    for i in range(x.size):
        visto=[]
        for n in range(y.size):
            if y[n]==x[i] and y[n] not in visto:
                c+=1
                visto.append(y[n])
    return c

lista_1=np.array([3,1,4,2])
lista_2=np.array([3,1,3,2])
lista_3=np.array([2,5,1,4])

print(lista_1)
print(lista_2)
print(lista_3)
print("Permutacion 1 y 2 =", algoritmo(lista_1,lista_2))
print("Permutacion 1 y 3 =", algoritmo(lista_1,lista_3))
print("Permutacion 2 y 3 =", algoritmo(lista_2,lista_3))


