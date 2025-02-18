import pygame
from nano_laser import Nanobot_Laser
WIDTH, HEIGHT = 800, 600

class NanoBot(pygame.sprite.Sprite):
    def __init__(self,laser_group):
        super().__init__()
        """Initialize the player"""
        self.image = pygame.image.load("SA1/nanobot.png")  # Replace with your image path
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize if needed
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH // 2)
        self.rect.bottom = HEIGHT
        self.velocity = 15
        self.laser_group=laser_group
        self.lives = 5
        self.velocity = 8

       

    def update(self, event):
        """Update the player movement based on key press"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.velocity

    def fire(self):
        """Handle firing lasers"""
        pass
       