class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 0
        res = set()
        while n != 1 and n not in res:
            total = 0
            res.add(n)
            while n != 0:
                r = n % 10
                total += r ** 2
                n = n / 10
            n = total
        return n == 1