def my_decorator(func):
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função")
    return wrapper


def uppercase_string(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        split = func.split()
        return split
    return wrapper