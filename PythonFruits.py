def nfruits(initialFruits, eatenFruits):
    """
    initialFruits is  a dictionary with letters and the quantity of each letter
    eatenFruits is a string of letters.
    
    The goal is to take eatenFruits and turn it into a list. Then we can walk
    down this new list. For each item, increase the quantity of each letter in
    initialFruits except for the current item in the eatenFruitsList
    """
    eatenFruitsList = []
    for i in eatenFruits:
        eatenFruitsList += i
    currentEatenFruitIndex = -1
    
    print initialFruits
    print eatenFruitsList
    print ""
    
    for i in eatenFruitsList:
        currentEatenFruitIndex +=1
        print ('eating a new fruit: ' +i)
        for m in initialFruits:
            print(i,m)
            if i != m and currentEatenFruitIndex != len(eatenFruitsList) -1:
                print 'adding'
                initialFruits[m] += 1
            if i == m and initialFruits[m] > 0:
                initialFruits[m] -= 1
                print 'substracting'
            print initialFruits
            print ''
    
    maxFruitNum = 0
    
    for i in initialFruits:
        if initialFruits[i] > maxFruitNum:
            maxFruitNum = initialFruits[i]

    return maxFruitNum
    
    
    
    
print(nfruits({'d':5,'a':6}, 'dadaa'))