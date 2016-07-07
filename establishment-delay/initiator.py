import socket
import time
from threading import Timer, Thread

class Initiator:

    def _sendMsg(self):
        self.start = time.time()
        while self._running:
            self._clientSock.sendto(str(time.time()), ('219.224.168.138', 2121))

    def _recvMsg(self):
        recvData = self.serverSock.recvfrom(1024)
        self._running = False
        self.end = float(recvData)

    def __init__(self):
        self.start = 0
        self.end = 0
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.bind(('', 2222))
        s = Thread(target=self._recvMsg)
        s.start()

        self._clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._running = True
        c = Timer(0.01, self._sendMsg)
        c.start()

        s.join()
        c.join()
        print round(abs(i.end - i.start), 2)


i = Initiator()
