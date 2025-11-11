class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        anchor = 0
        
        for read, c in enumerate(chars):
            # oxirgi element yoki keyingi element boshqa harf bo'lsa
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]  # harfni yozish
                write += 1
                count = read - anchor + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                anchor = read + 1  # keyingi blok boshlanishi
        return write