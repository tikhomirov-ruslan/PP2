import pygame

pygame.init()

pygame.mixer.music.load('fev.mp3')
pygame.mixer.music.play(-1)
# pygame.mixer.music.play()

image = pygame.image.load('12.jpg')
image = pygame.transform.scale(image, (320, 320))
show = image

_songs = [{
    "name" : 'fev.mp3',
    "photo": '12.jpg'
    },
    {
    "name" : 'love.mp3',
    "photo": 'clock.png'
    }]

H, M = 320, 320
White = (255,255,255)

#pause = pygame.image.load('pause.png')
#right = pygame.image.load('next.png')
#left = pygame.image.load('before.png')

screen = pygame.display.set_mode((H, M))
pygame.display.set_caption('Spotify')

flpause = False

ord_music = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # Set the x, y postions of the mouse click
        #     x, y = event.pos
        #     pos =  pygame.mouse.get_pos()
        #     pressed1 = pygame.mouse.get_pressed()[0]

        #     print(x , y)
        #     # if pause.get_rect().collidepoint(x, y):
        #     if pause.get_rect().collidepoint(pos) and pressed1:
        #         print("asd")
            
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                flpause = not flpause
                if flpause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                if event.key == pygame.K_RIGHT:
                    if ord_music == len(_songs)-1:
                        ord_music = 0
                    else:
                        ord_music +=1
                if event.key == pygame.K_LEFT:
                    if ord_music == 0:
                        ord_music = len(_songs) -1 
                    else:
                        ord_music -= 1
                show = pygame.image.load(_songs[ord_music]["photo"])
                show = pygame.transform.scale(show, (320, 320))
                pygame.mixer.music.load(_songs[ord_music]["name"])
                pygame.mixer.music.play(-1)

    poss = H * 0.8
    screen.fill(White)
    screen.blit(show, (0,0))

    #screen.blit(pause, (200,poss))
    #screen.blit(right, (300,poss))
    #screen.blit(left,  (100,poss))
    pygame.display.flip()