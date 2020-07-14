import pygame
import logging

from unogame.config import config
from unogame.utils import func_def

logger = logging.getLogger(__name__)


class Player:
    def __init__(self, name, x, y, width, height, color, vel):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = tuple(color)
        self.rect = (x, y, width, height)
        self.vel = vel

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.update_rect()

    def set_x(self, val):
        self.x = val
        self.update()

    def set_y(self, val):
        self.y = val
        self.update()

    def update_rect(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def __repr__(self):
        return f" <P({self.name}): ({self.x}x, {self.y}y, {self.width}w, {self.height}h)>"

    @staticmethod
    def init_players():
        return [Player(**v) for k, v in config.players.items()]
