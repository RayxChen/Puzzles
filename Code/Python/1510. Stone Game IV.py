from math import isqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        # dp[i]:= whether Alice win at number i
        # dp[i] <- dp[i-k*k]
        dp = [False for _ in range(n+1)]
        dp[1] = True

        for i in range(1, n+1):
            for j in range(1, isqrt(i) + 1):
                if not dp[i-j*j]:
                    dp[i] = True
                    break
        return dp[n]

