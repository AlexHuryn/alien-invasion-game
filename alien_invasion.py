import sys
import pygame
from settings import Settings


def run_game():
    # Initializes the game and creates a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    # Running the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill(ai_settings.bg_color)
                sys.exit()
        pygame.display.flip()


run_game()