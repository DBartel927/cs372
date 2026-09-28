import socket

s = socket.socket()

server = ('flip2.engr.oregonstate.edu', 2187)

s.connect(server)
while True:
    data = s.recv(10000000000)
    str = data.decode()
    print(str, end='')