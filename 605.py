class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        l = len(flowerbed)
        if n == 0 or (l==1 and  flowerbed[0]==0):
            return True
        for i in range(l-1):
            if flowerbed[i] == 0 and (flowerbed[i+1]==0) and(flowerbed[i-1] == 0 or i==0 or i==l-2):
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        return False
        