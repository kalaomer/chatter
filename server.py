
class Server():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def ready(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(False)
        self.socket.bind(SERVER.HOST, SERVER.PORT)
        self.socket.listen(SERVER.LISTEN)

        print("Server is ready!")

    def listen(self):
        while True:
            try:
                message = self.socket.recv(SERVER.MAX_PACKAGE_SIZE)
            except socket.error:
                break

    """Logging on Server"""

    def make_login(self):
        pass
