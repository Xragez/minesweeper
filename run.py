import pygame, sys
from block import Block
from game_screen import GameScreen
B_WIDTH, B_HEIGHT = 15, 15  # Game board size in blocks
W_WIDTH, W_HEIGHT = 500, 500    # Window size
NUM_OF_BOMBS = 30   # Number of bombs
GREY_COLOR = (150, 150, 150)
LEFT = 1
RIGHT = 3
class InfoScreen:
    def __init__(self, game):
        self.game = game

    def draw_background(self):
        pygame.draw.rect(self.game.screen, GREY_COLOR, pygame.Rect(285, 0, 285, 285))

    def draw(self):
        self.draw_background()

class Game:

    def __init__(self):
        self.tps_max = 2.0
        self.bw = B_WIDTH
        self.bh = B_HEIGHT
        self.screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
        self.game_screen = GameScreen(self, bombs=NUM_OF_BOMBS)
        self.info_screen = InfoScreen(self)
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0

    def run(self):
        '''
        Main loop
        '''
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT or
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.game_screen.block_on_click()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                    self.game_screen.on_right_click()
            self.delta_time += self.clock.tick()
            # print(self.delta_time)
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()


    def draw(self):
        self.info_screen.draw()
        self.game_screen.draw()

    def game_over(self):
        print("BOOOOOOOM!!!!")
        for x in range(B_WIDTH):
            for y in range(B_HEIGHT):
                self.game_screen.game_net[x][y].boom()


def main():
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
