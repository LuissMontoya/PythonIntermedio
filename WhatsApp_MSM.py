
import pywhatkit as py 
 
# Usamos Un try-except
try: 
 
  # Enviamos el mensaje


    py.sendwhatmsg("+573*********", "Texts MSG", 13,11)
  # py.sendwhatmsg("+57********", "Texts MSG", 18,38)
    print("Mensaje Enviado") 
 
  
 
except: 
  print("Ocurrio Un Error")