import socket
import select
import os
import sys

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    nama_file = conn.recv(1024)
    for file in os.listdir("dataset/"):
        if file == nama_file:
            file_ketemu = 1
            break

    if file_ketemu == 0:
        file_ketemu = 0
        print nama_file+" tidak ada di server"

    else:
        print "unduh "+nama_file+" dari alien"
        up_file = open("dataset/"+nama_file, "rb")
        read_file = up_file.read(1024)
        while read_file:
            conn.send(read_file)
            read_file = up_file.read(1024)
    break

server_socket.close()
server_socket.close()
sys.exit(0)