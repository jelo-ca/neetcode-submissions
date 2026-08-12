class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "/":
                    stack.append(int(b / a))
        return int(stack.pop())