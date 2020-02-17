# -*- coding: utf-8 -*-

import socket

host = 'www.facebook.com'
puerto=80

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host,puerto))

cliente.send("GET / HTTP/1.1\r\n host: www.facebook.com\r\n\r\n")

respuesta= cliente.recv(2048)

print(respuesta)