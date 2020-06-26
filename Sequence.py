from functools import reduce

#### simple MAP example
my_add = lambda a, b :a + b    
res = list(map(my_add, [1, 2, 3], [4, 5, 6]))
print(res)

#### simple FILTER example
def my_check(a):  
    return a > 10 and a%2
res = list(filter(my_check, [1, 5, 10, 11, 12, 25]))
print(res)

#### simple ZIP example
res = list(zip([1, 2, 3], [4, 5, 6]))
print(res)

#### simple REDUCE example
res = reduce(lambda a, b : a if a>b else b,
	    [3, 4, 6, 9, 34, 12])
print(res)

