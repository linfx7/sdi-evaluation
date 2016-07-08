import socket
import time
from threading import Timer, Thread

class initiator:

    def _sendMsg(self):
        self.start = time.time()
        while self._running:
            self._client_sock.sendto(str(time.time()), ('10.2.0.10', 2121))

    def _recvMsg(self):
        revc_data, remote = self._server_sock.recvfrom(1024)
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

        self._server_sock.close()
        self._client_sock.close()


i = initiator()
print round(abs(i.end - i.start), 2)