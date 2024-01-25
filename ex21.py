#Importa a função mixer da biblioteca pygame
import pygame.mixer
from pygame import mixer

#Implementando o código
mixer.init()

#Tocando a música Time do Pink Floyd
#Carregando a música
mixer.music.load("04 Pink Floyd - Time.mp3")
mixer.music.play()
input('Aperte Enter para encerrar a música')