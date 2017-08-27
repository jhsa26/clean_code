def largestRectangleArea(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        print height[i]
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            print h
            w = i - stack[-1] - 1
            print w
            ans = max(ans, h * w)
            print ans
        print stack
        stack.append(i)
        print stack
    height.pop()
    return ans

#print largestRectangleArea([5, 3, 6, 7, 1, 2, 8])
print largestRectangleArea([1, 2])

