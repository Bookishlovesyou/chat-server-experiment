import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    fullmsg = ''
    newmsg = True
    while True:
        #recv is a funtion that recieves data from socket. the argument tells the max amount of data to be recieved at once. 
        msg = s.recv(10)
        #bufferng
        if newmsg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            newmsg = False
        
        fullmsg += msg.decode("utf-8")
        #decode() a funtion that deocdes the bytes into a string. utf-8 is a format
        #print(msg.decode("utf-8"))
        if len(fullmsg) - HEADERSIZE == msglen:
            print("full msg recieved")
            print(fullmsg[HEADERSIZE:])
            newmsg = True
            fullmsg = ''
    print(fullmsg)
