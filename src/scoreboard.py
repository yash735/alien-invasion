import pygame.font
from pygame.sprite import Group
from spaceship import Spaceship

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, game_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (225, 225, 225)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_spaceships()


    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """Turn the level into a rendered image."""
        level_no = str(self.stats.level)
        self.level_no_image = self.font.render(level_no, True, self.text_color, self.game_settings.bg_color)

        # Put the level on the left most part of the screen.
        self.level_no_rect = self.level_no_image.get_rect()
        self.level_no_rect.right = self.score_rect.right
        self.level_no_rect.bottom = self.score_rect.bottom + 40

    def prep_spaceships(self):
        """Show how many ships are left."""
        self.spaceships = Group()
        for spaceship_number in range(self.stats.spaceship_left):
            spaceship = Spaceship(self.game_settings, self.screen)
            spaceship.rect.x = 10 + spaceship_number * spaceship.rect.width
            spaceship.rect.y = 10
            self.spaceships.add(spaceship)


    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_no_image, self.level_no_rect)

        # Draw ships.
        self.spaceships.draw(self.screen)

    
    def prep_images(self):
        """Preping initial score Images"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_spaceships()
