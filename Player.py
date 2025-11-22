import pygame
from Consts import *

class Player:
    def __init__(self, data, color, key_up, key_down, image_up ,image_down):
        self.rect = pygame.Rect(*data)
        self.key_up = key_up
        self.key_down = key_down
        self.color = color
        self.speed_y = 0
        self.score = 0
        self.image_up = pygame.transform.scale(image_up, (paddle_w, paddle_h))
        self.image_down = pygame.transform.scale(image_down, (paddle_w, paddle_h))
        self.image = pygame.transform.scale(image_up, (paddle_w, paddle_h))



    def draw(self, screen, ):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.y += self.speed_y
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > screen_h: self.rect.bottom = screen_h

    def check_push(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed_y = -1 *  paddle_speed
                self.image = self.image_up
            if event.key == self.key_down:
                self.speed_y = paddle_speed
                self.image = self.image_down

        if event.type == pygame.KEYUP:
            if event.key == self.key_up or event.key == self.key_down:
                self.speed_y = 0