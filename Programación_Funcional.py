# -*- coding: utf -8 -*-

def lower(elementos):
    return elementos.lower()


if __name__ == "__main__":
    lista=["JOSÉ","LuiS","CarLOS","mariA"]
    print(list(map(lower,lista)))
    print([cad.lower() for cad in lista])

