class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            import pdb; 
            pdb.set_trace()
            if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1 ))
        return area

if __name__ == "__main__":
    print Solution().largestRectangleArea([1,2,3,2,1])
    print Solution().largestRectangleArea([2, 0, 2])
    print Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])