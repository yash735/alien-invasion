import pygame
from settings import Settings
from spaceship import Spaceship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
    # Create an instance to store game statistics.
    stats = GameStats(game_settings)
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # Caption of the action
    pygame.display.set_caption("Alien Invasion")
    # Make a spaceship
    spaceship = Spaceship(game_settings, screen)
    bullets = Group()
    # Make an Alien
    aliens = Group()

    gf.create_fleet(game_settings, screen, spaceship, aliens)


    while True:
        gf.check_events(game_settings, screen, spaceship, bullets)

        if stats.game_active:
            spaceship.update()
            gf.update_bullets(game_settings, screen, spaceship, aliens, bullets) 
            gf.update_aliens(game_settings, stats, screen, spaceship, aliens, bullets)
            gf.update_screen(game_settings, screen, spaceship, aliens, bullets)

run_game()

