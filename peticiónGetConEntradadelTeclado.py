import requests

url = input('Ingresa la dirección del sitio Web: ')
r = requests.get('https://'+url)
print(r.status_code)
print(r.url)
data = r.text
print(data)
