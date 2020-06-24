import math

#Funcion a optimizar f(x)=2*math.sin(x)-pow(x,2)/10 ----> (2sinX-X^2/10)

#funcion primer derivada
def f_p(x):
    yp=2*math.cos(x)-x/5
    return (yp)

# funcion segunda derivada
def f_pp(x):
    ypp=-2*math.sin(x)-1/5
    return (ypp)

#introduciomos el valor x de partida (Xo asi como el numero de iteraciones)
xi=float(input("Introduce X_o: "))
iteraciones=int(input("Introduce el numero de iteraciones:  "))

raiz=[]
raiz.insert(0,0)

# inicializamos el contador de iteraciones
i=0

# Definimos un error inicial
error=1

# Aplicamos la formula Newton  para optimos
while iteraciones>i:
  xi_1=xi-(f_p(xi)/f_pp(xi))
  raiz.append(xi_1)
  i=i+1
  xi=xi_1
  error=(raiz[i]-raiz[i-1])/raiz[i]
  print(xi)
print("Error final:  " +str(error))
print("El optimo global aproximado es: " +str(2*math.sin(xi)-pow(xi,2)/10))