import socket
import time
from threading import Timer, Thread

class initiator:

    def _sendMsg(self):
        self.start = time.time()
        while self._running:
            self._client_sock.sendto(str(time.time()), ('219.224.168.138', 2121))

    def _recvMsg(self):
        revc_data = self._server_sock.recvfrom(1024)
        self._running = False
        self.end = float(revc_data)

    def __init__(self):
        self.start = 0
        self.end = 0
        self._server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._server_sock.bind(('', 2222))
        s = Thread(target=self._recvMsg)
        s.start()

        self._client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._running = True
        c = Timer(0.01, self._sendMsg)
        c.start()

        s.join()
        c.join()
        print round(abs(i.end - i.start), 2)


i = initiator()
