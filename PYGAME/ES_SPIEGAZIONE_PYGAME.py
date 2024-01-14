import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

# creiamo la Surface surf1, la coloriamo di rosso e la posizioniamo sullo schermo
surf1 = pygame.Surface((200, 200))
surf1.fill("red")
rect1 = surf1.get_rect()
rect1.topleft = (50, 50)
screen.blit(surf1, rect1)

# stessa cosa con surf2 (blu)
surf2 = pygame.Surface((100, 100))
surf2.fill("blue")
rect2 = surf2.get_rect()
rect2.topleft = rect1.topright
screen.blit(surf2, rect2)

# aggiorniamo lo schermo
pygame.display.flip()

# ciclo principale
done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == QUIT:                  # chiusura della finestra
            done = True
        elif ev.type == MOUSEBUTTONDOWN:     # click del mouse
            click = ev.pos
            if rect1.collidepoint(click):
                print("Hai cliccato il rettangolo rosso")
            elif rect2.collidepoint(click):
                print("Hai cliccato il rettangolo blu")
            else:
                print ("Hai cliccato fuori dalle superfici")

# fine del ciclo e termine del programma
pygame.quit()
    