import pygame
from classes import *
pygame.init()


def niveau_2():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('NIVEAU 2')

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
    img_block_hitbox = pygame.Rect(340,310,80,80)

    #Block2
    img_block2_hitbox = pygame.Rect(340,460,80,80)

    #Red
    img_red = pygame.image.load('assets/molecule/3.png')
    img_red_hitbox = [pygame.Rect((480,320,80,60)), pygame.Rect(520,350,70,70), pygame.Rect((560,400,70,70))]

    #Light blue
    img_lightblue = pygame.image.load('assets/molecule/2.png')
    img_lightblue_hitbox = [pygame.Rect(200,325,70,70), pygame.Rect(160,365,70,70), pygame.Rect(120,405,70,50)]

    #Restart
    recommencer = Restart(screen)
    recommencer.restart_button()

    control_list = [img_red_hitbox,img_lightblue_hitbox]
    control_list_names = ['Rouge', 'Bleu Clair']
    control_color = [(255,0,0),(25, 173, 227)]
    control_coordinates = [[470,300],[100,300]]
    control_bordures = [bordure_1, bordure_2, bordure_3, bordure_4]
    control_block = [img_block_hitbox, img_block2_hitbox]

    replace_haut = replace_bas = replace_droit = replace_gauche = False
    show_hitbox = False

    moving = 0

    run = True
    while run:



        for event in pygame.event.get():

            

            #Fermer la fenêtre
            if event.type == pygame.QUIT:
                run = False
            

            #Besoin de recommencer le niveau
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recommencer.get_rect_restart().collidepoint(event.pos):
                    niveau_2()
                
            

            #bouger les rectangles TOUT EN GÉRANT LES COLLISIONS
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].y -= 10
                        control_list[moving][i].x -= 10
                    control_coordinates[moving][1] -= 10
                    control_coordinates[moving][0] -= 10
                    #Collisions (bcp de possibilités)
                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or control_list[moving][i].collidelistall(control_block):
                            replace_haut = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_haut = True
                    
                    
                    if replace_haut:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].y += 10
                            control_list[moving][i].x += 10
                        control_coordinates[moving][1] += 10
                        control_coordinates[moving][0] += 10
                    replace_haut = False

                    
                
                if event.key == pygame.K_DOWN:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].y += 10
                        control_list[moving][i].x += 10
                    control_coordinates[moving][1] += 10
                    control_coordinates[moving][0] += 10

                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or control_list[moving][i].collidelistall(control_block):
                            replace_bas = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_bas = True
                    
                    if replace_bas:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].y -= 10
                            control_list[moving][i].x -= 10
                        control_coordinates[moving][1] -= 10
                        control_coordinates[moving][0] -= 10
                    replace_bas = False
                



                if event.key == pygame.K_RIGHT:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].x += 10
                        control_list[moving][i].y -= 10
                    control_coordinates[moving][0] += 10
                    control_coordinates[moving][1] -= 10

                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or control_list[moving][i].collidelistall(control_block):
                            replace_droit = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_droit = True
                    
                    if replace_droit:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].x -= 10
                            control_list[moving][i].y += 10
                        control_coordinates[moving][0]-= 10
                        control_coordinates[moving][1] += 10
                    replace_droit = False
                



                if event.key == pygame.K_LEFT:
                    for i in range(len(control_list[moving])):
                        control_list[moving][i].x -= 10
                        control_list[moving][i].y += 10
                    control_coordinates[moving][0] -= 10
                    control_coordinates[moving][1] +=10

                    for i in range(len(control_list[moving])):
                        if control_list[moving][i].collidelistall(control_list[not moving]) or control_list[moving][i].collidelistall(control_block):
                            replace_gauche = True
                        
                        elif control_list[moving][i].collidelistall(control_bordures):
                            replace_gauche = True
                    
                    if replace_gauche:
                        for i in range(len(control_list[moving])):
                            control_list[moving][i].x += 10
                            control_list[moving][i].y -= 10
                        control_coordinates[moving][0] += 10
                        control_coordinates[moving][1] -= 10
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
                run = False
                              
                
            
            
            #tout le temps mettre à jour l'écran
            screen.blit(background, (-100,200))
            pygame.draw.rect(screen, (0,0,0), black_back)
            write_text(control_list_names[moving], font, (control_color[moving]), 0, 0, screen)
            write_text('CTRL droit pour changer', little_font, control_color[moving], 0, 50, screen)
            write_text('H pour afficher/masquer les hitboxes', little_font, (255,255,255), 0, 100, screen)

            #afficher les images
            screen.blit(img_block, (330,300))
            screen.blit(img_block, (330,450))
            screen.blit(img_red,control_coordinates[0])
            screen.blit(img_lightblue, control_coordinates[1])
            recommencer.show_restart_button()

            if show_hitbox:
                for i in range(len(img_lightblue_hitbox)):
                    pygame.draw.rect(screen, control_color[1], img_lightblue_hitbox[i], 2)

                for i in range(len(img_red_hitbox)):
                    pygame.draw.rect(screen, control_color[0], img_red_hitbox[i], 2)
                
                pygame.draw.rect(screen, (100,100,100), img_block_hitbox, 2)
                pygame.draw.rect(screen, (100,100,100), img_block2_hitbox, 2)

                for i in range(4):
                    pygame.draw.rect(screen, (255,255,255), control_bordures[i], 2)

            



                
        
        pygame.display.update()

    pygame.quit()

