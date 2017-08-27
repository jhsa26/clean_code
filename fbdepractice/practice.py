'''
def merge(intervals):
    result = []
    intervals.sort(key = lambda x : x[0])
    for interval in intervals:
        if result and interval[0] <= result[-1][1]:
            result[-1][1] = max(interval[1], result[-1][1])
        else:
            result.append(interval)
    return sum([j - i for i, j in result])

print merge([[1, 3], [2, 6], [8, 10], [15, 18]])
def subset(nums):
    result = []
    dfs(result, [], nums)
    return result

def dfs(result, temp, nums):
    result.append(temp[:])
    for i in range(len(nums)):
        dfs(result, temp + [nums[i]], nums[i + 1:])
print subset([1, 2, 3])
def subset2(nums):
    results = []
    nums.sort()
    dfs(results, [], nums, 0)
    return results
def dfs(results, temp, nums, start):
    results.append(temp)
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        else:
            dfs(results, temp + [nums[i]], nums, i + 1)

print subset2([1, 3, 4, 3, 3, 2, 2])
def oneEdit(str1, str2):
    if abs(len(str1) - len(str2)) > 1 or str1 == str2:
        return False
    short = min(len(str1), len(str2))
    for i in range(short):
        if str1[i] != str2[i]:
            if len(str1) > len(str2):
                return str1[i + 1:] == str2[i:]
            elif len(str1) == len(str2):
                return str1[i + 1:] == str2[i + 1:]
            else:
                return str1[i:] == str2[i + 1:]
    return True
print oneEdit('chen', 'chenu')
print oneEdit('chen', 'chenuu')
print oneEdit('chen', 'chrnu')
def twosum(nums, target):
    res = {}
    for i in range(len(nums)):
        if target - nums[i] in res:
            return res[target - nums[i]] + i
        else:
            res[nums[i]] = i
    return None
print twosum([2, 7, 11, 15], 9)

def maxSubArrayLen(nums, k):
    result, acc = 0, 0
    res = {0:-1}
    for i in range(len(nums)):
        acc += nums[i]
        if acc not in res:
            res[acc] = i
        if acc - k in res:
            result = max(result, i - res[acc - k])
    return result
print maxSubArrayLen([1, -1, 5, -2, 3], 3)
print maxSubArrayLen([-2, -1, 2, 1], 1)


def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
def removedup(nums):
    if not nums:
        return 0
    bot = 0
    for i in range(len(nums)):
        if nums[i] != nums[bot]:
            bot += 1
            nums[bot] = nums[i]
    return bot + 1
print removedup([1, 1, 2, 2, 2, 3, 3, 4, 5])
'''
def flatten(container):
    result = []
    for i in container:
        if isinstance(i, list):
            for j in flatten(i):
                result.append(j)
        else:
            result.append(i)
    return result
print flatten([1, 2, 3, [3, 4, [5, 6, [7, 8]], 0]])

