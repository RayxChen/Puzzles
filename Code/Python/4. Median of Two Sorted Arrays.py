from math import inf

class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        
        # xxx  xxx   
        # xxx  xxx   
        # A select m1, B select m2
        # m1 + m2 = k = (n1 + n2 + 1) // 2

        # median Ck-1, Ck 
        # {A[m1], A[m1-1], B[m2], B[m2-1]}
        # Ck-1 = max(A[m1-1], B[m2-1])
        # Ck = min(A[m1], B[m2])
        # Binary search m1
        n1, n2 = len(A), len(B)
        if n1 > n2:  # Ensure that A is the smaller array
            A, B, n1, n2 = B, A, n2, n1

        k = (n1 + n2 + 1) // 2 # index-1 based system
        l, r = 0, n1
        while l < r:
            m1 = (l+r)//2
            m2 = k - m1
            if A[m1] < B[m2-1]: # A[m1] > B[m2-1]
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k - l
        c1 = max(A[m1-1] if m1>=1 else -inf, B[m2-1] if m2>=1 else -inf) # boundary condition
        if (n1 + n2) & 1:
            return c1
        c2 = min(A[m1] if m1 < n1 else inf, B[m2] if m2 < n2 else inf) # boundary condition
        return (c1 + c2) / 2