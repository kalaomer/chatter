

class User():
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def listen(self):
        while True:
            try:
                message = self.client_socket.recv(SERVER.MAX_PACKAGE_SIZE)
            except socket.error:
                break