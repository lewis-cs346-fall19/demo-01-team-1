"""
This is the client
This code thus sends a message to the server. It does this through creating a socket, connecting it to the server, 
it then creates a message (the string "this is a message") and sends it to the server. It then executes recv to receive
any messages from the server. Finally, it must close the socket so it can be potentially reused. 
This is an extra test comment.
"""

import socket


HOST = ""
PORT = 3429

#socket.AFNET and socket.SOCK_STREAM are kernel constants 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) #connects to the port

#create and send message
msg = "CODE RED! EVACUATE!"
s.sendall(msg.encode())

#receive data and close
data = s.recv(1024).decode()
print(data)

s.close()



