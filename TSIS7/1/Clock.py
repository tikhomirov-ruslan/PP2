import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((835, 837))

clock = pygame.time.Clock()
image = pygame.image.load('Clock.png')
image = pygame.transform.scale(image, (835, 837))

image1 = pygame.image.load('Right.png')
image1 = pygame.transform.scale(image1, (65, 837))

image2 = pygame.image.load('Left.png')
image2 = pygame.transform.scale(image2, (99, 837))

done = False
angle = 0
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        t = datetime.now()
        hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

        #now = datetime.datetime.now()
        #second = int(now.second)
        #minute = int(now.minute)
        
        
        angle1 = angle - second * 6 
        angle2 = angle - minute * 6
        angle3 = angle - hour * 6

        screen.blit(image, (0, 0))
        rotated_image = pygame.transform.rotate(image1, angle2)
        rotated_image1 = pygame.transform.rotate(image2, angle3)

        new_rect = rotated_image.get_rect(center = image.get_rect().center)
        new_rect1 = rotated_image1.get_rect(center = image.get_rect().center)

        screen.blit(rotated_image, new_rect)
        screen.blit(rotated_image1, new_rect1)

        pygame.display.flip()
        clock.tick(60)
