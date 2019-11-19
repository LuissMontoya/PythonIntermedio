# -*- coding: utf -8 -*-

class Clase():
    def __new__(cls):
        print("New")
        return super().__new__(cls)

    def __init__(self):
        print("Init")


if __name__ == "__main__":
    c1= Clase()
