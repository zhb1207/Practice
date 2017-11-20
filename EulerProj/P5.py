# coding:utf-8
# 数学方法：
# 2520 = 2*3*5*7*2*2*3
# print(2*3*5*7*2*2*3*11*13*17*19*2)

# 最小公倍数求法：

from functools import reduce


def lcm(fir, sec):
	s = fir * sec
	while fir % sec != 0:
		fir, sec = sec, fir % sec
	return s // sec


print(reduce(lcm, [x for x in range(1, 21)]))
