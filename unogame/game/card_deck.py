import logging

from unogame.utils import is_number
from unogame.config import config
from unogame.game.card import NumericCard, Card

logger = logging.getLogger(__name__)


class CardDeck:
    def __init__(self):
        self.deck = []
        self.universe = []
        for k, card in config.cards.items():
            if is_number(card.symbol):
                card_object = NumericCard(card.symbol, card.color, card.img)
            else:
                card_object = Card(card.symbol, card.color, card.img)
            self.universe.append(card_object)
            for i in range(card.quantity):
                self.deck.append(card_object)

    def __repr__(self):
        return f"<Deck({len(self.deck)}c, {len(self.universe)}uc)>"
