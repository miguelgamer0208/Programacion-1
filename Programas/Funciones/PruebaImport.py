import math;import Funciones as fx;from os import system;import time; system("cls")
while 1:
    try:
        p= int(input("Elige un numero entero:\n>>"))
        if p<2:primo=False;break
        elif p<1: print("Error: El valor tiene que ser positivo\n")
        else:break
    except ValueError:print("Introduzca un numero entero/ No introduzca letras\n")
x=time.time()
if fx.perfecto(p): print(f"{p} es perfecto")
else: print(f"{p} no es perfecto")
if fx.nprimo(p): print(f"{p} es primo")
else: print(f"{p} no es primo")
fx.tiempoT(x)