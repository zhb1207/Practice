n = 600851475143
ans = 2

while n > 1:
	if n % ans == 0:
		n /= ans
		print(ans)
	ans += 1
print(ans - 1)
