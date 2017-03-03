'''
pay attention to the function s[i].isalpha()
Time: O(n)
space: O(1)
'''
class Solution(object):
	def isPalindrome(self, s):
		i, j = 0, len(s) - 1
		while i < j:
			while i < j and not s[i].isalpha():
				i += 1
			while i < j and not s[j].isalpha():
				j -= 1
			if s[i].lower() != s[j].lower():
				return False
			i, j = i + 1, j - 1
		return True

if __name__ == '__main__':
	print Solution().isPalindrome('A man, a plan, a canal: Panama')
	print Solution().isPalindrome('race a car')
