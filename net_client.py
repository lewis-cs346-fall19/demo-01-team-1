"""
This is the client
"""

import socket


HOST = ""
PORT = 3429
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msg = "This is the message"
s.sendall(msg.encode())
data = s.recv(1024).decode()
s.close()



