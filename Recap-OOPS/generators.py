""""
Genrators in python 
Generators : have lazy propagation property
"""

def mygenerator(n):
    for x in range(n):
        yield x**3

values  = mygenerator(100)  # values will store the generator object 

print(values)

# NOTE : next keyword gives the next yield 
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

