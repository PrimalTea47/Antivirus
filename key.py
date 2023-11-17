import pygame

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Test mouvemnts clavier')

white = pygame.Rect(100,100,80,50)
img = pygame.image.load('rectangle.png')
img = pygame.transform.scale(img, (80,60))
img_hitbox = img.get_rect(center=(500,500))

control_list = [img_hitbox,white]
moving = 0

run = True
while run:



    for event in pygame.event.get():

        #Fermer la fenêtre
        if event.type == pygame.QUIT:
            run = False

        #bouger les rectangles
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if not pygame.Rect.colliderect(white,img_hitbox):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 5 , control_list[moving].y + 5
            
            if event.key == pygame.K_UP:
                if not pygame.Rect.colliderect(white,img_hitbox):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 5 , control_list[moving].y - 5
                
            if event.key == pygame.K_RIGHT:
                if not pygame.Rect.colliderect(white,img_hitbox):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x + 5 , control_list[moving].y - 5                
            
            if event.key == pygame.K_LEFT:
                if not pygame.Rect.colliderect(white,img_hitbox):
                    control_list[moving].x , control_list[moving].y  = control_list[moving].x - 5 , control_list[moving].y + 5
                
            
            #gérer le changement de rectangles
            if event.key == pygame.K_RCTRL:
                if moving == 0:
                    moving = 1
                else:
                    moving = 0
            
        #Gérer les collisions
        if pygame.Rect.colliderect(white,img_hitbox):
            print('collisions')
        
        
        screen.fill((0,0,0))
        
        screen.blit(img,img_hitbox)
        pygame.draw.rect(screen, (100,0,0), white)
            

            
    
    pygame.display.update()

pygame.quit()