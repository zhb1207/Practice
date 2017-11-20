n = range(1,101)
res = sum(n) ** 2 - sum([x**2 for x in n])
print(res)