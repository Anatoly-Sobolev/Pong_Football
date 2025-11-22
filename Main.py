import pygame
import sys

from Screen import Screen
from Ball import Ball
from Player import Player
from Consts import *

pygame.init()
pygame.mixer.init()


game_display = Screen()
ball = Ball()
red_player = Player(red_player_data, 'red', pygame.K_UP, pygame.K_DOWN, red_goalkeeper_up, red_goalkeeper_down)
blue_player = Player(blue_player_data, 'blue', pygame.K_w, pygame.K_s, blue_goalkeeper_up, blue_goalkeeper_down)
clock = pygame.time.Clock()
back_music.play(loops=-1)
back_sounds.play(loops=-1)

while True:
    game_display.screen.blit(game_display.image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        red_player.check_push(event)
        blue_player.check_push(event)

    game_display.draw(ball, blue_player, red_player)
    game_display.game_over(blue_player, red_player)
    clock.tick(60)
    


    pygame.display.update()


