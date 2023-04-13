import pygame
import random
import time
import datetime

pygame.init()
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((700, 700))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

font_small = pygame.font.SysFont('Verdana', 18) # Шрифт  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.block = BLOCK_SIZE
        self.dx = self.block  # by default snake is moving in the right direction
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

    def head(self):  # head of the snake
        return self.body[0]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
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
    def head_collide(self, particle) -> bool: # if snake collides with its tail, or wall, or food
        return self.body[0].x == particle.x and self.body[0].y == particle.y


# def draw_grid():
#     for x in range(0, WIDTH, BLOCK_SIZE):
#         pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
#     for y in range(0, HEIGHT, BLOCK_SIZE):
#         pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


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
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


def main():
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


        snake.draw()
        food.draw()

        if SCORE % 7 == 0 and SCORE != 0: # increasing level and speed if score is divisible by 7
            if not level_increased:
                level_increased = True
                LEVEL += 1
                FPS += 2
        elif SCORE % 7 == 1:
            level_increased = False

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()