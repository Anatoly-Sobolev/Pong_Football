import pygame
import sys
from Screen import Screen
from Ball import Ball
from Player import Player
import Consts
from Menu import Menu

def run_game():
    # Останавливаем все звуки перед стартом игры (на случай, если они играли в меню)
    pygame.mixer.stop()

    game_display = Screen()
    ball = Ball()
    red_player = Player(Consts.red_player_data, 'red', pygame.K_UP, pygame.K_DOWN,
                        Consts.red_goalkeeper_up, Consts.red_goalkeeper_down)
    blue_player = Player(Consts.blue_player_data, 'blue', pygame.K_w, pygame.K_s,
                         Consts.blue_goalkeeper_up, Consts.blue_goalkeeper_down)

    # Подключаем джойстики
    if pygame.joystick.get_count() > 0:
        blue_player.joystick = pygame.joystick.Joystick(0)
        blue_player.joystick.init()
    if pygame.joystick.get_count() > 1:
        red_player.joystick = pygame.joystick.Joystick(1)
        red_player.joystick.init()

    clock = pygame.time.Clock()
    Consts.back_music.play(loops=-1)
    Consts.back_sounds.play(loops=-1)

    def handle_joysticks():
        if blue_player.joystick:
            val = blue_player.joystick.get_axis(blue_player.axis)
            if val < -blue_player.deadzone:
                blue_player.speed_y = -Consts.paddle_speed[0]
                blue_player.image = blue_player.image_up
            elif val > blue_player.deadzone:
                blue_player.speed_y = Consts.paddle_speed[0]
                blue_player.image = blue_player.image_down
            else:
                blue_player.speed_y = 0
        if red_player.joystick:
            val = red_player.joystick.get_axis(red_player.axis)
            if val < -red_player.deadzone:
                red_player.speed_y = -Consts.paddle_speed[0]
                red_player.image = red_player.image_up
            elif val > red_player.deadzone:
                red_player.speed_y = Consts.paddle_speed[0]
                red_player.image = red_player.image_down
            else:
                red_player.speed_y = 0

    while True:
        game_display.screen.blit(game_display.image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.stop()
                return "menu"
            red_player.check_push(event)
            blue_player.check_push(event)

        handle_joysticks()
        game_display.draw(ball, blue_player, red_player)

        if red_player.score == Consts.game_over_score[0] or blue_player.score == Consts.game_over_score[0]:
            game_display.game_over(red_player, blue_player, ball)
            pygame.mixer.stop()  # останавливаем звуки после показа победителя
            return "menu"

        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pygame.joystick.init()
    screen = pygame.display.set_mode((Consts.screen_w, Consts.screen_h))
    pygame.display.set_caption(Consts.caption)

    menu = Menu(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            result = menu.handle_event(event)
            if result == "start":
                outcome = run_game()
                if outcome == "quit":
                    running = False
            elif result == "quit":
                running = False
        menu.draw()
        pygame.time.wait(10)

    pygame.quit()
    sys.exit()