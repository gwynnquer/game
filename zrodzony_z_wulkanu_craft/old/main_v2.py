import pygame
import game_window_settings
import states.city as city
import player_settings


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player_kwiat.left_pressed = True
                    if event.key == pygame.K_d:
                        player_kwiat.right_pressed = True
                    if event.key == pygame.K_SPACE:
                        player_kwiat.space_pressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player_kwiat.left_pressed = False
                    if event.key == pygame.K_d:
                        player_kwiat.right_pressed = False
                    if event.key == pygame.K_SPACE:
                        player_kwiat.space_pressed = False

        if game_active:
            player_kwiat.update_movement()
            if player_kwiat.pass_right == True or player_kwiat.pass_left == True:
                city_khorinis.set_img(player_kwiat.get_possition())

            city_sprite.draw(screen.display)
            player_sprite.draw(screen.display)

            pygame.display.update()
            screen.clock.tick(60)

        else:
            screen.display.fill('Yellow')


if __name__ == "__main__":
    pygame.init()
    game_active = True

    screen = game_window_settings.main_game_window_settings()

    city_sprite = pygame.sprite.GroupSingle()
    city_khorinis = city.Khorinis()
    city_sprite.add(city_khorinis)

    player_sprite = pygame.sprite.GroupSingle()
    player_kwiat = player_settings.player_do_kwiat()
    player_sprite.add(player_kwiat)

    main_game_loop = game_loop()
