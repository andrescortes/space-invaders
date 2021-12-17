import random
from builtins import print
import os
import pygame


def load_img(path_img, img):
    current_path = os.path.dirname(__file__)  # Where your .py file is located
    # The resource folder path
    resource_path = os.path.join(current_path, 'img')
    image_path = os.path.join(resource_path, path_img)  # The image folder path
    path_absolute = os.path.join(image_path, img)
    return path_absolute


def load_sound(sound):
    # Where your .py file is located
    current_path = os.path.dirname(__file__)
    # The resource folder path
    resource_path = os.path.join(current_path, 'sound')
    path_absolute = os.path.join(resource_path, sound)
    return path_absolute


def move_player_1(flag):
    if (flag == 1):
        player_1 = pygame.image.load(
            load_img('ship_yellow', 'spaceship_yellow_up.png'))
        return player_1
    elif(flag == 2):
        player_1 = pygame.image.load(
            load_img('ship_yellow', 'spaceship_yellow_down.png'))
        return player_1
    elif(flag == 3):
        player_1 = pygame.image.load(
            load_img('ship_yellow', 'spaceship_yellow_left.png'))
        return player_1
    elif(flag == 4):
        player_1 = pygame.image.load(
            load_img('ship_yellow', 'spaceship_yellow_right.png'))
        return player_1
    else:
        return None


def move_player_2(flag):
    if (flag == 1):
        player_2 = pygame.image.load(
            load_img('ship_red', 'spaceship_red_up.png'))
        return player_2
    elif(flag == 2):
        player_2 = pygame.image.load(
            load_img('ship_red', 'spaceship_red_down.png'))
        return player_2
    elif(flag == 3):
        player_2 = pygame.image.load(
            load_img('ship_red', 'spaceship_red_left.png'))
        return player_2
    elif(flag == 4):
        player_2 = pygame.image.load(
            load_img('ship_red', 'spaceship_red_right.png'))
        return player_2
    else:
        return None


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow > 0:  # LEFT
        yellow -= 3
    if keys_pressed[pygame.K_d] and yellow + 90 < 400:  # RIGHT
        yellow += 3
    return yellow


def yellow_handle_movement2(keys_pressed, yellow):
    if keys_pressed[pygame.K_w] and yellow > 0:  # UP
        yellow -= 3
    if keys_pressed[pygame.K_s] and yellow + 55 < 600 - 15:  # DOWN
        yellow += 3
    return yellow


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red - 5 > 400:  # LEFT
        red -= 3
    if keys_pressed[pygame.K_RIGHT] and red - 150 < 560:  # RIGHT
        red += 3
    return red


def red_handle_movement2(keys_pressed, red):
    if keys_pressed[pygame.K_UP] and red - 3 > 0:  # UP
        red -= 3
    if keys_pressed[pygame.K_DOWN] and red + 55 < 600 - 15:  # DOWN
        red += 3
    return red


def handle_bullets_player_1(yellow_bullets, player_2_rect, bullet_speed, red_hit, window_width):
    for bullet in yellow_bullets:
        bullet.x += bullet_speed
        if player_2_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > window_width:
            yellow_bullets.remove(bullet)


def handle_bullets_player_2(red_bullets, player_1_rect, bullet_speed, yellow_hit):
    for bullet in red_bullets:
        print("bullet red: ", bullet)
        bullet.x -= bullet_speed
        if player_1_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text, winner_font, width, height, colour_white, window_game):
    draw_text = winner_font.render(text, 1, colour_white)
    window_game.blit(draw_text, (width/2 - draw_text.get_width() /
                                 2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def check_collision(playerRect, obstacle):
    # convert rectangles into x,y,w,h
    playerX = playerRect[0]
    playerY = playerRect[1]
    playerWidth = playerRect[2]
    playerHeight = playerRect[3]

    obstacleX = obstacle[0]
    obstacleY = obstacle[1]
    obstacleWidth = obstacle[2]
    obstacleHeight = obstacle[3]

    # get the right left top and bottom
    myRight = playerX + playerWidth
    myLeft = playerX
    myTop = playerY
    myBottom = playerY + playerHeight

    otherRight = obstacleX + obstacleWidth
    otherLeft = obstacleX
    otherTop = obstacleY
    otherBottom = obstacleY + obstacleHeight

    # now the collision code
    collision = True
    if ((myRight < otherLeft) or (myLeft > otherRight) or (myBottom < otherTop) or (myTop > otherBottom)):
        collision = False
    return collision
