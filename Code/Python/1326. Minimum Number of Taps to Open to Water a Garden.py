class Solution:
    def minTaps(self, n, ranges):
        intervals = []
        for i in range(n + 1):
            left_span = max(0, i - ranges[i])
            right_span = min(n, i + ranges[i])
            intervals.append((left_span, right_span))
        
        # Sort intervals by their start point
        intervals.sort()
        i = 0
        res, end, farthest = 0, 0, 0

        while end < n:
            while i <= n and intervals[i][0] <= end:
                farthest = max(farthest, intervals[i][1])
                i += 1
            if farthest == end:
                return -1
            res += 1
            end = farthest
        return res

            

