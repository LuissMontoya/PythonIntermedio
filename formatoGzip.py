# -*- coding: utf-8 -*-

import gzip

if __name__ == "__main__":
    with open('spotify.txt','rb') as original:
        with gzip.open('archivo.txt.gz','wb') as archivo1:
            archivo1.writelines(original)