import random

print("Hola, ¿Como te llamas?")
name = input()

print("Bien, "+name+" , Estoy pensando en que adivinez el numero")
secretNumber = random.randint(1 ,20)
for guessTaken in range(1,7):
    print("Adivina el numero")
    guess = int(input())
    if(guess < secretNumber):
        print("Demasiado menor")
    elif (guess > secretNumber):
        print("Demasiado alto")
    else:
        break

if(guess == secretNumber):
    print("FELICIDADES, Lo haz logrado adivinar el numero con " + str(guessTaken) + " intentos")
else:
    print("Lo sentimos el numero era " + str(secretNumber) )