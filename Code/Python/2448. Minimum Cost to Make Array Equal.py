class Solution:
    def minCost(self, nums, cost):

        # |a - x| * k1 + |b - x| * k2 + ...
        # a, b, ... < x,  k1*(x-a) + k2*(x-b) + ... + ki * (i - x)
                
        # 1. find the first number slope become negative
        # match = list(sorted(zip(nums, cost)))
        # k_sum = sum(cost)
        # s = 0
        # x = 0
        # for num, k in match:
        #     if s >= (k_sum + 1) // 2: # the median may not in the arr
        #         break
        #     s += k
        #     x = num
        # return sum([k*abs(x-num) for num, k in match])

        # 2. binary search (V shape)

        def f(x):
            return sum([k * abs(x - a) for a, k in zip(nums, cost)])
        
        l, r = min(nums), max(nums) # find the x
        while l < r:
            mid = (l+r)//2
            if f(mid) > f(mid + 1):
                l = mid + 1
            else:
                r = mid
        return f(l)
