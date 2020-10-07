from time import sleep
import pygame
for f in range(10, - 1, - 1):
    print(f)
    sleep(1)
print('Start!')
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()
print('END.')


