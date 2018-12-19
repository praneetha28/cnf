import socket

def main():

	host = '127.0.0.1'
	port = 5001
	scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	scket.bind((host,port))
	msg = input("-")
	while msg != 'q':
		scket.sendto(str(msg).encode(), ('127.0.0.1',5000))
		data, addr = scket.recvfrom(1024)
		print("recieved from server: " + str(data.decode()))
		msg = input("-")
	scket.close()

if __name__ == '__main__':
	main()