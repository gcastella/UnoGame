import pygame
import logging

from unogame.config import config
from unogame.instances import Network

logger = logging.getLogger(__name__)


class Client:
    def __init__(self, bg_col, width, height, caption):
        # Window
        self.bg_col = tuple(bg_col)
        self.width = width
        self.height = height
        self.caption = caption
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        # Network
        self.network = Network(**config.network)

    def start(self):
        run = True
        clock = pygame.time.Clock()
        player1 = self.network.get_pos()
        while run:
            clock.tick(60)
            player2 = self.network.send(player1)
            logger.debug(f"Player1: {player1}")
            logger.debug(f"Player2: {player2}")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            player1.move()
            self.re_draw_window([player1, player2])

    def re_draw_window(self, players):
        self.win.fill(self.bg_col)
        for player in players:
            player.draw(self.win)
        pygame.display.update()
