import socket

s=socket.socket()
print("socket created")
s.bind((socket.gethostname(),9999))
s.listen(3)
print("waiting for the connection...")

while True:
    c,addr=s.accept()
    print("connected with",addr)

    c.send(bytes("welcome to the server",'utf-8'))
    incolor=input("please enter the color\n")
    incolor=incolor.upper()
    c.send(bytes(incolor,'utf-8'))
    break

c.close()
