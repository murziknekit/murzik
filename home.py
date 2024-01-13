import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

rad = 25
x = 250
y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill((255, 255, 255))
    pygame.draw.circle(win, (0, 255, 255), (x, y), rad)
    pygame.display.update()

    pygame.time.delay(5)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 3
    elif keys[pygame.K_d]:
        x += 3
    elif keys[pygame.K_w]:
        y -= 3
    elif keys[pygame.K_s]:
        y += 3
    else:
        if x<250 and y<250:
            stepx = (250 - x)/10
            stepy = (250 - y) / 10
            while x < 250 and y < 250:
                x+=stepx
                y+=stepy
                win.fill((255,255,255))
                pygame.draw.circle(win,(0,255,255),(x,y), rad)
                pygame.display.update()
                pygame.time.delay(100)
