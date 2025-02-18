import pygame
from nanobot import NanoBot  # Import the NanoBot class

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement")
# Create character instance
FPS=60
clock=pygame.time.Clock()


# Game loop
# Main game loop - Displaying Player
nanobot_laser_group = pygame.sprite.Group()

nanobot_group = pygame.sprite.Group()
nanobot = NanoBot(nanobot_laser_group)
nanobot_group.add(nanobot)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       

    screen.fill((0, 0, 0))  # Clear the screen before drawing

    # Update and draw the player
    nanobot_group.update(event)
    nanobot_group.draw(screen)

    nanobot_laser_group.update()
    nanobot_laser_group.draw(screen)
    
    
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
