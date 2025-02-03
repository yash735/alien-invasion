import pygame
import game_functions as gf

class GameStats():

    def __init__(self, game_settings):
        """Track statistics for Alien Invasion."""
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = False
        # High score should never be reset.
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.spaceship_left = self.game_settings.spaceship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """Getting high score from file"""

        filename = 'highscore.txt'
        try:
            with open(filename, 'r') as fileobj:
                high_score = fileobj.read()
                return int(high_score)
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0

