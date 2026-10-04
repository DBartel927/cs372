import socket
import sys

port = 28333

if len(sys.argv) > 1:
    port = int(sys.argv[1])

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", port))
s.listen()

while True:
    client_socket, client_addr = s.accept()
    print(client_addr)
    request = b""
    while b"\r\n\r\n" not in request:
        data = client_socket.recv(4096)
        if data == b"":
            break
        request += data
    print(request.decode("ISO-8859-1"))
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 6\r\n"
        "Connection: close\r\n"
        "\r\n"
        "Hello!"
    )

    client_socket.sendall(response.encode("ISO-8859-1"))
    client_socket.close()