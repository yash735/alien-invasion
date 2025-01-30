class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = ((179, 180, 175))
        self.spaceship_factor_speed = 1

        # Bullet settings - 1, 3, 15
        self.bullet_speed_factor = 1   
        self.bullet_width = 3           
        self.bullet_height = 15
        self.bullet_color = 247, 2, 2

        #limiting bullets to promote accurate shooting
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed_factor = 0.25
        self.fleet_drop_speed = 25
        self.fleet_direction = 1

        #spaceship settings
        self.spaceship_limit = 3

