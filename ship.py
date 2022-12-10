import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its initial position"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Loading an image of a ship and getting a rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)


