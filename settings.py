class Settings:
    """ Клас для збереження налаштувань Alien invasion."""

    def __init__(self):
        """Initialisation of static game settings"""
        # Параметри екрану
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Параметри куль
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 194,24,7
        self.bullets_allowed = 3

        # Alien ship settings
        self.fleet_drop_speed = 10
        # Game acceleration rate
        self.speedup_scale = 1.1
        # Alien value acceleration
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialization of chengable settings in game"""
        self.ship_speed_factor = 1.1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet direction = 1 - move to the right: -1 move to the left
        self.fleet_direction = 0.1
        self.alien_points = 50

    def increase_speed(self):
        """Increase settings of speed and score"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)