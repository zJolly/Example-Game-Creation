#!/usr/bin/python

import pygame
import random

pygame.init() #Dichiarazione start game

finestra = pygame.display.set_mode((640,480)) #Dimensione finestra
pygame.display.set_caption("PyGame") #Titolo finestra
finestra.fill((255,255,255)) #Cabiamento colore sfondo (Red,Green,Blue)
pygame.display.update() #Aggiornamento display
ciclo = pygame.time.Clock() #Contatore FPS
FPS = 14400 #Variabie

while True:
    ciclo.tick(FPS) #Ciclo FPS
    for evento in pygame.event.get(): #Il "get" ci torna uno alla volta tutti gli eventi in una struttura a pila
        if evento.type == pygame.QUIT:
            quit()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    y = random.randint(0,480)
    x = random.randint(0,640)
    pygame.draw.rect(finestra,(r,g,b),(x,y,30,30),1)
    pygame.display.update()
