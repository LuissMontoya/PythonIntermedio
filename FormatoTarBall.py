# -*- coding: utf-8 -*-
import tarfile

if __name__ == "__main__":
    archivo_tar=tarfile.open('primer.tar.gz','x:gz')
    archivo_tar.add('spotify.txt')
    archivo_tar.add('package.json')
    archivo_tar.close()