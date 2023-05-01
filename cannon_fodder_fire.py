import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT
)

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDBULLET = pygame.USEREVENT + 1

playSurf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
playSurf.fill((170,230,255))
playSurfRect = playSurf.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        self.color = (0,0,0)
        self.surf = pygame.Surface((50,25))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        #pos[0] is the left coordinate passed to the bullet
        self.rect.left = pos[0]
        #pos[1] is the bottom coordinate passed to the bullet
        self.rect.bottom = pos[1]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        self.color = (0,0,0)
        self.angle = 0
        self.surf = pygame.Surface((10,10))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        #pos[0] is the left coordinate passed to the bullet
        self.rect.left = pos[0]
        #pos[1] is the bottom coordinate passed to the bullet
        self.rect.bottom = pos[1]


        


player = Player([200,playSurfRect.bottom])

bullet = Bullet([player.rect.right,player.rect.top])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()

    screen.blit(playSurf,(0,0))
    screen.blit(player.surf, player.rect)
    screen.blit(bullet.surf, bullet.rect)

    pygame.display.flip()

pygame.quit()
