def check(n):
	test = 0
	num = n
	while n >= 1:
		r = n % 10
		n //= 10
		test = 10 * test + r
	return test == num


def find():
	result = 0
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			test = i * j
			if check(test) and test > result:
					result = test
	return result


print(find())
