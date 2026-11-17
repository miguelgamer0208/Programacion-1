from os import system
system('cls')

def interseccion(x,y):
    intersec=[]
    for a in x and y:
        if a in x and y:
            intersec.append(a)
    intersec.sort()
    return intersec

def interseccion2(x,y):
    intersec=[]
    for a in range(len(x)):
        for b in range(len(y)):
            if y[b]==x[a]:
                intersec.append(y[b])
    intersec.sort()
    return intersec

def interseccion3(x,y):
    k=[]; visto=[]; intersec=[]
    k= x+y
    for i in range(len(k)):
        if k[i] not in visto:
            visto.append(k[i])
        elif k[i] in visto and k[i] not in intersec:
            intersec.append(k[i])
    intersec.sort()
    return intersec

lista=[3,8,17,12,24]
lista2=[5,9,12,19,21]

print(lista)
print(lista2,end="\n\n")
print("Algoritmos de Intersecciones:")
print("Algoritmo 1: ",interseccion(lista,lista2))
print("Algoritmo 2: ",interseccion2(lista,lista2))
print("Algoritmo 3: ",interseccion3(lista,lista2))
print("Los algoritmos son iguales?", interseccion(lista,lista2)==interseccion2(lista,lista2)==interseccion3(lista,lista2))
