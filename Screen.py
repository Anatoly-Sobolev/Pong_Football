import pygame
from Consts import *
import sys


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.image = pygame.transform.scale(background, (screen_w, screen_h))
        pygame.display.set_caption(caption)
        self.font = pygame.font.Font(None, 150)
        self.goal_left = pygame.transform.scale(goal_left, (goal_w, screen_h))
        self.goal_right = pygame.transform.scale(goal_right, (goal_w, screen_h))

    def draw_players(self, ball):
        for player in ball.lst_of_teammate:
            player.draw(self.screen)


    def draw(self, ball, blue_player, red_player):
        ball.move()
        ball.refration()
        ball.check_colisions(blue_player, red_player)
        ball.check_push_players()

        red_player.draw(self.screen)
        blue_player.draw(self.screen)

        blue_player.move()
        red_player.move()

        self.draw_goals()
        self.draw_players(ball)
        self.show_score(blue_player, red_player)
        ball.draw(self.screen)
        self.draw_goals()


    def show_score(self, blue_player, red_player):
        player1_score_surface = self.font.render(str(blue_player.score), True, 'black')
        player2_score_surface = self.font.render(str(red_player.score), True, 'black')

        self.screen.blit(player1_score_surface, (screen_w / 4, 20))
        self.screen.blit(player2_score_surface, (3 * screen_w / 4, 20))

    def game_over(self, red_player, blue_player):
        if red_player.score == game_over_score or blue_player.score == game_over_score:
            pygame.mixer.stop()

            text_game_over = f'{['RED', 'BLUE'][red_player.score == game_over_score]} PLAYER WIN'
            font = pygame.font.Font(None, 150)
            text_surface = font.render(text_game_over, True, ['RED', 'BLUE'][red_player.score == game_over_score])
            text_rect = text_surface.get_rect()
            text_rect.center = (screen_w // 2, screen_h // 2)
            self.screen.blit(text_surface, text_rect)


            pygame.display.update()
            game_over_sound.play()
            game_over_aplod.play()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()


    def draw_goals(self):
        self.screen.blit(self.goal_left, (0, 0))
        self.screen.blit(self.goal_right, (screen_w-goal_w, 0))