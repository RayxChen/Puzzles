from heapq import *

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        start_fuel = startFuel
        pq = []
        res = 0
        idx = 0
        n = len(stations)
        while start_fuel < target:
            while idx < n and stations[idx][0] <= start_fuel:
                heappush(pq, -stations[idx][1])
                idx += 1
            if not pq:
                return -1
            
            start_fuel += -heappush(pq)
            res += 1

        return res
        