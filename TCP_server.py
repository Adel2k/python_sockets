import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = socket.gethostname()
ip = print(socket.gethostbyname(socket.gethostname()))

server_socket.bind((socket.gethostbyname(name), 12345))

server_socket.listen()

while True:
	client_socket, client_address = server_socket.accept()
	print("Succesfully connected to ---> ", client_address)

	client_socket.send(b"potato")

	server_socket.close()

	break