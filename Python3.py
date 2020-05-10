# Logico de Comparacion

# > Mayor que
# < Menor que
# >= Mayor o igual que
# <= Menor o igual que
# == Igual que

a = 5 > 3 ; b = 17 < 5
c = 5 >= 60 ; d = 3 <= 3
e = 1 == 1

print("a = ", a , "b = ", b, "c = ",c,"d = ",d,"e = ",e)

#Logicos de Agrupacion AND, OR, NOT

# True and True = True
# True and False = False
# False and True = False
# False and False = False

a = (2+2 == 4) and (2 > 1)
print(a)


#OR

#True or True = True
#True or False = True
#False or True = True
#False or False = False

t = 300

a = (33 == 44) or (1 > t)

#Not

a = False
print(not a)

print("Ejercicio")
f = 40
g = f%3
g+=2
print(g)