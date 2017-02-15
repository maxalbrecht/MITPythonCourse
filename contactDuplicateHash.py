def containsDuplicateHash(nums):
    hashMap = {}
    for i in nums:
        if i in hashMap:
            return True
        hashMap[i] = i
    return False
    
print(containsDuplicateHash([1,2,3,4,5,6,7,8,9]))