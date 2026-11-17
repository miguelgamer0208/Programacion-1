from math import sqrt;import time as tm;import threading;import os;os.system('cls')

print("Programa de numeros primos; \nSe encarga de encontrar numeros primos ó decirte si es primo o no.\nAh y tambien, Programa de Miguel Angel Encinas Bustillos\n")
cancelar = threading.Event();activo=False
def esperar_enter():
    input("Presiona ENTER para cancelar...\n")
    cancelar.set()
def tiempoT(x):
    if tm.time()-x <60:s="seg";tim = tm.time()-x
    elif tm.time()-x >=60 and (tm.time()-x)/60< 60:s="min";tim = (tm.time()-x)/60
    else:s="hr";tim = (tm.time()-x)/(60**2)
    print(f"tiempo transcurrido = {tim:.3f}{s}")
L=[]
while 1:
    try:
        p= int(input("Elige un numero entero: "))
        if p<2:
            print("Si es menor a 2, ten pon seguro que no sera primo\n")
        else:
            activo=True
            break
    except ValueError:
        print("Introduzca un numero entero/ No introduzca letras\n")
while 1:
    try:
        opt= int(input(f"Quieres saber...\n1)Todos los primos hasta {p}\n2)Saber si es primo {p}\n3)Saber los primos entre {p} hasta otro valor\n4)Saber los primos entre un numero hasta {p}\n>>"))    
        if opt >=1 and opt<=4:
            break
        else:
            print("Error: Porfavor elige una opcion de las anteriores, solo escribe su numero.\n")
    except ValueError:
        print("Error: ingrese un numero entero, y que sea una opcion, no letra o decimal/fraccion\n")
match opt:
    case 1:
        time=tm.time()
        s=""
        L+=[2]
        if activo:
            hilo = threading.Thread(target=esperar_enter, daemon=True)
            hilo.start()
        for n in range (3,p+1,2):
            primo=True
            for i in range(3,int(sqrt(n)+1),2):
                if n%i==0:
                    primo=False
                    break
            if cancelar.is_set():
                p=L[-1]
                break   
            if primo:
                L.append(n)
        print(L)
        print(f"Son un total de {len(L)} numeros primos hasta {p}")
        tiempoT(time)
    case 2:
        time=tm.time()
        primo=True
        if p != 2 and (p % 2 == 0 or (p % 5 == 0 and p != 5)):    
            primo = False
        elif p!=2:    
            for i in range(3,int(sqrt(p)+1),2):
                if p%i==0:
                    primo=False
                    break
        if primo:
            print(f"{p} si es un numero primo")
        else:
            print(f"{p} no es un numero primo")
        tiempoT(time)
    case 3:
        while 1:
            try:
                q= int(input("Elige un numero entero para el limite superior: "))
                if q<0 or q<p:
                    print(f"Error: El limite superior debe ser mayor o igual a {p} \n")
                else:
                    if p<=3:
                        L+=[2]
                    activo=True
                    time=tm.time()
                    s=""    
                    break
            except ValueError:
                print("Introduzca un numero entero/ No introduzca letras\n")
        p2=max(p,3)
        if p2%2==0:
            p2+=1
        if activo:
            hilo = threading.Thread(target=esperar_enter, daemon=True)
            hilo.start()
        for n in range (p2,q+1,2):
            primo=True
            for i in range(3,int(sqrt(n)+1),2):
                if n%i==0:
                    primo=False
                    break
            if cancelar.is_set():
                q=L[-1]
                break   
            if primo:
                L.append(n)
        L.sort()
        print(L)
        print(f"Son un total de {len(L)} numeros primos de {p} hasta {q}")
        tiempoT(time)
    case 4:
        while 1:
            try:
                q= int(input("Elige un numero entero para el limite inferior: "))
                if q<0:
                    print("Error: En los numeros negativos no hay primos... elige un numero positivo\n")
                else:
                    if q<3:
                        L+=[2]
                    activo=True
                    time=tm.time()
                    s=""    
                    break
            except ValueError:
                print("Introduzca un numero entero/ No introduzca letras\n")
        q2=max(q,3)
        if q2%2==0:
            q2+=1
        if activo:
            hilo = threading.Thread(target=esperar_enter, daemon=True)
            hilo.start()
        for n in range (q2,p+1,2):
            primo=True
            for i in range(3,int(sqrt(n)+1),2):
                if n%i==0:
                    primo=False
                    break
            if cancelar.is_set():
                p=L[-1]
                break   
            if primo:
                L.append(n)
        L.sort()
        print(L)
        print(f"Son un total de {len(L)} numeros primos de {q} hasta {p}")
        tiempoT(time)
    case _:
        print("No creo que debias ver este print... o caso, por lo que consideralo un error")