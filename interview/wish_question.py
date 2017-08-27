'''
We define a subarray of array a to be a contiguous block of a's elements having a length that is less than or equal to the length of array a. For example, the subarrays of array a = [1, 2, 3] are [1], [2], [1, 2], [2, 3], and [1, 2, 3]. Now, let's say we have an integer, k = 3. The subarrays of array a having elements that sum to a number ≤ k are [1], [2], and [1, 2]. The longest of these subarrays is [1, 2], which has a length of 2.
'''

#!/bin/python

import sys
import os

# Complete the function below.


def  maxLength(a, k):
    if len(a) == 1:
        return 1 if a[0] <= k else 0
    maximum = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if sum(a[i:j + 1]) <= k and j - i + 1 > maximum:
                maximum = j - i + 1
    return maximum
f = open(os.environ['OUTPUT_PATH'], 'w')


_a_cnt = 0
_a_cnt = int(raw_input())
_a_i=0
_a = []
while _a_i < _a_cnt:
    _a_item = int(raw_input());
    _a.append(_a_item)
    _a_i+=1



_k = int(raw_input());

res = maxLength(_a, _k);
f.write(str(res) + "\n")

f.close()
