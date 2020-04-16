import socket
# import tqdm
# import os

# SEPARATOR = "<SEPARATOR>"
# BUFFER_SIZE = 4096  # pengiriman buffer sebesar 4096
# # ip address yang akan di konekkan
# host = "10.20.48.32"
# # menggunakan port 5001
# port = 5001
# # inisiasi nama file yang akan di kirim
# filename = "test.txt"
# # mengambil size file
# filesize = os.path.getsize(filename)
# # membuat socket
# s = socket.socket()
# print(f"[+] Connecting to {host}:{port}")
# s.connect((host, port))
# print("[+] Connected.")
# # mengirim nama file dan size
# s.send(f"{filename}{SEPARATOR}{filesize}".encode())
# # mulai mengirimkan
# progress = tqdm.tqdm(range(
#     filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
# with open(filename, "rb") as f:
#     for _ in progress:
#         # membaca byte file
#         bytes_read = f.read(BUFFER_SIZE)
#         if not bytes_read:
#             # transmisi file jika selesai
#             break
#         # menggunakan send all
#         s.sendall(bytes_read)
#         # grafik bar
#         progress.update(len(bytes_read))
# # menutup socket
# s.close()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('coba.txt','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    print ("sending...")
    l = c.recv(1024)
    while (l):
        print ("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print ("Done Receiving")
    c.send(b"Thank you for connecting")
    c.close()                # Close the connection