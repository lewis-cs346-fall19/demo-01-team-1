'''
This is the server side

'''


import socket



def main():
	HOST = ""
	PORT = 3429
	
	s = socket.socket(AF_INET, SOCK_STREAM)

	s.bind((host, port))

	s.listen(1)

	conn, addr = s.accept()

	while(1):
		data = conn.recv(1024)
		if not data: break
		conn.sendall(data)

	conn.close() 
	


if __name__ == "__main__":
	main()
