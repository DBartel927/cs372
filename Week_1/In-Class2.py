import socket

s = socket.socket()

server = ("localhost", 3490)

s.connect(server)
while True:
    data = s.recv(10000000000)
    if (data == b""):
        break
    str = data.decode()
    print(str, end='')