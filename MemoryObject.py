x = 5555
y = x
#y = 7777

a = ['a','b','c']
b = a

print(y is x)

print('\nX ADDRESS : ' + hex(id(x)))
print('X VALUE : ' + str(x))

print('\nY ADDRESS : ' + hex(id(y)))
print('Y VALUE : ' + str(y))
