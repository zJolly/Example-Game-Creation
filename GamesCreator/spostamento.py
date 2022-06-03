#!/usr/bin/python

import pygame
import random

pygame.init()
finestra = pygame.display.set_mode((650,500))
pygame.display.set_caption("PyGame")
finestra.fill((200,0,0))
pygame.display.update()
ciclo = pygame.time.Clock() #Contatore FPS
FPS = 60
y = 0
x = 0
t = 50
h = 1
ok = 0
ok1 = 0

while True:
    ciclo.tick(FPS)
    for evento in pygame.event.get():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pygame.draw.rect(finestra,(r,g,b),(y,x,t,t),h)
        pygame.display.update()
        if evento.type == pygame.QUIT:
            quit()
        else:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    quit()
                elif evento.key == pygame.K_UP:
                    if x > 0:
                        x=x-50
                elif evento.key == pygame.K_DOWN:
                    if x < 450:
                        x=x+50
                elif evento.key == pygame.K_RIGHT:
                    if y < 600:
                        y=y+50
                elif evento.key == pygame.K_LEFT:
                    if y > 0:
                        y=y-50
                elif evento.key == pygame.K_q:
                        if ok == 0:
                            x=x+1
                            pygame.display.update()
                            if x == 450:
                                ok=1
                        elif ok == 1:
                            x=x-1
                            pygame.display.update()
                            if x == 0:
                                ok=0
                elif evento.key == pygame.K_e:
                        if ok1 == 0:
                            y=y+1
                            pygame.display.update()
                            if y == 600:
                                ok1=1
                        elif ok1 == 1:
                            y=y-1
                            pygame.display.update()
                            if y == 0:
                                ok1=0
    finestra.fill((200,0,0))
