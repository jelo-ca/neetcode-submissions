class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['[','(','{']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if stack:
                    if c == ')' and stack.pop() == '(':
                        continue
                    elif c == '}' and stack.pop() == '{':
                        continue
                    elif c == ']' and stack.pop() == '[':
                        continue
                    else:
                        return False
                else:
                    return False
        return (stack == [])