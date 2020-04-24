import pygame, sys
from block import Block
from game_screen import GameScreen
from info_screen import InfoScreen
m, n = 5, 5
LEFT = 1
RIGHT = 3
class Game(object):

    def __init__(self):
        self.tps_max = 2.0
        self.m = m
        self.n = n
        pygame.init()
        self.screen = pygame.display.set_mode((450, 285))
        self.game_screen = GameScreen(self)
        self.info_screen = InfoScreen(self)
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    self.game_screen.block_on_click()
                    #print("MOUSE_LEFT pos: ", coordinates)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                    print("MOUSE_RIGHT pos: ", pygame.mouse.get_pos())
            self.delta_time += self.clock.tick()
            #print(self.delta_time)
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()


    def draw(self):
        self.info_screen.draw()
        self.game_screen.draw()

    def game_over(self):
        print("GG")

if __name__ == "__main__":
    Game()
