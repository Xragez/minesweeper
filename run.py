import os

import pygame, sys
from info_screen import MenuScreen
from info_screen import InfoScreen
from game_screen import GameScreen
import time

W_WIDTH, W_HEIGHT = 600, 425  # Window size
BOARD_WIDTH, BOARD_HEIGHT = 425, 425  # Board size
INFO_WIDTH, INFO_HEIGHT = 175, 425  # info and menu size
LEFT = 1
RIGHT = 3

class FileLoadErrorException(Exception):
    pass

class Game:

    def __init__(self):
        self.load_settings()
        self.tps_max = 2.0
        self.bw = B_WIDTH
        self.bh = B_HEIGHT
        self.width = W_WIDTH
        self.height = W_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.num_of_bombs = NUM_OF_BOMBS
        self.game_screen = GameScreen(self, self.num_of_bombs, BOARD_WIDTH, BOARD_HEIGHT)
        self.info_screen = InfoScreen(self, BOARD_WIDTH, 0, INFO_WIDTH, INFO_HEIGHT)
        self.menu_screen = MenuScreen(self, BOARD_WIDTH, 0, INFO_WIDTH, INFO_HEIGHT)
        self.show_menu = False
        self.clock = pygame.time.Clock()
        self.timer_sec = 0
        self.time_start = time.time()
        self.restart = False
        self.freeze = False
        self.win = -1  # 0 - lose, 1 - win, -1 - default

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
                        keys = pygame.key.get_pressed()
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
            if self.show_menu:
                self.menu_screen.text_events(event)
                self.draw_menu()
            else:
                self.draw_info()
            pygame.display.flip()

    def restart_game(self):
        """
        Stops main loop and resets game
        """
        self.restart = True
        global B_HEIGHT
        B_HEIGHT = 10

    def draw(self):
        """
        Draw game board
        """
        self.game_screen.draw()

    def draw_info(self):
        """
        Draws info screen
        """
        self.info_screen.draw()

    def draw_menu(self):
        """
        Draws menu screen
        """
        self.menu_screen.draw()

    def game_over(self):
        """
        Freezes game board and time, reveals al bombs
        """
        self.info_screen.freeze_time()
        self.freeze = True
        for x in range(B_WIDTH):
            for y in range(B_HEIGHT):
                self.game_screen.game_net[x][y].boom()

    def xyzzy(self):
        """
        Reveals all bombs locations with dark grey color
        """
        for x in range(B_WIDTH):
            for y in range(B_HEIGHT):
                self.game_screen.game_net[x][y].cheats_enabled = True
        self.draw()

    def load_settings(self):
        try:
            if not os.path.isfile("settings.csv"):
                raise FileLoadErrorException
            with open('settings.csv') as cfg:
                data = cfg.readlines()
                for line in data:
                    setting = line.split(" = ")
                    print(setting[0], " - ", setting[1])
                    if setting[0] =='B_WIDTH':
                        global B_WIDTH
                        B_WIDTH = int(setting[1])
                    if setting[0] =='B_HEIGHT':
                        global B_HEIGHT
                        B_HEIGHT = int(setting[1])
                    if setting[0] == 'NUM_OF_BOMBS':
                        global NUM_OF_BOMBS
                        NUM_OF_BOMBS = int(setting[1])
        except FileLoadErrorException:
            print("Can't find configuration file. Default settings loaded.")

    def apply_settings(self):
        self.bw = self.menu_screen.bw.getText()
        self.bh = self.menu_screen.bh.getText()
        self.num_of_bombs = self.menu_screen.nob.getText()
        self.save_settings()
        self.restart_game()

    def save_settings(self):
        with open('settings.csv', 'w') as cfg:
            print(self.num_of_bombs)
            cfg.write(f'B_WIDTH = {self.bw}\n'
                      f'B_HEIGHT = {self.bh}\n'
                      f'NUM_OF_BOMBS = {self.num_of_bombs}')


def main():
    while True:
        pygame.init()
        pygame.display.set_caption('Minesweeper')
        game = Game()
        game.run()
        del game


if __name__ == "__main__":
    main()
