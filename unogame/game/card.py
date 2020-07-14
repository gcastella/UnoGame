import logging
from PIL import Image

from unogame.utils import is_number

logger = logging.getLogger(__name__)


class Card:
    def __init__(self, symbol, color, img):
        self.is_number = is_number(symbol)
        self.symbol = symbol
        self.color = color
        self.img = Image.open(img)

    def __repr__(self):
        return f"<C({self.symbol}, {self.color})>"

    def get_number(self):
        if self.is_number:
            return int(self.symbol)
        else:
            return False

    def show_card(self):
        self.img.show()

    # To implement in subclass
    def next_player_step(self):
        return 1

    # To implement in sublcass
    def effect(self):
        return None


class NumericCard(Card):
    def next_player_step(self):
        return 1

    def effect(self):
        return None


# Todo: implement
class ChangeDirection(Card):
    def next_player_step(self):
        return -1

    def effect(self):
        pass


# Todo: implement
class PassTurn(Card):
    def next_player_step(self):
        return 2

    def effect(self):
        pass


# Todo: implement
class Draw2(Card):
    def next_player_step(self):
        return 1

    def effect(self):
        pass


# Todo: implement
class ChangeColor(Card):
    def next_player_step(self):
        return 1

    def effect(self):
        pass


# Todo: implement
class Draw4(Card):
    def next_player_step(self):
        return 1

    def effect(self):
        pass
