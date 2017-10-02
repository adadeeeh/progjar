import sys
import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1", 2545))

F_name = raw_input("enter filename to download from server : ")
F_namelist = F_name.split()

while True:
    c.send(F_namelist[1])
    F_data = c.recv(1024)
    F_down = open("/home/pedro/Documents/python/511510027_5115100082/client/downloads/"+F_namelist[1], "wb")
    while F_data:
        F_down.write(F_data)
        F_data = c.recv(1024)
    print "download completed\n"
    break

c.close()