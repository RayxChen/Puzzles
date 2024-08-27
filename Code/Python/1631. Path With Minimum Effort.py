from math import inf
from heapq import *

class Solution:
    def minimumEffortPath(self, heights):
        pq = [(0, 0, 0)] # (abs, x, y)
        m, n = len(heights), len(heights[0])
        min_effort = [[inf for _ in range(n)] for _ in range(m)]
        min_effort[0][0] = 0

        while pq:
            cur = heappop(pq)
            effort, x, y = cur
            if (x, y) == (m-1, n-1):
                return effort
            for nx, ny in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if new_effort < min_effort[nx][ny]:
                        min_effort[nx][ny] = new_effort
                        heappush(pq, (new_effort, nx, ny))
        
