import logging

logger = logging.getLogger(__name__)


class TurnTracker:
    def __init__(self, n_players=2, current_turn_player=0):
        self.current_turn_player = current_turn_player
        self.n_players = n_players
        self.order = [str(i) for i in range(n_players)]
        self.modifiers = []
        self.turn_tracker = [current_turn_player]

    def reduce_modifiers(self):
        new_mods = []
        for i, mod in enumerate(self.modifiers):
            if self.modifiers[i] > 1:
                new_mods.append([mod[0], mod[1], mod[2] - 1])
        self.modifiers = new_mods

    def add_modifiers(self, modifiers=None):
        if modifiers is not None:
            self.modifiers.append(modifiers)

    def next_turn(self, step=1, modifiers=None):
        self.current_turn_player = (self.current_turn_player + step) % self.n_players
        self.turn_tracker.append(self.current_turn_player)
        self.reduce_modifiers()
        self.add_modifiers(modifiers)

    def __repr__(self):
        ctp_str = f"[{str(self.current_turn_player)}]"
        turn_str = " - ".join(self.order).replace(str(self.current_turn_player), ctp_str)
        return f"<T{len(self.turn_tracker)}: {turn_str}>"
