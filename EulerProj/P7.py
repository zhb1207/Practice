from math import sqrt
i = 2
step = 0


def isprime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


while step != 10001:
	if isprime(i):
		step += 1
	i += 1

print(i - 1)
