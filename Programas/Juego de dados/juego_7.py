import time
import random
import os
dinero=250
j=0
record=1
b2=1
r3=1
os.system('cls')
print("<><><><><><><><><><><><><><><><><><><><><><> \n-- Juego de Dados --   --Adivina el valor --\n<><><><><><><><><><><><><><><><><><><><><><>")
time.sleep(1)
jugar=input("¿Quieres Jugar?[y/n]")
jugar=jugar.lower()


if jugar == "n" or (jugar not in("y","")):
    time.sleep(1)
    print("Bueno... )")
else:
    while dinero >0 and jugar in("y",""):
        if dinero<1000:
            b= ""
            b2=dinero
            r3=record
        elif 1000<=dinero<1000000:
            b= "k"
            b2=dinero/1000
            r3=record/1000
        elif dinero>=1000000 and dinero<1000000000:
            b="M"
            b2=dinero/1000000
            r3=record/1000000
        else:
            b="B"
            b2=dinero/1000000000
            r3=record/1000000000
        if j>0:
            print("<><><><><><><><><><><><><><><><><><><><><><> \n-- Juego de Dados --   --Adivina el valor --\n<><><><><><><><><><><><><><><><><><><><><><>")
            time.sleep(1)
            print(f"Tu record actual es de: ${r3}{b}")
        if j==0:
            time.sleep(1)
            print("Es tu primera vez jugando")
        else:
            time.sleep(1)
            print(f"Es tu partida #{j}")
        
        time.sleep(1)
        print("Opcion 1 es para elegir que la suma de los dados es menor a 7 \nOpcion 2 es para elegir que la suma de los dados es igual a 7 \nOpcion 3 es para elegir que la suma de los Dados es mayor a 7")
        time.sleep(1.5)
        e=int(input("¿Cual Eliges?"))
        
        if e<1 or e>3:
            print("Error: Opcion no valida")
            time.sleep(2)
            os.system('cls')
        else:
            time.sleep(1)
            ap=int(input(f"¿Cuanto Apuestas?\ntienes ${b2}{b}: "))
            if ap>dinero or ap <=0:
                print("Error: Valor de Apuesta No valido")
                time.sleep(2)
                os.system('cls')
            else:
                d1= random.randint(1,6)
                d2= random.randint(1,6)
                t= d1+d2
                time.sleep(1)
                if (e == 1 and t<7) or (e == 2 and t==7) or (e == 3 and t>7):
                    print(f"Ganaste, salio un: {t}")
                    dinero= dinero + ap
                else:
                    print(f"Perdiste, salio un: {t}")
                    dinero= dinero - ap
                            
        if dinero>record:
            record=dinero
    
        if ((e<1 or e>3) or (ap>dinero or ap <=0)) and dinero>0:
            jugar=input("¿Quieres intentarlo de nuevo? [y/n}")
            jugar=jugar.lower()
            os.system('cls')
        elif dinero>0 and (e>0 and e<=3):
            j=j+1
            jugar=input("¿Quieres Jugar de nuevo? [y/n}")
            jugar=jugar.lower()
            time.sleep(1)
            os.system('cls')
        time.sleep(1)
    if dinero<=0:
        print("Estas en Bancarrota D:")
    time.sleep(1)
    print(f"Jugaste un total de: {j} ronda/s")
if j>0 and record>250:
    time.sleep(1)
    print(f"Tu record de dinero fue de: ${r3}{b}")
time.sleep(1)
print("Gracias Por Jugar :D")
    

        