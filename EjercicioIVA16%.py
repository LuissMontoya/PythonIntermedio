# -*- coding: utf-8 -*-

# Diseña un algoritmo que calcule el IVA (16%)
# de un producto dado su precio de venta sin IVA.

if __name__ == "__main__":
    nombre = input('Digita el Nombre del producto:\t ')
    precio =input('Digita el precio de ('+nombre+')\t')
    aux=int(precio)
    iva =16*aux/100
    print('Producto: '+nombre+'\nPrecio: '+precio+'\nDescuento: '+iva
          + '\nTotal a Pagar: '+precio)
