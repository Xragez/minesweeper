import pygame, time, sys
from colors import *
from default import *

# Number of blocks x and y
# Number of bombs
class InfoScreen:
    def __init__(self, game, x, y, width, height):
        """
        :param game: game object
        :param x: left upper side x coord
        :param y: left upper side y coord
        :param width: screen width
        :param height: screen height
        """
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.time_sec = 0
        self.time_min = 0
        self.freeze = False

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        """
        Draws button
        :param msg: text which will appear on the button
        :param x: x coord
        :param y: y coord
        :param w: width
        :param h: height
        :param ic: button color
        :param ac: action color (when cursor is on the button)
        :param action: Action
        :return:
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.game.screen, ac, (x, y, w, h))

            if click[0] == 1 and action is not None:
                exec(action)

        else:
            pygame.draw.rect(self.game.screen, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("timesnewroman", 20)
        textSurf = smallText.render(msg, True, BLACK_COLOR)
        textRect = textSurf.get_rect()
        textRect.center = ((x + (w // 2)), (y + (h // 2)))
        self.game.screen.blit(textSurf, textRect)

    def draw_background(self):
        """
        Draws background
        """
        pygame.draw.rect(self.game.screen, GREY_COLOR, pygame.Rect(self.x, self.y, self.width, self.height))

    def draw_timer(self):
        """
        Draws timer
        """
        pygame.draw.rect(self.game.screen, BLACK_COLOR, pygame.Rect(self.x + 60, self.y + 10, 60, 20))
        font = pygame.font.SysFont("timesnewroman", 20, bold=True)
        font_color = YELLOW_COLOR
        if not self.freeze:
            self.time_sec = int(time.time() - self.game.time_start) - self.time_min * 60
            if self.time_sec >= 60:
                self.time_sec = 0
                self.time_min += 1
        timer_text = str(self.time_min) + ":" + str(self.time_sec)
        text = font.render(str(timer_text), True, font_color)
        textRect = text.get_rect()
        textRect.center = (self.x + 90, self.y + 20)
        self.game.screen.blit(text, textRect)

    def freeze_time(self):
        """
        For freezing timer
        :return:
        """
        self.freeze = True

    def draw(self):
        """
        Draws Info screen with timer, bomb counter and buttons
        """
        button_width = 100
        middle_x = self.x + self.width // 2 - button_width // 2
        self.draw_background()
        self.draw_timer()
        self.button("Restart", middle_x, self.y + 50, button_width, 30,
                    LIGHT_GREY_COLOR, WHITE_COLOR, "self.game.restart_game()")
        self.button("Settings", middle_x, self.y + 340, button_width, 30,
                    LIGHT_GREY_COLOR, WHITE_COLOR, 'self.game.menu_screen.on_button_click()')
        self.button("EXIT", middle_x, self.y + 380, button_width, 30,
                    LIGHT_GREY_COLOR, WHITE_COLOR, 'sys.exit(0)')
        self.end_msg()
        self.bomb_counter()

    def bomb_counter(self):
        """
        Shows how many bombs are left
        """
        smallText = pygame.font.SysFont("timesnewroman", 20)
        textSurf = smallText.render("Bombs: " + str(+self.game.game_screen.bomb_flag_counter), True, RED_COLOR)
        textRect = textSurf.get_rect()
        textRect.center = (self.x + self.width // 2, self.y + self.height // 3)
        self.game.screen.blit(textSurf, textRect)

    def end_msg(self):
        """
        Draws end message (You Win or Game Over)
        """
        msg = ''
        if self.game.win == 1:
            msg = "You Win"
        elif self.game.win == 0:
            msg = "Game Over"

        smallText = pygame.font.SysFont("timesnewroman", 20)
        textSurf = smallText.render(msg, True, RED_COLOR)
        textRect = textSurf.get_rect()
        textRect.center = (self.x + self.width // 2, self.y + self.height // 4)
        self.game.screen.blit(textSurf, textRect)


class MenuScreen(InfoScreen):

    def __init__(self, game, x, y, width, height):
        """

        :param game: game object
        :param x: left upper side x coord
        :param y: left upper side y coord
        :param width: screen width
        :param height: screen height
        """
        super().__init__(game, x, y, width, height)
        self.screen = game.screen
        self.bw = TextArea(self.screen, x + 20, y + 20, 40, 30, str(self.game.bw))
        self.bh = TextArea(self.screen, x + 20, y + 60, 40, 30, str(self.game.bh))
        self.nob = TextArea(self.screen, x + 20, y + 100, 40, 30, str(self.game.num_of_bombs))

    def on_button_click(self):
        self.game.show_menu = True
        self.bw.text = str(self.game.bw)
        self.bh.text = str(self.game.bh)
        self.nob.text = str(self.game.num_of_bombs)
        self.bw.draw(self.screen)
        self.bh.draw(self.screen)
        self.nob.draw(self.screen)

    def draw(self):
        """
        Draws menu screen
        """
        self.draw_background()
        button_width = 100
        middle_x = self.x + self.width // 2 - button_width // 2
        self.button("Back", middle_x, self.y + 340, button_width, 30,
                    LIGHT_GREY_COLOR, WHITE_COLOR, 'self.game.show_menu = False')
        self.button("Apply", middle_x, self.y + 380, button_width, 30,
                    LIGHT_GREY_COLOR, WHITE_COLOR, 'self.game.apply_settings()')
        self.bw.draw(self.screen)
        self.bh.draw(self.screen)
        self.nob.draw(self.screen)

    def text_events(self, event):
        self.bw.events(event)
        self.bh.events(event)
        self.nob.events(event)

class TextArea:
    def __init__(self, screen, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = LIGHT_GREY_COLOR
        self.text_color = BLACK_COLOR
        self.active = False
        self.screen = screen
        self.font = pygame.font.SysFont("timesnewroman", 20)
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.last_key = None
        self.max_signs = 3

    def getText(self):
        return self.text

    def draw(self, screen):
        self.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        self.txt_surface = self.font.render(self.text, True, self.text_color)

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = RED_COLOR if self.active else LIGHT_GREY_COLOR
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    pygame.time.wait(150)
                else:
                    key = event.unicode
                    if (not key == self.last_key) and len(self.text) < self.max_signs:
                        self.text += event.unicode
                    self.last_key = event.unicode
                self.txt_surface = self.font.render(self.text, True, self.text_color)
        if event.type == pygame.KEYUP:
            self.last_key = None
