import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = socket.gethostname()

ip = socket.gethostbyname(socket.gethostname())

client_socket.connect((socket.gethostbyname(name), 12345))

massage = client_socket.recv(1024)

print(massage.decode())

client_socket.close()