from math import sqrt
max_num = 2000000

result = [True] * (max_num + 1)

for i in range(2, int(sqrt(max_num)) + 1):
	k = i
	while(i * k < max_num):
		result[i * k] = False
		k += 1
total = 0
for i in range(2, max_num):
	if result[i] is True:
		total += i
print(total)
