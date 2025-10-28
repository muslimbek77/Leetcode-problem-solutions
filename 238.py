class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        chap = 1
        for i in range(n):
            res[i] = chap
            chap *= nums[i]
        on = 1 
        for i in range(n-1,-1,-1):
            res[i]  *= on
            on *= nums[i]
        return res
    
