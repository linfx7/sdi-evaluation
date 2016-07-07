import socket
import threading

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

prb = packet_report_builder('127.0.0.1', 1919)
src = bytearray((10, 0, 0, 1))
dst = bytearray((10, 0, 0, 1))
prb.send(src, dst)
prb.close()
