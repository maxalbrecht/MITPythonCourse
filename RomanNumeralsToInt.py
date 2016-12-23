def numeralsMapping(string):
    if string == 'I':
        return 1
    if string == 'V':
        return 5
    if string == 'X':
        return 10
    if string == 'L':
        return 50
    if string == 'C':
        return 100
    if string == 'D':
        return 500
    if string == 'M':
        return 1000
    else:
        return 0
        
def romanToInt(string):
    result = 0
    currentNumeralIndex = len(string) - 1
    while currentNumeralIndex >= 0:
        if currentNumeralIndex == len(string) - 1:
            result += numeralsMapping(string[currentNumeralIndex])
        if currentNumeralIndex < len(string) - 1:
            if numeralsMapping(string[currentNumeralIndex]) >= numeralsMapping(string[currentNumeralIndex + 1]):
                result += numeralsMapping(string[currentNumeralIndex])
            if numeralsMapping(string[currentNumeralIndex]) < numeralsMapping(string[currentNumeralIndex + 1]):
                result -= numeralsMapping(string[currentNumeralIndex])
        currentNumeralIndex -= 1
    print(result)
    
#romanToInt('CDXXVII')
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    