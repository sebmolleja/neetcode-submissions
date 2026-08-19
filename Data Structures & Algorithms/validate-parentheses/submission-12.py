class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        }

        for char in s:
            if char in brackets and stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                stack.append(char)
        
        return False if stack else True