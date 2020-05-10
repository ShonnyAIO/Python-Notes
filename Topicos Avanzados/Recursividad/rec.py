def a():
	for i in range(10):
		print(i+1, end=" ")

a()

def b(n):
	if (n == 11): return
	print(n, end=" ")
	b(n+1)

b(1)