import pygame
from classes import *

from niveau1 import niveau_1
from niveau2 import niveau_2
from niveau3 import niveau_3

####MENU####
def menu():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('Sélectionnez votre niveau')

    #Bouton de niveaux
    cadre_niveau_1 = pygame.Rect(290,140,230,70)
    cadre_niveau_2 = pygame.Rect(290, 290, 230, 70)
    cadre_niveau_3 = pygame.Rect(290, 440, 230, 70)
    cadre_quit = pygame.Rect(310, 590, 190,70)

    run = True
    while run:

        #ajout des boutons
        pygame.draw.rect(screen, (0, 153, 51), cadre_niveau_1)
        write_text('Niveau 1', font, (0, 0, 0), 300, 150, screen)

        pygame.draw.rect(screen, (255, 102, 0), cadre_niveau_2)
        write_text('Niveau 2', font, (0,0,0), 300, 300, screen)

        pygame.draw.rect(screen, (200, 0, 0), cadre_niveau_3)
        write_text('Niveau 3',font, (0,0,0), 300, 450, screen)

        pygame.draw.rect(screen, (100,100,100), cadre_quit)
        write_text('Quitter', font, (0,0,0), 320,600, screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            #Éxécution des niveaux
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cadre_niveau_1.collidepoint(event.pos):
                    niveau_1()
                
                if cadre_niveau_2.collidepoint(event.pos):
                    niveau_2()
                
                if cadre_niveau_3.collidepoint(event.pos):
                    niveau_3()
                
                if cadre_quit.collidepoint(event.pos):
                    run = False
                    
                    
    
        pygame.display.update()


    pygame.quit()
####FIN MENU####

#Exécution du programme
menu()