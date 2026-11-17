from math import sqrt; import os; os.system('cls')
from time import time; L=[]
def tiempoT(t):
    if time()-t <60:
        s="seg";tim =time()-t
    elif time()-t >=60 and (time()-t)/60< 60:
        s="min";tim = (time()-t)/60
    else:
        s="hr";tim = (time()-t)/(60**2)
    print(f"tiempo transcurrido = {tim:.3f}{s}")
def perfecto(x):
    suma=1
    for i in range(2,int(sqrt(x)+1)):
        if x%i==0:suma+=i; suma+= x//i
    if suma==x: return True
    else: return False
while 1:
    try:
        x= int(input("Ingrese un numero entero para definir hasta donde quieres saber los numeros perfectos:\n>>"))
        if x<1: print("Error: El Valor tiene que ser positivo\n")
        else: t=time(); break
    except: print("Error: Ingrese un numero entero, no decimal, y que no sea un caracter no numerico\n")
for e in range(2,x+1):
    p=perfecto(e)
    if p: L.append(e)
print(f"\n{L} son numeros perfectos");tiempoT(t)