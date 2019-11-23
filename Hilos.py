# -*- coding: utf -8 -*-
import threading
import time

class MiHilo(threading.Thread):
    def run(self):
        print("{} inicio".format(self.getName()))
        time.sleep(1)
        print("{} Terminado".format(self.getName()))


if __name__ == "__main__":
    for x in range (4):
        hilo=MiHilo(name="Thread {} ".format(x+1))
        hilo.start()
        time.sleep(0.99)
