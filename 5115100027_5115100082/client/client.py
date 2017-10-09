import socket
import sys
import os

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

nama_file = raw_input()
nama_file_split = nama_file.split(" ")
while nama_file_split[0] != 'unduh':
    print "Perintah yang anda masukkan salah"
    client_socket.send(nama_file)
    break
file_ada = 0
for file in os.listdir("/home/pedro/Documents/python-networking/5115100027_5115100082/server/dataset/"):
    if file == nama_file_split[1]:
        file_ada = 1
        break

if file_ada == 1:
    client_socket.send(nama_file)
    tmp = client_socket.recv(2048)
    down_file = open("downloads/"+nama_file_split[1], "wb")
    while tmp:
        down_file.write(tmp)
        tmp = client_socket.recv(2048)
    print "unduh selesai"
else:
    print nama_file_split[1]+" tidak ketemu"

client_socket.close()