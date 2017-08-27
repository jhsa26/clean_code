class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        results = [[0 for i in range(len1)] for j in range(len2)]
        for i in range(len1):
            results[0][i] = i
        for j in range(len2):
            results[j][0] = j
        for i in range(1, len2):
            for j in range(1, len1):
                results[i][j] = min(results[i][j - 1] + 1, results[i - 1][j] + 1, results[i - 1][j - 1] + (0 if word1[j - 1] == word2[i - 1] else 1))
        return results[-1][-1]
        
print Solution().minDistance('asdf', 'sdf')