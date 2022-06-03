#!/usr/bin/python

import pygame
import random

titolo =raw_input("Dai un titolo alla finestra:")
print("Inserisi le dimensioni della finestra")
h =input("Altezza:")
l =input("Larghezza:")
print("Inserisci le gradazioni di colore")
red =input("Rosso(da 0 a 255):")
green =input("Verde(da 0 a 255:")
blue =input("Blu(da 0 a 255:")

pygame.init() #Dichiarazione start game

finestra = pygame.display.set_mode((l,h)) #Dimensione finestra
pygame.display.set_caption(titolo) #Titolo finestra
finestra.fill((red,green,blue)) #Cabiamento colore sfondo (Red,Green,Blue)
pygame.display.update() #Aggiornamento display
ciclo = pygame.time.Clock() #Contatore FPS
FPS = 60 #Variabie

while True:
    ciclo.tick(FPS) #Ciclo FPS
    for evento in pygame.event.get(): #Il "get" ci torna uno alla volta tutti gli eventi in una struttura a pila
        if evento.type == pygame.QUIT:
            quit()
