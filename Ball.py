import pygame
import random

from Consts import *
from Teammate import Teammate

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(screen_w//2, screen_h//2, ball_size, ball_size)
        self.image = pygame.transform.scale(ball_image, (ball_size, ball_size))
        self.last_tuch = None
        self.lst_of_teammate = []
        self.speed_x = speed_x
        self.speed_y = speed_y





    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def refration(self):
        if self.rect.right > screen_w: self.speed_x *= -1
        if self.rect.left < 0: self.speed_x *= -1

        if self.rect.y < 0: self.speed_y *= -1
        if self.rect.bottom > screen_h: self.speed_y *= -1

    def check_colisions(self, blue_player, red_player):
        if self.rect.right >= screen_w:
            blue_player.score += 1
            self.start_position()
            self.lst_of_teammate = []
            goal_sound.play()
            pygame.time.wait(1000)


        if self.rect.left<= 0:
            red_player.score += 1
            self.start_position()
            self.lst_of_teammate = []
            goal_sound.play()
            pygame.time.wait(1000)





        if self.rect.colliderect(blue_player.rect):
            kick_sound.play()
            self.rect.left = blue_player.rect.right + 1
            self.speed_x *= -1


            self.last_tuch = blue_player.color
            new_teammate = Teammate('blue', blue_player_image)
            self.lst_of_teammate.append(new_teammate)

        if self.rect.colliderect(red_player.rect):
            kick_sound.play()
            self.rect.right = red_player.rect.left - 1
            self.speed_x *= -1
            self.last_tuch = red_player.color
            new_teammate = Teammate('red', red_player_image)
            self.lst_of_teammate.append(new_teammate)

        if 0 < self.speed_x < 15 or self.speed_x > 40: self.speed_x = 30
        if -6 < self.speed_x < 0 or self.speed_x < -25: self.speed_x = -30
        if 0 < self.speed_y < 15 or self.speed_y > 30: self.speed_y = 25
        if -30 < self.speed_y < 0 or self.speed_y < -20: self.speed_y = -25


        if self.speed_x == 0 or self.speed_y == 0:
            goal_sound.play()
            pygame.time.wait(1000)
            self.start_position()

    def start_position(self):
        self.rect.center = (screen_w//2, screen_h//2)
        self.speed_x = random.choice([-1, 1]) * speed_x
        self.speed_y = random.choice([-1, 1]) * speed_y


    def check_push_players(self):
        for player in self.lst_of_teammate:
            if self.rect.colliderect(player.rect) and player.color != self.last_tuch:
                kick_sound.play()
                self.speed_x += random.choice([-2, 2])
                self.speed_y *= random.choice([-2, 2])
                self.speed_x *= -1
                self.speed_y *= random.choice([-1, 1])
                self.last_tuch = player.color
                self.lst_of_teammate.remove(player)