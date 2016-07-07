import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 2121))
revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
sock.sendto(revcData, (remoteHost, 2222))
print revcData