import pygame
from entity_main import Entity
import game_window_settings


class Player(Entity):
    def __init__(self, name, hp, ac, dmg, speed, jump, image):
        self.name = name
        super().__init__(hp, ac, dmg, speed, jump, image)

        self.vel_x = 0
        self.vel_y = 0

        self.rect.y = 400
        self.rect.x = 400

        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False

        self.pos_index = 4

    def update_movement(self):
        self.vel_x = 0

        if self.left_pressed and not self.right_pressed:
            self.vel_x = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.vel_x = self.speed
        if self.space_pressed and self.rect.bottom == game_window_settings.MainWindow.HEIGHT:
            self.vel_y = -self.jump
            self.space_pressed = False
        if not self.space_pressed:
            self.apply_gravity()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        Entity.movement_limit(self)

    def apply_gravity(self):
        self.vel_y += self.GRAVITY

    def get_possition(self):
        if self.pass_left == True:
            self.pos_index += 1
            if self.pos_index >= 7:
                self.pos_index = 7
        if self.pass_right == True:
            self.pos_index -= 1
            if self.pos_index <= 0:
                self.pos_index = 0

        return self.pos_index


def player_do_kwiat():
    name = 'ZRODZONY Z WULKANU'
    hp = 100
    ac = 16
    dmg = 12
    speed = 5
    jump = 21
    image = 'graphics\characters\kwiat.png'

    player = Player(name=name, hp=hp, ac=ac, dmg=dmg,
                    speed=speed, jump=jump, image=image)

    return player
