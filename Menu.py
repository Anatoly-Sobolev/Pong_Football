import pygame
import Consts

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)
        self.background = pygame.transform.scale(Consts.background, (Consts.screen_w, Consts.screen_h))

        # Основные пункты меню
        self.main_options = ["Start Game", "Settings", "Quit"]
        self.selected_main = 0

        # Подменю настроек
        self.settings_options = ["Player speed", "Ball speed", "Score to win", "Back"]
        self.selected_settings = 0
        self.in_settings = False

        # Режим редактирования параметра
        self.editing = False
        self.edit_index = -1

        # Ссылки на изменяемые константы (списки)
        self.player_speed = Consts.player_speed
        self.ball_speed = Consts.ball_speed
        self.score_to_win = Consts.game_over_score

        # Джойстик для навигации (если есть)
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        self.last_axis_move = 0  # для анти-дребезга

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        if not self.in_settings:
            # Главное меню
            for i, option in enumerate(self.main_options):
                color = (255, 255, 0) if i == self.selected_main else (255, 255, 255)
                text = self.font.render(option, True, color)
                rect = text.get_rect(center=(Consts.screen_w//2, Consts.screen_h//2 - 100 + i*100))
                self.screen.blit(text, rect)
        else:
            # Экран настроек
            title = self.font.render("Settings", True, (255, 255, 255))
            title_rect = title.get_rect(center=(Consts.screen_w//2, Consts.screen_h//4))
            self.screen.blit(title, title_rect)

            for i, option in enumerate(self.settings_options):
                y = Consts.screen_h//2 - 50 + i*70
                if i < 3:  # параметры
                    # Название
                    color = (255, 255, 0) if i == self.selected_settings and not self.editing else (255, 255, 255)
                    name_text = self.small_font.render(option, True, color)
                    name_rect = name_text.get_rect(midleft=(Consts.screen_w//4, y))
                    self.screen.blit(name_text, name_rect)

                    # Значение
                    if i == 0:
                        value = self.player_speed[0]
                    elif i == 1:
                        value = self.ball_speed[0]
                    else:
                        value = self.score_to_win[0]

                    if self.editing and i == self.edit_index:
                        val_color = (255, 255, 0)
                        val_text = self.small_font.render(f"< {value} >", True, val_color)
                    else:
                        val_color = (255, 255, 255)
                        val_text = self.small_font.render(str(value), True, val_color)

                    val_rect = val_text.get_rect(midright=(3*Consts.screen_w//4, y))
                    self.screen.blit(val_text, val_rect)
                else:  # пункт "Back"
                    color = (255, 255, 0) if i == self.selected_settings and not self.editing else (255, 255, 255)
                    back_text = self.small_font.render(option, True, color)
                    back_rect = back_text.get_rect(center=(Consts.screen_w//2, Consts.screen_h - 100))
                    self.screen.blit(back_text, back_rect)

        pygame.display.flip()

    def handle_event(self, event):
        # Клавиатура
        if event.type == pygame.KEYDOWN:
            if not self.in_settings:
                if event.key == pygame.K_UP:
                    self.selected_main = (self.selected_main - 1) % len(self.main_options)
                elif event.key == pygame.K_DOWN:
                    self.selected_main = (self.selected_main + 1) % len(self.main_options)
                elif event.key == pygame.K_RETURN:
                    return self.activate_main_option()
                elif event.key == pygame.K_ESCAPE:
                    return "quit"
            else:
                if self.editing:
                    if event.key == pygame.K_LEFT:
                        self.change_setting(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.change_setting(1)
                    elif event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        self.editing = False
                        self.edit_index = -1
                else:
                    if event.key == pygame.K_UP:
                        self.selected_settings = (self.selected_settings - 1) % len(self.settings_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_settings = (self.selected_settings + 1) % len(self.settings_options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_settings == 3:  # Back
                            self.in_settings = False
                        else:
                            self.editing = True
                            self.edit_index = self.selected_settings
                    elif event.key == pygame.K_ESCAPE:
                        self.in_settings = False

        # Джойстик
        if self.joystick:
            # Оси
            axis_x = self.joystick.get_axis(0)
            axis_y = self.joystick.get_axis(1)
            deadzone = 0.5

            if abs(axis_y) > deadzone and pygame.time.get_ticks() - self.last_axis_move > 200:
                self.last_axis_move = pygame.time.get_ticks()
                if axis_y < -deadzone:  # вверх
                    if not self.in_settings:
                        self.selected_main = (self.selected_main - 1) % len(self.main_options)
                    elif not self.editing:
                        self.selected_settings = (self.selected_settings - 1) % len(self.settings_options)
                elif axis_y > deadzone:  # вниз
                    if not self.in_settings:
                        self.selected_main = (self.selected_main + 1) % len(self.main_options)
                    elif not self.editing:
                        self.selected_settings = (self.selected_settings + 1) % len(self.settings_options)

            if self.in_settings and self.editing and abs(axis_x) > deadzone and pygame.time.get_ticks() - self.last_axis_move > 200:
                self.last_axis_move = pygame.time.get_ticks()
                if axis_x < -deadzone:
                    self.change_setting(-1)
                elif axis_x > deadzone:
                    self.change_setting(1)

            # Кнопки
            if event.type == pygame.JOYBUTTONDOWN and event.joy == 0:
                if event.button == 0:  # A (подтверждение)
                    if not self.in_settings:
                        return self.activate_main_option()
                    else:
                        if self.editing:
                            self.editing = False
                            self.edit_index = -1
                        else:
                            if self.selected_settings == 3:
                                self.in_settings = False
                            else:
                                self.editing = True
                                self.edit_index = self.selected_settings
                elif event.button == 1:  # B (отмена)
                    if self.in_settings:
                        if self.editing:
                            self.editing = False
                            self.edit_index = -1
                        else:
                            self.in_settings = False
                    else:
                        return "quit"

        return None

    def activate_main_option(self):
        if self.selected_main == 0:  # Start
            return "start"
        elif self.selected_main == 1:  # Settings
            self.in_settings = True
            self.selected_settings = 0
            self.editing = False
        elif self.selected_main == 2:  # Quit
            return "quit"
        return None

    def change_setting(self, delta):
        if self.edit_index == 0:  # player speed
            new = self.player_speed[0] + delta
            if 5 <= new <= 50:
                self.player_speed[0] = new
        elif self.edit_index == 1:  # ball speed
            new = self.ball_speed[0] + delta
            if 1 <= new <= 30:
                self.ball_speed[0] = new
        elif self.edit_index == 2:  # score to win
            new = self.score_to_win[0] + delta
            if 1 <= new <= 50:
                self.score_to_win[0] = new