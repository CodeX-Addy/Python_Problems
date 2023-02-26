#Inverted star pattern
n = int(input("Enter the value of n:"))
for i in range (n, 0, -1):
	print((n-i) * ' ' + i * '*')
