# -*- coding: utf-8 -*-
import signal

def ctrl_c(signum,rfm):
    print("No puedes Cerrar el programa presionando CTRL+C")

if __name__ == "__main__":
    print("Intalando el instalador Signal")
    signal.signal(signal.SIGINT,ctrl_c)
    print("Listo")
    while True:
        pass
