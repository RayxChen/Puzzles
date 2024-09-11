from functools import cache

class Solution:

    # 0 <= n <= 10**9 -> digit DP
    def numDupDigitsAtMostN(self, n: int) -> int:
        # n - # of all distinct digits
        s = str(n)
        
        @cache
        def dfs(i, mask, limit_upper, is_num):
            if i == len(s):
                return int(is_num) # whether it's an actual number 00007
            res = 0
            if not is_num:
                res += dfs(i+1, mask, False, False)

            lower = 0 if is_num else 1
            upper = int(s[i]) if limit_upper else 9
            # The limit_upper variable is critical for ensuring that
            # we count valid numbers up to n without exceeding it. 
            # When to Use limit_lower:
            # Counting or Generating Numbers within a Range: [L, R]
            for d in range(lower, upper + 1):
                if mask & (1 << d): # duplicated number
                    continue
                # limit_upper will apply only if cur digit d reaches upper limit
                res += dfs(i+1, mask | (1<<d), limit_upper and d==upper, True) 
            return res
        
        return n - dfs(0, 0, True, False)
            