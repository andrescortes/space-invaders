import pygame
import os
import time
# utils
import utils as util

#button sounds
pygame.init()
pygame.mixer.init()
help_sound_load = util.load_sound('help.wav')
help_sound = pygame.mixer.Sound(help_sound_load)
play_sound_load = util.load_sound('play.wav')
play_sound = pygame.mixer.Sound(play_sound_load)
exit_sound_load = util.load_sound('exit.wav')
exit_sound = pygame.mixer.Sound(exit_sound_load)


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
    bullet_speed = 10
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
    # rect_ship_red = pygame.Rect(700, 300, ship_width, ship_height)
    # rect_ship_yellow = pygame.Rect(100, 300, ship_width, ship_height)

    # ships load image
    player_1 = pygame.image.load(
        util.load_img('ship_yellow', 'spaceship_yellow_right.png'))
    player_2 = pygame.image.load(
        util.load_img('ship_red', 'spaceship_red_left.png'))

    # Coordenadas y velocidad del jugador 1
    coord_player1_X = 30
    coord_player1_Y = 250

    # Coordenadas y velocidad del jugador 2
    coord_player2_X = 680
    coord_player2_Y = 250

    game_over = False
    flag_player_1 = 0
    flag_player_2 = 0
    winner_text = ""
    obstacles = []
    start = time.time()
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # tecla presionada
            if event.type == pygame.KEYDOWN:
                # ------------Jugador 1-------------------
                if event.key == pygame.K_w:
                    flag_player_1 = 1
                if event.key == pygame.K_s:
                    flag_player_1 = 2
                if event.key == pygame.K_a:
                    flag_player_1 = 3
                if event.key == pygame.K_d:
                    flag_player_1 = 4
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullet:
                    bullet = pygame.Rect(player_1_rect.x + player_1_rect.width + 10,
                                         player_1_rect.y + player_1_rect.height//2 - 1, 20, 5)
                    yellow_bullets.append(bullet)
                    bullet_hit_shot.play()

                # ------------Jugador 2 ------------------
                if event.key == pygame.K_UP:
                    flag_player_2 = 1
                if event.key == pygame.K_DOWN:
                    flag_player_2 = 2
                if event.key == pygame.K_LEFT:
                    flag_player_2 = 3
                if event.key == pygame.K_RIGHT:
                    flag_player_2 = 4
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullet:
                    bullet = pygame.Rect(player_2_rect.x + player_2_rect.width - 100,
                                         player_2_rect.y + player_2_rect.height//2 - 1, 20, 5)
                    red_bullets.append(bullet)
                    bullet_hit_shot.play()
                # if var is none do nothing but is !None assign a img
                var_player_1, var_player_2 = util.move_player_1(
                    flag_player_1), util.move_player_2(flag_player_2),
                if(var_player_1):
                    player_1 = var_player_1
                if(var_player_2):
                    player_2 = var_player_2

            # impact discount life
            if event.type == red_hit:
                print("shot red")
                red_health -= 1
                bullet_hit_sound.play()

            if event.type == yellow_hit:
                print("shot yellow")
                yellow_health -= 1
                bullet_hit_sound.play()
            
        # draw winner
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            util.draw_winner(winner_text, winner_font, window_width,
                             window_height, colour_white, window_game)
            break

        keys_pressed = pygame.key.get_pressed()
        # if keys_pressed[pygame.K_UP] == True and  keys_pressed[pygame.K_w] == True
        coord_player1_X = util.yellow_handle_movement(
            keys_pressed, coord_player1_X)
        coord_player1_Y = util.yellow_handle_movement2(
            keys_pressed, coord_player1_Y)
        coord_player2_X = util.red_handle_movement(
            keys_pressed, coord_player2_X)
        coord_player2_Y = util.red_handle_movement2(
            keys_pressed, coord_player2_Y)

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
        # handle bullets
        util.handle_bullets_player_1(
            yellow_bullets, player_2_rect, bullet_speed, red_hit, window_width)
        util.handle_bullets_player_2(
            red_bullets, player_1_rect, bullet_speed, yellow_hit)
        # Actualiza la pantalla
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


def start():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgPresentation = pygame.image.load(
        util.load_img('img_project', 'Init.png'))
    window.blit(imgPresentation, (0, 0))
    pygame.display.update()
    time.sleep(1)

def play_again():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgHelp = pygame.image.load(util.load_img('img_project', 'PlayAgain.png'))
    window.blit(imgHelp, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_sound.play()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(x >= 329 and y >= 211 and x <= 575 and y <= 299):
                    play_sound.play()
                    game()
                if(x >= 290 and y >= 343 and x <= 510 and y <= 430):
                    exit_sound.play()
                    exit()
    

def menu():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgmenu = pygame.image.load(util.load_img('img_project', 'Beginning.png'))
    window.blit(imgmenu, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_sound.play()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(x >= 160 and y >= 152 and x <= 533 and y <= 228):
                    play_sound.play()
                    game()
                    menu()
                if(x >= 160 and y >= 236 and x <= 533 and y <= 314):
                    help_sound.play()
                    help()
                if(x >= 160 and y >= 322 and x <= 533 and y <= 397):
                    exit_sound.play()
                    exit()
            


def help():
    pygame.init()
    window = pygame.display.set_mode((800, 450))
    imgHelp = pygame.image.load(util.load_img('img_project', 'Help.png'))
    window.blit(imgHelp, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_sound.play()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if(x >= 567 and y >= 29 and x <= 736 and y <= 90):
                    help_sound.play()
                    menu()


start()
menu()
