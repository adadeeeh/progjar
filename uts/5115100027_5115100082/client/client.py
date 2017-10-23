import socket
import sys
import time
import random
import math

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
    while True:
        soal = client_socket.recv(1024)
        sys.stdout.write(soal)
        sys.stdout.write("jawaban: ")
        jawaban = input()
        jawaban_str = str(jawaban)
        client_socket.send(jawaban_str)
        print "jawaban terkirim"

except KeyboardInterrupt:
    client_socket.close()
sys.exit(0)
