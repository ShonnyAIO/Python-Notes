i = 1
while(i <= 10):
	print(i, end=' ')
	i += 1

#range(n) -> 0, n-1
#range(1,11,2) -> 1,3,5,7,9,11
print("")
for i in range(1,11):
	print(i, end=' ')

print("")
a = "abcdefgh"
for i in a:
	if(i == 'e' ): break
	print(i, end=' ')