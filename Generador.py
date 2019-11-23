# -*- coding: utf -8 -*-

def Numeros():
    n=1
    while True:
        yield n
        n=n+1

if __name__ == "__main__":
    i=Numeros()
    print(i)
    print(i.__next__())
    print(i.__next__())