from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """O(n) solution using a hash map (counts).

        For each number, check if its complement (k - num) is available
        in the map. If yes, form a pair and decrement the complement count.
        Otherwise, record this number for future pairing.
        """
        counts = {}
        pairs = 0
        for num in nums:
            comp = k - num
            if counts.get(comp, 0) > 0:
                pairs += 1
                counts[comp] -= 1
            else:
                counts[num] = counts.get(num, 0) + 1
        return pairs


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations([1, 2, 3, 4], 5))