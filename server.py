# import socket
# import tqdm
# import os
# # ip addres yang digunakan
# SERVER_HOST = "0.0.0.0"
# SERVER_PORT = 5001
# # menerima 4096
# BUFFER_SIZE = 4096
# SEPARATOR = "<SEPARATOR>"
# # membuat socket
# # TCP socket
# s = socket.socket()
# # bind socket sebagai local address
# s.bind((SERVER_HOST, SERVER_PORT))
# s.listen(5)
# print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# # menerima koneksi
# client_socket, address = s.accept()
# # jika ada user konek akan tereksekusi
# print(f"[+] {address} is connected.")
# # menerima info file
# received = client_socket.recv(BUFFER_SIZE).decode()
# filename, filesize = received.split(SEPARATOR)
# filename = os.path.basename(filename)
# # mengubah string menjad integer
# filesize = int(filesize)b  
# # mulai menerima file dari socket
# progress = tqdm.tqdm(range(
#     filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
# with open(filename, "wb") as f:
#     for _ in progress:
#         bytes_read = client_socket.recv(BUFFER_SIZE)
#         if not bytes_read:
#             break
#         # menulis besaran bytes file yang di terima
#         f.write(bytes_read)
#         # update progress bar grafik
#         progress.update(len(bytes_read))



# client_socket.close()
# s.close()

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
s.send(b"Hello masbud!")
f = open('coba.txt','rb')
print ('downloading...')
l = f.read(1024)
while (l):
    print ('downloading...')
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done downloading")
print (s.recv(1024))
s.close            
