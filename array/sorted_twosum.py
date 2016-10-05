## bineary search
class Solution:
	def sortedTwosum(self, array, total):
		def biSearch(a):
			L = 0
			R = len(array) - 1
			while L < R:
				mid = (L + R) / 2
				if array[mid] < a:
					L = mid + 1
				elif array[mid] > a:
					R = mid
				else:
					return mid
			return -1
		for i in range(len(array)):
			index = biSearch(total - array[i])
			if index != -1:
				return i + 1, index + 1
		return None

## two pointers
class Solution:
	def sortedTwosum(self, array, total):
		i = 0
		j = len(array) - 1
		while True:
			if array[i] + array[j] == total:
				return i + 1, j + 1
			elif array[i] + array[j] < total:
				i += 1
			else:
				j -= 1
		return -1

if __name__ == "__main__":
	array = [3,5,7,8,90]
	total = 12
	print Solution().sortedTwosum(array, total)

