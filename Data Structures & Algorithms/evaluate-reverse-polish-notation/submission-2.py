class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print(stack)
            if i.lstrip('-').isnumeric():
                stack.append(int(i))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                match(i):
                    case "+":
                        stack.append(num2 + num1)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(float(num2)/num1))
                    case "_":
                        pass
        print(stack)
        return stack[-1]
                    