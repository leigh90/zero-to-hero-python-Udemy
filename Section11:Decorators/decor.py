# DECORATORS
# Allow you to add extra functionality to your functions in a flexible way that is easily removable
# def func():
#     print('one')
#     return 1
# # you can assign functions to variables since they are objects that can be passed on to other objects
# greet = func

# del func
# greet()
# func()

# def hello(name='Jose'):
#     print("I am going to return a function")

#     def greet():
#         return '\t This is the greet() function inside hello'
#     # print(greet()) # you have to use the print statement to call greet if you dont you wont be able to call it using just plain (greet())
#     # greet() this wont work

#     def welcome():
#         return "\t This is welcome() inside hello()"
#     # print(welcome())

#     # print("This is the end of the hello() function ")
#     # function greet() and welcome() are not available outside of hello they are local to hello

#     if name == 'Jose':
#         return greet()
#         # what this will do is allow you to assign hello to a variable that will now have greet as its return value
#     else:
#         return welcome

# my_new_func = hello
# # my_new_func()
# print(my_new_func())


# def cool():

#     print( 'I am papa cool')
#     def super_cool():
#         return 'I am ice cool'
#     return super_cool()

# cool_func = cool
# print(cool_func())
    
def hiya():
    return 'Hiya JOse'

def other(some_def_func):
    print('Other code runs here')
    print(some_def_func())


other(hiya)

def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before the original function')

        original_func() # this is the function that is passed in and that willbe wrapped it is executed inside its wrapper
        print('Some extra code, after the original function ')
    
    return wrap_func

def to_be_wrapped():
    print("I want to be wrapped")

# new_decorator(to_be_wrapped())

# decorated_func = new_decorator(to_be_wrapped)
# decorated_func()

# the typical notation is actually 
@new_decorator
def to_be_wrapped():
    print("I want to be wrapped")

to_be_wrapped()