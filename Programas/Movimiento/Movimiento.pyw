import pygame
ANCHO, ALTO, LADO = 640, 400, 40
VEL = 260 # píxeles por segundo
COLOR_A, COLOR_B, COLOR_C =  (0, 0, 0), (225, 225, 225), (155,25,155)
COLOR_D,COLOR_E=(200, 250, 90),(250, 90, 200)
FPS=60

pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO),pygame.RESIZABLE)

clock = pygame.time.Clock()
x, y = ANCHO / 2 - LADO / 2, ALTO / 2 - LADO / 2
diagonal= 1 / (2 ** 0.5)
running = True
while running:
    ANCHO, ALTO = screen.get_size()
    dt = clock.tick(FPS) / 1000 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    teclas = pygame.key.get_pressed()
    der = teclas[pygame.K_RIGHT]
    izq = teclas[pygame.K_LEFT]
    aba = teclas[pygame.K_DOWN]
    arr = teclas[pygame.K_UP]
    colision=pygame.Rect(x,y,LADO,LADO)
    
    dx, dy = der - izq, aba - arr
    if dx!=0 and dy!=0:
        dx *=diagonal
        dy *=diagonal
    x += dx * VEL * dt
    y += dy * VEL * dt
    #por lo que entendi, es para mantener dentro de la ventana al cubo
    x,y = max(0, min(x, ANCHO - LADO)), max(0, min(y, ALTO - LADO))

    screen.fill((25, 28, 40))
    pygame.display.set_caption(f"{dx} | {dy} | {x} | {y} | {clock.get_fps():.2f}")

    if colision.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, COLOR_E, (round(x), round(y), LADO, LADO), border_radius=6)
    else:
        pygame.draw.rect(screen, COLOR_D, (round(x), round(y), LADO, LADO), border_radius=6)
    pygame.display.flip()

pygame.quit()
