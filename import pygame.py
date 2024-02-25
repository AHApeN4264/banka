import pygame
from pygame import *
from time import sleep

# Ініціалізація Pygame
pygame.init()

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Розміри вікна
screen_width = 800
screen_height = 600

# Створення вікна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Лабіринт")

# Завантаження фонового зображення
background_image = pygame.image.load('D:\payton\labirint2/Blank.jpg')
background_rect = background_image.get_rect()

# Розміри фонового зображення
background_image = transform.scale(image.load('D:\payton\labirint2/Blank.jpg'),(800, 600))

# Швидкість руху спрайтів
speed = 5

finish = False

font_style = pygame.font.SysFont(None, 60)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (100, 250))

def messages(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, (240, 250))

# Ігрові спрайти
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        global dx, dy
        keys = key.get_pressed()# Отримання натискання клавіш
        if keys[K_LEFT] and self.rect.x  > 5:
            dx = -1
        if keys[K_RIGHT] and self.rect.x < screen_width - 80:
            dx = 1
        if keys [K_UP] and self.rect.y  > 5:
            dy = -1
        if keys[K_DOWN] and self.rect.y  < screen_height - 80:
            dy = 1

class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1, screen_x, color_2, screen_y, color_3, width, height):
        super().__init__()
        self.color_1 = color_1 #color_2 та color_3 аналогічно
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = screen_x  
        self.rect.y = screen_y
        self.speed = 2
    def draw_wall (self):
        screen.blit(self.image, (self.rect.x, self.rect.y)) 

class Enemy(Wall):
    def update(self):
        if self.rect.x <= 180: 
            self.direction = "right"
        if self.rect.x >= screen_width - 315:
            self.direction = "left"
        if self.direction == "left": 
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

hero = Player('D:\payton\labirint2/hero.png', 30, 30, 5)
finish = GameSprite('D:\payton\labirint2/finish.jpg', 690, 30, 0)
lazer = Enemy(255, 150, 0, 303, 0, 90, 10)

# стены игры
# 1 цвет, 2 лево право, 3 цвет, 4 висота, 5 цвет, 6 ширена стени, 7 висота стени,
wall_1 = Wall(200, 20, 0, 17, 100, 750, 10)
wall_2 = Wall(200, 20, 10, 20, 100, 10, 573)
wall_3 = Wall(200, 20, 0, 580, 100, 760, 10)
wall_4 = Wall(200, 760, 10, 20, 100, 10, 570)
wall_5 = Wall(200, 183, 10, 120, 100, 10, 370)
wall_6 = Wall(200, 20, 10, 143, 100, 85, 10)
wall_7 = Wall(200, 105, 10, 303, 100, 85, 10)
wall_8 = Wall(200, 20, 10, 453, 100, 85, 10)
wall_9 = Wall(200, 283, 10, 27, 100, 10, 300)
wall_10 = Wall(200, 183, 10, 490, 100, 200, 10)
wall_11 = Wall(200, 373, 10, 100, 100, 10, 400)
wall_12 = Wall(200, 283, 10, 410, 100, 10, 79)
wall_13 = Wall(200, 373, 10, 490, 100, 10, 100)
wall_14 = Wall(200, 470, 10, 100, 100, 200, 10)
wall_15 = Wall(200, 670, 10, 25, 100, 10, 85)
wall_16 = Wall(200, 470, 10, 100, 100, 10, 400)
wall_17 = Wall(200, 470, 10, 500, 100, 210, 10)
wall_18 = Wall(200, 670, 10, 410, 100, 10, 100)
wall_19 = Wall(200, 570, 10, 180, 100, 10, 240)
wall_20 = Wall(200, 570, 10, 180, 100, 200, 160)

walls = sprite.Group()
walls.add(wall_1)
walls.add(wall_2)
walls.add(wall_3)
walls.add(wall_4)
walls.add(wall_5)
walls.add(wall_6)
walls.add(wall_7)
walls.add(wall_8)
walls.add(wall_9)
walls.add(wall_10)
walls.add(wall_11)
walls.add(wall_12)
walls.add(wall_13)
walls.add(wall_14)
walls.add(wall_15)
walls.add(wall_16)
walls.add(wall_17)
walls.add(wall_18)
walls.add(wall_19)
walls.add(wall_20)

# текст
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (255, 215, 0))

if finish != True:
    if sprite.collide_rect(hero, finish): 
        screen.blit(win, (200, 200))
        finish = True

# Основний цикл програми
running = True
clock = pygame.time.Clock()

while running:
    dx, dy = 0, 0
    screen.blit(background_image, (0, 0))
    hero.reset()
    hero.update()
    finish.reset()
    walls.draw(screen)  
    lazer.draw_wall()
    lazer.update()
    # sprites_list = sprite.spritecollide(hero, finish, True, True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hero.rect.x += dx * hero.speed
    hero.rect.y += dy * hero.speed
    if pygame.sprite.spritecollideany(hero, walls):
        hero.rect.x -= dx * hero.speed
        hero.rect.y -= dy * hero.speed
    if pygame.sprite.collide_rect(hero, finish):
        screen.fill(black)
        message("Молодец ты прошол лаберинт", green)
        pygame.display.update()
        sleep(2)
        pygame.quit()
    if pygame.sprite.collide_rect(hero, lazer):
        screen.fill(black)
        messages("Ты проиграл", red)
        pygame.display.update()
        sleep(2)
        pygame.quit()

    # Оновлення екрану
    pygame.display.flip()

    # Керування частотою кадрів
    clock.tick(60)

# Завершення роботи Pygame
pygame.quit()