import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас для керування кулями, випущенеми кораблем"""
    def __init__(self, ai_settings, screen, ship):
        """Створює обєкт кулі в данній позиції корабля"""
        super().__init__()
        self.screen = screen

        # Створення кулі в позиції (0, 0) і призначення правильної позиції
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиція кулі зберігається в реччовому форматі
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Переміща кулю вверх по екрану"""
        # Оновлює позицію кулі в дробовому форматі
        self.y -= self.speed_factor
    # оновлення позиції прямокутника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вивід кулі на екран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
