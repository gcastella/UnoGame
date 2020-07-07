import pygame
import logging

from unogame.config import config
from unogame.utils import func_def

logger = logging.getLogger(__name__)


def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def start_client(width, height, caption):

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    clientNumber = 0

    player = func_def(**config.instances.dummy_client.player)()

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player.move()
        redrawWindow(win, player)
