import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Ініціює корабель і задає початкову позицію"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Завантаження зображення корабля і отримання прямокутника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Кожен новий корабель зявляється в нижній частині екрану
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Збереження речової координати центра корабля
        self.center = float(self.rect.centerx)

        # Флаги переміщення
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Оновлює позицію корабля з врахуванням флага"""
        # Оновлюється атрибут center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Оновлення тарибута rect на основі self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Малює корабель в данній позиції"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """setting ship in the bottom center"""
        self.center = self.screen_rect.centerx