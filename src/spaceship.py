import pygame

class Spaceship():

    def __init__(self, game_settings, screen):
        """Initialize the spaceship and set its starting position."""
        self.screen = screen
        self.game_settings = game_settings

        # MOVING FLAGS
        self.moving_right = False
        self.moving_left = False

        # Load the spaceship image and get its rect.
        self.image = pygame.image.load('assets/images/Spaceship.bmp')

        #resizing the image
        original_width, original_height = self.image.get_size()
        scale_factor = 0.07  # Adjust this for how much smaller or larger you want
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        self.image = pygame.transform.scale(self.image, (new_width, new_height))


        # Put invisible rectangle around the image - to help us find where the ship is on the screen
        self.rect = self.image.get_rect()
        # Gets the edges of the screen
        self.screen_rect = screen.get_rect()

        # Start each new spaceship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the spaceship's center.
        self.center = float(self.rect.centerx)



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.spaceship_factor_speed
        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.game_settings.spaceship_factor_speed

        self.rect.centerx = self.center

    def center_spaceship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

