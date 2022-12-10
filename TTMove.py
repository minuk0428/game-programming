import pygame
import PIL
import random as r
import sys

Moniter = None
colorList = ["red","green","blue","black","magenta","orange","gray"]

pygame.init()
pygame.key.set_repeat(5, 5)
monitor = pygame.display.set_mode((500,700))
color = r.choice(colorList)
turtle= pygame.image.load("/Users/imin-ug/Python/PythonGame/OneDrive_2022-10-13/turtle.png")
tx,ty = 200,300

while True:
    monitor.fill(color)
    monitor.blit(turtle, (tx,ty))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()
        
        if e.type in [pygame.KEYDOWN]:
            if e.key == pygame.K_SPACE:
                tx = r.randint(0,500)
                ty = r.randint(0,700)           
        if e.type in [pygame.KEYDOWN]:
            if e.key == pygame.K_LEFT : tx -= 5
            elif e.key == pygame.K_RIGHT : tx += 5
            elif e.key == pygame.K_UP : ty -= 5
            elif e.key == pygame.K_DOWN : ty += 5