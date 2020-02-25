# -*- coding: utf-8 -*-

import socket

socket.setdefaulttimeout(2)
cliente= socket.socket()

cliente.connect(("ftp.serxion.com",21))
respuesta= cliente.recv(1024)

print(respuesta)