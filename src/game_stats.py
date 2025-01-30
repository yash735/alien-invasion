import pygame

class GameStats():

    def __init__(self, game_settings):
        """Track statistics for Alien Invasion."""
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.spaceship_left = self.game_settings.spaceship_limit
