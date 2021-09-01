import socket
import threading
bind_ip = "localhost"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5) #Acumulación Máxima de 5.

print ("[*] Listening on %s:%d" % (bind_ip, bind_port))
# este es nuestro hilo de manejo de clientes


def handle_client(client_socket):
    # imprime lo que envía el cliente
    request = client_socket.recv(1024)
    print ("[*] Received: %s" % request)
    # enviar un paquete
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print ("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
# hilo de cliente para manejar los datos entrantes
client_handler = threading.Thread(target=handle_client, args=(client,))
client_handler.start()
