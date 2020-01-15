# -*- coding: utf-8 -*-
import zipfile
from zipfile import ZipFile

if __name__ == "__main__":
    with zipfile.ZipFile('comprension.zip','w') as fzip:
        fzip.write('spotify.txt')
        fzip.write('Repositorio Python.doc')
        fzip.printdir()
        fzip.extractall()