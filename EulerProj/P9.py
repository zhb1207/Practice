def check(a, b, c):
	return ((a**2 + b**2) == c**2) or ((c**2 + b**2) == a**2) or ((a**2 + c**2) == b**2)


def find():
	for i in range(1, 1000):
		for j in range(1, 1000):
			k = 1000 - i - j
			if check(i, j, k):
				print(i, j, k, i * j * k)
				return
find()