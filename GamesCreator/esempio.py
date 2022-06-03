#!/usr/bin/python

import pygame
import random

pygame.init() #Dichiarazione start game

finestra = pygame.display.set_mode((640,480)) #Dimensione finestra
pygame.display.set_caption("PyGame") #Titolo finestra
finestra.fill((255,0,0)) #Cabiamento colore sfondo (Red,Green,Blue)
pygame.display.update() #Aggiornamento display
ciclo = pygame.time.Clock() #Contatore FPS
FPS = 60 #Variabie

while True:
    ciclo.tick(FPS) #Ciclo FPS
    for evento in pygame.event.get(): #Il "get" ci torna uno alla volta tutti gli eventi in una struttura a pila
        if evento.type == pygame.QUIT:
            quit()
    pygame.draw.rect(finestra,(0,255,0),(0,0,30,30),1) #Implementazione figura (nome finestra dove verra collegato,(R,G,B),(x,y,altezza,larghezza),vuoto1 o riempito0)
    pygame.display.update()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    finestra.fill((r,g,b))
