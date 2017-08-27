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
        valueList = []
    	#candidates.sort()
    	self.combinationSumHelper(candidates, target, 0, valueList, res)
    	return res

    def combinationSumHelper(self, candidates, target, index, valueList, res):
        if target < 0:
            return
    	elif target == 0:
    		res.append(valueList)
    	else:
    		for i in range(index, len(candidates)):
    			self.combinationSumHelper(candidates, target - candidates[i], i, valueList + [candidates[i]], res) # use i here not i + 1, since we can use the same element multiple times

## notes there like append() and sort() are destructive function which means they modifies objects in place instead of returning
## a new modified object, so here we use valueList + [candidates[i]] not valueList.append(candidates[i])

if __name__ == '__main__':
	print Solution().combinationSum([3, 1, 2], 7)


