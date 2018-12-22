import socket
import sys
import threading

def receivemsg(sock):
    serverdown = False
    while client and (not serverdown):
        try:
            msg = sock.recv(1024).decode('ascii')
            print(msg)
        except:
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    uname = input("Enter your username")
    ip = input("Enter your IP address")
    port = 5011
    s.connect((ip,port))
    s.send(uname.encode('ascii'))
    client = True
    threading.Thread(target = receivemsg, args = (s,)).start()
    while client:
        tempmsg = input()
        msg = uname + '>>' + tempmsg
        if('**quit' in msg):
            client = False
            s.send('**quit'.encode('ascii'))
        else:
            s.send(msg.encode('ascii'))