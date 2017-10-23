import socket
import threading
import time
import random
import math
import sys
import select

class ClientHandler(threading.Thread):

    def __init__(self,client,address):
        threading.Thread.__init__(self)
        self._client = client

    def run(self):
        for x in range(10):
            self._client.send(listsoal[x])
            jawaban_peserta = self._client.recv(1024)
            list_jawaban_peserta.append(jawaban_peserta)
            print list_jawaban_peserta
            time.sleep(2)


server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)
sockets=[]
addresses=[]
listsoal = []
listhasil = []
list_jawaban_peserta = []
z = 1
while (z <= 10):
    ops = ['+', '-', '*', '/']
    soal = []
    loop = random.randint(4, 6)
    i = 0
    # membuat soal dan memasukkan soal ke list maths
    while (i < loop):
        num1 = random.randint(1, 10)
        numstr = str(num1)
        soal.append(numstr)
        operation = random.choice(ops)
        operation = str(operation)
        soal.append(operation)
        i = i + 1
    num2 = random.randint(1, 10)
    numstr2 = str(num2)
    soal.append(numstr2)
    soal = ' '.join(soal)
    soal = soal+'\n'
    listsoal.append(soal)
    #print(soal)
    hasil = eval(soal)
    #print (hasil)
    listhasil.append(hasil)
    #print (listhasil)
    z = z + 1


try:
    while True:
        print "Menunggu peserta lengkap"
        client, address = server_socket.accept()
        sockets.append(client)
        print('Peserta masuk: ',address)
        jumlah_peserta = len(sockets)
        if jumlah_peserta >=3:
            for client in sockets:
                handler = ClientHandler(client,address)
                handler.start()

except KeyboardInterrupt:
    server_socket.close()
sys.exit(0)