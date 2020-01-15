# -*- coding: utf-8 -*-
import smtplib

if __name__ == "__main__":
    from email.mime.text import MIMEText
    msg= MIMEText('Contenido de Correo')

    msg['subject']='Asunto del correo'
    msg['From']='desdedonde@gmail.com'
    msg['To']='haciadonde@gmail.com'

    mailServer=smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('micorreo@gmail.com','xxxxxxxxx')
    mailServer.sendmail('luisgoemon@gmail.com','luisgoemon64@gmail.com',msg_as_string())

    mailServer.close()