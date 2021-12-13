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
        bullet.x -= bullet_speed
        if player_1_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)
