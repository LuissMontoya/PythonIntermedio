def reverse(s):
    global values

    values = values + [s]

    result = ""
    for c in s:
        result = c + result
        
    return result

values = []

t = input('Digite el string: ')
while t.strip() != "":
    print("La reversa de ", t , " es: ", reverse(t))
    t = input('Digite otro string o enter para salir: ')

print('sal: ')

for val in values:
    print(val)