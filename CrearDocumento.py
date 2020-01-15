# -*- coding: utf-8 -*-

if __name__ == "__main__":
    archivo=open("Documento.txt","w")
    archivo
    for contador in range(1,101):
        archivo.write(str(contador)+'\n')
  
    archivo2=open("Documento.txt","a")
    archivo2
    for contador2 in range(101,201):
        archivo2.write(str(contador2)+'\n')

    #Leer Documento
    documento= open("Documento.txt","r")
    for linea in documento.readline():
        print(linea.strip())
    documento.close()