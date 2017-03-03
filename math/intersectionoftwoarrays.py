def intersection(list1, list2):
	lis1 = set(list1)
	result = [i for i in lis1 if i in list2]
	return result

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1, dic2 = {}, {}
        result = []
        for i in nums1:
            dic1[i] = dic1.get(i, 0) + 1
        for j in nums2:
            dic2[j] = dic2.get(j, 0) + 1
        for i in dic1.keys():
            if i in dic2.keys():
                result += [i] * min(dic1[i], dic2[i])
        return result

# simple way to use counter for the above:
def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements()


def intersect(self, nums1, nums2):
    C = collections.Counter
    return list((C(nums1) & C(nums2)).elements())
    
def intersect(self, nums1, nums2):
    return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())