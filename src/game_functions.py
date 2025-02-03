import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(game_settings, screen, stats, sb, play_button, spaceship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_q:
            save_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event, game_settings, screen, spaceship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, sb, play_button, spaceship, aliens, bullets, mouse_x, mouse_y)


def check_keydown_events(event, game_settings, screen, spaceship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = True
    elif event.key == pygame.K_LEFT:
        spaceship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Fire bullets
        fire_bullets(game_settings, screen, spaceship, bullets)

def check_keyup_events(event, spaceship ):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    elif event.key == pygame.K_LEFT:
        spaceship.moving_left = False
            


def fire_bullets(game_settings, screen, spaceship, bullets ):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, spaceship)
        bullets.add(new_bullet)


def update_bullets(game_settings, screen, stats, sb, spaceship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""

    #Update Position of bullet
    bullets.update()

    #Remove bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_collisions_fleet(game_settings, screen, stats, sb, spaceship, bullets, aliens)



def check_collisions_fleet(game_settings, screen, stats, sb, spaceship, bullets, aliens):
    """Check for any bullets that have hit aliens. If all aliens are gone, create a new fleet"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            sb.prep_score()

        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy exsisting bullets and create new fleet
        bullets.empty()
        game_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(game_settings, screen, spaceship, aliens)




def update_screen(game_settings, screen, stats, sb, spaceship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(game_settings.bg_color)
    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    spaceship.blitme()
    aliens.draw(screen)
    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_aliens_x(game_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = game_settings.screen_width - (5 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(game_settings, spaceship_height, alien_height):

    avalable_space_y = game_settings.screen_height - (spaceship_height) - (6 * alien_height)
    number_rows = int(avalable_space_y / (2 * alien_height))
    return number_rows

def create_fleet(game_settings, screen, spaceship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(game_settings, alien_width)
    number_rows = get_number_rows(game_settings, spaceship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
             create_alien(game_settings, screen, aliens, alien_number, row_number)



def update_aliens(game_settings, screen, stats, sb, spaceship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    """

    check_fleet_edges(game_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(spaceship, aliens):
        spaceship_down(game_settings, screen, stats, sb, spaceship, aliens, bullets)
    
    check_aliens_bottom(game_settings, screen, stats, sb, spaceship, aliens, bullets)


    


def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed

    game_settings.fleet_direction *= -1


def spaceship_down(game_settings, screen, stats, sb, spaceship, aliens, bullets):
    """Respond to spaceship being hit by alien."""
    # Decrement spaceship.
    if stats.spaceship_left > 0:
        stats.spaceship_left -= 1

        # Update scoreboard.
        sb.prep_spaceships()

        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the spaceship.
        create_fleet(game_settings, screen, spaceship, aliens)
        spaceship.center_spaceship()

        # Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    


def check_aliens_bottom(game_settings, screen, stats, sb, spaceship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            spaceship_down(game_settings, screen, stats, sb, spaceship, aliens, bullets)
            break


def check_play_button(game_settings, screen, stats, sb, play_button, spaceship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        ## Reset the game settings.
        game_settings.initialize_dynamic_settings()

        # Hide the game Cursor
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_images()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fellet and center the ship
        create_fleet(game_settings, screen, spaceship, aliens)
        spaceship.center_spaceship()
        

def check_high_score(stats, sb):
    """Check to see if there is a new hight score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def save_high_score(stats):
    """Saving all the high scores to a file"""
    filename = "highscore.txt"
    with open(filename, 'w') as fileobj:
        fileobj.write(str(stats.high_score))
