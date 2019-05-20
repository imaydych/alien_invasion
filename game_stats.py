class GameStats():
    """Statistics for Alien Ivasion"""

    def __init__(self, ai_settings):
        """Initialisation of statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Game Alien Invasion starts in not active mode
        self.game_active = False
        # Don't drop the record
        self.high_score = 0

    def reset_stats(self):
        """Initialisation of statistic which change along the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
