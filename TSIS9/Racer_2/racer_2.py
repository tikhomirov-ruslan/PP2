import math
import random
import time
import pygame

clock = pygame.time.Clock() 

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

SPEED = 6  
SCORE = 0 
FPS = 60  

WIDTH = 393
HEIGHT = 600 
pygame.init()
screen = pygame.display.set_mode((393, 600)) 

font = pygame.font.SysFont('Verdana', 63)  
font_small = pygame.font.SysFont('Verdana', 18) 

game_over_text_label = font.render('Game over!', True, BLACK)
background = pygame.image.load('street.png')

pygame.mixer.init()
pygame.mixer.music.set_volume(0.45)
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(loops=10 ** 9)

pygame.display.set_caption('GAME')

game_over = False  


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.set_random_position()

    def move(self):
        self.rect.move_ip(0, 3) # движение по у
        if self.rect.top > HEIGHT:
            self.set_random_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_random_position(self):
        self.rect.center = (random.randint(40, WIDTH - 40), 0) # 40 - расстояние до линии
        self.rect.bottom = 0  # монета начинает дивжение сверху

class Super_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('super_coin.png')
        self.rect = self.image.get_rect()
        self.set_random_position()

    def move(self):
        self.rect.move_ip(0, 3) # движение по у
        if self.rect.top > HEIGHT:
            self.set_random_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_random_position(self):
        self.rect.center = (random.randint(40, WIDTH - 40), 0) # 40 - расстояние до линии
        self.rect.bottom = 0  # монета начинает дивжение сверху

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png') 
        self.rect = self.image.get_rect()
        self.set_random_position()

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED) #движение по у

        if self.rect.top > HEIGHT: # если машина выходит за рамки игры
            SCORE += 1  
            self.set_random_position()

    def set_random_position(self):
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
        self.rect.bottom = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect) 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png') 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 40:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 40:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


player = Player()  
enemy = Enemy() 
coin = Coin()
super_coin = Super_Coin()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)
all_sprites.add(super_coin)

enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

super_coins = pygame.sprite.Group()
#super_coins.add(super_coins)


Boost = pygame.USEREVENT + 1 
pygame.time.set_timer(Boost, 4000) # таймер ускорение 4с

captured_coins = 0
is_super_coin_generated = False

def generated_new_coin(type=1):
    global coin
    global super_coin
    if type == 1:
        coin = Coin()  
        coins.add(coin) # создать новую монетку
        all_sprites.add(coin)
    else:
        super_coin = Super_Coin()
        super_coins.add(super_coin)
        all_sprites.add(super_coin)


while not game_over:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            game_over = True
        if event.type == Boost:
            SPEED += 0.5

    screen.blit(background, (0, 0))

    screen.blit(font_small.render(f'Score: {SCORE}', True, BLUE), (293, 10))

    screen.blit(font_small.render(f'Coins: {captured_coins}', True, BLUE), (293, 30))  

    if SCORE % 12 == 0 and SCORE != 0:
        if not is_super_coin_generated:
            is_super_coin_generated = True
            generated_new_coin(type=2)
    elif SCORE % 12 == 1:
        is_super_coin_generated = False

    for sprite in all_sprites:
        sprite.move() 
        sprite.draw(screen)

    if pygame.sprite.spritecollideany(player, coins):  
        coin.kill()  
        captured_coins += 1  
        SCORE += 1 
        generated_new_coin() 
    

    if pygame.sprite.spritecollideany(player, super_coins):
        super_coin.kill()
        super_coins += 1
        SCORE += 2
        generated_new_coin()

    if pygame.sprite.spritecollideany(player, enemies): 
        pygame.mixer.music.stop() # остановить музыку и включить звук крушения
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1) # ждать 1 сек

        screen.fill(RED)  
        screen.blit(game_over_text_label, (12, 190))
        # screen.blit(font_small.render(f'Your score: {SCORE}', True, WHITE), (15, 270))
        # screen.blit(font_small.render(f'Captured coins: {captured_coins}', True, WHITE), (15, 290))

        pygame.display.update() 

        for sprite in all_sprites:
            sprite.kill()  # остановить игру

        time.sleep(7) 

        game_over = True

    pygame.display.update() 
    clock.tick(FPS) 

pygame.quit()