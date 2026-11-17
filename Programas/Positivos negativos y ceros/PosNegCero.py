positivos=[]
negativos=[]
ceros=[]
lista=[]
for i in range(1,11):
    try:
        n=int(input(f"Escribe el numero {i}: "))
        lista+= [n] 
        if n<0:
            negativos+= [n]
        elif n==0:
            ceros+= [n]
        elif n>0:
            positivos+= [n]
    except ValueError:
        print("Por favor, escribe un numero entero.\n")
        continue

print(f"Hay {len(positivos)} positivos")
print(f"Hay {len(negativos)} negativos")
print(f"Hay {len(ceros)} ceros")
print("Numeros introducidos: ",lista)