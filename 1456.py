def count_vowels(s):
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels_count = count_vowels(s[:k])
        for i in range(len(s)-k+1):
            x = count_vowels(s[i:i+k])
            if max_vowels_count < x:
                max_vowels_count = x
            if max_vowels_count == k:
                return k
        return max_vowels_count

solution = Solution()
print(solution.maxVowels("weallloveyou", 7))   