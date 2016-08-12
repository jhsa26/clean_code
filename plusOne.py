class Solution:
	def plusOne(self, arr):
		for i in range(len(arr) - 1, -1, -1):
			if arr[i] < 9:
				arr[i] += 1
				break
			else:
				arr[i] = 0
		if i == 0:
			arr[0] = 1
			arr.append(0)
			
