class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s :
            if char in "(":
                stack.append(char)
            elif char in ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else :
                    stack.append(char)
        return len(stack)