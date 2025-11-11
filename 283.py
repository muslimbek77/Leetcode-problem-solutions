
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        zero_nums = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_nums.append(0)
            else:
                result.append(nums[i])
        nums[:] = result + zero_nums
        return nums

# Example usage:
sol = Solution()
arr = [0, 1, 0, 3, 12]    
sol.moveZeroes(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]
