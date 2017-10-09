import socket
import select
import os
import sys
import StringIO

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

file_ketemu = 0

c = "/home/pedro/Documents/python-networking/5115100027_5115100082/server/dataset"


while True:
    conn, addr = server_socket.accept()
    nama_file = conn.recv(1024)
    nama_file = nama_file.split(" ")
    if nama_file[0] != "unduh":
        print "Perintah yang dimasukkan salah"
        break
    for file in os.listdir("dataset/"):
        if file == nama_file[1]:
            file_ketemu = 1
            break

    if file_ketemu == 0:
        print nama_file[1]+" tidak ada di server"

    else:
        print "unduh "+nama_file[1]+" dari alien"
        up_file = open("dataset/"+nama_file[1], "rb")
            #up_file = file.read()
        header = "nama_file: "+nama_file[1] + '\n'+"file_size: "+str(os.path.getsize('/home/pedro/Documents/python-networking/5115100027_5115100082/server/dataset/'+nama_file[1]))+'\n'+'\n\n'
        #print header
        data = header+nama_file[1]
        print data
        #data = data.split('\n')
        #print data
        #data1 = [StringIO.StringIO(x) for x in data]
        #read_file = data1.read(2048)
        read_file = up_file.read(2048)
        while read_file:
            conn.send(read_file)
            read_file = up_file.read(2048)
    break

server_socket.close()