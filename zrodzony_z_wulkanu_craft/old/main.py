from turtle import up
import pygame
from sys import exit
import city


def display_score():
    current_time = round((pygame.time.get_ticks() - start_time)/1000)
    score_surf = font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    pygame.draw.rect(screen, 'White', score_rect)
    screen.blit(score_surf, score_rect)


def kwiat_animation():
    global kwiat_surf, kwiat_index
    kwiat_index += 0.1
    if kwiat_index >= len(kwiat_walk):
        kwiat_index = 0
    kwiat_surf = kwiat_walk[int(kwiat_index)]


pygame.init()
d_x = 800
d_y = 400
screen = pygame.display.set_mode((d_x, d_y))
pygame.display.set_caption('ZRODZONY Z WULKANU CRAFT')
clock = pygame.time.Clock()
font = pygame.font.Font('font\Tickerbit-mono.otf', 25)
icon_raw = pygame.image.load(
    'graphics\icon.png').convert_alpha()
game_active = True
start_time = 0
icon_final = pygame.transform.smoothscale(icon_raw, (32, 32))
pygame.display.set_icon(icon_final)
Khorinis = pygame.sprite.GroupSingle()
num_sprit = 3
Khorinis.add(city.Khorinis(num_sprit))

# pygame.mixer.init()
# pygame.mixer.music.load("music\danheim2.mp3")
# pygame.mixer.music.set_volume(0.05)
# pygame.mixer.music.play()


org_kwiat = pygame.image.load(
    'graphics\characters\kwiat.png').convert_alpha()
kwiat_small = pygame.transform.smoothscale(org_kwiat, (100, 141))
org_dasher = pygame.image.load(
    'graphics\characters\dasher.png').convert_alpha()
dasher_small = pygame.transform.smoothscale(org_dasher, (50, 71))

text_surface1 = font.render('.....', False, 'Black')
text_surface2 = font.render('kwiecie...', False, 'Black')
text_surface3 = font.render('DAJ MI SPOKÓJ', False, 'Black')

kwiat1 = pygame.transform.rotozoom(kwiat_small, 10, 1).convert_alpha()
kwiat2 = pygame.transform.rotozoom(kwiat_small, -10, 1).convert_alpha()
kwiat_index = 0
kwiat_walk = [kwiat1, kwiat2]

kwiat_surf = kwiat_walk[kwiat_index]
kwiat_rect = kwiat_surf.get_rect(midbottom=(150, 400))

dasher_rect = dasher_small.get_rect(midbottom=(650, 400))

kwiat_gravity = 0
kwiat_movement = 0

moveLeft = False
moveRight = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and kwiat_rect.rect.bottom == 400:
                    kwiat_gravity = -21
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moveLeft = True
                if event.key == pygame.K_d:
                    moveRight = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moveLeft = False
                if event.key == pygame.K_d:
                    moveRight = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                kwiat_rect.left = 0
                start_time = pygame.time.get_ticks()

    if game_active:
        # backgroundsssss
        x = 0
        Khorinis.draw(screen)
        display_score()
        # Kwiat
        kwiat_gravity += 0.8
        kwiat_rect.y += kwiat_gravity
        if kwiat_rect.bottom >= 400:
            kwiat_rect.bottom = 400
        if kwiat_rect.left > 810:
            kwiat_rect.right = 0
            while num_sprit > 0:
                num_sprit += 1
                Khorinis.add(city.Khorinis(num_sprit))
        if kwiat_rect.right < -10:
            kwiat_rect.left = 800
            while num_sprit < 8:
                num_sprit += 1
                Khorinis.add(city.Khorinis(num_sprit))
        if moveLeft == True:
            kwiat_rect.x -= 5
        if moveRight == True:
            kwiat_rect.x += 5
        kwiat_animation()
        screen.blit(kwiat_surf, kwiat_rect)

        # Dasher
        screen.blit(dasher_small, dasher_rect)

        # if kwiat_rect.colliderect(dasher_rect):
        #     game_active = False
    else:
        screen.fill('Yellow')
        # screen.blit(text_surface2, text2_rect)
        # screen.blit(text_surface3, text3_rect)
        # Teksty
        # pygame.draw.rect(screen, 'White', text_rect)
        # pygame.draw.rect(screen, 'Black', text_rect, 2)
        # screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(60)
