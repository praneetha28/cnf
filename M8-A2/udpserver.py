import socket

def conversion(data):
	tokens = data.split(" ")
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

	host = '127.0.0.1'
	port = 5000
	scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	scket.bind((host,port))
	print ("server started")
	while True:
		data, addr = scket.recvfrom(1024)
		print("message from " + str(addr))
		print("from connect user " + str(data))
		message = conversion(data.decode())
		print("sending " + str(message))
		scket.sendto(str(message).encode(), addr)
	scket.close()

if __name__ == '__main__':
	main()