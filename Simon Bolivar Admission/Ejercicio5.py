# Ejercicio 31, OPCION D
sum = 0
for i in range (0, 2002):
    if(i%2 == 0):
        sum = sum - i
    else:
        sum = sum + i
print(sum)