import pygame
from block import Block

class GameScreen(object):
    def __init__(self, game, block_size = 25):
        x = 10
        y = 10
        self.game = game
        self.m = game.m
        self.n = game.n
        self.block_size = block_size
        self.width = self.m * (self.block_size + 5) + 15
        self.height = self.n * (self.block_size + 5) + 15
        self.game_net = [[Block(game.screen, block_size ) for i in range(self.m)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                self.game_net[i][j].x = x
                self.game_net[i][j].y = y
                self.game_net[i][j].draw()
                x += self.game_net[i][j].size + 5
            x = 10
            y += self.game_net[i][j].size + 5

    def draw(self):
        self.draw_background()
        for i in range(self.n):
            for j in range(self.m):
                self.game_net[i][j].draw()

    def draw_background(self):
        pygame.draw.rect(self.game.screen, (100, 200, 100), pygame.Rect(0, 0, self.width, self.height))

    def reveal(self, i, j):
        list = [0 for i in range(9)]
        it = 0
        for a in range(i - 1, i + 2, 1):
            for b in range(j - 1, j + 2, 1):

                list[it] = (a, b)
                it += 1

        for x in range(len(list)):
            print(list[x])
        self.game_net[i][j].status = 1

    def block_on_click(self):
        coordinates = pygame.mouse.get_pos()
        for i in range(self.n):
            for j in range(self.m):
                if (coordinates[0] >= self.game_net[i][j].x) \
                        and (coordinates[1] >= self.game_net[i][j].y) \
                        and (coordinates[0] <= self.game_net[i][j].x + self.block_size) \
                        and (coordinates[1] <= self.game_net[i][j].y + self.block_size):
                    if self.game_net[i][j].status == 0:
                        if self.game_net[i][j].isBomb:
                            self.game.game_over()
                        self.reveal(i, j)