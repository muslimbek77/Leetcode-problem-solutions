class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt = len(t)
        ls = len(s)
        subsq = 0
        if ls > lt:return False
        if ls == lt: return s == t
        for i in range(lt):
            if subsq <= ls - 1:
                if s[subsq] == t[i]:
                    subsq += 1
        return subsq == len(s)