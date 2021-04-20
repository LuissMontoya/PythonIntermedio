# Cliente

import socket
s = socket.socket()
host = "127.0.0.1"
port = 2345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    data= input('Escribe un mensaje para el Servidor! ')
    s.sendall(data.encode())
    data = s.recv(1024)

print('Recibido!', repr(data))