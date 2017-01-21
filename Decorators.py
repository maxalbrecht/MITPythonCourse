#DECORATORS

"""
A DECORATOR does the following:
    * takes a function as a parameter
    * and returns another function
    
Basically, it "takes ina function, adds some functionality and returns it."
    
This can be compared to CLOSURES, which can be described as having the following 
criteria:
        * We must have a nested function (i.e. a function inside a function)
        * The nested function must refer to a value defined in the enclosing function
        * The enclosing function must return the nested function
---
From the internet, it seems that the distinction is that a DECORATOR uses a CLOSURE
---------
*****   NOTE
*****   The @symbol is used for class, function, and method DECORATORS
*****   The most common Python DECORATORS are
        
*****   @Property
*****   @classmethod
*****   @staticmethod

--------

Below is an example fo a DECORATOR:
"""

#EXAMPLE 1:
    
def my_decorator(some_function):
    
    def wrapper():
        print("something is happening before some_function() is called")
        some_function()
        print("Something is happening after somefunction() is called.")
        
    return wrapper

def just_some_function():
    print("Whee!")
    
my_decorator(just_some_function)   #This will return the wrapper() function
my_decorator(just_some_function)() #As we saw in the line above, we have returned
                                   # a function, so by adding () we can execute that function
                                   
#This would normally actually be done by binding the returned function to a variable,
# and only then execute the returned function. For example:

theReturnedFunction = my_decorator(just_some_function)

theReturnedFunction()


#EXAMPLE 2:

def my_decorator(some_function):
    def wrapper():
        num = 10
        if num== 10:
            print("Yes!")
        else:
            print("No!")
        
        some_function()
        
        print("something is happening after some_function() is called.")
    
    return wrapper
    
def just_some_function():
    print("Whee!")
    
myDecoratedFunction = my_decorator(just_some_function)

myDecoratedFunction()
    
#####################################
## HOW TO SYMPLIFY TTHE CALLING OF DECORATORS
## USING THE @ SYMBOL
#####################################

    
    
    
    
    
    
    
    


        