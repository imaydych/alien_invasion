import sys, pygame
import ship
from bullet import Bullet
from alien import Alien
from time import sleep

def get_number_aliens_x(ai_settings, alien_width):
    """"Calculate number of aliens in the row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculation of number of rows on the screen"""
    available_space_y = (ai_settings.screen_height -
                         (16 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creation of aliens fleet"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Creation of aliens fleet"""
    # Creation of an alien and calculating quantity of an aliens in the row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Creation of aliens fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                     row_number)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагує на натискання клавіш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Send bullets if maximum did not met"""
    # Creating of new bullet and adding it to group bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb,  play_button, ship, aliens,
                 bullets):
    """Обробка натисків клавіатурі і миші"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Starting new game after press Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Drop of game settings
        ai_settings.initialize_dynamic_settings()
        # Hide mouse cursor
        pygame.mouse.set_visible(False)
        # Drop of statistics
        stats.reset_stats()
        stats.game_active = True
        # Drop of score and level image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        #cleaning up bullets and aliens
        aliens.empty()
        bullets.empty()
        # Creating new ship and setting it up in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship,  aliens, bullets,
                  play_button):
    """Оновлює зображення на екрані і відображає новий екран"""
    # Прикаждом переходе цыкла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # All bullets getting off behind image of ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Show score
    sb.show_score()
    # Button Play showing in case if game is not active
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованого экрана
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship,  aliens, bullets):
    """Updating bullets positions and deleting old bullets"""
    # Updating bullets positions
    bullets.update()
    # Deleting bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_alien_collisions(ai_settings, screen, stats,sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # checking hits to aliens
    # deleting aline and bullet after hit
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # if whole fleet is distroed - starts new level
        bullets.empty()
        ai_settings.increase_speed()
        # increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(ai_settings, aliens):
    """Reacting on reaching screen edge by alien"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """lower fleet and changes direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats,screen,ship,aliens, bullets):
    """Working with aliens-ship hit"""
    if stats.ships_left > 0:
        # Decreasing of ship_left
        stats.ships_left -= 1
        #deleting list of aliens and bullets
        aliens.empty()
        bullets.empty()
        # Creation of new fleet and ship in the center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    """Checking if new high score appear"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checking if aliens get to the bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Happening the same as we have with hit aliens-ship
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship,  aliens, bullets):
    """
    Checking of the edge is met by fleet and
    update fleets position
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Checking alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # checking of aliens who get to the bottom of screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)