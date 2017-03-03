'''
play around the math way and cs way both
'''
def missingNumber(nums):
    result = 0
    for i in range(len(nums)):
        result = result ^ i ^ nums[i]
    return result ^ (i + 1)

def missingNumberI(nums):
    n = len(nums)
    return (1 + n) * n / 2 - sum(nums)

print missingNumber([0, 1, 2, 4, 5])
print missingNumberI([0, 1, 2, 4, 5])
