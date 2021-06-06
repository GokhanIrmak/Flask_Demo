# def inner():
#     return "Hello World"

# def outer():
#     return inner

def repeat(n):
    def deco(func):
        def inner():
            for i in range(0,n):
                func()
        return inner
    return deco

@repeat(2)
def do_something():
    print("do_something() was called")


do_something()
