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

    def draw(self, screen):
        screen.blit(self.image, self.rect)
