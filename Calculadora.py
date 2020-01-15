# -*- coding: utf-8 -*-


class Calculadora():
    def __init__(self, inta, intb):
        self.inta = inta
        self.intb = intb

    def sumar(self):
        return self.inta+self.intb

    def Multiplicar(self):
        return self.inta*self.intb

    def dividir(self):
        return self.inta/self.intb

    def resta(self):
        return self.inta-self.intb

if __name__ == "__main__":
    cal=Calculadora(20,10)
    print('a=10\nb=20\n')
    print('a+b: %d'%cal.sumar())
    print('a*b: %d'%cal.Multiplicar())
    print('a-b: %d'%cal.resta())
    print('a/b: %d'%cal.dividir())