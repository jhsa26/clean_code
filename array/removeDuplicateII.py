def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i - 2]:
            nums[i] = n
            i += 1
    return i

print removeDuplicates([1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5])

'''
start from the beginning and compare if it's larger than
the previous two numbers, let i to identify the first few numbers
'''
