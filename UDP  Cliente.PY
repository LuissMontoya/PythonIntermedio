import socket
target_host = "localhost"
target_port = 6190
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send some data
data= 'ABCDEF'
client.sendto(data.encode('utf-8'),(target_host,target_port))
# receive some data
data, addr = client.recvfrom(1024)
print (data)