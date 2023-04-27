import pygame
import random
import time
import datetime

# name = input("Enter your name: ")

pygame.init()
WIDTH, HEIGHT = 599, 599
SCREEN = pygame.display.set_mode((600, 700))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 50)
font_small = pygame.font.SysFont('Verdana', 20) # Шрифт  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.block = BLOCK_SIZE
        self.dx = self.block  
        self.dy = 0
        self.body = [
            Point(
                x = WIDTH // BLOCK_SIZE // 2,
                y = HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x = WIDTH // BLOCK_SIZE // 2 + 1,
                y = HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def head(self): 
        return self.body[0]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    # def move(self):  # motion
    #     for i in range(len(self.body)-1, 0, -1):  # all particles move
    #         # self.body[i].set_coordinates(self.body[i].get_coordinates())
    #         self.body[i].x = self.body[i-1].x  # except head, all blocks get coordinates of previous block
    #         self.body[i].y = self.body[i-1].y

    #     self.head().x += self.dx  # head moves by dx
    #     self.head().y += self.dy

    #     if self.head().x > WIDTH:   # if snake reaches the border, it starts motion form the opposite edge
    #         self.head().x = 0
    #     if self.head().x < 0:
    #         self.head().x = WIDTH
    #     if self.head().y > HEIGHT:
    #         self.head().y = 0
    #     if self.head().y < 0:
    #         self.head().y = HEIGHT

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
    def check_self_collision(self):
        head = self.body[0]
        if len(self.body) <= 2:
            return False
        for index in range(len(self.body)-1, 0 ,-1):
            if head.x == self.body[index].x and head.y == self.body[index].y:
                return True
            # else:
            #     print("NO")
    # def head_collide(self, particle) -> bool: # if snake collides with its tail, or wall, or food
    #     return self.body[0].x == particle.x and self.body[0].y == particle.y


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE // 2,
                BLOCK_SIZE // 2,
            )
        )
    
class SuperFood(Food):
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            WHITE,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

# def start_menu():
#     global start_game
#     SCREEN.fill((69, 172, 116))
#     SCREEN.blit(font.render('Start', True, WHITE), (30, 170))
#     SCREEN.blit(font_small.render('Easy', True, WHITE), (30, 300))
#     SCREEN.blit(font_small.render('Medium', True, WHITE), (30, 350))
#     SCREEN.blit(font_small.render('Hard', True, WHITE), (30, 400))

# def game_over():

# super_food_appeared = False  # conditions
# level_increased = False
# super_food = None
DISAPPEAR_SUPER_FOOD_EVENT = pygame.USEREVENT+1

def super_food_disappears_after_some_seconds(seconds=6):  
    pygame.time.set_timer(DISAPPEAR_SUPER_FOOD_EVENT, seconds*1000)  

def main():
    super_food_appeared = False  
    level_increased = False
    super_food = None
    # DISAPPEAR_SUPER_FOOD_EVENT = pygame.USEREVENT+1
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    level_increased = False
    SCORE = 0
    LEVEL = 0
    FPS = 5
    while running:
        SCREEN.fill(BLACK)

        # start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
            

        snake.move(dx, dy)
        if snake.check_self_collision():
            running = False            
        if snake.check_collision(food):
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y)
            )
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            SCORE += 1

        SCREEN.blit(font_small.render(f"Score: {SCORE}", True, BLUE), (11, HEIGHT+30))
        SCREEN.blit(font_small.render(f"Level: {LEVEL}", True, BLUE), (11, HEIGHT+53))

        draw_grid()
        snake.draw()
        food.draw()


       

        if SCORE != 0:
            if SCORE % 5 == 0: 
                if not super_food_appeared:
                    super_food_appeared = True
                    super_food = SuperFood(5, 5)
                    super_food_disappears_after_some_seconds()
        if SCORE % 5 == 1:
            super_food_appeared = False

        if SCORE % 7 == 0: 
            if not level_increased:
                level_increased = True
                LEVEL += 1
                FPS += 2
        elif SCORE % 7 == 1:
            level_increased = False

        if super_food: 
            super_food.draw()

        if super_food:
            if snake.check_collision(super_food):
                SCORE += 2
                snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
                super_food = None

        pygame.draw.line(SCREEN, WHITE, (599, 0), (599, 600), width=1)
        pygame.draw.line(SCREEN, WHITE, (0, 600), (600, 600), width=1)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()