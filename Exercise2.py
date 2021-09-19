import math

n = input()
xn = float(n)
part1 = math.cos(xn) - 2 * math.sin(2 * xn)
part2 = math.sin(xn) + math.cos(2 * xn)
numerador = xn * part1 - part2
denominador = math.cos(xn) - 2 * math.sin(xn)
print("Numerador:", numerador, "Denominador:", denominador)
xn2 = numerador / denominador
print("xn+1 =", xn2)
