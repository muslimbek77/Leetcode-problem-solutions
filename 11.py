from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxarea = 0
        
        while left < right:
            # Hozirgi maydon
            area = (right - left) * min(height[left], height[right])
            maxarea = max(maxarea, area)
            
            # Past devorni ichkariga siljitamiz
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea
