import socket
import logging
import pickle
from _thread import *

from unogame.instances import Player

logger = logging.getLogger(__name__)


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.players = Player.init_players()

        self.current_player = 0

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.ip, self.port))
        except socket.error as e:
            str(e)
        s.listen(2)
        logger.info("Server Started.")
        logger.info("Waiting for a connection.")

        while True:
            conn, address = s.accept()
            logger.info(f"Connected to: {address}")
            logger.info(f"{self.current_player + 1} players connected")
            logger.info(f"Initial: {self.players[self.current_player]}")

            start_new_thread(self.threaded_client, (conn, self.current_player, self.players))
            self.current_player += 1

    @staticmethod
    def threaded_client(conn, player, players):
        conn.send(pickle.dumps(players[player]))
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                players[player] = data

                if not data:
                    logger.info("Disconnected")
                    break
                else:
                    if player == 1:
                        reply = players[0]
                    else:
                        reply = players[1]
                    logger.info(f"Received: {data}")
                    logger.info(f"Sending : {reply}")

                conn.sendall(pickle.dumps(reply))
            except:
                break

        logger.info("Lost connection")
        conn.close()

