"""
The cirteria that must be met to create CLOSURE in Python are the following:
    
        * We must have a nested function (i.e. a function inside a function)
        * The nested function must refer to a value defined in the enclosing function
        * The enclosing function must return the nested function
"""
def make_a_multiplier_of (n):
    def multiplier(x):
         return x*n
    return multiplier
      
times3 = make_a_multiplier_of(3)
times5 = make_a_multiplier_of(5)

print(times3(3))
print(times3(5))

print(times5(4))
print(times5(10))