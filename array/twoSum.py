'''
dict.items() vs enumerate(array)
if using two pointers, you have to sort the list
first which will takes O(nlog(n)) bigger than 
the O(n) that it really needs
'''
class Solution:
	def two_sum(self, array, total):
		res = {}
		for i, item in enumerate(array):	## this way only loop one time 
			if total - item in res:			## if we construct the dict first, we will loop twice
				return i, res[total - item]
			res[item] = i
		return None

if __name__ == "__main__":	
	array = [3,6,1,7,8,90]
	total = 93
	print Solution().two_sum(array, total)

'''
use hashtable
Time: O(n)
Space: O(n)
''' 