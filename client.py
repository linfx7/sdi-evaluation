import socket
import time

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
now = time.time()
print str(now)
while True:
    sendDataLen = clientSock.sendto(str(now), ('219.224.168.140', 2121))
    time.sleep(0.05)
    now = time.time()