class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        def power(n):
            if n % 2 == 1:
                return False
            elif n == 2:
                return True
            else:
                return power(n//2)
        return power(n)