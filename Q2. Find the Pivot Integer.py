import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        x = int(math.isqrt(s))  # butun ildiz
        return x if x * x == s else -1