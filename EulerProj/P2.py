a, b = 1, 1
sum = 0
while True:
	a, b = b, a + b
	if b > 4000000:
		break
	if b % 2 == 0:
		sum += b
		print(b)
print(sum)
