class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)

            elif char in ")}]":
                if len(stack) == 0:
                    return False
                    
                char2 = stack.pop()

                if char == ")" and char2 != "(":
                    return False

                elif char == "]" and char2 != "[":
                    return False

                elif char == "}" and char2 != "{":
                    return False
        
        if len(stack) == 0:
            return True

        return False
