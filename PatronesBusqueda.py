# -*- coding: utf-8 -*-
import re

if __name__ == "__main__":
    print(re.search(r"k", "kilómetro"))
    print(re.search(r"\d\d\d", "kiló912metro"))
    patron = re.compile("\d\d\d")
    print(patron.search("kiló912metro").group())

    if (re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
        print("Se encontró el patrón")

    print(re.sub(r"\d","*","Mangu8era990"))
    print(re.sub(r"\d","*","Mangu8era990",2))

    #modificadores
    regex= re.compile(r"ab",re.IGNORECASE)
    print(regex.search("junmilaAbuimtntna"))