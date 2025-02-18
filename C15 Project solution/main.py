import pygame
from paddle import Paddle
from ball import Ball

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paddle and Ball")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)

# Create sprite groups
paddle_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

# Create paddle and ball objects
paddle = Paddle(WINDOW_WIDTH, WINDOW_HEIGHT)
ball = Ball(WINDOW_WIDTH, WINDOW_HEIGHT)

# Add objects to their respective groups
paddle_group.add(paddle)
ball_group.add(ball)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass the event to the paddle's update method
        paddle.update(event)

    # Update
    ball_group.update()


    # Draw everything
    display_surface.fill(BLACK)
    paddle_group.draw(display_surface)
    ball_group.draw(display_surface)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

# End the game
pygame.quit()