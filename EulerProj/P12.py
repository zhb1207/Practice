from math import sqrt


def factors(n):
	total = 0
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			total += 1
	if total > 250:
		if int(sqrt(n)) ** 2 == n:
			print(total * 2 - 1)
		else:
			print(total * 2)
		return True
	else:
		return False


n = 1
while True:
	triangle_num = n * (n + 1) // 2
	result = factors(triangle_num)
	if not result:
		n += 1
	else:
		print(triangle_num)
		break

"""
Or we can use the properties of 'Divisor function':
	d(nm) = d(n)d(m) - If m and n are coprime
	d(n^k) = k + 1

def get_number_of_divisors(n):
    powers = {}
    f = 2
    while n > 1:
        if n % f == 0:
            powers[f] = powers.get(f, 0) + 1
            n /= f
        else:
            f += 1

    if powers:
        return reduce(lambda a,b: a*b, [p+1 for p in powers.values()])
    return 1

i, n = 0, 0
while True:
    i += 1
    n += i
    divisors = get_number_of_divisors(n)
    if divisors > 500:
        print(n, divisors)
        break
"""