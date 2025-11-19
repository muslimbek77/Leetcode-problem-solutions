from typing import List


def longestOnes(nums, k):
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        # Agar 0 bo'lsa, oynadagi 0 lar sonini oshiramiz
        if nums[right] == 0:
            zero_count += 1
        
        # Agar 0 lar soni k dan oshsa -> left ni suramiz
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Oynaning maksimal uzunligini yangilaymiz
        max_length = max(max_length, right - left + 1)

    return max_length

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        return longestOnes(nums,k)
        