import sys
import socket
import os

host = ''
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,2545))
s.listen(5)
print "Server Active"
F_found = 0

while True:
    conn,addr = s.accept()
    print addr
    F_name = conn.recv(1024)
    for file in os.listdir("/home/pedro/Documents/python/511510027_5115100082/server/dataset/"):
        if file == F_name:
            F_found = 1
            break

    if F_found == 0:
        print F_name+"not found\n"

    else:
        print F_name+"found"
        F_upload = open("/home/pedro/Documents/python/511510027_5115100082/server/dataset/"+F_name, "rb")
        s_read = F_upload.read(1024)
        while s_read:
            conn.send(s_read)
            s_read = F_upload.read(1024)
        print "sending completed"
    break

conn.close()
s.close()