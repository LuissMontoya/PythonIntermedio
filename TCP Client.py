import socket

target_host = "www.google.com"
target_port = 80

# Crear un objeto de SOCKET [(IPV4),(TCP)] 
client  =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el Cliente
client.connect((target_host,target_port))
print('Iniciamos Cliente')
# Enviar algun dato

data= "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data.encode('utf-8'))

#Recibir algunos datos
response = client.recv(4096)
http_response_len = len(response)

print('Length: ',http_response_len)
print('----------------------------')
print(response)