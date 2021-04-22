import socket
import sys 

def checkPortsSocket(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print('Puerto {}: \t Abierto'.format(port))
            else:
                print('Puerto {}: \t Cerrado'.format(port))

    except socket.error as error:
        print(str(error))
        print("Error de la Conexión")
        sys.exit()

checkPortsSocket('localhost',[3306,5432,80,8080,443])