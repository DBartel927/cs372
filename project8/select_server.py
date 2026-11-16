# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", port))
    s.listen()
    sockets = [s]
    addresses = {}
    print("waiting for connections")
    while True:
        readable, _, _ = select.select(sockets, [], [])
        for sock in readable:
            if sock is s:
                client_socket, client_address = s.accept()
                sockets.append(client_socket)
                addresses[client_socket] = client_address
                print(f"{client_address}: connected")
            else:
                data = sock.recv(4096)
                client_address = addresses[sock]
                if data == b"":
                    print(f"{client_address}: disconnected")
                    sockets.remove(sock)
                    del addresses[sock]
                    sock.close()
                else:
                    print(f"{client_address} {len(data)} bytes: {data}")

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))