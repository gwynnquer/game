import pygame
import game_window_settings


class Khorinis(pygame.sprite.Sprite):

    Khorinis_images = [
        'graphics\lokacje\_brama.png',
        'graphics\lokacje\kurt.png',
        'graphics\lokacje\_targ.png',
        'graphics\lokacje\gailen.png',
        'graphics\lokacje\gildia.png',
        'graphics\lokacje\kuznia.png',
        'graphics\lokacje\straz.png',
        'graphics\lokacje\mlyn.png'
    ]
    d_x = game_window_settings.MainWindow.WIDTH
    d_y = game_window_settings.MainWindow.HEIGHT
    check_index = 4

    def __init__(self, index=0):
        super().__init__()
        self.set_img(index)

    def set_img(self, index):
        self.check_index = index
        self.image = pygame.image.load(
            self.Khorinis_images[index]).convert_alpha()
        self.transform = pygame.transform.smoothscale(
            self.image, (self.d_x, self.d_y))
        # pygame.image.save(self.transform, 'graphics\lokacje\gailen2.png')
        self.image = self.transform
        self.rect = self.transform.get_rect(topleft=(0, 0))
