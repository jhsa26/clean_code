class Solution(object):
    def partition(self, s):
        res = []
        self.dfs(s, res, [])
        return res
    def dfs(self, s, res, temp):
        if len(s) == 0:
            res.append(temp)
        else:
            for i in range(1, len(s) + 1):
                if self.isPalin(s[:i]):
                    self.dfs(s[i:], res, temp + [s[:i]])
    def isPalin(self, s):
        return s == s[::-1]

print Solution().partition('aab')

'''
summary:
1. in python we do not have to manully backtrack
2. only duplicate questions, we use sort()
3. if not manually backtrack, we do not have to use temp[:] instead of temp
4. we use manully index to pass in cases when we would like to deal with duplicates cases, so for normal cases, we even do not have to care about the extra index parameter, directly pass the a[s:] into the recursive function
