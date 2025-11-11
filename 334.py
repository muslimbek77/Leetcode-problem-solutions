class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                # demak, first < second < n
                return True
        return False
# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Medium