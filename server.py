import socket

# Create a TCP/IP socket. This one uses IPv4 (AF_INET) and TCP (SOCK_STREAM).
#socket.socket() creates a new socket object that can be used to communicate over the network. The first argument specifies the address family (AF_INET for IPv4), and the second argument specifies the socket type (SOCK_STREAM for TCP).
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port. The bind() method associates the socket with a specific network interface and port number. In this case, it binds to the hostname of the machine (socket.gethostname()) i think its Booki thats the name i guess and port 1234.
s.bind((socket.gethostname(), 1234))

# Listen for incoming connections. The argument specifies the maximum number of queued connections. in tis case we allow 5 connections i guess
s.listen(5)  

while True:
    clientsocket, adress = s.accept()
    