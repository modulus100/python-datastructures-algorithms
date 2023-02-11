class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1

        while end > start:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            start += 1
            end -= 1
        return s