'''un  robot può spostarsi su un pavimento con ostacoli; bisogna definire una mappa (in un file csv)
'''

'''fare matrice numerata con celle libere, poi dizionario di adiacenze(a partire da matrice numerata)'''


import pygame
from pygame.locals import *

def calc_pav():
    with open("pavimento.csv", "r") as f:
        mat = [[int(c) for c in riga.split(", ")] for riga in f.readlines()]
    return mat

def main():

    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    k = 1

    #SETUP per schermo, immagini e font
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro.png")
    strada = pygame.image.load("strada.jpg")
    robot = pygame.image.load("robot.png")
    font = pygame.font.SysFont("Verdana", 18) 
    
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            surf2 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0,0,0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x-100, lato_y-100))  
            elif casella == 0:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))  
                screen.blit(text, text_pos)
                k += 1
            elif casella == 3:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))
                surf2.blit(robot, (lato_x-100, lato_y-100))
                screen.blit(surf1, (lato_x-100, lato_y-100)) 
                screen.blit(text, text_pos)
                k += 1
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100

        screen.blit(robot, (0, 0))

        
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()


if __name__ == "__main__":
    main()