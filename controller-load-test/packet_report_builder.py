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
        self._sock.send(msg + src + dst)
        rtn_msg = str(self._sock.recv(100))
        return rtn_msg

    def close(self):
        self._sock.close()


def request_thread(i, j):
    for x in range(j*i, j*i+j):
        src = bytearray((10, 1, x, 1))
        for y in range(10):
            prb = packet_report_builder('219.224.168.140', 1919)
            dst = bytearray((10, 2, y, 1))
            rtn = prb.send(src, dst)
            if bytearray(rtn)[2] != 0x80:
                print "Request not accepted!"
            prb.close()

start = time.time()
tl = []

for i in range(20):
    t = threading.Thread(target=request_thread, args=(i,10))
    tl.append(t)

for t in tl:
    t.start()

print "here"
for t in tl:
    t.join()

end = time.time()

print round(end - start, 2)