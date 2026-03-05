class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_occ = 0
        for char in s :
            if char == "(":
                stack.append(char)
            elif char == ")":
                length = len(stack)
                stack.pop()
                max_occ = max(length,max_occ)
        return max_occ