from functools import wraps  
  
def my_decorator(f):  
    @wraps(f)  
    def wrapper(*args, **kwargs):  
        print('Calling decorated functions')  
        return f(*args, **kwargs)  
    return wrapper

def mydecorator_takes_arg(data: str):

    def test_type(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            print
            return data

        return wrapper

    return test_type

@my_decorator  
def example():  
    """Docstring"""  
    #print('Called example function')
    pass

@mydecorator_takes_arg
def example2(func):
    pass


example2('test')


