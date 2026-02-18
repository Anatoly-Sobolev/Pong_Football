import pygame
import sys
from Screen import Screen
from Ball import Ball
from Player import Player
from Consts import *

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.joystick.init()

    game_display = Screen()
    ball = Ball()
    red_player = Player(red_player_data, 'red', pygame.K_UP, pygame.K_DOWN,
                        red_goalkeeper_up, red_goalkeeper_down)
    blue_player = Player(blue_player_data, 'blue', pygame.K_w, pygame.K_s,
                         blue_goalkeeper_up, blue_goalkeeper_down)


    if pygame.joystick.get_count() > 0:
        blue_player.joystick = pygame.joystick.Joystick(0)
        blue_player.joystick.init()
        print(f"Джойстик для синего: {blue_player.joystick.get_name()}")
    if pygame.joystick.get_count() > 1:
        red_player.joystick = pygame.joystick.Joystick(1)
        red_player.joystick.init()
        print(f"Джойстик для красного: {red_player.joystick.get_name()}")

    clock = pygame.time.Clock()
    back_music.play(loops=-1)
    back_sounds.play(loops=-1)


    def handle_joysticks():
        # Синий игрок
        if blue_player.joystick:
            val = blue_player.joystick.get_axis(blue_player.axis)
            if val < -blue_player.deadzone:
                blue_player.speed_y = -paddle_speed
                blue_player.image = blue_player.image_up
            elif val > blue_player.deadzone:
                blue_player.speed_y = paddle_speed
                blue_player.image = blue_player.image_down
            else:
                blue_player.speed_y = 0
        # Красный игрок
        if red_player.joystick:
            val = red_player.joystick.get_axis(red_player.axis)
            if val < -red_player.deadzone:
                red_player.speed_y = -paddle_speed
                red_player.image = red_player.image_up
            elif val > red_player.deadzone:
                red_player.speed_y = paddle_speed
                red_player.image = red_player.image_down
            else:
                red_player.speed_y = 0

    while True:
        game_display.screen.blit(game_display.image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            red_player.check_push(event)
            blue_player.check_push(event)


        handle_joysticks()

        game_display.draw(ball, blue_player, red_player)
        game_display.game_over(blue_player, red_player, ball)
        clock.tick(60)
        pygame.display.update()


