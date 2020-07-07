import socket
from _thread import *
import logging

logger = logging.getLogger(__name__)


def start_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((ip, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    logger.info("Server Started.")
    logger.info("Waiting for a connection.")

    def threaded_client(conn):
        conn.send(str.encode("Connected"))
        reply = ""
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode("utf-8")

                if not data:
                    logger.info("Disconnected")
                    break
                else:
                    logger.info("Received: ", reply)
                    logger.info("Sending : ", reply)

                conn.sendall(str.encode(reply))
            except:
                break

        logger.info("Lost connection")
        conn.close()

    while True:
        conn, addr = s.accept()
        logger.info("Connected to:", addr)

        start_new_thread(threaded_client, (conn,))
