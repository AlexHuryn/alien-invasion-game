class Settings():
    """Class to store all Alien Invasion game settings"""
    def __init__(self):
        """Initializes game settings"""
        # Screen Options
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60