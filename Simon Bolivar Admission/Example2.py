import math
"""
progress = [-3,0,5,12] # 1,2,3,4
n = 5
sucesion = n**2 - 4
print(sucesion)
"""

"""
# an = a1 + (n - 1) * r
a4 = 6*1/3
a1 = 3*1/3
r = a4 - a1 /(4-1)
print(int(r))
"""
r = 2
x = 1
n = 1
sum = 1
while (x < 25):
    n = n + r
    sum = sum + n
    x = x+1
print(sum)