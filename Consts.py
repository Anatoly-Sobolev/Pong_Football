import pygame
pygame.init()



ball_speed = 25
player_speed = 40




speed_x = ball_speed
speed_y = ball_speed * 8 // 10
paddle_speed = player_speed
info = pygame.display.Info()
screen_w, screen_h = info.current_w, info.current_h

background = pygame.image.load('images/background.png')
caption = "FOOTBALL GAME!"
ball_size = 50
ball_image = pygame.image.load('images/ball.png')

paddle_w = 50
paddle_h = 180

blue_player_image = pygame.image.load('images/blue_player.png')
red_player_image = pygame.image.load('images/red_player.png')
size_player = 150
game_over_score = 3
blue_goalkeeper_up = pygame.image.load('images/blue_goalkeeper_up.png')
blue_goalkeeper_down = pygame.image.load('images/blue_goalkeeper_dawn.png')
red_goalkeeper_up = pygame.image.load('images/red_goalkeeper_up.png')
red_goalkeeper_down = pygame.image.load('images/red_goalkeeper_down.png')
goal_right = pygame.image.load("images/goal_right.png")
goal_left = pygame.image.load("images/goal_left.png")

otstup = 40
goal_w = paddle_w + otstup



blue_player_data = (otstup + 20, screen_h//2, paddle_w, paddle_h)
red_player_data = (screen_w - otstup - paddle_w - 20, screen_h//2, paddle_w, paddle_h)

game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
game_over_sound.set_volume(0.4)
goal_sound = pygame.mixer.Sound('sounds/whistle.wav')
game_over_aplod = pygame.mixer.Sound('sounds/game_over_aplod.wav')

back_music = pygame.mixer.Sound('sounds/back_music.wav')
back_sounds = pygame.mixer.Sound('sounds/back_sounds.wav')
kick_sound = pygame.mixer.Sound('sounds/kick.wav')

