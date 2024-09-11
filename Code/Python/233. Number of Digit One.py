from functools import cache

class Solution:
    def countDigitOne(self, n: int) -> int:

        s = list(map(int, str(n)))
        
        @cache
        def dfs(i, ones, limit_upper):
            if i == len(s):
                return ones
            res = 0
            upper = s[i] if limit_upper else 9  

            for d in range(upper + 1):
                new_ones = ones + (1 if d == 1 else 0)
                res += dfs(i + 1, new_ones, limit_upper and d == upper)
            return res

        return dfs(0, 0, True)