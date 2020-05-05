import random
import pygame
from block import Block
LIGHT_GREY_COLOR = (200, 200, 200)
class GameScreen:
    def __init__(self, game, bombs, block_size=25):
        x = 10
        y = 10
        self.game = game
        self.bw = game.bw
        self.bh = game.bh
        self.block_size = block_size
        self.num_of_bombs = bombs
        self.width = self.bw * (self.block_size + 2) + 20
        self.height = self.bh * (self.block_size + 2) + 20
        self.game_net = [[Block(game.screen, block_size) for i in range(self.bw)] for j in range(self.bh)]
        for i in range(self.bw):
            for j in range(self.bh):
                self.game_net[i][j].x = x
                self.game_net[i][j].y = y
                self.game_net[i][j].bw = i
                self.game_net[i][j].bh = j
                y += self.game_net[i][j].size + 2
            y = 10
            x += self.game_net[i][j].size + 2
        self.place_bombs()
    def draw(self):
        '''
        Draws game board
        '''
        pass
        self.draw_background()
        for i in range(self.bh):
            for j in range(self.bw):
                self.game_net[i][j].draw()

    def draw_background(self):
        '''
        Draws background for the board
        '''
        pygame.draw.rect(self.game.screen, LIGHT_GREY_COLOR, pygame.Rect(0, 0, self.width, self.height))

    def neighbours_list(self, block):
        '''
        Returns a list of adjacent blocks
        '''
        i = block.bw
        j = block.bh
        list = []
        for a in range(i - 1, i + 2, 1):
            for b in range(j - 1, j + 2, 1):
                if ((a >= 0 and a <= (self.bw - 1)) and
                        (b >= 0 and b <= (self.bh - 1)) and
                                            (a != i or b != j)):
                    list.append((a, b))
        print(self.game_net[i][j].bh,self.game_net[i][j].bw)
        print(list)
        return list

    def board_reveal(self, block):
        block.reveal()
        nlist = self.neighbours_list(block)
        if not self.count_bombs(nlist, block):
            for x, y in nlist:
                if self.game_net[x][y].status == 0:
                    self.board_reveal(self.game_net[x][y])

    def count_bombs(self, nlist, block):
        '''
        Counts adjacent bombs
        '''
        bombs = 0
        for a, b in nlist:
            if self.game_net[a][b].isBomb:
                bombs += 1
        block.neighbours = bombs
        print(bombs)
        return bombs
    def place_bombs(self):
        '''
        Places bombs in random positions

        '''
        bombs_set = set()
        while len(bombs_set) < self.num_of_bombs:
            bombs_set.add((random.randrange(0, self.bw), random.randrange(0, self.bh)))
        print(bombs_set)
        for x, y in bombs_set:
            self.game_net[x][y].isBomb = True

    def coords(self, coordinates):
        x, y = coordinates
        for i in range(self.bh):
            for j in range(self.bw):
                if ((coordinates[0] >= self.game_net[i][j].x)
                        and (coordinates[1] >= self.game_net[i][j].y)
                        and (coordinates[0] <= self.game_net[i][j].x + self.block_size)
                        and (coordinates[1] <= self.game_net[i][j].y + self.block_size)):
                    return i, j
        else:
            return -1, -1

    def block_on_click(self):
        '''
        Checks on which block is the mouse cursor,
        if there's a bomb in this block then game is over,
        if not then the block is being revealed
        '''
        coordinates = pygame.mouse.get_pos()
        i, j = self.coords(coordinates)
        if not (i, j) == (-1, -1):
            if self.game_net[i][j].status == 0:
                if self.game_net[i][j].isBomb:
                    self.game.game_over()
                self.board_reveal(self.game_net[i][j])
    def on_right_click(self):
        '''
        Handles bomb flag
        '''
        coordinates = pygame.mouse.get_pos()
        i, j = self.coords(coordinates)
        if not (i, j) == (-1, -1):
            if self.game_net[i][j].status == 0:
                self.game_net[i][j].set_bomb_flag()
            elif self.game_net[i][j].status == 2:
                self.game_net[i][j].set_maybe_flag()
            elif self.game_net[i][j].status == 3:
                self.game_net[i][j].reset_status()
