import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((socket.gethostbyname(socket.gethostname()), 12345))

message, information = server.recvfrom(1024)

print(message.decode())