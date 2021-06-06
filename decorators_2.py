# def inner():
#     return "Hello World"

# def outer():
#     return inner

def outer(func):
    cached = {}
    def inner(x):
        if x in cached:
            return cached[x]

        result = func(x)
        cached[x] = result     
        return result

    return inner


# x = outer()
# print(x)
# print(x())

# Decorator, overriding function and calling outer instead
@outer
def calculate_something(x):
    print("calculate_something("+ str(x) +")")
    return x*x

print(calculate_something(5))
print(calculate_something(5))
