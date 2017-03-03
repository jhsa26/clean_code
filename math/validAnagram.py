def isAnagram(s, t):
	s1 = sorted(s)
	t1 = sorted(t)
	return s1 == t1

def isAnagram(s, t):
	dic1, dic2 = {}, {}
	for item1 in s:
		dic1[item1] = dic1.get(item1, 0) + 1
	for item2 in t:
		dic2[item2] = dic2.get(item2, 0) + 1   ## these way we can work around with the 0 problem better
	return dic1 == dic2

## use list as a dic with the index as the key
def isAnagram(s, t):
	dic1, dic2 = [0] * 26, [0] * 26
	for item in s:
		dic1[ord(item) - ord('a')] += 1
	for item in t:
		dic2[ord(item) - ord('a')] += 1
	return dic1 == dic2