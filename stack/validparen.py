class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s :
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack :
                    return False
                top_element = stack.pop()
                if(top_element == "(" and char != ")") or (top_element == "[" and char != "]" ) or (top_element == "{" and char != "}"):
                    return False
        return len(stack) == 0
