import socket
import sys
import os

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
    # print(request.decode("ISO-8859-1"))
    request = request.decode("ISO-8859-1")
    lines = request.split("\r\n")
    get_line = lines[0]
    parts = get_line.split(" ")
    path = parts[1]
    file_name = path.split("/")[-1]
    try:
        with open(file_name, "rb") as fp:
            file_data = fp.read()
    except:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 13\r\n"
            "Connection: close\r\n"
            "\r\n"
            "404 not found"
        )

        client_socket.sendall(response.encode("ISO-8859-1"))
        client_socket.close()
        continue
    root, ext = os.path.splitext(file_name)
    if ext == ".html":
        content_type = "text/html"
    elif ext == ".txt":
        content_type = "text/plain"
    else:
        content_type = "application/octet-stream"

    response = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(file_data)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    client_socket.sendall(response.encode("ISO-8859-1"))
    client_socket.sendall(file_data)
    client_socket.close()