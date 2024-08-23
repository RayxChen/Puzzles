from itertools import accumulate
from functools import cache

class Solution:
    def stoneGameII(self, piles) -> int:
        # xx | xxxx | xxxx..
        #    i      j            
        n = len(piles)
        suffix = list(accumulate(piles[::-1]))[::-1]
        # dfs calc max stones Alice can get from index i with the constraint M
        @cache
        def dfs(i, M):
            if i >= n:
                return 0
            res = 0 
            for x in range(1, 2*M + 1):
                if i + x <= n:
                    res = max(res, suffix[i] - dfs(i+x, max(x, M)))
            return res
        
        return dfs(0, 1)

