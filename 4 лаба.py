a, b = map(int, input("Enter A and B ").split())
if (a < b):
	for i in range(a, b + 1):
		print (i)
else:
	for i in range(a,b - 1,-1):
		print(i)
