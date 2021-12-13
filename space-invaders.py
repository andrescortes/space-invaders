import pygame
import time
import os

# utils
import utils as util


def game():
    pygame.init()
    pygame.mixer.init()
    # Colores
    colour_black = (0, 0, 0)
    colour_white = (255, 255, 255)
    colour_red = (255, 0, 0)
    colour_yellow = (255, 255, 0)

    # vars
    window_width = 800
    window_height = 600
    player_width = 15
    player_height = 90

    #size and clock
    window_game = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    # border screen
    border_screen = pygame.Rect(window_width//2 - 5, 0, 10, window_height)

    # bullet sounds
    sound_grenade = util.load_sound('Grenade.wav')
    bullet_hit_sound = pygame.mixer.Sound(sound_grenade)
    soung_shot = util.load_sound('Shot.wav')
    bullet_hit_shot = pygame.mixer.Sound(soung_shot)

    # font
    health_font = pygame.font.SysFont('comicsans', 40)
    winner_font = pygame.font.SysFont('comicsans', 100)
    
    winner_font = pygame.font.SysFont('comicsans', 100)
    # health
    red_health = 10
    yellow_health = 10

    # fps
    fps = 60
    speed = 5
    bullet_speed = 7
    max_bullet = 3
    ship_width, ship_height = 90, 70
    # user event
    yellow_hit = pygame.USEREVENT + 1
    red_hit = pygame.USEREVENT + 2

    # bullets
    red_bullets = []
    yellow_bullets = []

    # load background image
    backgroung_space = pygame.transform.scale(pygame.image.load(
        util.load_img('img_project', 'space.png')), (window_width, window_height))

    # Estos rectángulos representan las spaceship
    rect_ship_red = pygame.Rect(700, 300, ship_width, ship_height)
    rect_ship_yellow = pygame.Rect(100, 300, ship_width, ship_height)

    # ships load image
    player_1 = pygame.image.load(
        util.load_img('ship_yellow', 'spaceship_yellow_right.png'))
    player_2 = pygame.image.load(
        util.load_img('ship_red', 'spaceship_red_left.png'))

    # Coordenadas y velocidad del jugador 1
    coord_player1_X = 50
    coord_player1_Y = 300 - 45
    player1_speed_Y = 0
    player1_speed_X = 0

    # Coordenadas y velocidad del jugador 2
    coord_player2_X = 750 - player_width
    coord_player2_Y = 300 - 45
    player2_speed_Y = 0
    player2_speed_X = 0

    # Coordenadas de la pelota
    ball_X = 400
    ball_Y = 300
    ball_speed_X = 3
    ball_speed_Y = 3

    game_over = False
    flag_player_1 = 0
    flag_player_2 = 0
    movie = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # tecla presionada
            if event.type == pygame.KEYDOWN:
                # ------------Jugador 1-------------------
                if event.key == pygame.K_w:
                    player1_speed_Y = -3
                    flag_player_1 = 1
                if event.key == pygame.K_s:
                    player1_speed_Y = 3
                    flag_player_1 = 2
                if event.key == pygame.K_a:
                    player1_speed_X = -3
                    flag_player_1 = 3
                if event.key == pygame.K_d:
                    player1_speed_X = 3
                    flag_player_1 = 4
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullet:
                    bullet = pygame.Rect(player_1_rect.x + player_1_rect.width,
                                         player_1_rect.y + player_1_rect.height//2 + 5, 10, 5)
                    yellow_bullets.append(bullet)
                    bullet_hit_shot.play()

                # ------------Jugador 2 ------------------
                if event.key == pygame.K_UP:
                    player2_speed_Y = -3
                    flag_player_2 = 1
                if event.key == pygame.K_DOWN:
                    player2_speed_Y = 3
                    flag_player_2 = 2
                if event.key == pygame.K_LEFT:
                    player2_speed_X = -3
                    flag_player_2 = 3
                if event.key == pygame.K_RIGHT:
                    player2_speed_X = 3
                    flag_player_2 = 4
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullet:
                    bullet = pygame.Rect(player_2_rect.x + player_2_rect.width,
                                         player_2_rect.y + player_2_rect.height//2 + 5, 10, 5)
                    red_bullets.append(bullet)
                    bullet_hit_shot.play()
                # if var is none do nothing but is !None assign a img
                var_player_1, var_player_2 = util.move_player_1(
                    flag_player_1), util.move_player_2(flag_player_2),
                if(var_player_1):
                    player_1 = var_player_1
                if(var_player_2):
                    player_2 = var_player_2

            # key up = tecla soltada
            if event.type == pygame.KEYUP:

                # ---------------Jugador 1 ----------------
                if event.key == pygame.K_w:
                    player1_speed_Y = 0
                if event.key == pygame.K_s:
                    player1_speed_Y = 0
                if event.key == pygame.K_a:
                    player1_speed_X = 0
                if event.key == pygame.K_d:
                    player1_speed_X = 0

                # ----------------Jugador 2 ---------------
                if event.key == pygame.K_UP:
                    player2_speed_Y = 0
                if event.key == pygame.K_DOWN:
                    player2_speed_Y = 0
                if event.key == pygame.K_LEFT:
                    player2_speed_X = 0
                if event.key == pygame.K_RIGHT:
                    player2_speed_X = 0

        if ball_Y > 590 or ball_Y < 10:
            ball_speed_Y *= -1

        # Revisa si la pelota sale del lado derecho
        if ball_X > 800:
            ball_X = 400
            ball_Y = 300
            # Si sale de la pantalla, invierte direccion
            ball_speed_X *= -1
            ball_speed_Y *= -1

        # Revisa si la pelota sale del lado izquierdo
        if ball_X < 0:
            ball_X = 400
            ball_Y = 300
            # Si sale de la pantalla, invierte direccion
            ball_speed_X *= -1
            ball_speed_Y *= -1

        # Modifica las coordenadas para dar mov. a los jugadores/ pelota
        # suma posiciones en y para los dos jugadores

        # player 1
        coord_player1_Y += player1_speed_Y
        coord_player1_X += player1_speed_X
        # player 2
        coord_player2_Y += player2_speed_Y
        coord_player2_X += player2_speed_X

        # Movimiento pelota
        ball_X += ball_speed_X
        ball_Y += ball_speed_Y
        # window_game.fill(colour_black)

        # Zona de dibujo
        player_1_rect = pygame.draw.rect(
            window_game, colour_white, (coord_player1_X, coord_player1_Y, ship_width, ship_height))
        player_2_rect = pygame.draw.rect(
            window_game, colour_white, (coord_player2_X, coord_player2_Y, ship_width, ship_height))

        window_game.blit(backgroung_space, (0, 0))
        pygame.draw.rect(window_game, colour_black, border_screen)

        red_health_text = health_font.render(
            "Health: " + str(red_health), 1, colour_white)
        yellow_health_text = health_font.render(
            "Health: " + str(yellow_health), 1, colour_white)

        window_game.blit(red_health_text, (window_width -
                         red_health_text.get_width() - 10, 10))
        window_game.blit(yellow_health_text, (10, 10))

        window_game.blit(player_1, (coord_player1_X, coord_player1_Y))
        window_game.blit(player_2, (coord_player2_X, coord_player2_Y))

        # draw bullets
        for bullet in red_bullets:
            pygame.draw.rect(window_game, colour_red, bullet)

        for bullet in yellow_bullets:
            pygame.draw.rect(window_game, colour_yellow, bullet)
        """ pelota = pygame.draw.circle(
            window_game, colour_white, (ball_X, ball_Y), 10)
        
        # Colisiones
        if pelota.colliderect(player_1_rect) or pelota.colliderect(player_2_rect):
            ball_speed_X *= -1 """
        util.handle_bullets_player_1(
            yellow_bullets, player_2_rect, bullet_speed, red_hit, window_width)
        util.handle_bullets_player_2(red_bullets,player_1_rect,bullet_speed,yellow_hit)
        # Actualiza la pantalla
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


def start():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgPresentation = pygame.image.load(
        util.load_img('img_project', 'Presentacion.jpg'))
    window.blit(imgPresentation, (0, 0))
    pygame.display.update()
    time.sleep(1)


def menu():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgmenu = pygame.image.load(util.load_img('img_project', 'Menu.jpg'))
    window.blit(imgmenu, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(x >= 160 and y >= 152 and x <= 533 and y <= 228):
                    game()
                if(x >= 160 and y >= 236 and x <= 533 and y <= 314):
                    help()
                if(x >= 160 and y >= 322 and x <= 533 and y <= 397):
                    exit()


def help():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgHelp = pygame.image.load(util.load_img('img_project', 'Ayuda.jpg'))
    window.blit(imgHelp, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(x >= 86 and y >= 394 and x <= 242 and y <= 433):
                    menu()


start()
menu()
