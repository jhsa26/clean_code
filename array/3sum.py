
class Solution:
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length - 2):
			if i and nums[i] == nums[i - 1]:
				continue
			j, k = i + 1, length - 1
			while j < k:
				if nums[i] + nums[j] + nums[k] == 0:
					#import pdb
					#pdb.set_trace()
					res.append([nums[i], nums[j], nums[k]])
					j += 1
					k -= 1
					while j < k and nums[j] == nums[j - 1]:
						j += 1
					while j < k and nums[k] == nums[k + 1]:
						k -= 1
				elif nums[i] + nums[j] + nums[k] > 0:
					k -= 1
				else:
					j += 1
		return res


if __name__ == '__main__':
	nums = [4, -1, -3, 6, -3, -7, 9]
	print Solution().threeSum(nums)

'''
use two pointers way to solve the two sum in O(n) and then go over the list for threeSum
as a result the totol complexity is O(n^2). (Sort is O(nlogn))
be careful of the unique set, move the pointer properly to remove the duplicate cases
the space is O(1)
