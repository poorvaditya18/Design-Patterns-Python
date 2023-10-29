
def mydecorator(function):

    def wrapper():
        print("I am decorating function your function!")
        function()

    return wrapper


# now we want to decorate this hello world function
# means you want additonal functionalities 
def hello_world():
    print("hello world!")


# mydecorator(hello_world) --> this returns a wrapper function 
# --> now to call this fuction myfunction(hello_world)()

mydecorator(hello_world)()

# output: 
# I am decorating function your function!
# hello world!

# ----------------------------------------------------------------

# modern way to use decorators : 

@mydecorator
def HelloWorld():
    print("Helloooo Modern World!")


HelloWorld()