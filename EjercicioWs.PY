# Sea conteo un vector de longitud 5 con los siguientes valores
conteo  = [1, 2, 2, 3, 3]  
m = 5

conteo2 = conteo 
n = len(conteo)     # Es cinco
i=1


conteo_i = conteo2[i]
print(conteo_i) # 2
j = 1
while (i <= n): # 1 - 5
    while (j <= m): #11 - 5 
            if (j == conteo_i):
                #del(conteo[i])
                #conteo.pop(1)
                conteo.pop(0)
                #conteo = conteo[j]-1  # Elimina el primer elemento que este en el vector "conteo"
                m = m - j
                break  # Rompe el ciclo en el q se encuentra
            else:
                j = j + 1 

 
    i = i + 1
    print('i: ',i)

resultado = len(conteo)
print(conteo)
print('el resultado es: ',resultado)