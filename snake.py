import pygame
import random
from pygame import *

# Инициализация pygame
pygame.init()

# Размеры окна
width = 800
height = 600

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

# Создание окна
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

background_image = pygame.image.load('D:\payton\galactika_war/galaxy.jpg')
background_rect = background_image.get_rect()

background_image = transform.scale(image.load('D:\payton\dogonialki/background.png'),(800, 600))

clock = pygame.time.Clock()

block_size = 20
snake_speed = 8

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, orange, [x[0], x[1], block_size, block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Координаты головы змеи
    x1 = width / 2
    y1 = height / 2

    # Изменение координат
    x1_change = 0
    y1_change = 0

    # Змея состоит из нескольких блоков, хранятся в списке
    snake_list = []
    snake_length = 1

    # Координаты яблока
    apple_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(black)
            message("Ви програли! Натисніть Q-вихід або C-грати знову", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Проверка столкновения с границей окна
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.blit(background_image, (0, 0))
        pygame.draw.rect(window, red, [apple_x, apple_y, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        pygame.display.update()

        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()


game_loop()