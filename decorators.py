# def inner():
#     return "Hello World"

# def outer():
#     return inner

def outer(func):
    counter = 0

    def inner():
        nonlocal counter
        print("was called " + str(counter)+"times")
        counter += 1
        func()  # do_something will be called because it takes it as argument


    return inner


# x = outer()
# print(x)
# print(x())

# Decorator, overriding function and calling outer instead
@outer
def do_something():
    print("do_something() was called")


do_something()
do_something()
do_something()
do_something()
