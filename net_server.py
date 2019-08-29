'''
This is the server side

'''

import socket

HOST = ""
PORT = 3429

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

conn, addr = s.accept()

while(1):
	data = conn.recv(1024).decode()
	if not data: break
	conn.sendall(data)
	print(data)

conn.close() 
