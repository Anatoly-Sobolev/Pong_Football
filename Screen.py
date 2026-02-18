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

    '''def game_over(self, red_player, blue_player, ball):
        if red_player.score == game_over_score or blue_player.score == game_over_score:
            pygame.mixer.stop()

            winner = 'RED' if red_player.score == game_over_score else 'BLUE'
            text_game_over = f'{winner} PLAYER WIN'
            font = pygame.font.Font(None, 150)
            text_surface = font.render(text_game_over, True, winner)
            text_rect = text_surface.get_rect()
            text_rect.center = (screen_w // 2, screen_h // 2)
            self.screen.blit(text_surface, text_rect)

            pygame.display.update()
            game_over_sound.play()
            game_over_aplod.play()
            pygame.time.wait(5000)

            self.reset_game(blue_player, red_player, ball)

            back_music.play(loops=-1)
            back_sounds.play(loops=-1)'''

    def game_over(self, red_player, blue_player, ball):
        if red_player.score == game_over_score[0] or blue_player.score == game_over_score[0]:
            pygame.mixer.stop()
            winner = 'RED' if red_player.score == game_over_score[0] else 'BLUE'
            text_game_over = f'{winner} PLAYER WIN'
            font = pygame.font.Font(None, 150)
            text_surface = font.render(text_game_over, True, winner)
            text_rect = text_surface.get_rect()
            text_rect.center = (screen_w // 2, screen_h // 2)
            self.screen.blit(text_surface, text_rect)

            pygame.display.update()
            game_over_sound.play()
            game_over_aplod.play()
            pygame.time.wait(5000)  # после паузы просто возвращаемся в меню

    def reset_game(self, blue_player, red_player, ball):

        blue_player.score = 0
        red_player.score = 0

        ball.start_position()
        ball.lst_of_teammate.clear()
        ball.last_tuch = None


        blue_player.rect.y = screen_h // 2
        red_player.rect.y = screen_h // 2


        blue_player.speed_y = 0
        red_player.speed_y = 0


        blue_player.image = blue_player.image_up
        red_player.image = red_player.image_up

    def draw_goals(self):
        self.screen.blit(self.goal_left, (0, 0))
        self.screen.blit(self.goal_right, (screen_w - goal_w, 0))