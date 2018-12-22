import socket
import threading
import random
import time
from threading import *
def Main():
    host = '10.10.9.105'
    port = 5001
    server = True
    clients = []
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)
    while True:
        c, addr = s.accept()
        print("Connected Server" +str(addr))
        x = int(random.randint(0,50))
        print(x)
        print(start_new_thread(clientsThread,(c,x)))
def clientsThread(c):
    count =  int(0)
    value = int(0)
    while True:
        data = c.recv(1024)
        if not data:
            break
        if data.decode() == 'Q':
            return
        value = int(data.decode())

        print("Guess" + str(data.decode()))
        count = count + 1
        if (value == x):
            x1 = "Correct trials" + str(count)
            c.send(str(x1).encode())
        elif (value < x):
            x1 = "Think bigger"
            c.send(str(x1).encode())
        elif (value > x):
            x1 = "Think smaller"
            c.send(str(x1).encode())


    # print("Connected")
    c.close()
if __name__ == '__main__':
    Main()