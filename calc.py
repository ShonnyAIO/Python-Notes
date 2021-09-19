x = float(input())
y = float(input())

t = (2*(x**2) + (y**2) ) / ( 4*(x**2) + 4.84*(y**2) )
xn2 = 1 + (-2*t)
yn2 = 1 + (-2.2*t)
print('t: {:.4f}'.format(t))
print('(1-2*t): {:.4f}'.format(xn2))
print('(1-2.2*t): {:.4f}'.format(yn2))