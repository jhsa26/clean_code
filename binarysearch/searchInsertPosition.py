'''
Time: O(logn)
Space: O(1)
use the template like:
int L = 0, R = A.length - 1;
while (L < R) {
   int M = (L + R) / 2;
   // TODO: Implement conditional checks.
}
then a good thing to avoid stucking into a infinite loop to verify the code
at last provide proper end up method
'''

class Solution:
	def searchInsert(self, nums, target):
		head = 0
		tail = len(nums) - 1
		while head < tail:
			mid = (head + tail) / 2   ## verify by create a vector with two elements like [1,3] target: 0 and 1
			if nums[mid] < target:
				head = mid + 1
			else:
				tail = mid
		return head + 1 if nums[head] < target else head                    
## stops when head = tail, then divide it into different situations, the plus one case is for case like 
# only one element