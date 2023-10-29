
# decorators : Generally good practice to pass *args and **kwargs to decorators to be universally accessible. 
def mydecorator(function):

    def wrapper(*args, **kwargs):
        print(f"I am decorating function your function! {args[0]} ")
        function(*args, **kwargs)

    return wrapper


# now we want to decorate this hello world function
# means you want additonal functionalities 
# def hello_world():
#     print("hello world!")


# mydecorator(hello_world) --> this returns a wrapper function 
# --> now to call this fuction myfunction(hello_world)()

# mydecorator(hello_world)()

# output: 
# I am decorating function your function!
# hello world!

# ----------------------------------------------------------------

# modern way to use decorators : 

@mydecorator
def HelloWorld(name):
    print(f"Helloooo Modern {name} World!")


HelloWorld("Mike")