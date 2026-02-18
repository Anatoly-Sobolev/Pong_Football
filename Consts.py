import pygame
import sys
import os

pygame.init()

# --- Функция для получения правильного пути (для разработки и для .exe) ---
def resource_path(relative_path):
    """Получает путь к ресурсу, работает и в режиме разработки, и в собранном .exe"""
    try:
        # PyInstaller создает временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Если мы не в собранном exe, то base_path - это папка проекта
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# ----------------------------------------------------------------------

ball_speed = 10
player_speed = 25
speed_x = ball_speed
speed_y = ball_speed * 8 // 10
paddle_speed = player_speed
info = pygame.display.Info()
screen_w, screen_h = info.current_w, info.current_h

# --- Загружаем ресурсы через нашу функцию resource_path ---
background = pygame.image.load(resource_path('images/background.png'))
caption = "FOOTBALL GAME!"
ball_size = 50
ball_image = pygame.image.load(resource_path('images/ball.png'))

paddle_w = 50
paddle_h = 180

blue_player_image = pygame.image.load(resource_path('images/blue_player.png'))
red_player_image = pygame.image.load(resource_path('images/red_player.png'))
size_player = 150
game_over_score = [10]  # Теперь это список, как вы сделали ранее
blue_goalkeeper_up = pygame.image.load(resource_path('images/blue_goalkeeper_up.png'))
blue_goalkeeper_down = pygame.image.load(resource_path('images/blue_goalkeeper_dawn.png')) # Убедитесь, что имя файла правильное (dawn или down?)
red_goalkeeper_up = pygame.image.load(resource_path('images/red_goalkeeper_up.png'))
red_goalkeeper_down = pygame.image.load(resource_path('images/red_goalkeeper_down.png'))
goal_right = pygame.image.load(resource_path("images/goal_right.png"))
goal_left = pygame.image.load(resource_path("images/goal_left.png"))

otstup = 40
goal_w = paddle_w + otstup

blue_player_data = (otstup + 20, screen_h//2, paddle_w, paddle_h)
red_player_data = (screen_w - otstup - paddle_w - 20, screen_h//2, paddle_w, paddle_h)

game_over_sound = pygame.mixer.Sound(resource_path('sounds/game_over.wav'))
game_over_sound.set_volume(0.4)
goal_sound = pygame.mixer.Sound(resource_path('sounds/whistle.wav'))
game_over_aplod = pygame.mixer.Sound(resource_path('sounds/game_over_aplod.wav'))

back_music = pygame.mixer.Sound(resource_path('sounds/back_music.wav'))
back_sounds = pygame.mixer.Sound(resource_path('sounds/back_sounds.wav'))
kick_sound = pygame.mixer.Sound(resource_path('sounds/kick.wav'))
# ---------------------------------------------------------