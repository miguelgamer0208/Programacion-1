import numpy as np;from os import system;system('cls')
invertido=False;Vacio=False
#sim="ø"
sim="*"
while 1:
    try:
        n=int(input("Que tan grande quieres tu figura?[Mayor a 3]\n>>"))
        if n<=3:print("Error:Porfavor elige un valor mayor a 3\n")
        else:break
    except ValueError:print("Error:Ingresa un numero entero, no decimal ni tampoco no numerico.")

while 1:
    try:
        eleccion=int(input("Que figura quieres hacer?\n1)Un cuadrado\n2)Una piramide\n3)Un reloj\n4)Un Rombo\n5)Una Casa\n>>"))
        if eleccion<1 or eleccion>5: print("Error:Opcion fuera del rango de opciones")
        else: break
    except ValueError:print("Error:Ingresa un numero entero, no decimal ni tampoco no numerico.")

if eleccion!=5:
    if eleccion not in [1,3,4]:
        while 1:
            inv=input("Lo quieres que este invertido?\n1)Si\n2)No \n[Nota:Cualquier cosa que no sea 1 o Si, es no, incluyendo el no escribir nada]\n>>").lower()
            if inv == "si" or inv=="yes" or inv=="1":
                invertido=True
                break
            else:
                break
    while 1:
        vacio=input("Lo quieres que este Vacio?\n1)Si\n2)No \n[Nota:Cualquier cosa que no sea 1 o Si, es no, incluyendo el no escribir nada]\n>>").lower()
        if vacio == "si" or vacio=="yes" or vacio=="1":
            Vacio=True
            break
        else:break

#Pa que el rombo quede impar siempre, y no quede doble **
if (eleccion == 4 or eleccion==3) and n % 2 == 0:
    n += 1

# El ancho de los triangulos, pa no tener que escribirlo a cada rato
a=2*n-1

match eleccion:
    case 1:
        # El cuadrado usa n filas y n columnas.
        matriz=np.full((n,n)," ",np.dtype("U1"))
    case 2: 
        # El triangulo necesita n filas y a columnas para quedar centrado.
        matriz=np.full((n,a)," ",np.dtype("U1"))
    case 3:
        # El lienzo del reloj tiene una fila adicional que el triangulo
        matriz=np.full((n+1,n+1)," ",np.dtype("U1"))
    case 4:
        # El rombo ocupa una matriz cuadrada de n por n.
        matriz=np.full((n,n)," ",np.dtype("U1"))
    case 5:
        matriz=np.full((25,31)," ",np.dtype("U1"))
# DIBUJO DEL CUADRADO
if eleccion==1 and Vacio==False:
   for fila in range(n):
        matriz[fila,:]=sim
elif eleccion==1 and Vacio==True:
    for fila in range(n):
        matriz[fila,0]=sim
        matriz[fila,n-1]=sim
    matriz[0,:]=sim
    matriz[n-1,:]=sim


# Piramide/Triangulo
if eleccion==2 and invertido==False and Vacio==False:
    for fila in range(n):
        c=n-fila-1
        d=n+fila
        # Recordatorio: si incluye c mas no d, pero si d-1
        matriz[fila,c:d]=sim
# Piramide Invertida
elif eleccion==2 and invertido==True and Vacio==False:
    for fila in range(n):
        c=fila
        d=a-fila
        matriz[fila,c:d]=sim
# Piramide Vacia
elif eleccion==2 and invertido==False and Vacio==True:
    for fila in range(n):
        #Recordatorio personal 2: Solo dibuja los contornos
        c=n-fila-1
        d=n+fila
        matriz[fila,c]=sim
        matriz[fila,d-1]=sim
        # Recordatorio 3 nomas asi: Dibuja la base
        if fila==n-1:matriz[fila,c:d]=sim

# Piramide con todo
elif eleccion==2 and invertido==True and Vacio==True:
    for fila in range(n):
        c=fila
        d=a-fila
        if fila==0:
            # La base primero  pa que amarre
            matriz[fila,c:d]=sim
        else:
            matriz[fila,c]=sim
            matriz[fila,d-1]=sim

if eleccion==3 and Vacio==False:
    for fila in range(n):
        dist=abs(fila)
        c=dist
        d=n-dist
        if c<d:
            matriz[fila,c:d]=sim
        else:
            matriz[fila,d-1:c+1]=sim
    
elif eleccion==3 and Vacio==True:
    for fila in range(n):
        dist=abs(fila)
        c=dist
        d=n-dist
        if fila==0:
            matriz[fila,c:d]=sim
        elif fila==n-1:
            matriz[fila,d-1:c+1]=sim
        else:
            matriz[fila,c]=sim
            matriz[fila,d-1]=sim

if eleccion==4 and Vacio==False:
    cen=n//2
    for fila in range(n):
        dist = abs(cen - fila)
        c = dist
        d = n-dist-1
        matriz[fila, c:d+1] = sim
elif eleccion==4 and Vacio==True:
    cen=n//2
    for fila in range(n):
        dist = abs(cen - fila)
        c = dist
        d = n-dist-1
        matriz[fila, c] = sim
        matriz[fila, d] = sim
if eleccion==5:
    print("Se ignoro el tamaño dado por ti")
    for fila in range(16):
        c=16-fila-1
        d=16+fila
        matriz[fila,c]=sim
        matriz[fila,d-1]=sim
        if fila==15:matriz[fila,c:d]=sim

    for fila in range(15,25):
        matriz[fila,3]=sim
        matriz[fila,27]=sim
    matriz[19,12:18]=sim
    for fila in range(19,25):
            matriz[fila,12]=sim
            matriz[fila,18]=sim
    for fila in range(18,23):
            matriz[fila,9]=sim
            matriz[fila,5]=sim
            matriz[fila,21]=sim
            matriz[fila,25]=sim
            matriz[fila,7]=sim
            matriz[fila,23]=sim
    matriz[20,5:9]=sim
    matriz[20,21:25]=sim
    matriz[18,5:9]=sim
    matriz[22,5:9]=sim
    matriz[18,21:25]=sim
    matriz[22,21:25]=sim
    matriz[15,:]=sim
    matriz[24,:]=sim





# Mostramos una fila de la matriz por linea, separando las columnas con espacios.
for fila in matriz:
    print(" ".join((fila)))

# Dibujamos una linea debajo de la figura como separador.
print(" ".join("-"*(n+5)))
