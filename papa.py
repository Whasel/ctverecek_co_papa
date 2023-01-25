import random
import pygame

pygame.init()
speed = 5
OSA_X = 1024
OSA_Y = 800
BLACK = (0, 0, 0)
GREY = (77,77,77)
GOLD = (255,215,0)
FPS = 60
main_cube = 50
smaller_cube = 25

hodiny = pygame.time.Clock()

main_x = (OSA_X - main_cube) / 2
main_y = (OSA_Y - main_cube) / 2
sc_x = (OSA_X - smaller_cube) - random.randint(1,OSA_X - smaller_cube)
sc_y = (OSA_Y - smaller_cube) - random.randint(1,OSA_Y - smaller_cube)
sc2_x = (OSA_X - smaller_cube) - random.randint(1,OSA_X - smaller_cube)
sc2_y = (OSA_Y - smaller_cube) - random.randint(1,OSA_Y - smaller_cube)
sc3_x = (OSA_X - smaller_cube) - random.randint(1,OSA_X - smaller_cube)
sc3_y = (OSA_Y - smaller_cube) - random.randint(1,OSA_Y - smaller_cube)
sc4_x = (OSA_X - smaller_cube) - random.randint(1,OSA_X - smaller_cube)
sc4_y = (OSA_Y - smaller_cube) - random.randint(1,OSA_Y - smaller_cube)


okno = pygame.display.set_mode((OSA_X, OSA_Y))
pygame.display.set_caption('čtvereček co papá')

okno = pygame.display.set_mode((OSA_X, OSA_Y))

while True:
    hodiny.tick(FPS)
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

    if main_x > OSA_X - main_cube:
        main_x = OSA_X - main_cube
    if main_y > OSA_Y - main_cube:
        main_y = OSA_Y - main_cube
    if main_x < 0:
        main_x = 0
    if main_y < 0:
        main_y = 0  
    if main_x == sc_x:
        main_cube += 10
        speed /= 1.1
    elif main_y == sc_y:
        main_cube += 10
        speed /= 1.1
    if main_x == sc2_x:
        main_cube += 10
        speed /= 1.1
    elif main_y == sc2_y:
        main_cube += 10
        speed /= 1.1
    if main_x == sc3_x:
        main_cube += 100
        speed /= 1.1
    elif main_y == sc3_y:
        main_cube += 10
        speed /= 1.1
    if main_x == sc4_x:
        main_cube += 10
        speed /= 1.1
    elif main_y == sc4_y:
        main_cube += 10
        speed /= 1.1
    
    

        
        
    okno.fill(GREY)
    pygame.draw.rect(okno, GOLD, (sc_x, sc_y, smaller_cube, smaller_cube))
    pygame.draw.rect(okno, GOLD, (sc2_x, sc2_y, smaller_cube, smaller_cube))
    pygame.draw.rect(okno, GOLD, (sc3_x, sc3_y, smaller_cube, smaller_cube))
    pygame.draw.rect(okno, GOLD, (sc4_x, sc4_y, smaller_cube, smaller_cube))
    pygame.draw.rect(okno, BLACK, (main_x, main_y, main_cube, main_cube))  
    pygame.display.update()
