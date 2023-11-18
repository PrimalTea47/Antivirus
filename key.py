import pygame
#from classes import *

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Test mouvements clavier')

background = pygame.image.load('assets/backgroundPlay.jpg')
black_back = pygame.Rect(0,0,800,200)

bordure_1 = pygame.Rect(50,760,700,50)
bordure_2 = pygame.Rect(640,200,50,600)
bordure_3 = pygame.Rect(65,320,50,550)
bordure_4 = pygame.Rect(200,190,700,50)


#Block
img_block = pygame.image.load('assets/molecule/block.png')
img_block_hitbox = img_block.get_rect(center=(300,300))

#Red
img_red = pygame.image.load('assets/molecule/3.png')
img_red_hitbox = img_red.get_rect(center = (600,700))

#Purple
img_purple = pygame.image.load('assets/molecule/5.png')
img_purple_hitbox = img_purple.get_rect(center=(100,600))

control_list = [img_red_hitbox, img_purple_hitbox]
control_list_names = ['Red', 'Violet']
collisions_list = control_list[0] or control_list[1]

moving = 0

run = True
while run:

    for event in pygame.event.get():

        #Fermer la fenêtre
        if event.type == pygame.QUIT:
            run = False

        #bouger les rectangles TOUT EN GÉRANT LES COLLISIONS
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN:
                control_list[moving].x , control_list[moving].y  = control_list[moving].x + 5 , control_list[moving].y + 5
                
                if img_block_hitbox.collidelistall(control_list):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 5 , control_list[moving].y - 5
            
            
            if event.key == pygame.K_UP:
                control_list[moving].x , control_list[moving].y  = control_list[moving].x - 5 , control_list[moving].y - 5
                
                if img_block_hitbox.collidelistall(control_list):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 5 , control_list[moving].y + 5
                    
                
            if event.key == pygame.K_RIGHT:
                control_list[moving].x , control_list[moving].y  = control_list[moving].x + 5 , control_list[moving].y - 5            
                
                if img_block_hitbox.collidelistall(control_list):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 5 , control_list[moving].y + 5 
            
            
            if event.key == pygame.K_LEFT:
                control_list[moving].x , control_list[moving].y  = control_list[moving].x - 5 , control_list[moving].y + 5
                
                if img_block_hitbox.collidelistall(control_list):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 5 , control_list[moving].y - 5
                
            
            #gérer le changement de rectangles si '(CTRL) droit' est appuyé
            if event.key == pygame.K_RCTRL:
                if moving == len(control_list)-1:
                    moving = 0
                    print(control_list_names[moving])
                else:
                    moving += 1
                    print(control_list_names[moving])
            
        
        #Le but du jeu est atteint
        if pygame.Rect.colliderect(img_red_hitbox, black_back):
            run = False
                
            
        
        
        #tout le temps mettre à jour l'écran
        screen.blit(background, (-100,200))
        pygame.draw.rect(screen, (0,0,0), black_back)
        #afficher les images
        screen.blit(img_block, img_block_hitbox)
        screen.blit(img_red, img_red_hitbox)
        screen.blit(img_purple, img_purple_hitbox)

        #bordures
        pygame.draw.rect(screen, (255,0,0), bordure_1)
        pygame.draw.rect(screen, (255,0,0), bordure_2)
        pygame.draw.rect(screen, (255,0,0), bordure_3)
        pygame.draw.rect(screen, (255,0,0), bordure_4)

            
    
    pygame.display.update()

pygame.quit()