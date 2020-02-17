# -*- coding: utf-8 -*-

import argparse

descripcion = """ Ejemplos de Uso:
    + Escaneo Basico:
        -target 127.0.0.1
    + Indica un puerto especifico:
        -target 127.0.0.1 -port 21
    + solo mostrar puertos abiertos
        -target 127.0.0.1 --open True """

parser = argparse.ArgumentParser(description='port scanning', epilog=descripcion,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-target", metavar='TARGET',
                    dest="target", help="taget to scan", required=True)
parser.add_argument("-ports", dest="ports",
                    help="Please, specify the target port(s) separated by comma[80,8080 by default]",
                    default="80,8080")

parser.add_argument('-v', dest='verbosity', default=0,
                    action="count", help="verbosity level: -v, -vv, -vvv.")

parser.add_argument("--open", dest="only_open", action="store_true", help="only display open port",
                    default=False)

params = parser.parse_args()
portlist = params.ports.split(',')
print(params.ports)
print(portlist)

for port in portlist:
    print("Puerto: "+port)
