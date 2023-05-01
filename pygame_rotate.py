import pygame

pygame.init()

screen = pygame.display.set_mode(100,100)
screen.fill((255,255,255))

surf = pygame.Surface((100,100))
surfRect = surf.get_rect()
surf.fill((255,255,255))

thing = pygame.Surface((10,10))
thingRect = thing.get_rect()
thing.fill((0,0,0))
thingRect.center = surfRect.center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(surf,(0,0))
    screen.blit(thing, thingRect.center)

    pygame.display.flip()

pygame.QUIT