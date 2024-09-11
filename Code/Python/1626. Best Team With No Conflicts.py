class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        # dp[age]:= max scores up to age
        # O(nlogn + n*max_age)
        dp = [0]*(max(ages) + 1)
        for score, age in sorted(zip(scores, ages)):
            dp[age] = max(dp[:age+1]) + score

        return max(dp)


        # pairs = sorted(zip(ages, scores))
        # n = len(scores)
        # dp = [0]*n 
        # for i in range(n):
        #     dp[i] = pairs[i][1]
        #     for j in range(i):
        #         if pairs[j][1] <= pairs[i][1]:
        #             dp[i] = max(dp[i], dp[j] + pairs[i][1])
        # return max(dp)


              
            