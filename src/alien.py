import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen =  screen
        self.game_settings = game_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("assets/images/alien.bmp")

        #resizing the image
        original_width, original_height = self.image.get_size()
        scale_factor = 0.08  # Adjust this for how much smaller or larger you want
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        self.image = pygame.transform.scale(self.image, (new_width, new_height))


        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

