def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    currentNumIndex = 0
    currentCompareIndex = 0
    while currentNumIndex < len(nums):
        currentCompare = currentNumIndex + 1
        while currentCompare < len(nums):
           if nums[currentNumIndex] == nums[currentCompareIndex]:
               return True
           currentCompare += 1  
        currentNumIndex += 1
    return False
    
print(containsDuplicate([1,2,3,4,5,6,1,7,8,9]))