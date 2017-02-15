def containsDuplicateSort(nums):
    nums.sort()
    currentIndex = 0
    while currentIndex < len(nums) - 1:
        if nums[currentIndex] == nums[currentIndex+1]:
            return True
        currentIndex += 1
    return False

print(containsDuplicateSort([1,2,3,4,5,6,7,8,9, 1]))