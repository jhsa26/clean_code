## if check the palindrome of strings then we can use two pointers or 
## leverage the string symmetric property

## if for integer we can also make it like string and then reverse it
## if the practice of converting integer to string is deemed as bad
## then use it the other way
def isPalindrome(num):
	if num < 0:
		return False
	copy, rev = num, 0
	while True:
		rev *= 10
		low = num % 10
		rev += low
		num = num / 10
		if num == 0:
			break
	return copy == rev

def validPalindrome(string):
	s = filter(lambda x: x.isalnum(), s).lower()
	return s == s[::-1]

def validPalindrome(string):
	start = 0
	end = len(string) - 1
	while start < end:
		while start < end and not string[start].isalnum():
			start += 1
		while start < end and not string[end].isalnum():
			end -= 1
		if start < end and string[start].lower() != string[end].lower():
			return False
		start += 1
		end -= 1
	return True

