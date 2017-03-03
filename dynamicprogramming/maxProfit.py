'''
pay attention to the method itself, keep track of the minimum and maxprofit
along the way
Time: O(n)
Space: O(1)
'''

class Solution(object):
	def maxProfit(self, prices):
	    if not prices:
	        return 0
	    maxprofit, minimum = 0, prices[0]
	    for price in prices:
	    	minimum = min(minimum, price)
	    	maxprofit = max(maxprofit, price - minimum)
	    return maxprofit

if __name__ == '__main__':
	print Solution().maxProfit([7, 1, 5, 3, 6, 4])
