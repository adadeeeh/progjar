import socket
import sys

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

nama_file = raw_input()
nama_file = nama_file.split(" ", 1)

while True:
    client_socket.send(nama_file[1])
    tmp = client_socket.recv(1024)
    print tmp
    new_tmp = tmp.splitlines(True)
    down_file = open("downloads/"+nama_file[1], "wb")
    while tmp:
        print new_tmp[0]
        down_file.writelines(new_tmp[2:])
        tmp = client_socket.recv(1024)
    break

client_socket.close()
sys.exit(0)
