class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        from math import gcd
        
        if target > x + y:
            return False
        if target % gcd(x, y) != 0:
            return False
        return True
