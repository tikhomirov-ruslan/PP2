import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((800, 800))

# set ball coordinates
ball_x = (800 // 2) - 25
ball_y = (800 // 2) - 25

velocity = 20

ball_color = RED
ball_radius = 25

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - velocity, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + velocity, screen_height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - velocity, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + velocity, screen_width - ball_radius)


    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()