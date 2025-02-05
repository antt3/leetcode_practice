class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

    # Initial Solution Without Comments
        # stack = []
        # for p in range(len(s)):
        #     if s[p] in ('(', '[', '{'):
        #         stack.append(s[p])
        #         continue
        #     if len(stack) == 0:
        #         return False
        #     popped = stack.pop()
        #     if (
        #         (popped == '(' and s[p] == ')') or
        #         (popped == '[' and s[p] == ']') or
        #         (popped == '{' and s[p] == '}')
        #     ):
        #         continue
        #     return False
        # if len(stack) > 0:
        #     return False
        # return True
        
        # Initial Solution With Brainstorm Comments
        # # empty list (stack)
        # stack = []
        # # for loop through s
        # for p in range(len(s)):
        #     # if the symbol is a beg parentheses
        #     if s[p] in ('(', '[', '{'):
        #         # push to stack
        #         stack.append(s[p])
        #         # continue
        #         continue
        #     if len(stack) == 0:
        #         return False
        #     # pop the element from stack
        #     popped = stack.pop()
        #     # 3 if statements for parentheses matching top of stack (peek)
        #     if (
        #         (popped == '(' and s[p] == ')') or
        #         (popped == '[' and s[p] == ']') or
        #         (popped == '{' and s[p] == '}')
        #     ):
        #         continue
        #     # if it doesn't match any if statement return False
        #     return False
        # # if stack is not empty
        # if len(stack) > 0:
        #     # return False
        #     return False
        # # else return True
        # return True