import pygame
from colors import *

class Block:
    """
    status:
        0 - hidden block
        1 - unveiled block
        2 - bomb flag
        3 - "may be bomb" flag
    """
    def __init__(self, screen, size):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.bw = 0
        self.bh = 0
        self.size = size
        self.status = 0
        self.isBomb = False
        self.neighbours = 0
        self.bomb_draw = False
        self.cheats_enabled = False

    def draw(self):
        """
        Draws block
        """
        font = pygame.font.SysFont("timesnewroman", 20, bold=True)
        font_color = BLACK_COLOR

        if self.neighbours == 1:
            font_color = BLUE_COLOR
        elif self.neighbours == 2:
            font_color = GREEN_COLOR
        elif self.neighbours == 3:
            font_color = RED_COLOR
        elif self.neighbours == 4:
            font_color = PURPLE_COLOR

        text = font.render(str(self.neighbours), True, font_color)

        if self.status == 1:
            self.color = WHITE_COLOR
        elif self.status == 2:
            self.color = RED_COLOR
        elif self.status == 3:
            self.color = BLUE_COLOR

        else:
            self.color = GREY_COLOR

        if self.status == 0 and self.cheats_enabled and self.isBomb:
            self.color = DARK_GREY_COLOR

        textRect = text.get_rect()
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

        if self.neighbours:
            textRect.center = (self.x + self.size // 2, self.y + self.size // 2)
            self.screen.blit(text, textRect)

        if self.bomb_draw:
            self.neighbours = 0
            pygame.draw.circle(self.screen, BLACK_COLOR, (self.x + self.size // 2, self.y + self.size // 2),
                               self.size // 4)


    def reveal(self):
        """
        Reveals the block
        """
        if not self.status:
            self.status = 1

    def set_bomb_flag(self):
        self.status = 2

    def set_maybe_flag(self):
        self.status = 3

    def reset_status(self):
        self.status = 0

    def boom(self):
        if self.isBomb:
            self.reveal()
            self.bomb_draw = True
