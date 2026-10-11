class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    num = int(num1) + int(num2)
                    stack.append(num)

                elif token == "-":
                    num = int(num1) - int(num2)
                    stack.append(num)

                elif token == "*":
                    num = int(num1) * int(num2)
                    stack.append(num)

                else:
                    num = int(num1) / int(num2)
                    stack.append(int(num))
            
            else:
                stack.append(token)
        
        return int(stack.pop())

        