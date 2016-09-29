import time
twoTimesNum = raw_input('Type a number to multiply by 2: ' + '\n' + '   ')
######
print(
    '2 times ' 
    + twoTimesNum + ' equals '
    + str(2*int(twoTimesNum))
)
###
loopOne = True
while loopOne == True:
    print('Give me a word and I will print it two letters at a time')
    origString = raw_input('   ')
    while len(origString) >= 2:
        print(origString[0:2])
        origString = origString[2:]
        time.sleep(.5)
    if len(origString) > 0:
        print(origString)
        time.sleep(.5)
    ##
    response = 'I'
    while response != 'Y' and response != 'N':
        print('Would you like to go through this loop again? (Y for Yes, N for No)')
        response = raw_input('')
        if response == 'Y':
            loopOne = True
        elif response == 'N':
            loopOne = False
        else:
            print('Incorrect input')
            time.sleep(1.0)
        time.sleep(0.5)
##
print('Give me a word and I will print it one word at a time')
oStr = raw_input('   ')
print(oStr)

'''
import re
>>> aString = 'this is a string where the substring "is" is repeated several times'
>>> print [(a.start(), a.end()) for a in list(re.finditer('is', astring))]
[(2, 4), (5, 7), (38, 40), (42, 44)]
'''