
import pywhatkit as kt
from PIL import Image

print("Convertir imagenes a ASCII!")

im = Image.open(r"C:\Users\Luiss\Documents\Python\PythonIntermedio\fl.png") 

im.show() 

#capture source and target path
source_path = "C:\Users\Luiss\Documents\Python\PythonIntermedio\fl.png"
target_path = 'demo_ascii_art2.text'
#target_path = 'demo_ascii_art.text'

#Llamar el método
kt.image_to_ascii_art(source_path, target_path)