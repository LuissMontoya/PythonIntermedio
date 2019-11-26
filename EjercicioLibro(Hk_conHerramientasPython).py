# -*- coding: utf-8 -*-

# Escribe un programa que cree una lista de cuatro elementos y solicite al usuario
# cumplimentarlos uno  a uno.pueden ser direcciones IP(192.168.1.1) o números
# de puerto (21,22,80).
# Tras rellenar todos los campos, estos deberán mostrarse en pantalla.


if __name__ == "__main__":
    lista = []
    for i in range(4):
        aux = input("digite : ")
        lista.insert(i, aux)

    for elemento in lista:
        print(elemento)

