import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # creation of button Play
    play_button = Button(ai_settings, screen, "Play")
    #creation of exemplar for saving game statistics
    # Creation exemplar for Gamestats and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen, stats)
    # Creation of ship, bullet group and aliens group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Creation of alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Запуск основного цыкла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship,  aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()