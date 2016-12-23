def letterCombinations(digits):
    return letterCombinationsHelper(digits, [])

def letterCombinationsHelper(digits, resultList):
    if len(digits) == 0:
        return resultList
    else:
        lastDigitIndex = len(digits) - 1
        curDigit = digits[lastDigitIndex]
        remainingDigits = digits[:lastDigitIndex]
        mappingList = mapping(curDigit)
        for n in curDigit:
            letterCombinationsHelper(

def mapping(n):
    if n == 2:
        return ["a", "b", "c"]
    if n == 3:
        return ["d", "e", "f"]
    if n == 4:
        return ["g", "h", "i"]
    if n == 5:
        return ["j", "k", "l"]
    if n == 6:
        return ["m", "n", "o"]
    if n == 7:
        return ["p", "q", "r", "s"]
    if n == 8:
        return ["t", "u", "v"]
    if n == 9:
        return ["w", "x", "y", "z"]
