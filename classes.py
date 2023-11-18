import pygame

screen = pygame.display.set_mode((800,800))

rect1 = pygame.Rect(100,100,100,100)
image = pygame.image.load('rectangle.png')

run = True
while run:

    pygame.draw.rect(screen, (255,0,0), rect1)
    screen.blit(image, (400,400), rect1)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.flip()

pygame.quit()