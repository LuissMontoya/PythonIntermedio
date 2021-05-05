import pyautogui as pg
import time
import webbrowser as web
phone_no="+57**********"
parsedMessage=" "
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(8)
for i in range(150):
    pg.write('msg')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Spam finalizada')