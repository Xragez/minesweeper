import pygame, sys
from block import Block
from colors import *
from game_screen import GameScreen
import time

B_WIDTH, B_HEIGHT = 15, 15 # Game board size in blocks
W_WIDTH, W_HEIGHT = 600, 425  # Window size
BOARD_WIDTH, BOARD_HEIGHT = 425, 425  # Board size
INFO_WIDTH, INFO_HEIGHT = 175, 425
NUM_OF_BOMBS = 20  # Number of bombs
LEFT = 1
RIGHT = 3


class InfoScreen:
    def __init__(self, game, x, y, width, height):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.time_sec = 0
        self.time_min = 0
        self.freeze = False

    def button(self, msg, x, y, w, h, ic, ac, action=None):
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
        pygame.draw.rect(self.game.screen, GREY_COLOR, pygame.Rect(self.x, self.y, self.width, self.height))

    def draw_timer(self):

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
        self.freeze = True

    def draw(self):
        button_width = 100
        middle_x = self.x + self.width//2 - button_width//2
        self.draw_background()
        self.draw_timer()
        self.button("Restart", middle_x, self.y + 50, button_width, 30,
                    LIGHT_GREY_COLOR, WHITE_COLOR, "self.game.restart_game()")
        self.button("Settings", middle_x, self.y + 320, button_width, 30, LIGHT_GREY_COLOR, WHITE_COLOR)
        self.button("EXIT", middle_x, self.y + 380, button_width, 30, LIGHT_GREY_COLOR, WHITE_COLOR, 'sys.exit(0)')
        self.end_msg()
        self.bomb_counter()
    def bomb_counter(self):
        smallText = pygame.font.SysFont("timesnewroman", 20)
        textSurf = smallText.render("Bombs: " + str(+self.game.game_screen.bomb_flag_counter), True, RED_COLOR)
        textRect = textSurf.get_rect()
        textRect.center = (self.x + self.width // 2, self.y + self.height // 3)
        self.game.screen.blit(textSurf, textRect)

    def end_msg(self):
        msg = ''
        if self.game.win == 1:
            msg = "You Win"
        elif self.game.win == 0:
            msg = "Game Over"

        smallText = pygame.font.SysFont("timesnewroman", 20)
        textSurf = smallText.render(msg, True, RED_COLOR)
        textRect = textSurf.get_rect()
        textRect.center = (self.x + self.width//2, self.y + self.height//4)
        self.game.screen.blit(textSurf, textRect)

class Game:

    def __init__(self):
        self.tps_max = 2.0
        self.bw = B_WIDTH
        self.bh = B_HEIGHT
        self.width = W_WIDTH
        self.height = W_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.num_of_bombs = NUM_OF_BOMBS
        self.game_screen = GameScreen(self, self.num_of_bombs, BOARD_WIDTH, BOARD_HEIGHT)
        self.info_screen = InfoScreen(self, BOARD_WIDTH, 0, INFO_WIDTH, INFO_HEIGHT)
        self.clock = pygame.time.Clock()
        self.timer_sec = 0
        self.time_start = time.time()
        self.restart = False
        self.freeze = False
        self.win = -1

    def run(self):
        """
        Main loop
        """

        cheat_code = ['x', 'y', 'z', 'z', 'y']
        key_queue = []
        self.draw()
        while not self.restart:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key_queue.append(event.unicode)
                    if len(key_queue) >= 6:
                        key_queue.pop(0)
                    if key_queue == cheat_code:
                        self.xyzzy()
                if (event.type == pygame.QUIT or
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    sys.exit(0)
                if not self.freeze:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                        if self.game_screen.block_on_click():
                            self.win = 0
                            self.game_over()
                        elif self.game_screen.check_bombs():
                            self.win = 1
                            self.game_over()
                        self.draw()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                        if self.game_screen.on_right_click():
                            self.win = 1
                            self.game_over()
                        self.draw()

            self.draw_info()
            pygame.display.flip()

    def restart_game(self):
        self.restart = True

    def draw(self):
        self.game_screen.draw()

    def draw_info(self):
        self.info_screen.draw()

    def game_over(self):
        self.info_screen.freeze_time()
        self.freeze = True
        for x in range(B_WIDTH):
            for y in range(B_HEIGHT):
                self.game_screen.game_net[x][y].boom()
        self.over = True

    def xyzzy(self):
        for x in range(B_WIDTH):
            for y in range(B_HEIGHT):
                self.game_screen.game_net[x][y].cheats_enabled = True
        self.draw()

def main():
    while True:
        pygame.init()
        pygame.display.set_caption('Minesweeper')
        game = Game()
        game.run()
        del game



if __name__ == "__main__":
    main()
