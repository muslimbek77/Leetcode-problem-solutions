class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxAvg = windowSum / k

        for i in range(k, len(nums)):
            windowSum += nums[i]
            windowSum -= nums[i -k]
            maxAvg = max(windowSum / k, maxAvg)
        return maxAvg