import socket
import select
import sys
import os


server_address = ('127.0.0.1',5000)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
   while True:
         read_ready,write_ready,exception = select.select(input_socket,[],[])

         for sock in read_ready:
            if sock ==server_socket:
               client_socket,client_address = server_socket.accept()
               input_socket.append(client_socket)

            else:
               file = sock.recv(1024)
               if file:
                  file2 = file.replace("\n","")
                  path = 'dataset/'+file2
                  print "unduh "+file2+" dari alien"
                  with open(path, 'rb') as file:
                     up_file = file.read()
                  header = "name: "+file2+"\n"+"file_size: " + str(os.path.getsize('/home/pedro/Documents/python-networking/5115100027_5115100082/server/dataset/'+file2))+"\n"
                  print up_file
                  paket = header+up_file
                  print paket
                  sock.sendall(paket)
               else:
                  sock.close()
                  input_socket.remove(sock)

except KeyboardInterrupt:
   server_socket.close
   sys.exit(0)