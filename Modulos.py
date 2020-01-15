# -*- coding: utf-8 -*-

class Calculadora():
    def __init__(self,ina,inb):
        self.ina=ina
        self.inb=inb
    def suma(self):
        return self.ina+self.inb
    def multi(self):
        return self.ina*self.inb
    
class cientifica(Calculadora):
    def potencia(self):
        return pow(self.ina,self.inb)

def sumaRapida(a,b):
    return a+b

