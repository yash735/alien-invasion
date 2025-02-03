class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = ((179, 180, 175))

        # Bullet settings - 1, 3, 15
        self.bullet_speed_factor = 1   
        self.bullet_width = 3          
        self.bullet_height = 15
        self.bullet_color = 247, 2, 2

        # Spaceship settings
        self.spaceship_limit = 3
        self.spaceship_factor_speed = 1

        # Limiting bullets to promote accurate shooting
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.25
        self.fleet_drop_speed = 25
        self.fleet_direction = 1
        self.alien_points = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Score scale as each level gets harder
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.spaceship_factor_speed = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.25

        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Alien Points
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.spaceship_factor_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    





