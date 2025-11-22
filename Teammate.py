import pygame
import random

from Consts import *

class Teammate:
    def __init__(self, color, image):
        self.rect = pygame.Rect(random.randint(size_player, screen_w - 2 * size_player),
                                random.randint(ball_size, screen_h - size_player),
                                size_player, size_player)
        self.image = pygame.transform.scale(image, (size_player, size_player))
        self.color = color
        self.speed_x = random.choice([5, -5, 10, -10])
        self.speed_y = random.choice([5, -5, 10, -10])

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > screen_w - paddle_w * 5: self.speed_x *= -1
        if self.rect.left < paddle_w * 5: self.speed_x *= -1

        if self.rect.top < paddle_w: self.speed_y *= -1
        if self.rect.bottom > screen_h - paddle_w: self.speed_y *= -1

    def draw(self, screen):
        self.move()
        screen.blit(self.image, self.rect)


