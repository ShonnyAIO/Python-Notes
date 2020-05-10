def fibo(n):
	if(n == 0 or n == 1):
		return n
	return fibo(n-2) + fibo(n-1)

x = int(input())

for i in range(x):
	print(fibo(i), end=" ")
	print(" ")