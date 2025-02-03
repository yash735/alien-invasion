import pygame
from settings import Settings
from spaceship import Spaceship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    # Create an instance to store game statistics.
    stats = GameStats(game_settings)
    # Create an instance to store game statistics and create a scoreboard.
    sb = Scoreboard(game_settings, screen, stats)
    # msg = "PLAY"
    play_button = Button(game_settings, screen, "PLAY")
    # Caption of the action
    pygame.display.set_caption("Alien Invasion")
    # Make a spaceship
    spaceship = Spaceship(game_settings, screen)
    # Bullets
    bullets = Group()
    # Make an Alien
    aliens = Group()

    gf.create_fleet(game_settings, screen, spaceship, aliens)


    while True:
        gf.check_events(game_settings, screen, stats, sb, play_button, spaceship, aliens, bullets)

        if stats.game_active:
            spaceship.update()
            gf.update_bullets(game_settings, screen, stats, sb, spaceship, aliens, bullets) 
            gf.update_aliens(game_settings, screen, stats, sb, spaceship, aliens, bullets)

        gf.update_screen(game_settings, screen, stats, sb, spaceship, aliens, bullets, play_button)

run_game()

