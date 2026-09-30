# Just like with the client before, create a socket.

# Assuming the socket is referred to by the variable s, call this magical line of code to prevent "Address already in use" errors:

# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# This is really useful to call on any socket that you're using for a server. Might want to remember it.

# Bind the server to the port. You can run many different servers at once, but they all have to be on different ports so that clients can tell them apart.

# s.bind(("localhost", 3490))    # Or whatever port you want
# Tell the socket that you'll be listening for incoming connections. This is the big differentiator between servers and clients. Servers listen for incoming connections.

# s.listen()
# In a loop, do the following:

# Accept a new connection:

# client_socket, client_addr = s.accept()
# Notice that a new socket (client_socket) is created especially for this one new connection. The original listenening socket (s) is still able to take new connections the next time you call .accept().

# Print out the client_addr. This tells you where the connection came from.

# Send some data back to the client. This has to be sent as bytes, so we have to encode it.

# client_socket.sendall("Some data!\n".encode())
# Hang up on the client.

# client_socket.close()

import socket

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("localhost", 3490))
s.listen()

while True:
    client_socket, client_addr = s.accept()
    print(client_addr)
    client_socket.sendall("It's me from the past!\n".encode())
    client_socket.close()