import socket
from threading import Thread

class Responder:

    def _listen(self):
        while True:
            try:
                revcData, (remoteHost, remotePort) = self._sock.recvfrom(1024)
                self._sock.sendto(revcData, (remoteHost, 2222))
                print revcData
            except BaseException, e:
                break

    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind(('', 2121))
        thread = Thread(target=self._listen)
        thread.setDaemon(True)
        thread.start()

    def stop(self):
        self._sock.close()

r = Responder()
while True:
    words = str(raw_input())
    if words == 'END':
        break
r.stop()
exit()
