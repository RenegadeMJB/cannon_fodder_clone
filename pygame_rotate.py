import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Rectangle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Rectangle properties
rect_width, rect_height = 100, 50
rect_x = width // 2 - rect_width // 2
rect_y = height // 2 - rect_height // 2

# Rotation angle
angle = 0

#clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Rotate the rectangle
    rotated_rect = pygame.transform.rotate(pygame.Surface((rect_width, rect_height)), angle)
    rotated_rect_rect = rotated_rect.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))

    # Draw the rotated rectangle on the screen
    screen.blit(rotated_rect, rotated_rect_rect)

    # Update the screen
    pygame.display.flip()

    # Increment the rotation angle
    angle += 1
    clock.tick(3)
    if angle >= 360:
        angle = 0

'''import pygame

pygame.init()

screen = pygame.display.set_mode((100,100))
screen.fill((255,255,255))

surf = pygame.Surface((100,100))
surfRect = surf.get_rect()
surf.fill((255,255,255))

thing = pygame.Surface((10,10))
thingRect = thing.get_rect()
thing.fill((0,0,0))
thingRect.center = surfRect.center

clock = pygame.time.Clock()

angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(surf,(0,0))
    screen.blit(thing, (thingRect.left,thingRect.top))

    angle += 1
    if angle == 360:
        angle = 0

    thing = pygame.transform.rotate(thing,angle)
    clock.tick(3000)

    pygame.display.flip()

pygame.QUIT'''