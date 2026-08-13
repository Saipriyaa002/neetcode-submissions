class Solution:
    def numDecodings(self, s: str) -> int:
        a = 1
        b = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                c = 0
            else:
                c = a

                if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    c += b

            b = a
            a = c

        return a