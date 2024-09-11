from itertools import accumulate

class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0]*(n+1)
        for start, end, k in bookings: 
            res[start-1] += k # start from 1
            res[end] += k
        return list(accumulate(res[:-1]))