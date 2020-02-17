# -*- coding: utf-8 -*-

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Paso de parametros')
    parser.add_argument("-p1", dest="param1", help="parameter1")
    parser.add_argument("-p2", dest="param2", type=int, help="parameter2")
    params = parser.parse_args()
    print(params.param1)
    print(params.param2)

    # python paso_parametros.py -p1 "parametro 1" -p2 180

