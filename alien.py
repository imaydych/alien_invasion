import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for singe alien"""
    def __init__(self, ai_settings, screen):
        """Initialization of alien and setting possition"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Downloading image of alien and assigning rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every alien appears in left right corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving exact position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Entering alien to current position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Returns true if aline is on the screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Movind to the right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

