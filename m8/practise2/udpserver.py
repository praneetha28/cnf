import socket

def main():

	host = '127.0.0.1'
	port = 5000
	scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	scket.bind((host,port))
	print ("server started")
	while True:
		data, addr = scket.recvfrom(1024)
		print("message from " + str(addr))
		print("from connect user " + str(data.decode()))
		message = str(data.decode()).upper()
		print("sending " + str(data))
		scket.sendto(message.encode(), addr)
	scket.close()

if __name__ == '__main__':
	main()