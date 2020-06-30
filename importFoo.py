#import foo
import bar

import importlib

a = 123
b = 456

...

foo = importlib.import_module('foo')

x = foo()
y = foo()