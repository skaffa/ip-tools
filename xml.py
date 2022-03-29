import socket

ip = socket.gethostbyname(socket.getfqdn())

print(ip)