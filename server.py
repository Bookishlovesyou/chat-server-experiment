import socket
import time

HEADERSIZE = 10

# Create a TCP/IP socket. This one uses IPv4 (AF_INET) and TCP (SOCK_STREAM).
#socket.socket() creates a new socket object that can be used to communicate over the network. The first argument specifies the address family (AF_INET for IPv4), and the second argument specifies the socket type (SOCK_STREAM for TCP).
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port. The bind() method associates the socket with a specific network interface and port number. In this case, it binds to the hostname of the machine (socket.gethostname()) i think its Booki thats the name i guess and port 1234.
s.bind((socket.gethostname(), 1234))

# Listen for incoming connections. The argument specifies the maximum number of queued connections. in tis case we allow 5 connections i guess
s.listen(5)  

while True:
    # wait for connection accept() return a tuple containing a new socket onject and the adress of the client. The new socket object can be used to communicate with the client, while the address contains the client's IP address and port number.
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established!") #print the adress..... {adress} is the adress of the client that was accepted.

    msg = "Welcome to the server!"

    # this is like %10s in c.
    msg = f'{len(msg):<{HEADERSIZE}}' + msg



    #bytes() is a built-in function that turn string into a byte cause sockets communicate using bytes
    #utf-8 is an en
    clientsocket.send(bytes(msg, "utf-8"))
    
    #clientsocket.close() #close the connection after sending the message. This is important to free up resources and allow the server to accept new connections.

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
