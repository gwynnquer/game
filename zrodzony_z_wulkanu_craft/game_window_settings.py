import pygame


class MainWindow():
    WIDTH = 960
    HEIGHT = 540
    WIDTH_2 = WIDTH / 2
    HEIGHT_2 = HEIGHT / 2
    ICON_X = 32
    ICON_Y = 32
    FONT_SIZE = 25

    def __init__(self, icon, font, caption, image=None):
        self.icon = icon
        self.font = pygame.font.Font(font, self.FONT_SIZE)
        self.caption = pygame.display.set_caption(caption)
        self.image = image
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

    def program_icon(self):
        raw_icon = pygame.image.load(self.icon).convert_alpha()
        transformed_icon = pygame.transform.smoothscale(
            raw_icon, (self.ICON_X, self.ICON_Y))
        display_icon = pygame.display.set_icon(transformed_icon)


def main_game_window_settings():
    icon = 'graphics\icon.png'
    font = 'font\Tickerbit-mono.otf'
    caption = 'ZRODZONY_Z_WULKANU_CRAFT_V2'

    screen = MainWindow(icon=icon, font=font, caption=caption)
    screen.program_icon()

    return screen


print(MainWindow.WIDTH)
