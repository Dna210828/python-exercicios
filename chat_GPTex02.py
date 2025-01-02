import pygame
import time

# Inicializa o Pygame
pygame.init()

# Mensagem inicial
print('Contagem Regressiva:')
time.sleep(1)  # Pausa de 1 segundo antes de começar a contagem

# Contagem regressiva
for c in range(5, 0, -1):
    print(c)
    time.sleep(1)  # Pausa de 1 segundo entre os números
print('fique com a risada do gordinho')

# Carrega e toca a música
pygame.mixer.music.load('ex02.mp3')
pygame.mixer.music.play()

# Aguarda até que a música termine
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera até que a música termine








































    







