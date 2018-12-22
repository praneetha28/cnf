import socket
import sys
import threading

def receivemsg(sock):
    while True:
        recv = s.recv(1024).decode()
        if recv != "ROLLNUMBER-NOTFOUND":
            ans = input()
            s.send(ans.encode())


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = '127.0.0.1'
    port = 5011
    s.connect((ip,port))
    # s.send(uname.encode())
    threading.Thread(target = receivemsg, args = (s,)).start()

    while True:
        i = input()
        s.send(i.encode())
    s.close()

