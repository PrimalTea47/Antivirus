import pygame
from classes import *
from niveau2 import niveau_2


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
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
####NIVEAU 1####
def niveau_1():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('NIVEAU 1')

    #Autres variables
    background = pygame.image.load('assets/backgroundPlay.jpg')
    black_back = pygame.Rect(0,0,800,200)

    #Bordures pour ne pas sortir du plateau de jeu
    bordure_1 = pygame.Rect(50,760,700,50)
    bordure_2 = pygame.Rect(640,200,50,600)
    bordure_3 = pygame.Rect(65,320,50,550)
    bordure_4 = pygame.Rect(200,190,700,50)
    


    #Block
    img_block = pygame.image.load('assets/molecule/block.png')
    img_block_hitbox = pygame.Rect(410,530,80,80)

    #Red
    img_red = pygame.image.load('assets/molecule/3.png')
    img_red_hitbox = [pygame.Rect((260,380,80,70)), pygame.Rect((340,460,80,70)), pygame.Rect(300,420,70,70)]

    #Purple
    img_purple = pygame.image.load('assets/molecule/5.png')
    img_purple_hitbox = [pygame.Rect(190,305,70,70), pygame.Rect(190,460,80,80), pygame.Rect(205,380,50,80), pygame.Rect(340,310,80,80), pygame.Rect(265,320,80,55)]

    #Restart & Home
    recommencer = Restart(screen)
    recommencer.restart_button()

    control_list = [img_red_hitbox,img_purple_hitbox]
    control_list_names = ['Rouge', 'Violet']
    control_color = [(255,0,0),(153, 0, 255)]
    control_coordinates = [[250,370],[180,300]]
    control_bordures = [bordure_1, bordure_2, bordure_3, bordure_4]

    replace_haut = replace_bas = replace_droit = replace_gauche = False
    show_hitbox = False

    moving = 0

    run = True
    while run:



        for event in pygame.event.get():

            

            #Fermer la fenêtre
            if event.type == pygame.QUIT:
                run = False
            

            #Besoin de recommencer le niveau OU retourner au menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recommencer.get_rect_restart().collidepoint(event.pos):
                    niveau_1()
                
           

            #bouger les rectangles TOUT EN GÉRANT LES COLLISIONS
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].y -= 10
                        control_list[moving][i].x += 10
                    control_coordinates[moving][1] -= 10
                    control_coordinates[moving][0] += 10
                    #Collisions (bcp de possibilités)
                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or pygame.Rect.colliderect(control_list[moving][i], img_block_hitbox):
                            replace_haut = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_haut = True
                    
                    
                    if replace_haut:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].y += 10
                            control_list[moving][i].x -= 10
                        control_coordinates[moving][1] += 10
                        control_coordinates[moving][0] -= 10
                    replace_haut = False

                    
                
                if event.key == pygame.K_DOWN:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].y += 10
                        control_list[moving][i].x -= 10
                    control_coordinates[moving][1] += 10
                    control_coordinates[moving][0] -= 10

                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or pygame.Rect.colliderect(control_list[moving][i], img_block_hitbox):
                            replace_bas = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_bas = True
                    
                    if replace_bas:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].y -= 10
                            control_list[moving][i].x += 10
                        control_coordinates[moving][1] -= 10
                        control_coordinates[moving][0] += 10
                    replace_bas = False
                



                if event.key == pygame.K_RIGHT:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].x += 10
                        control_list[moving][i].y += 10
                    control_coordinates[moving][0] += 10
                    control_coordinates[moving][1] += 10

                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or pygame.Rect.colliderect(control_list[moving][i], img_block_hitbox):
                            replace_droit = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_droit = True
                    
                    if replace_droit:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].x -= 10
                            control_list[moving][i].y -= 10
                        control_coordinates[moving][0]-= 10
                        control_coordinates[moving][1] -= 10
                    replace_droit = False
                



                if event.key == pygame.K_LEFT:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].x -= 10
                        control_list[moving][i].y -= 10
                    control_coordinates[moving][0] -= 10
                    control_coordinates[moving][1] -=10

                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or pygame.Rect.colliderect(control_list[moving][i], img_block_hitbox):
                            replace_gauche = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_gauche = True
                    
                    if replace_gauche:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].x += 10
                            control_list[moving][i].y += 10
                        control_coordinates[moving][0] += 10
                        control_coordinates[moving][1] += 10
                    replace_gauche = False
                    
                
                #gérer le changement de rectangles si '(CTRL) droit' est appuyé
                if event.key == pygame.K_RCTRL:
                    if moving == 1:
                        moving = 0
                    else:
                        moving += 1
                
                #gérer l'affichage des hitboxes
                if event.key == pygame.K_h:
                    show_hitbox = not show_hitbox
                                      
                
            
            #Le but du jeu est atteint
            
            if black_back.collidelistall(img_red_hitbox):
                menu()
                              


            
            #tout le temps mettre à jour l'écran
            screen.blit(background, (-100,200))
            pygame.draw.rect(screen, (0,0,0), black_back)
            write_text(control_list_names[moving], font, (control_color[moving]), 0, 0, screen)
            write_text('CTRL droit pour changer', little_font, control_color[moving], 0, 50, screen)
            write_text('H pour afficher/masquer les hitboxes', little_font, (255,255,255), 0, 100, screen)

            #afficher les images
            screen.blit(img_block, (400,520))
            screen.blit(img_red,control_coordinates[0])
            screen.blit(img_purple, control_coordinates[1])
            recommencer.show_restart_button()

            if show_hitbox:
                for i in range(len(img_purple_hitbox)):
                    pygame.draw.rect(screen, control_color[1], img_purple_hitbox[i], 2)

                for i in range(len(img_red_hitbox)):
                    pygame.draw.rect(screen, control_color[0], img_red_hitbox[i], 2)
                
                pygame.draw.rect(screen, (100,100,100), img_block_hitbox, 2)

                for i in range(4):
                    pygame.draw.rect(screen, (255,255,255), control_bordures[i], 2)

            

            

                
        
        pygame.display.update()

    pygame.quit()

####FIN NIVEAU 1####
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
####NIVEAU 2####
def niveau_2():
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('NIVEAU 2')

    #Autres variables
    background = pygame.image.load('assets/backgroundPlay.jpg')
    black_back = pygame.Rect(0,0,800,200)

    #Block
    img_block = pygame.image.load('assets/molecule/block.png')
    img_block_hitbox = img_block.get_rect(center=(380,350))

    #Block 2
    img_block2_hitbox = img_block.get_rect(center=(380,490))

    #Red
    img_red = pygame.image.load('assets/molecule/3.png')
    img_red_hitbox = img_red.get_rect(center = (565,390))

    #Light Blue
    img_lightBlue = pygame.image.load('assets/molecule/2.png')
    img_lightBlue_hitbox = img_lightBlue.get_rect(center=(190,390))

    #Restart & Home
    recommencer = Restart(screen)
    recommencer.restart_button()

    control_list = [img_red_hitbox, img_lightBlue_hitbox]
    control_list_names = ['Rouge', 'Bleu Clair']
    control_color = [(255,0,0),(25, 173, 227)]

    moving = 0

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

            #Besoin de recommencer le niveau OU retourner au menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recommencer.get_rect_restart().collidepoint(event.pos):
                    niveau_2()
                
           

            #bouger les rectangles TOUT EN GÉRANT LES COLLISIONS
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_DOWN:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y + 10
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_lightBlue_hitbox, img_red_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y - 10
                
                
                if event.key == pygame.K_UP:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y - 10
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_lightBlue_hitbox, img_red_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y + 10
                        
                    
                if event.key == pygame.K_RIGHT:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y - 10            
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_lightBlue_hitbox, img_red_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y + 10 
                
                
                if event.key == pygame.K_LEFT:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y + 10
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_lightBlue_hitbox, img_red_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y - 10
                    
                
                #gérer le changement de rectangles si '(CTRL) droit' est appuyé
                if event.key == pygame.K_RCTRL:
                    if moving == 1:
                        moving = 0
                    else:
                        moving += 1
                        
                
            
            #Le but du jeu est atteint
            if pygame.Rect.colliderect(img_red_hitbox, black_back):
                menu()
            
            #tout le temps mettre à jour l'écran
            screen.blit(background, (-100,200))
            pygame.draw.rect(screen, (0,0,0), black_back)
            write_text(control_list_names[moving], font, (control_color[moving]), 0, 0, screen)
            write_text('CTRL droit pour changer', little_font, control_color[moving], 0, 50, screen)

            #afficher les images
            screen.blit(img_block, img_block_hitbox)
            screen.blit(img_block, img_block2_hitbox)
            screen.blit(img_red, img_red_hitbox)
            screen.blit(img_lightBlue, img_lightBlue_hitbox)
            recommencer.show_restart_button()
            pygame.draw.rect(screen, (0,0,255), img_red_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_lightBlue_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_block_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_block2_hitbox, 2)
        
        pygame.display.update()
    pygame.quit()

####FIN NIVEAU 2####
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
####NIVEAU 3####
def niveau_3():
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('NIVEAU 3')

    #Autres variables
    background = pygame.image.load('assets/backgroundPlay.jpg')
    black_back = pygame.Rect(0,0,800,200)

    #Block
    img_block = pygame.image.load('assets/molecule/block.png')
    img_block_hitbox = img_block.get_rect(center=(380,350))

    #Block 2
    img_block2_hitbox = img_block.get_rect(center=(380,490))

    #Red
    img_red = pygame.image.load('assets/molecule/3.png')
    img_red_hitbox = img_red.get_rect(center = (565,700))

    #Dark Blue
    img_darkBlue = pygame.image.load('assets/molecule/6.png')
    img_darkBlue_hitbox = img_darkBlue.get_rect(center=(190,390))

    #Orange
    img_orange = pygame.image.load('assets/molecule/9.png')
    img_orange_hitbox = img_orange.get_rect(center=(0,700))

    #Light Green
    img_lightGreen = pygame.image.load('assets/molecule/1.png')
    img_lightGreen_hitbox = img_lightGreen.get_rect(center=(700,400))

    #Restart & Home
    recommencer = Restart(screen)
    recommencer.restart_button()

    control_list = [img_red_hitbox, img_darkBlue_hitbox, img_orange_hitbox, img_lightGreen_hitbox]
    control_list_names = ['Rouge', 'Bleu foncé', 'Orange', 'Vert clair']
    control_color = [(255,0,0),(0, 0, 255), (217, 95, 9), (123, 191, 46)]

    moving = 0
    

    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #Besoin de recommencer le niveau OU retourner au menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recommencer.get_rect_restart().collidepoint(event.pos):
                    niveau_3()
            

            

            #bouger les rectangles TOUT EN GÉRANT LES COLLISIONS
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_DOWN:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y + 10
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_red_hitbox) or pygame.Rect.colliderect(img_red_hitbox,img_darkBlue_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_lightGreen_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_lightGreen_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_orange_hitbox, img_darkBlue_hitbox) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_lightGreen_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y - 10
                
                
                if event.key == pygame.K_UP:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y - 10
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_red_hitbox) or pygame.Rect.colliderect(img_red_hitbox,img_darkBlue_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_lightGreen_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_lightGreen_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_orange_hitbox, img_darkBlue_hitbox) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_lightGreen_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y + 10
                        
                    
                if event.key == pygame.K_RIGHT:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y - 10            
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_red_hitbox) or pygame.Rect.colliderect(img_red_hitbox,img_darkBlue_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_lightGreen_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_lightGreen_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_orange_hitbox, img_darkBlue_hitbox) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_lightGreen_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y + 10 
                
                
                if event.key == pygame.K_LEFT:
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 10 , control_list[moving].y + 10
                    
                    if img_block_hitbox.collidelistall(control_list) or img_block2_hitbox.collidelistall(control_list) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_red_hitbox) or pygame.Rect.colliderect(img_red_hitbox,img_darkBlue_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_lightGreen_hitbox) or pygame.Rect.colliderect(img_red_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_lightGreen_hitbox, img_orange_hitbox) or pygame.Rect.colliderect(img_orange_hitbox, img_darkBlue_hitbox) or pygame.Rect.colliderect(img_darkBlue_hitbox, img_lightGreen_hitbox):
                        control_list[moving].x , control_list[moving].y  = control_list[moving].x + 10 , control_list[moving].y - 10
                    
                
                #gérer le changement de rectangles si '(CTRL) droit' est appuyé
                if event.key == pygame.K_RCTRL:
                    if moving == 3:
                        moving = 0
                    else:
                        moving += 1
                        
                
            
            #Le but du jeu est atteint
            if pygame.Rect.colliderect(img_red_hitbox, black_back):
                menu()
            
            #tout le temps mettre à jour l'écran
            screen.blit(background, (-100,200))
            pygame.draw.rect(screen, (0,0,0), black_back)
            write_text(control_list_names[moving], font, (control_color[moving]), 0, 0, screen)
            write_text('CTRL droit pour changer', little_font, control_color[moving], 0, 50, screen)

            #afficher les images
            screen.blit(img_block, img_block_hitbox)
            screen.blit(img_block, img_block2_hitbox)
            screen.blit(img_red, img_red_hitbox)
            screen.blit(img_darkBlue, img_darkBlue_hitbox)
            screen.blit(img_orange, img_orange_hitbox)
            screen.blit(img_lightGreen, img_lightGreen_hitbox)
            recommencer.show_restart_button()
            pygame.draw.rect(screen, (0,0,255), img_red_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_darkBlue_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_block_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_block2_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_orange_hitbox, 2)
            pygame.draw.rect(screen, (0,0,255), img_lightGreen_hitbox, 2)



        pygame.display.update()
    pygame.quit()


#Exécution du programme
menu()