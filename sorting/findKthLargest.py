def findKthLargest(nums, k):
    return sorted(nums, reverse = True)[k - 1]

## bubble sort idea
def findKthLargest(nums, k):
    for i in range(k):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums[len(nums) - k]

## selection sort idea
def findKthLargest(nums, k):
    for i in xrange(len(nums), len(nums) - k, -1):
        temp = 0
        for j in xrange(i):
            if nums[j] > nums[temp]:
                temp = j
        nums[i - 1] , nums[temp] = nums[temp], nums[i - 1]
    return nums[len(nums) - k]
