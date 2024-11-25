import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("potato".encode(), (socket.gethostbyname(socket.gethostname()), 12345))