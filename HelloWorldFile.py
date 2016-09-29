import time
UserInt = int(
    raw_input(
         'Please type an int. We will then tell you if it is an '
        +'even or odd number.'
        +'\n'
    )
)
print('')
time.sleep(1)
##
if UserInt % 2 == 0:
    print('Your number is even')
else:
    print('It is odd!') 
print('') 
time.sleep(1)
##
print('This has been another MA original.')