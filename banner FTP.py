# -*- coding: utf-8 -*-

import socket

socket.setdefaulttimeout(2)
cliente = socket.socket()
#nmap -P 21 -n serxiom.com 
cliente.connect(("ftp.serxiom.com",21))
respuesta= cliente.recv(1024)

print(respuesta)
