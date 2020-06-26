def set_x():
    x = 2
    return None

#print(set_x())

#print(list(map(int,"123")))

items = ['Banana', 'Apple', 'Orange' ]
qty = [1, 2, 3]

print(list(zip(items, map(lambda x: x*10, qty))))
