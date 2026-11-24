import random
import time
import os

os.system('cls')
r= True
c="y"
i=1
a=1
b=100
d= random.randint(a,b)
while c == ("y" or "") or len(c)==0:
    r= True
    while r == True:
        c=float(input(f"Tienes {8-i} intentos\nAdivina el Numero Magico[{a},{b}]: "))
        time.sleep(0.25)
        if c%1!=0:
            print(f"Error: Pon un numero entero, no: {c}\n")
            time.sleep(0.25)
        elif c>d:
            print("El numero magico es menor\n")
            i+=1
            if b>=c:
                b=int(c-1)
            time.sleep(0.25)
        elif c<d:
            print("El numero magico es mayor\n")
            i+=1
            if a<=c:
                a=int(c+1)
            time.sleep(0.25)
        if (c==d) or (i==8):
            break
    time.sleep(1)
    if c!=d:
        print(f"\nNo le atinaste, era: {d}")
    else:
        print(f"\nLe atinaste, era: {d}\n te tomo {i} intentos")
    c= input("¿Quieres jugar de nuevo?[y/n]" )
    c= c.lower
    if c != "y" or " ":
           break