# -*- coding:utf-8 -*-
# Importamos smtplib  
import smtplib    

# Importamos los módulos necesarios  
from email.mime.text import MIMEText    

# Creamos el mensaje  
msg = MIMEText("Contenido del e-mail a enviar")    

# Conexión con el server  
msg['Subject'] = 'Asunto del correo'  
msg['From'] = 'aramayo.fabian@gmail.com'  
msg['To'] = 'android.541440@gmail.com'    

# Autenticamos
mailServer = smtplib.SMTP('smtp.gmail.com',587)  
mailServer.ehlo()  
mailServer.starttls()  
mailServer.ehlo()  
mailServer.login("aramayo.fabian@gmail.com","314159265358979a")    

# Enviamos  
mailServer.sendmail("aramayo.fabian@gmail.com", "android.541440@gmail.com", msg.as_string())    

# Cerramos conexión 
mailServer.close() 