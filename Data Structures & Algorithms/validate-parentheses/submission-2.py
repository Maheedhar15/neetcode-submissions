class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '[{(':
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                else:
                    if i == ']':
                        if stack[-1] == '[':
                            _ = stack.pop()
                        else:
                            stack.append(i)
                    elif i == '}':
                        if stack[-1] == '{':
                            _ = stack.pop()
                        else:
                            stack.append(i)
                    else:
                        if stack[-1] == '(':
                            _ = stack.pop()
                        else:
                            stack.append(i)
        return len(stack) == 0
        