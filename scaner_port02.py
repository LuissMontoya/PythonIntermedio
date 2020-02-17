# -*- coding: utf-8 -*-

import socket
from socket import *


if __name__ == "__main__":
    equipo = input('Ingresa el dominio(IP) a Escanear ')
    ipequipo= gethostbyname(equipo)
    print("Comenzando el escaneo.. IP: ",ipequipo)

    for puertos in range(19,1000):
        cliente= socket(AF_INET,SOCK_STREAM)
        resultado= cliente.connect_ex((ipequipo,puertos))
        if (resultado==0):
            print('puerto %d:' %(puertos))
            cliente.close()

        #proxychanins ./scaner_port02.py 
        #para ver porque puerto esta haciendo el escaneo