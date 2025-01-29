import pygame
from settings import Settings
from spaceship import Spaceship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
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
        spaceship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(game_settings, aliens)
        gf.update_screen(game_settings, screen, spaceship, aliens, bullets)

run_game()

