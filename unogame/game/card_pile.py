import logging

from unogame.game.turn import TurnTracker

logger = logging.getLogger(__name__)


class CardPile:
    def __init__(self, n_players=2, current_player=0, current_pile=[]):
        self.pile = current_pile
        self.last_card = None
        self.pile_len = len(current_pile)
        self.current_turn_player = current_player
        self.n_players = 2
        self.next_turn_player = TurnTracker(n_players, current_player)
        self.update()

    def __repr__(self):
        pile_str = ", ".join([c.__repr__() for c in self.pile[-self.n_players:]])
        if self.last_card is None:
            last_card_str = "empty"
        else:
            last_card_str = f"{self.last_card.symbol}, {self.last_card.color}"
        return f"<CP({last_card_str}): [{pile_str}]>"

    def update(self):
        if self.pile_len != len(self.pile):
            self.pile_len = len(self.pile)
            self.last_card = self.pile[-1]
            self.next_turn_player.next_turn(
                step=self.next_turn_step(), modifiers=None
            )
        logger.info("Updated pile attributes")

    def add(self, card):
        if self.pile_len == 0 or self.is_valid_play(card):
            self.pile.append(card)
            self.update()
            logger.info("A card was played.")
        else:
            logger.warning("Played card must be a correlative number or share the color.")

    def next_turn_step(self):
        if self.pile_len == 0:
            return 1
        else:
            return self.last_card.next_player_step()

    def is_valid_play(self, card):
        if self.last_card.color == card.color:
            return True
        elif self.last_card.symbol == card.symbol:
            return True
        elif self.last_card.is_number and card.is_number:
            return abs(self.last_card.get_number() - card.get_number()) <= 1
        else:
            return False

    def valid_next_play(self, universe):
        valid_plays = []
        for card in universe:
            if self.valid_play(card):
                valid_plays.append(card)
        return valid_plays
