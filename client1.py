mport socket


s =socket.socket()

host = socket.gethostname()
port = 5189

s.connect((host,port))

while True:
    data = raw_input('Please Enter data you want to send : ')
    s.sendall(data)
    print ("Waiting for client 2")
    data=s.recv(1024)
    print ("Client 2 said : " , data)
    if data == 'end':
        break
s.close()
