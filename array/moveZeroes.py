def moveZeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums
print moveZeroes([1, 0, 2, 2, 3, 0, 1, 0, 2])
