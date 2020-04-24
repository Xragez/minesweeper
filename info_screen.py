import pygame

class InfoScreen(object):
    def __init__(self, game):
        self.game = game

    def draw_background(self):
        pygame.draw.rect(self.game.screen, (100, 100, 100), pygame.Rect(285, 0, 285, 285))

    def draw(self):
        self.draw_background()