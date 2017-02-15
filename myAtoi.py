def myAtoi(str):
    import string
    isPositive = True
    if '-' in str:
        isPositive = False
    str = string.replace(str, '-', '')
    str = string.replace(str, '+', '')
    #
    dictionary = {
         '0':0
        ,'1':1
        ,'2':2
        ,'3':3
        ,'4':4
        ,'5':5
        ,'6':6
        ,'7':7
        ,'8':8
        ,'9':9
        }
    result = 0
    decimalPlaces = len(str) - 1
    #
    for i in str:
        result += dictionary[i]*(10**decimalPlaces)
        decimalPlaces -= 1
    if isPositive == False:
        result *= -1
    print(result)
    
myAtoi('-1863456')