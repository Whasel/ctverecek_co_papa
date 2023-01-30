import random
import pygame
import sys

pygame.init()
speed = 5
OSA_X = 1920
OSA_Y = 1080
BLACK = (0, 0, 0)
GREY = (77,77,77)
GOLD = (255,215,0)
FPS = 60
main_cube = 50
smaller_cube = 25
big = 5
decrease_speed = 0.25
hodiny = pygame.time.Clock()
mc = pygame.Rect(512, 400, main_cube, main_cube) 

cubes = []
for i in range(15):
    rect = pygame.Rect(random.randint(25,1870), random.randint(25,1030), smaller_cube, smaller_cube)
    cubes.append(rect)

    

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
        mc.x += speed
    if keys[pygame.K_LEFT]:
        mc.x -= speed
    if keys[pygame.K_DOWN]:
        mc.y += speed
    if keys[pygame.K_UP]:
        mc.y -= speed

    if mc.x > OSA_X - main_cube:
        mc.x = OSA_X - main_cube
    if mc.y > OSA_Y - main_cube:
       mc.y = OSA_Y - main_cube
    if mc.x < 0:
        mc.x = 0
    if mc.y < 0:
        mc.y = 0
        
    for i in cubes:
        collide = pygame.Rect.colliderect(mc, i)
        if collide == True:
            cubes.remove(i)
            mc.height += big
            mc.width += big
            speed -= decrease_speed
        
    okno.fill(GREY)
    for cube in cubes:
       pygame.draw.rect(okno, GOLD, cube) 
    pygame.draw.rect(okno, BLACK, mc) 
    pygame.display.update()
