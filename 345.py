class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s = list(s)
        n = len(s) - 1
        i = 0
        while i < n:
            if s[i] in vowels and s[n] in vowels:
                s[i],s[n] = s[n],s[i]
                i += 1
                n -= 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[n] not in vowels:
                    n -= 1
        return ''.join(s)