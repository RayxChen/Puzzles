from itertools import accumulate
from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue):
        suffix = list(accumulate(stoneValue[::-1]))[::-1]
        n = len(stoneValue)

        @cache
        def dfs(i):
            if i >= n:
                return 0
            res = -float('inf')
            for x in range(1, 4):
                res = max(res, suffix[i] - dfs(i+x))
            return res
        
        A = dfs(0)
        B = suffix[0] - A

        return 'Alice' if A > B else 'Bob' if B > A else 'Tie'