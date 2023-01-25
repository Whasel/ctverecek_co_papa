import random
import pygame

pygame.init()

OSA_X = 1024
OSA_Y = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255,215,0)
speed = 0.5
main_cube = 50
smaller_cube = 25

main_x = (OSA_X - main_cube) / 2
main_y = (OSA_Y - main_cube) / 2

okno = pygame.display.set_mode((OSA_X, OSA_Y))
pygame.display.set_caption('čtvereček co papá')

okno = pygame.display.set_mode((OSA_X, OSA_Y))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_RIGHT]:
        main_x += speed
    if keys[pygame.K_LEFT]:
        main_x -= speed
    if keys[pygame.K_DOWN]:
        main_y += speed
    if keys[pygame.K_UP]:
        main_y -= speed
    if keys[pygame.K_SPACE] == True:
        speed = 2
    if keys[pygame.K_SPACE] == False:
        speed = 0.5
    if main_x > OSA_X - main_cube:
        main_x = OSA_X - main_cube
    if main_y > OSA_Y - main_cube:
        main_y = OSA_Y - main_cube
    if main_x < 0:
        main_x = 0
    if main_y < 0:
        main_y = 0  
        
    okno.fill(WHITE)
    pygame.draw.rect(okno, BLACK, (main_x, main_y, main_cube, main_cube))  
    pygame.display.update()
