import smtplib

con = smtplib.SMTP('smtp.gmail.com',587)
con.ehlo()
con.starttls()
con.login('exodiakah@gmail.com', 'Django.20$')
con.sendmail('exodiakah@gmail.com', 'jtorres@itconectas.com', 'Asunto: Esto es una prueba de Python \n\n Hola, como estas ?')
