import socket
from threading import Thread

class responder:

    def _listen(self):
        while True:
            try:
                revc_data, (remote_host, remote_port) = self._sock.recvfrom(1024)
                self._sock.sendto(revc_data, (remote_host, 2222))
                print revc_data
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

r = responder()
while True:
    words = str(raw_input())
    if words == 'END':
        break
r.stop()
exit()
