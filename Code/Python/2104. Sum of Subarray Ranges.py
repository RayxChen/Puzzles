from math import inf

class Solution:
    def subArrayRanges(self, nums):
        # find next greater/smaller -> mono stack questions
        # max(x) - min(x)
        # o x x x x o
        # j     k   i

        res = 0
        
        # next greater mono decreasing stack sentinels
        nums.append(inf)
        nums.insert(0, inf)

        stack = [0]
        for i, x in enumerate(nums):
            while nums[stack[-1]] < x:
                k = stack.pop()
                res += (i - k) * (k - stack[-1]) * nums[k]
            stack.append(i)

        # next smaller mono increasing stack sentinels
        nums[0], nums[-1] = -inf, -inf 
        stack = [0]
        for i, x in enumerate(nums):
            while nums[stack[-1]] > x:
                k = stack.pop()
                res -= (i - k) * (k - stack[-1]) * nums[k]
            stack.append(i)

        return res
