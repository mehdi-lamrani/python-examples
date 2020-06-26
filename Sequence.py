from functools import reduce

res = reduce(lambda a, b : a if a>b else b,
	    [3, 4, 6, 9, 34, 12])


print(res)

