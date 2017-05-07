class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        temp = []
        i, j = 0, 0
        while True:
            if num1[i] < num2[j]:
                temp.append(num1[i])
                i += 1
            else:
                temp.append(num2[j])
                j += 1
            if i == len(num1):
                temp = temp + num2[j:]
                break
            if j == len(num2):
                temp = temp + num1[i:]
                break
        length = len(temp)
        if len(temp) % 2 == 1:
            return temp[length%2]
        else:
            return (temp[length%2 - 1] + temp[length%2]) / 2.0

print Solution().findMedianSortedArrays([1, 3], [2])
print Solution().findMedianSortedArrays([1, 2], [3, 4])
