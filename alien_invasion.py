import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initializes the game and creates a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bg_color = (230, 230, 230)
    # Running the main game loop
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


run_game()