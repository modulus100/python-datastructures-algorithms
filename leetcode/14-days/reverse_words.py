class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        str = ""

        for word in words:
            str += word[::-1] + " "
        
        return str[0:len(str) -  1]