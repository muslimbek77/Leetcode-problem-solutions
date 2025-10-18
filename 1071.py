class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        min_len = min(len(str1),len(str2))
        for i in range(min_len,0,-1):
            result = str1[:i]
            if (len(str1) % i  == 0 ) and (len(str2) % i  == 0 ) and (result * (len(str1)//i) == str1) and (result * (len(str2)//i) == str2):
                return result
        return ""