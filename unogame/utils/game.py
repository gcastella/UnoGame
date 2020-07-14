from unogame.config import config


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def get_positions():
    return [(v.params.x, v.params.y) for k, v in config.players.items()]
