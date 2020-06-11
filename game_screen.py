import random
import pygame
from default import *
from colors import *
from block import Block


class GameScreen:
    def __init__(self, game, bombs, width, height, block_size=25):
        """
        :param game: game object
        :param bombs: number of bombs
        :param width: board width
        :param height: board height
        :param block_size: size of single block
        """
        self.game = game
        self.bw = game.bw
        self.bh = game.bh
        self.block_size = block_size
        self.num_of_bombs = bombs
        self.width = self.bw * (self.block_size + 2) + 20
        self.height = self.bh * (self.block_size + 2) + 20
        self.board_width = width
        self.board_height = height
        self.game_net = [[Block(game.screen, block_size) for i in range(self.bh)]
                         for j in range(self.bw)]
        x = (self.board_width - self.width) // 2 + 10
        y = (self.board_height - self.height) // 2 + 10
        for i in range(self.bw):
            for j in range(self.bh):
                self.game_net[i][j].x = x
                self.game_net[i][j].y = y
                self.game_net[i][j].bw = i
                self.game_net[i][j].bh = j
                y += self.game_net[i][j].size + 2
            y = (self.board_height - self.height) // 2 + 10
            x += self.game_net[i][j].size + 2
            self.bomb_set = None
        self.place_bombs()
        self.bomb_flag_counter = game.num_of_bombs

    def draw(self):
        """
        Draws game board
        """
        pass
        self.draw_background()
        for i in range(self.bw):
            for j in range(self.bh):
                self.game_net[i][j].draw()

    def draw_background(self):
        """
        Draws background for the board
        """
        x0 = (self.board_width - self.width) // 2
        y0 = (self.board_height - self.height) // 2
        pygame.draw.rect(self.game.screen, LIGHT_GREY_COLOR, pygame.Rect(x0, y0, self.width, self.height))

    def neighbours_list(self, block):
        """
        Returns a list of adjacent blocks
        :param block: block
        :return: list of adjacent blocks
        """
        i = block.bw
        j = block.bh
        list = []
        for a in range(i - 1, i + 2, 1):
            for b in range(j - 1, j + 2, 1):
                if ((a >= 0 and a <= (self.bw - 1)) and
                        (b >= 0 and b <= (self.bh - 1)) and
                        (a != i or b != j)):
                    list.append((a, b))
        return list

    def board_reveal(self, block):
        block.reveal()
        nlist = self.neighbours_list(block)
        if not self.count_bombs(nlist, block):
            for x, y in nlist:
                if self.game_net[x][y].status == 0:
                    self.board_reveal(self.game_net[x][y])

    def count_bombs(self, nlist, block):
        """
        Counts adjacent bombs
        :param nlist: list of adjacent blocks
        :param block: block
        :return: number of adjacent bombs
        """
        bombs = 0
        for b, a in nlist:
            if self.game_net[b][a].isBomb:
                bombs += 1
        block.neighbours = bombs
        return bombs

    def place_bombs(self):
        """
        Places bombs in random positions
        """
        bombs_set = set()
        while len(bombs_set) < self.num_of_bombs:
            bombs_set.add((random.randrange(0, self.bw), random.randrange(0, self.bh)))
        self.bomb_set = bombs_set.copy()
        for x, y in bombs_set:
            self.game_net[x][y].isBomb = True

    def coords(self, coordinates):
        """
        :param coordinates: mouse position
        :return: x, y coords in number of blocks,
        (-1, -1) if outside of the board
        """
        x, y = coordinates
        for i in range(self.bw):
            for j in range(self.bh):
                if ((coordinates[0] >= self.game_net[i][j].x)
                        and (coordinates[1] >= self.game_net[i][j].y)
                        and (coordinates[0] <= self.game_net[i][j].x + self.block_size)
                        and (coordinates[1] <= self.game_net[i][j].y + self.block_size)):
                    return i, j
        else:
            return -1, -1

    def block_on_click(self):
        """
        Checks on which block is the mouse cursor,
        if there's a bomb in this block then game is over,
        if not then the block is being revealed
        :return: False when there is no bomb on that block
                 True when there is a bomb
        """
        coordinates = pygame.mouse.get_pos()
        i, j = self.coords(coordinates)
        if not (i, j) == (-1, -1):
            if self.game_net[i][j].status == 0:
                if self.game_net[i][j].isBomb:
                    return True
                self.board_reveal(self.game_net[i][j])
            return False

    def on_right_click(self):
        """
        Handles bomb flag
        :return: False when there are hidden bombs left
                 True when all bombs have been found
        """
        coordinates = pygame.mouse.get_pos()
        i, j = self.coords(coordinates)
        if not (i, j) == (-1, -1):
            if self.game_net[i][j].status == 2:
                self.bomb_flag_counter += 1
                self.game_net[i][j].set_maybe_flag()
                if self.game_net[i][j].isBomb:
                    self.bomb_set.add((i, j))
            elif self.game_net[i][j].status == 3:
                self.game_net[i][j].reset_status()
            elif self.bomb_flag_counter > 0:
                if self.game_net[i][j].status == 0:
                    self.game_net[i][j].set_bomb_flag()
                    self.bomb_flag_counter -= 1
                    if self.game_net[i][j].isBomb:
                        self.bomb_set.remove((i, j))
        return self.check_bombs()

    def check_bombs(self):
        """
        CHecks if all bombs have been found
        :return: False when there are hidden bombs left
                 True when all bombs have been found
        """
        if len(self.bomb_set) == 0:
            return True
        for i in range(self.bw):
            for j in range(self.bh):
                if not (self.game_net[i][j].isBomb or self.game_net[i][j].status == 1):
                    return False
        return True
