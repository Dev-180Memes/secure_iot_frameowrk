import socket
import pickle
from config.config import config


class Communicator:
    def __init__(self):
        self.server_address = config.SERVER_ADDRESS
        self.server_port = config.SERVER_PORT

    def send_data(self, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_address, self.server_port))
                s.sendall(pickle.dumps(data))
        except Exception as e:
            print(f"Error sending data: {e}")

    def receive_data(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.server_address, self.server_port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    data = b""
                    while True:
                        packet = conn.recv(4096)
                        if not packet:
                            break
                        data += packet
                    return pickle.loads(data)
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None
