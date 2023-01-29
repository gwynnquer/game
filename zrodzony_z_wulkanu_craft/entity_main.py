import pygame
import game_window_settings


class Entity(pygame.sprite.Sprite):
    DEFAULT_IMAGE_HIGHT = 141
    DEFAULT_IMAGE_WIDTH = 100
    GRAVITY = 1

    def __init__(self, hp, ac, dmg, speed, jump, image):
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.speed = speed
        self.jump = jump
        self.image = pygame.transform.smoothscale(
            pygame.image.load(image).convert_alpha(), (self.DEFAULT_IMAGE_WIDTH, self.DEFAULT_IMAGE_HIGHT))
        self.rect = self.image.get_rect()

        self.pass_left = False
        self.pass_right = False

        super().__init__()

    def movement_limit(self):
        self.pass_left = False
        self.pass_right = False

        if self.rect.bottom >= game_window_settings.MainWindow.HEIGHT + 10:
            self.rect.bottom = game_window_settings.MainWindow.HEIGHT
        if self.rect.left > game_window_settings.MainWindow.WIDTH + 10:
            self.rect.right = 0
            self.pass_left = True
        if self.rect.right < -10:
            self.rect.left = game_window_settings.MainWindow.WIDTH
            self.pass_right = True

        # def load_image(self):
        #     image_raw = pygame.image.load(self.image).convert_alpha()
        #     default_image = pygame.transform.smoothscale(
        #         image_raw, (self.DEFAULT_IMAGE_HIGHT, self.DEFAULT_IMAGE_WIDTH))
        #     default_rect = default_image.get_rect(midbottom=(
        #         self.DEFAULT_IMAGE_HIGHT, self.DEFAULT_IMAGE_WIDTH))
