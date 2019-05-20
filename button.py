import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialisation button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # assigning size and button details
        self.width, self.height = 200, 50
        self.button_color = (49, 51, 53)
        self.text_color = (194, 24, 7)
        self.font = pygame.font.SysFont(None, 48)

        # Building object rect button and setting up in the screen center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message appear only one time
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Changing msg into ractangel and setting up in the center"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Showing empty  button and message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)