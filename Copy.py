import pyperclip

pyperclip.copy('Hola, como estas ?')
pyperclip.paste()

spam = 42 # Global Variable
def eggs():
    global spam
    spam = 32 #local variable

"""
Asignacion de variables = Local
No asignaciones = Global
"""

def div42by(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print('Lo sentimos, no puedes dividir entre 0')
