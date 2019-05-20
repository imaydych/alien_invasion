import pygame.font
class Scoreboard():
    """Class for showing game information"""
    def __init__(self, ai_settings, screen, stats):
        """Initialization of score count attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Settings of font for scores
        self.text_color = (194, 24, 7)
        self.font = pygame.font.SysFont(None, 38)
        # Preparing of initial scores images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Changing current text into image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color,
                                            self.ai_settings.bg_color)
        # Showing score in the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Changing current score into image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
                                             True,
                            self.text_color, self.ai_settings.bg_color)
        # High score in the top of screen
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Moving score, level and ships to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_level(self):
        """Changing level into image"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                             self.text_color, self.ai_settings.bg_color)

        # Level shows under the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
