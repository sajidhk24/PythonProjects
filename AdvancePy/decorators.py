"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object
without modifying its structure. Decorators are usually called before the definition of a function you want to 
decorate.
"""


# def decorator_fun(original_function):
#     def wrapper_function():
#         print("Wrapper function executed before {} function".format(original_function.__name__))
#         return original_function()
#
#     return wrapper_function


#
# def display():
#     print( "Decorated Display function ran!")
#
#
# my_func = decorator_fun(display)
# my_func()

'''
def decorator_fun(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper function executed before {} function".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_fun  # By using this we reduce all kaam-jhaan of calling and assigning return function
def display():
    print("Decorated Display function ran!")


@decorator_fun
def display_info(name, age):
    print("The display info function ran with arguments {}".format(name, age))


display()
display_info('sajid', 21)
'''

'''
def logger_info(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level= logging.INFO)

    def wrapper_function(*args, **kwargs):
        logging.info("Run With Arguments: {} {}".format(args, kwargs))
        return original_function(args, kwargs)
    return wrapper_function


@logger_info
def display(name, age):
    print("Display Function ran with decorators and arguments {}".format(name, age))


display("sajid", 21)
'''