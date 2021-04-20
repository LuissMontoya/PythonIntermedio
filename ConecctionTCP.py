# Servidor

import socket

host = '127.0.0.1'
port = 2345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print('Servidor en Escucha ..')
    conn, addr = s.accept()
    with conn:
        print('Conexión Detectada: ', addr)
        while True:
            data = conn.recv(1024)
            if data:
                print('El Cliente ha enviado: ',data)
            else:
                break
            conn.sendall(data)