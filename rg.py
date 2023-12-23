import pygame
pygame.init()
win = pygame.display.set_mode((300, 300))
color = (153, 156, 239)

win.fill(color)
x = 150
y = 200
w = 200
h = 100

pygame.draw.ellipse(win,(255, 255, 255), (135, 50, 40, 200), 2)
pygame.draw.ellipse(win,(255, 255, 255), (135, 50, 80, 200), 2)
pygame.draw.ellipse(win,(255, 255, 255), (135, 50, 40, 200), 2)
pygame.display.update()
