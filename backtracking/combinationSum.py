'''
backtracking: a general algorithm for finding solutions to a
computational problem by trying partial solutions and then
abandon them if they are not suitable
can be implemented by both brute force way or recursively
pseudo-code:
-- if there are no more choices to make: stop
-- else for each available choice C;
	choose C
	explore the remaining choices
	un-choose C if necessary
also note that it's given a set of candidate numbers which means there is no 
duplicate numbers in the candidate vector
Here although it's a set, we should use index to keep track of the progress
prevent it from generating duplicate cases
Time: O(n ^ k) -- traverse all the nodes
Space: O(k)
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
    	res = []
    	index = 0
    	valueList = []
    	candidates.sort()
    	self.combinationSumHelper(candidates, target, index, valueList, res)
    	return res

    def combinationSumHelper(self, candidates, target, index, valueList, res):
    	length = len(candidates)
    	if target == 0:
    		res.append(valueList)
    	else:
    		for i in range(index, length):
    			if target < candidates[i]:
    				return
    			else:
    				self.combinationSumHelper(candidates, target - candidates[i], i, valueList + [candidates[i]], res)

## notes there like append() and sort() are destructive function which means they modifies objects in place instead of returning
## a new modified object, so here we use valueList + [candidates[i]] not valueList.append(candidates[i])

if __name__ == '__main__':
	print Solution().combinationSum([2, 3], 7)


