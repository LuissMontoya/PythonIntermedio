# -*- coding: utf-8 -*-

if __name__ == "__main__":
    conjunto= set("8923")
    conjunto2={'8','3','5'}

    print(conjunto)
    print(conjunto2)

    #Intersección de Conjuntos
    print(conjunto & conjunto2)
    print(conjunto.intersection(conjunto2))
    print(conjunto.union(conjunto2))
