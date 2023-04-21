import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import random

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
PlaySurf = pygame.Surface((3/4*SCREEN_WIDTH,3/4*SCREEN_HEIGHT))
PlaySurf.fill((170,230,255))
PlaySurfRect = PlaySurf.get_rect()
StatsSurf = pygame.Surface((SCREEN_WIDTH/4,3*SCREEN_HEIGHT/4))
StatsSurf.fill((0,0,255))
StatsSurfRect = StatsSurf.get_rect()
MenuSurf = pygame.Surface((SCREEN_WIDTH/4, SCREEN_HEIGHT/4))
MenuSurf.fill((255,0,0))
MenuSurfRect = MenuSurf.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

    def setCoords(self,x,y):
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

        if self.rect.left <= SCREEN_WIDTH/4:
            self.rect.move_ip(5,0)
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.move_ip(-5,0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.Surface(10,10)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(PlaySurfRect.left, PlaySurfRect.right),
                5,
            )
        )


player = Player()
player.setCoords(PlaySurfRect.centerx,PlaySurfRect.bottom)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pressed_keys= pygame.key.get_pressed()
    print(pressed_keys[K_RIGHT])

    player.update(pressed_keys)

    screen.fill((0,255,0))

    screen.blit(PlaySurf, (SCREEN_WIDTH/4,0))
    screen.blit(StatsSurf, (0,0))
    screen.blit(MenuSurf, (0, 3*SCREEN_HEIGHT/4))


    screen.blit(player.surf, player.rect)

    pygame.display.flip()

pygame.quit()