import pygame
class Block(object):

    def __init__(self, screen, size):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.size = size
        self.status = 0
        self.isBomb = False
        self.neighbours = 0

    def draw(self):
        if self.status:
            self.color = (255, 255, 255)
        else:
            self.color = (255, 100, 0)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
    def count_bombs(self):
        pass