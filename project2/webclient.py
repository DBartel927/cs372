import socket
import sys

host = sys.argv[1]
port = 80

if len(sys.argv) > 2:
    port = int(sys.argv[2])

s = socket.socket()
server = (host, port)
s.connect(server)

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

s.sendall(request.encode("ISO-8859-1"))
response = b""

while True:
    data = s.recv(4096)
    if data == b"":
        break
    response += data

print(response.decode("ISO-8859-1"), end="")
s.close()