'''
This is the server side
This code creates a socket, decides which port it will be attached to and starts listening to it. Once it receives a message,
it turns it into a string and then sends it back to the client. 
Deadjoe comment test
'''

import socket

#initialize port and create socket
HOST = ""
PORT = 3429
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binds to port
s.bind((HOST, PORT))

s.listen(1)

conn, addr = s.accept()

#this while loop allows the data to be recieved
while(1):
	data = conn.recv(1024).decode()
	if not data: break
	print(data)
	data += " This message has been received. Evacuate! Abandon all assets!"
	conn.sendall(data)

conn.close() 
