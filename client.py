import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

#recv is a funtion that recieves data from socket. the argument tells the max amount of data to be recieved at once. 
msg = s.recv(1024)

#decode() a funtion that deocdes the bytes into a string. utf-8 is a format
print(msg.decode("utf-8"))