class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "]" : "[",
            "}" : "{",
            ")" : "(",
        }
        stack = []

        for char in s:
            if stack and char in brackets and stack[-1] == brackets[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return False if stack else True
        