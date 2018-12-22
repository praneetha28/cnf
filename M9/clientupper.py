import socket
def Main():
    host = '10.10.9.105'
    port = 5001
    client = True
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))


    print("Connected")
    # print("Welcome to Guess my number")
    # print("I'm thinking of a number between 1 and 50. Please guess in few attempts possible.")
    message = input("Enter your guess: Q for abort")
    while message != 'Q':

        s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received" + str(data))
        val = data.split()
        if (val[0] == 'Correct' or val[0] == 'q'):
            s.send('Q'.encode())
            break
        message = input("-> ")
    s.close()
if __name__ == '__main__':
    Main()