from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        # Equivalently find the LIS (non-decreasing) at each pos
        res = []
        cur = []
        for x in obstacles:
            idx = bisect_right(cur, x) # the place it would insert
            if idx == len(cur):
                cur.append(idx)
            else:
                cur[idx] = x
            res.append(idx + 1)
        return res

