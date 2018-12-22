import socket
import threading
import csv
def handleclients(client,uname):
    f = "data.csv"
    fields = []
    rows = []
    with open(f, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
    while True:
        try:
            msg = client.recv(1024).decode()
            if (msg == "MARK-ATTENDANCE"):
                input1 = input()
                for row in range(1):
                    for col in range(rows):
                        if msg in rows[row][col]:
                            message = ("SECRET QUESTION - " + str(rows[row][col+1]))
                            s.send(message.encode())
                        else:
                            m = ("ROLLNUMBER-NOTFOUND")
                            s.send(m.encode())
        except:
            clients.pop(uname)
            print(str(uname) + "logged out")
            client1 = False

if __name__ == '__main__':
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host1 = '127.0.0.1'
    port = 5011
    clients = {}
    host = socket.gethostbyname(host1)
    s.bind((host,port))
    print("Server start")
    s.listen(10)
    while True:
        client, addr = s.accept()
        uname = client.recv(1024).decode('ascii')
        print("connected to the server" + str(uname))
        if(client not in clients):
            clients[uname] = client
            threading.Thread(target = handleclients, args = (client,uname,)).start()