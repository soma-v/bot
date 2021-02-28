import socket
def client():
    c = socket.socket()

    c.connect((socket.gethostname(),9999))
    print(c.recv(1024).decode('utf-8'))
    incolor=c.recv(20)
    incolor=incolor.decode('utf-8')
    return incolor
