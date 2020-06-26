from functools import reduce


my_add = lambda a, b :a + b    
list(map(my_add, [1, 2, 3], [4, 5, 6]))


def my_check(a):  
    return a > 10 and a%2  
list(filter(my_check, [1, 5, 10, 11, 12, 25])) 

 list(zip([1, 2, 3], [4, 5, 6])) 

res = reduce(lambda a, b : a if a>b else b,
	    [3, 4, 6, 9, 34, 12])


print(res)

