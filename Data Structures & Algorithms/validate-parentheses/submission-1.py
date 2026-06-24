class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in mapping:
                stack.append(s[i])
            else:
                top = stack.pop() if len(stack) > 0 else '#'
                if top == '#' or mapping[top] != s[i]:
                    return False
        return len(stack) == 0

        