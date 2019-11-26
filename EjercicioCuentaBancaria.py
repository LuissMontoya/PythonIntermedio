
# -*- coding: utf-8 -*-


class CuentaBancaria():
    def __init__(self, titular, Ncuenta, saldo):
        self.titular = titular
        self.Ncuenta = Ncuenta
        self.saldo = saldo

    def add(self, valor):
        self.saldo = self.saldo+valor

    def retirar(self, valor):
        if valor > self.saldo:
            print("No tienes la cantidad suficiente!")
        else:
            self.saldo = self.saldo-valor
            print("Retirando..")

    def consultarSaldo(self):
       return self.saldo




if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Jorge", 1, 120000)
    print(cuenta1.saldo)
    cuenta1.add(50000)
    print(cuenta1.saldo)
    cuenta1.retirar(200000)
    cuenta1.retirar(10000)
    print(cuenta1.consultarSaldo())
