import time
import os
import random
j="y"
r=1
v=0
d=0
m=0
m2=""
while j in ("y",""):
    print("<><><><><><><><><><><><><><><><>\n Juego: Piedra, Papel o Tijeras \n<><><><><><><><><><><><><><><><>")
    time.sleep(1)
    print(f"Ronda #{r}, Victorias: {v}, Derrotas: {d}")
    time.sleep(1)
    print("1) es para Piedra\n2) es para Papel\n3) es para Tijeras")
    time.sleep(1)
    e=int(input("¿Cual elijes? "))
    if not 1<=e<=3:
        print("Error: Opcion no valida")
        time.sleep(1)
        break
    time.sleep(1)
    m=random.randint(1,3)
    if m==1:
        m2="Piedra"
    elif m==2:
        m2="Papel"
    else:
        m2="Tijeras"
    print("Piedra...")
    time.sleep(1)
    print("Papel...")
    time.sleep(1)
    print("o Tijeras...!")
    time.sleep(1)
    if (e==1 and m==3 or e==2 and m==1 or e==3 and m==2) and 1<=e<=3:
        print(f"Ganaste, la maquina uso {m2}")
        v=v+1
    elif e==m and 1<=e<=3:
        print(f"Empate, Ambos sacaron {m2}")
    elif not (e==1 and m==3 or e==2 and m==1 or e==3 and m==2) and 1<=e<=3:
        print(f"Perdiste, la maquina uso {m2}")
        d=d+1
    time.sleep(1)
    r=r+1
    j= input("¿Quieres jugar de nuevo?[y,n] ")
    j= j.lower()
    os.system('cls')
    time.sleep(1)
if not e in '123':
    j= input("¿Quieres internarlo de nuevo?[y,n] ")
    j= j.lower()
    os.system('cls')
time.sleep(1)
print(f"Jugaste {r} ronda/s")
time.sleep(1)
print(f"Ganaste {v} veces y Perdiste {d} veces")
time.sleep(1)
print("Hasta la Proxima :D")
    
        