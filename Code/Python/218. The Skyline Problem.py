from heapq import *

class Solution:
    def getSkyline(self, buildings):
        # sweepline 
        events = []
        for L, H, R in buildings:
            events.append((L, -H, R)) # in 
            events.append((R, 0, 0)) # out

        events.sort()

        pq = [(0, float('inf'))] # sentinel  (-H, R)
        res = [(0, 0)] # sentinel
        for L, neg_H, R in events:
            while pq[0][1] <= L: # right < left, kick out
                heappop(pq)
            if neg_H != 0:
                heappush((neg_H, R)) # add
            if res[-1][1] != -pq[0][0]:
                res.append([L, -pq[0][0]])
        
        return res[1:]