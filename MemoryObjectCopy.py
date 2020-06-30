import copy

class Arr(object):
    def __init__(self, arr):
        self._arr = arr

    @property
    def arr(self):
        return self._arr

    @arr.setter
    def arr(self, value):
        self._arr = value


x = Arr(['a','b','c'])
y = copy.copy(x)
y.arr = ['e','f','g']

print('\nY IS X ? ' + str(y is x))

print('\nX ADDRESS : ' + hex(id(x)))
print('X VALUE : ' + str(x.arr))

print('\nY ADDRESS : ' + hex(id(y)))
print('Y VALUE : ' + str(y.arr))
