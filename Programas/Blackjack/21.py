import random; from os import system; system('cls')
Jugar=True;Dinero=1000;Acepto= ["y","s","1","yes","si"]
while Jugar and Dinero>0:
    print("Blackjack\nAproximate u obten un valor de 21 con tus cartas\nLos valores del 2 al 10 valen lo que dicen, el A vale 1 y/o 11\nLas cartas como el K,Q, y J valen 10 aqui\n")

    # Aqui solo pedimos cuanto dinero apostara
    while 1:
        try:
            dapuesta= int(input(f"Cuanto Apuestas?\nDinero actual:${Dinero}\n>>"))
            if dapuesta>0 and dapuesta<=Dinero:break
            else:print("Error:Apuesta un valor mayor a 0")
        except ValueError: print("Error:Ingrese un numero entero y no letras")
    Apuesta=False;Victoria=False;Perdio=False
    valores=["A","2","3","4","5","6","7","8","9","10","Q","J","K"]
    baraja = [];jugador=[];banca=[]
    figuras = ['♣','♠','♦','♥']
    # Creamos la baraja
    for palo in figuras:
        for valor in valores:
            baraja.append([valor,palo])

    def cambio(x):
        y=0;z=0
        for i in x:
            if i=="Carta Secreta":break
            else:
                p= i[0]
                if p=='A':y+=11;z+=1
                elif p in ["K","J","Q","10"]:y+=10
                else:y+= int(p)
        while y>21 and z>0:
            y-=10;z-=1
        return y
    random.shuffle(baraja)

    # Repartimos las cartas
    for i in range(2):
        jugador.append(baraja.pop())
        banca.append(baraja.pop())

    banca.append("Carta Secreta")
    system('cls')
    # Aqui empieza el Juego
    print("Jugador: ", *(jugador))
    print("Banca:", banca[0],",",banca[2])
    print(f"Puntos Jugador:{cambio(jugador)}")
    #Confirmamos algunas condiciones antes de que empieze a preguntar por mas cartas
    if cambio(jugador)==21:Victoria=True;break
    elif cambio(jugador)>21:Perdio=True;break
    elif cambio(jugador)<21:
        while 1:
            try:
                if len(jugador)>=3:
                    system('cls')
                    print("Jugador: ", *(jugador))
                    print("Banca:", banca[0],",",banca[2])
                    print(f"Puntos Jugador:{cambio(jugador)}")
                agarrar= int(input("Quieres agarrar otra carta?\n1)Si\n2)No\n>>"))
                if agarrar ==1:jugador.append(baraja.pop())
                else:break
                # Chequeo de nuevo por si pierde/gana
                if cambio(jugador)==21:Victoria=True;break
                elif cambio(jugador)>21:Perdio=True;break
            except ValueError:print("Ingrese un numero entero/ no ingrese caracteres no numericos/no dejar vacio\n")
    while 1 and Victoria==False and Perdio==False:
        try:
            #Si cree que no ganara incluso asi, puede decir que no y aun asi puede ganar porque prediccion
            apuesta=int(input("Crees que ganaras?\n1)Si\n2)No\n>>"))
            if apuesta==1:Apuesta=True;break
            elif apuesta==2:Apuesta=False;break
            else: print("Porfavor, ingresa un 1 o 2 para elegir una opcion\n")
        except ValueError: print("Ingrese un numero entero/ No ingrese caracteres no numericos\n")

    system('cls');print("Jugador: ", *(jugador));print("Banca: ", banca[0],banca[1])
    print(f"Puntos Jugador:{cambio(jugador)}, Puntos Bancas:{cambio(banca)}")
    if ((cambio(jugador)>cambio(banca) and Apuesta) or (cambio(jugador)<cambio(banca) and Apuesta==False) or Victoria) and Perdio==False:
        if Apuesta==False and Victoria!=True:print("♦ Le atinaste!, Apostaste que no ganarias y fue asi, pero no ganaras dinero ♦\n")
        else:print("♦ Ganaste! ♦\n")
        if Victoria!=True and Apuesta:Dinero+=dapuesta
        else:print("♥ Como obtuviste 21, ganas el doble ♥");Dinero+=(dapuesta*2)
    elif cambio(jugador)==cambio(banca) and Victoria!=True and Perdio!=True: print("♠ Empate, No pierdes dinero ♠\n")
    else:print("♣ Perdiste D: ♣");Dinero-=dapuesta

    #Si tiene dinero y si el programa aun anda abierto (Obviamente), le dara la chance de seguir jugando
    while 1 and Dinero>0:
        try:
            jugar= int(input("Quieres seguir jugando?\n1)Si\n2)No\n>>"))
            if jugar==1:system('cls');Jugar=True;break
            elif jugar==2 or jugar!=1:Jugar=False;break
        except ValueError:print("Ingrese un numero entero/ no caracteres no numericos/ no vacio\n")
if Dinero>0:print("Gracias por jugar :D")
else: print("Tas pobre, pero gracias por jugar :D")