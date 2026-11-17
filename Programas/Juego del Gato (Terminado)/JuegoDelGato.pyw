#Creado por Miguel Angel Encinas Bustillos

import pygame,random;import numpy as np; from os import system;system('cls');from time import sleep
import sys
def ganador(ficha):
    #Del bot, generado con ia porque no supe como sin romper el programa
    for i in range(3):
        if np.all(tablero[i, :] == ficha):
            return True
        if np.all(tablero[:, i] == ficha):
            return True
    return (
        (tablero[0, 0] == ficha and tablero[1, 1] == ficha and tablero[2, 2] == ficha)
        or (tablero[0, 2] == ficha and tablero[1, 1] == ficha and tablero[2, 0] == ficha)
    )

def elegir_jugada():
    #Del bot, generado con ia porque no supe como sin romper el programa
    # Prioridad: ganar y luego bloquear al jugador.
    for ficha in ("O", "X"):
        candidatas = []
        for fila in range(3):
            for columna in range(3):
                if tablero[fila, columna] == "_":
                    tablero[fila, columna] = ficha
                    gana = ganador(ficha)
                    tablero[fila, columna] = "_"
                    if gana:
                        candidatas.append((fila, columna))

        if candidatas:
            return random.choice(candidatas)

    preferidas = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]
    candidatas = [
        (fila, columna)
        for fila, columna in preferidas
        if tablero[fila, columna] == "_"
    ]
    if candidatas:
        return random.choice(candidatas)
    # Si no quedan esas, elige cualquier espacio libre.
    libres = [
        (fila, columna)
        for fila in range(3)
        for columna in range(3)
        if tablero[fila, columna] == "_"
    ]
    return random.choice(libres) if libres else None

# Como dice el nombre, checa si el jugador/es cumple con ciertas condiciones para ganar/perder
def chequeo_gameover():
    global tablero, WIN, GAMEOVER,EMPATE
    for fila in range(3):
        for columna in range(3):
            if np.all(tablero[fila,:]=="X"):WIN=True
            if np.all(tablero[fila,:]=="O"):GAMEOVER=True
            if (tablero[0,0]=="X" and tablero[1,1]=="X" and tablero[2,2]=="X") or (tablero[2,0]=="X" and tablero[1,1]=="X" and tablero[0,2]=="X"):WIN=True
            if (tablero[0,0]=="O" and tablero[1,1]=="O" and tablero[2,2]=="O") or (tablero[2,0]=="O" and tablero[1,1]=="O" and tablero[0,2]=="O"):GAMEOVER=True
            if np.all(tablero[:,columna]=="X"):WIN=True
            if np.all(tablero[:,columna]=="O"):GAMEOVER=True
            if not WIN and not GAMEOVER and not np.any(tablero == "_"):
                EMPATE = True
# Intercambia el X por una O en la terminal, para que cuando se este dibujando la pantalla, dibuje correctamente
def cambio(x,y):
    global turno_jugador,turno_jugador2,jugador
    tablero[x,y]=jugador
    if turno_jugador==True and turno_jugador2==False:
        turno_jugador=False
        turno_jugador2=True
        jugador="O"
    else:
        turno_jugador=True
        turno_jugador2=False
        jugador="X"

# Cuando se gana o pierde, se usa esta funcion para dejar las partes que se usan al jugar del programa de vuelta a su estado de origen
def otravez():
    global tablero,WIN,GAMEOVER,turno_jugador,turno_jugador2,jugador,EMPATE,ESPERANDO
    tablero = np.full((3,3),"_",dtype="U1")
    col=COLOR_B
    for fila2 in range(FILA):
        for columna2 in range(COLUMNA):
            if ((fila2==0 or fila2==2) and columna2==1) or (fila2==1 and (columna2==0 or columna2==2)):
                col=COLOR_A
            pygame.draw.rect(pantalla,col,(200*columna2,200*fila2,200,200))
            col=COLOR_B
    jugador='X'
    turno_jugador=True
    turno_jugador2=False
    WIN,GAMEOVER,EMPATE,ESPERANDO = False, False, False, False

# Esta funcion solo muestra quien gano tanto para Partida contra bots, como contra partidas contra otro jugador
def postgame():
    global ESPERANDO,inicio
    if not ESPERANDO:
        ESPERANDO=True
        inicio= pygame.time.get_ticks()
    if ESPERANDO:
        if pygame.time.get_ticks()-inicio<3000:
            pygame.draw.rect(pantalla,COLOR_B,(200, 200, 200, 200))
            if BOT:
                if WIN:
                    texto_post= fuente.render("Ganaste!", True, (COLOR_A))
                    pantalla.blit(texto_post, texto_post.get_rect(center=casilla5.center))
                if GAMEOVER:
                    texto_post= fuente.render("Perdiste...", True, (COLOR_A))
                    pantalla.blit(texto_post, texto_post.get_rect(center=casilla5.center))
                if EMPATE:
                    texto_post= fuente.render("Empate", True, (COLOR_A))
                    pantalla.blit(texto_post, texto_post.get_rect(center=casilla5.center))
            else:
                if WIN:
                    texto_post= fuente.render("J1 Gana!", True, (COLOR_A))
                    pantalla.blit(texto_post, texto_post.get_rect(center=casilla5.center))
                if GAMEOVER:
                    texto_post= fuente.render("J2 Gana!", True, (COLOR_A))
                    pantalla.blit(texto_post, texto_post.get_rect(center=casilla5.center))
                if EMPATE:
                    texto_post= fuente.render("Empate", True, (COLOR_A))
                    pantalla.blit(texto_post, texto_post.get_rect(center=casilla5.center)) 
            pygame.display.flip()
            clock.tick(1)
    else:
        ESPERANDO=False

# Establecemos los valores iniciales / Constantes
ANCHO, ALTO = 600, 600
COLOR_A, COLOR_B, COLOR_C =  (10, 10, 10), (225, 225, 225), (155,25,155)
GAMEOVER=False
WIN=False
EMPATE=False
BOT=None
ESPERANDO=False
FILA= ALTO//200
COLUMNA= ANCHO//200

jugador='X'
inicio=None
tiempo=None
turno_jugador=True
turno_jugador2=False
running=None
tablero = np.array([
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
])
victorias=0
derrotas=0
empate=0
col=COLOR_B
clock= pygame.time.Clock()

#Iniciamos el Pygame/Programa
pygame.init()
pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego del Gato | Elegir Modo")
pantalla= pygame.display.get_surface()

fuente = pygame.font.SysFont("yumincho", 30)
boton_bot = pygame.Rect(150, 250, 300, 70)
boton_jugadores = pygame.Rect(100, 350, 400, 70)

#Menu de seleccion de modo
menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if boton_bot.collidepoint(event.pos):
                BOT = True
                menu = False
            elif boton_jugadores.collidepoint(event.pos):
                BOT = False
                menu = False

    pantalla.fill((COLOR_B))

    titulo = fuente.render("Juego del Gato", True, (COLOR_A))
    texto_bot = fuente.render("Jugar contra el bot", True, (COLOR_A))
    texto_jugadores = fuente.render("Jugar contra otra persona", True, (COLOR_A))

    pantalla.blit(titulo, titulo.get_rect(center=(300, 150)))

    if boton_bot.collidepoint(pygame.mouse.get_pos()):
        texto_bot = fuente.render("Jugar contra el bot", True, (COLOR_B))
        pygame.draw.rect(pantalla, (COLOR_A), boton_bot)
    else:
        pygame.draw.rect(pantalla, (COLOR_A), boton_bot,width=2)
    if boton_jugadores.collidepoint(pygame.mouse.get_pos()):
        texto_jugadores = fuente.render("Jugar contra otra persona", True, (COLOR_B))
        pygame.draw.rect(pantalla, (COLOR_A), boton_jugadores)
    else:
        pygame.draw.rect(pantalla, (COLOR_A), boton_jugadores,width=2)
    pantalla.blit(texto_bot, texto_bot.get_rect(center=boton_bot.center))
    pantalla.blit(texto_jugadores, texto_jugadores.get_rect(center=boton_jugadores.center))

    pygame.display.flip()
    clock.tick(60)

#Crea las casillas cuales el jugador interactua en cierto modo al jugar
if BOT is not None:
    print("Juego del Gato\nSe te abrio una ventana aparte de la terminal")
    print("No la borres, es el juego, y la terminal tampoco, o sino se cierra el juego")
    print("Es para 2 jugadores, se espera agregarse funcionalidad contra maquina")
    running=True
    casilla = pygame.Rect(0, 0, 200, 200)
    casilla2 = pygame.Rect(200, 0, 200, 200)
    casilla3 = pygame.Rect(400, 0, 200, 200)
    casilla4 = pygame.Rect(0, 200, 200, 200)
    casilla5 = pygame.Rect(200, 200, 200, 200)
    casilla6 = pygame.Rect(400, 200, 200, 200)
    casilla7 = pygame.Rect(0, 400, 200, 200)
    casilla8 = pygame.Rect(200, 400, 200, 200)
    casilla9 = pygame.Rect(400, 400, 200, 200)
    tiempo_partida=pygame.time.get_ticks()
#Ahora empieza la parte del juego en caso que no haya cerrado el programa
while running:
    STotal=(pygame.time.get_ticks()-tiempo_partida)//1000
    if STotal<60: tiempo=f"{STotal}s"
    elif STotal<3600: tiempo=f"{STotal//60}m"
    else: tiempo= f"{STotal//3600}h"
    for fila2 in range(FILA):
        for columna2 in range(COLUMNA):
            if ((fila2==0 or fila2==2) and columna2==1) or (fila2==1 and (columna2==0 or columna2==2)):
                col=COLOR_A
            pygame.draw.rect(pantalla,col,(200*columna2,200*fila2,200,200))
            col=COLOR_B

    #Dibuja las figuras para ver donde ya esta ocupado/libre
    for fila in range(3):
        for columna in range(3):
            if tablero[fila,columna]=="X":
                pygame.draw.line(pantalla, (255,75,75), (50+200*columna, 50+200*fila), (150+200*columna, 150+200*fila), 12)
                pygame.draw.line(pantalla, (255,75,75), (50+200*columna, 150+200*fila), (150+200*columna, 50+200*fila), 12)
            if tablero[fila,columna]=="O":
                #Nota pal futuro, los ultimos 2 numeros son el radio, y el grosor de la figura
                pygame.draw.circle(pantalla, (75,75,255), (100+200*columna, 100+200*fila),60,6)
    

    pos = pygame.mouse.get_pos()
    ANCHO,ALTO=pantalla.get_size()
    chequeo_gameover()
    if BOT==True:
        if jugador == "O" and not WIN and not GAMEOVER and not EMPATE:
            jugada = elegir_jugada()
            if jugada is not None:
                cambio(*jugada) #Nota: el * es para cada elemento de jugada
                chequeo_gameover()
    #Lo siento por esta parte, pero es para hacer que en la matriz de antes, en donde diste click con tu mouse, cambie a tu figura
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running=False
        if casilla.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[0,0]=="_":
            cambio(0,0)
        if casilla2.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[0,1]=="_":
            cambio(0,1)
        if casilla3.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[0,2]=="_":
            cambio(0,2)
        if casilla4.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[1,0]=="_":
            cambio(1,0)
        if casilla5.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[1,1]=="_":
            cambio(1,1)
        if casilla6.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[1,2]=="_":
            cambio(1,2)
        if casilla7.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[2,0]=="_":
            cambio(2,0)
        if casilla8.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[2,1]=="_":
            cambio(2,1)
        if casilla9.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and tablero[2,2]=="_":
            cambio(2,2)
    #Pone en el titulo de la ventana dependiendo del modo, las estadisticas de la partida, aparte del tiempo transcurrido
    if WIN==False and GAMEOVER==False and BOT==True:
        pygame.display.set_caption(f"Gato | Modo: Bot | Tiempo: {tiempo} | Victorias: {victorias} | Derrotas: {derrotas} | Empates: {empate}")
    if WIN==False and GAMEOVER==False and BOT==False:
        pygame.display.set_caption(f"Gato | Modo: 1v1 | Tiempo: {tiempo} | Victorias J1: {victorias} | Victorias J2: {derrotas} | Empates: {empate}")
    if GAMEOVER:
        derrotas+=1
        postgame()
        otravez()
    elif WIN:
        victorias+=1
        postgame()
        otravez()
    elif EMPATE:
        empate+=1
        postgame()
        otravez()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()