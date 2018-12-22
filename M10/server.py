import socket
import threading

def handleclients(client,uname):
    client1 = True
    keys = clients.keys()
    help = "1)**broadcast -Broadcasting your message.2) **uname -Personal Chat.3)**quit in msg"
    while client1:
        try:
            msg = client.recv(1024).decode('ascii')
            if('**broadcast' in msg):
                msg = msg.replace('**broadcast','')
                for k,v in clients.items():
                    v.send(msg.encode('ascii'))
            elif('**help' in msg):
                client.send(help.encode('ascii'))
            elif('**quit' in msg):
                clients.pop(uname)
                message = str(uname) + 'Logged Out'
                client.send(message.encode('ascii'))
                client1 = False
            else:
                for name in keys:
                    if('**'+name in msg):
                        msg = msg.replace('**'+name,'')
                        clients.get(name).send(msg.encode())
                        found = True
                    elif(not found):
                        message1 = 'You entered an invalid person'
                        client.send(message1.encode('ascii'))
        except:
            clients.pop(uname)
            print(str(uname) + "logged out")
            client1 = False

if __name__ == '__main__':
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server = True
    host1 = socket.gethostname()
    port = 5011
    clients = {}
    host = socket.gethostbyname(host1)
    s.bind((host,port))
    print("Server start")
    print("IP address of the server::%s"%host)
    s.listen(10)
    while server:
        client, addr = s.accept()
        uname = client.recv(1024).decode('ascii')
        print("connected to the server" + str(uname))
        client.send("Welcome to chat press **help for help".encode('ascii'))
        if(client not in clients):
            clients[uname] = client
            threading.Thread(target = handleclients, args = (client,uname,)).start()