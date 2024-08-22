class Solution:
    def majorityElement(self, nums):
        # Voting algo
        a, b, c1, c2 = 0, 0, 0, 0
        for num in nums:
            if c1 == 0 and num != b:
                a = num
                c1 = 1
            elif c2 == 0 and num != a:
                b = num
                c2 = 1
            elif num == a:
                c1 += 1
            elif num == b:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        d1, d2 = 0, 0                            
        n = len(nums)
        for num in nums:
            if a == num:
                d1 += 1
            elif b == num:
                d2 += 1
        res = []
        if d1 > n//3:
            res.append(a)
        if d2 > n//3:
            res.append(b)
        return res