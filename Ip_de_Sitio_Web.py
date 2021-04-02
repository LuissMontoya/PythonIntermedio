import socket as s

website= input('Ingresa la dirección del Sitio Web: ')

print('IP del Sitio Web: ', s.gethostbyname(website))