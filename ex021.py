# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init() # Inicializa o mixer do Pygame

pygame.mixer.music.load('ex021.mp3')  # Carrega a música

pygame.mixer.music.play() # Toca a música

while pygame.mixer.music.get_busy():  # Mantém o programa em execução enquanto a música toca
    pygame.time.Clock().tick(10)


