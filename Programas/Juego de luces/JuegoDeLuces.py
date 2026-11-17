import numpy as np;from os import system;system('cls');from time import sleep
c=10;intentos=1
def cambios(x,y):
    if x[y]==1:x[y]=0
    elif x[y]==0:x[y]=1
    if x[y-1]==1 and y!=0:x[y-1]=0
    elif x[y-1]==0 and y!=0:x[y-1]=1
    if y<9:
        if x[y+1]==1:x[y+1]=0
        elif x[y+1]==0:x[y+1]=1

posiciones= np.full( c, " ", np.dtype("U2"))
for pos in range(c):
    posiciones[pos]=pos+1
while 1:   
    luces=np.zeros(c ,dtype=np.uint8)
    for n in range(c):
        if np.random.randint(2)==1:
            if n>0: luces[n-1]=1-luces[n-1]
            if n<c-1: luces[n+1]=1-luces[n+1]
            luces[n]=1-luces[n]
    if np.any(luces==1):break

while 1:
    print("Posiciones:"+"   "+"   ".join(posiciones))
    print("Juego Luces:"+" ".join(str(luces)))
    if np.any(luces==0):
        while 1:
            try:
                pose= int(input("Elige una posicion de la tabla de posiciones\n>>"))-1
                if pose<0 or pose>9:print("Error: Valor fuera del rango de posiciones\n")
                elif 0<=pose<=9:break
            except ValueError: print("Ingrese un valor entero, numerico y/o no vacio\n")
        print(pose)
        cambios(luces,pose)
    if np.all(luces==1):break
    else:intentos+=1
print(f"Ganaste!, te tomo unos {intentos} intentos")
    

