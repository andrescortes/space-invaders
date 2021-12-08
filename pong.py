import pygame
import time
import os
def game():
    pygame.init()
    #Colores
    Negro = (0, 0, 0)
    Blanco = (255, 255, 255)
    Tamano = (800, 600)
    PlayerAncho = 15
    PlayerAlto = 90

    Ventana = pygame.display.set_mode(Tamano)
    clock = pygame.time.Clock()

    #Coordenadas y velocidad del jugador 1
    CoorPlayer1_X = 50
    CoorPlayer1_Y = 300 - 45
    
    player1Vel_Y = 0
    player1Vel_X = 0
    #Coordenadas y velocidad del jugador 2
    CoorPlayer2_X = 750 - PlayerAncho
    CoorPlayer2_Y = 300 - 45
    
    Player2Vel_Y = 0
    Player2Vel_X = 0

    # Coordenadas de la pelota
    Pelota_X = 400
    Pelota_Y = 300
    PelotaVel_X = 3
    PelotaVel_Y = 3

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            #tecla presionada
            if event.type == pygame.KEYDOWN:
                
                #------------Jugador 1-------------------
                if event.key == pygame.K_w:
                    player1Vel_Y = -3
                    pygame.display.flip('universe.jpeg', 90)
                if event.key == pygame.K_s:
                    player1Vel_Y = 3
                if event.key == pygame.K_a:
                    player1Vel_X = -3
                if event.key == pygame.K_d:
                    player1Vel_X = 3
                    
                # ------------Jugador 2 ------------------
                if event.key == pygame.K_UP:
                    Player2Vel_Y = -3
                if event.key == pygame.K_DOWN:
                    Player2Vel_Y = 3
                if event.key == pygame.K_LEFT:
                    Player2Vel_X = -3
                if event.key == pygame.K_RIGHT:
                    Player2Vel_X = 3
                    
            #key up = tecla soltada
            if event.type == pygame.KEYUP:
                
                # ---------------Jugador 1 ----------------
                if event.key == pygame.K_w:
                    player1Vel_Y = 0
                if event.key == pygame.K_s:
                    player1Vel_Y = 0
                if event.key == pygame.K_a:
                    player1Vel_X = 0
                if event.key == pygame.K_d:
                    player1Vel_X = 0
                    
                # ----------------Jugador 2 ---------------
                if event.key == pygame.K_UP:
                    Player2Vel_Y = 0
                if event.key == pygame.K_DOWN:
                    Player2Vel_Y = 0
                if event.key == pygame.K_LEFT:
                    Player2Vel_X = 0
                if event.key == pygame.K_RIGHT:
                    Player2Vel_X = 0

        if Pelota_Y > 590 or Pelota_Y < 10:
            print()
            print("position pelota y: ", Pelota_Y)
            print()
            PelotaVel_Y *= -1
            print()
            print("Pelota y: ", PelotaVel_Y)
            print()

        # Revisa si la pelota sale del lado derecho
        if Pelota_X > 800:
            Pelota_X = 400
            Pelota_Y = 300
            # Si sale de la pantalla, invierte direccion
            PelotaVel_X *= -1
            PelotaVel_Y *= -1

        # Revisa si la pelota sale del lado izquierdo
        if Pelota_X < 0:
            Pelota_X = 400
            Pelota_Y = 300
            # Si sale de la pantalla, invierte direccion
            PelotaVel_X *= -1
            PelotaVel_Y *= -1


        # Modifica las coordenadas para dar mov. a los jugadores/ pelota
        #suma posiciones en y para los dos jugadores
        
        #player 1
        CoorPlayer1_Y += player1Vel_Y
        CoorPlayer1_X += player1Vel_X
        #player 2
        CoorPlayer2_Y += Player2Vel_Y
        CoorPlayer2_X += Player2Vel_X
        
        # Movimiento pelota
        Pelota_X += PelotaVel_X
        Pelota_Y += PelotaVel_Y
        universe = os.path.join("universe.jpeg")
        Ventana.fill(Negro)
        
        #Ventana.blit(pygame.image.load(universe),(0,0))
        #Zona de dibujo
        jugador1 = pygame.draw.rect(Ventana, Blanco, (CoorPlayer1_X, CoorPlayer1_Y, PlayerAncho, PlayerAlto))
        jugador2 = pygame.draw.rect(Ventana, Blanco, (CoorPlayer2_X, CoorPlayer2_Y, PlayerAncho, PlayerAlto))
        pelota = pygame.draw.circle(Ventana, Blanco, (Pelota_X, Pelota_Y), 10)

        # Colisiones
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            PelotaVel_X *= -1

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def start():
    pygame.init()
    window = pygame.display.set_mode((800,450))
    presentation = os.path.join("Presentation.jpg")
    imgPresentation = pygame.image.load('/home/andres/Documents/Semester-12/graphics-computation/ping-pong/pong/Presentacion.jpg')
    window.blit(imgPresentation,(0,0))
    pygame.display.update()
    time.sleep(1)
    
def menu():
    pygame.init()
    window = pygame.display.set_mode((800,450))
    menuImag =os.path.join("/home/andres/Documents/Semester-12/graphics-computation/ping-pong/pong/Menu.jpg")
    imgmenu = pygame.image.load(menuImag)
    window.blit(imgmenu,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if(x>= 160 and y >= 152 and x <= 533 and y<=228):
                    game()
                if(x>= 160 and y >= 236 and x <= 533 and y<=314):
                    help()
                if(x>= 160 and y >= 322 and x <= 533 and y<=397):
                    exit()
def help():
    pygame.init()
    window = pygame.display.set_mode((800,450))
    imgHelp = pygame.image.load("/home/andres/Documents/Semester-12/graphics-computation/ping-pong/pong/Ayuda.jpg")
    window.blit(imgHelp,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if(x>= 86 and y >= 394 and x<=242 and y<=433):
                    menu()
                    
start()
menu()