class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = candies[0]
        result = []
        for candy in candies:
            if candy > max_candy:
                max_candy = candy
        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
                continue
            result.append(False)
        return result