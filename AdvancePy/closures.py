# A clouser is a nested function that allow us to access variable of outer function even after the outer function
# is closed

"""
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
"""


def say():
    greet = "Hello"

    def display():
        print(greet)

    display()

# say()
# a = say()
# a


def outerfunction(message):
    def innerfunction():
        print(message)

    return innerfunction
# myfunc = outerfunction("Sajid")
# myfunc()


def outerfunc():
    message = "Hello"

    def innerfunc():
        print(message)

    return innerfunc
# myfunc = outerfunc()
# myfunc()
# outerfunc()
# print(outerfunc().__name__)


def outer():
    name = "Python"

    def inner(prefix):
        print(f"{prefix} {name}")

    return inner
# myfunc = outer()
# myfunc('This is')


def counter(start):
    def incr(step=1):
        nonlocal start
        start += step
        print(start)

    return incr

# myfunc = counter(23)
# myfunc()  # 24
# myfunc()  # 25
