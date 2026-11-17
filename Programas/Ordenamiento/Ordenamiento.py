import numpy as np; from os import system
system('cls')

def intercambio(x):
    y=np.array(x)
    for o in range(x.size-1):
        for i in range(x.size-1):
            if y[i]>y[i+1]:
                y[i],y[i+1]= y[i+1],y[i]
    return y
def es_palindromo(x):
    y=""
    x.split()
    for i in range(len(x)):
        if x[i]==" ":
            continue
        else:
            y+=x[i]
    return y

original= np.array([1,3,2,5,4,7,6,9,8,16,13,15,11,12,10,0,0.5,5.5,10.5,3.1416])
Nuevo= intercambio(original)

print(*(original))
print(*(Nuevo))

frase="Anita lava la tina"
frase2=es_palindromo(frase)
fraseinv=es_palindromo(frase)[::-1]
frase2,fraseinv= frase2.lower(),fraseinv.lower()

palindromo= (frase2==fraseinv)
print(frase)
print(frase2)
print(fraseinv)
print(palindromo)