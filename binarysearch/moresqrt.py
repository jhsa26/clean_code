'''
binary search basic methods:
we use basic rule:
int L = 0, R = A.length - 1;
while (L < R) {
   int M = (L + R) / 2;
   // TODO: Implement conditional checks.
}
but for a specific problem we have to pay attention to the edge cases, like for sqrt:
we prefer smaller one since sqrt will down to lower integer, so here use left <= right,
no matter right invalid or left invalid, we both prefer the smaller one, so the result value
is "left - 1"
Time: log(n)
Space: O(1)
'''
# This problem is a little tricky since we have to lower down the result, so we use the way "left <= right" and also left = mid + 1 with left - 1: one hand it can avoid the infinite loop, another hand is that it can lower back to the correct result
# refined github version
class Solution:
	def mySqrt(self, x):
		if x < 2:
			return x
		left = 1
		right = x/2
		while left <= right:
			mid = left + (right - left) / 2 # care about overflow here so we use "left + (right - left) / 2" instead of (left + right) / 2
			if mid > x / mid:    # we do not have to worry about float or not here
				right = mid - 1
			else:
				left = mid + 1
		return left - 1

## jiuzhang algorithm way
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start, end = 1, x
        while start + 1 < end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start

if __name__ == "__main__":
	print Solution().mySqrt(10)
	print Solution().mySqrt(44)

'''
if the result may not be integer, then the normal way to
calculate the sqrt is like below
'''

def sqrtBI(x, epsilon):
    assert x>0, 'X must be non-nagtive, not ' + str(x)
    assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon)

    low = 0
    high = max(x, 1.0)
    ## high = x
    guess = (low + high)/2.0
    counter = 1
    while (abs(guess ** 2 - x) > epsilon) and (counter <= 100):
        if guess ** 2 < x:
            low = guess
        else :
            high = guess
        guess = (low + high)/2.0
        counter += 1
    return guess



