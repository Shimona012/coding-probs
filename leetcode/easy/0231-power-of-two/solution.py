class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n <= 0:
            return False
        return math.log2(n).is_integer()
        