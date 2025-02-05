class MinStack:
    # Slightly Cleaner Solution
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]) if self.min_stack else val)
        # val = min(val, self.min_stack[-1]) if self.min_stack else val
        # self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    # Initial Solution
    # def __init__(self):
    #     self.stack = []
    #     self.min = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.min:
    #         self.min.append(val)
    #     elif self.min[-1] > val:
    #         self.min.append(val)
    #     else:
    #         self.min.append(self.min[-1])

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.min.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.min[-1]