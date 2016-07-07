import socket
import threading
import time

class packet_report_builder:

    def __init__(self, server_ip, server_port):
        self._server_ip = server_ip
        self._server_port = server_port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((server_ip, server_port))

    def send(self, src, dst):
        msg = bytearray((0x80, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x40, 0x80))
        self._sock.sendall(msg + src + dst)

    def close(self):
        self._sock.close()


def request_thread(i):
    for x in range(10*i, 10*i+10):
        src = bytearray((10, 1, x, 1))
        for y in range(100):
            prb = packet_report_builder('127.0.0.1', 1919)
            dst = bytearray((10, 2, y, 1))
            prb.send(src, dst)
            prb.close()

start = time.time()
tl = []

for i in range(5):
    t = threading.Thread(target=request_thread, args=(i,))
    tl.append(t)

for t in tl:
    t.start()

print "here"
for t in tl:
    t.join()

end = time.time()

print round(end - start, 2)