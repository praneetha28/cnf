import socket

def conversion(data):
	tokens = data.split()
	if (tokens[1] == "INR"):
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 67)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75) / 67
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41) / 67
	if (tokens[1] == "Dollar"):
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75)
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41)
	if (tokens[1] == "Pounds"):
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67) / 0.75
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 0.75)
		if (tokens[4] == "Yen"):
			return (int(tokens[2]) * 113.41) / 0.75
	if (tokens[1] == "Yen"):
		if (tokens[4] == "INR"):
			return (int(tokens[2]) * 67) / 113.41
		if (tokens[4] == "Dollar"):
			return (int(tokens[2]) / 113.41)
		if (tokens[4] == "Pounds"):
			return (int(tokens[2]) * 0.75) / 113.41

def main():
	host = "127.0.0.1"
	port = 3128

	scket = socket.socket()
	scket.bind((host, port))

	scket.listen(1)
	conn, addr = scket.accept()
	print("Connection from " + str(addr))
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("from connected user " + str(data))

		data = str(conversion(data))
		print ("sending: " + str(data))
		conn.send(data.encode())
	conn.close()


if __name__ == '__main__':
	main()