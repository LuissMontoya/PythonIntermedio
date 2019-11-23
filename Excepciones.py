# -*- coding: utf -8 -*-

class Err(Exception):
    def __init__(self,valor):
        print("fue el error por :",valor)


if __name__ == "__main__":
    lista=[2,4]    
    print(lista[0])
    

    try:
        print(lista[5])
    except IndexError: 
        print("Hay un error en el índice")
    else:
        print("No hay ningún error")
    finally:
        print("Se ejectó")


    try:
        raise TypeError
    except:
        print("Errores con los Tipos")
    print("----------------")
    try:
        raise Err(4)
    except:
        print("Error Escrito")