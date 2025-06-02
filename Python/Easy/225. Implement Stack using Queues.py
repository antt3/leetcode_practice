from collections import deque

class MyStack:
    # Ideal Solution
    def __init__(self):
        self.q = None

    # Time: O(1)
    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    # Time: O(1)
    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft()
        return top

    # Time: O(1)
    def top(self) -> int:
        return self.q[0]

    # Time: O(1)
    def empty(self) -> bool:
        return not self.q
    
    # Initial Solution
    # def __init__(self):
    #     self.q1 = deque()
    #     self.q2 = deque()
    
    # # Time: O(n)
    # def push(self, x: int) -> None:
    #     while self.q1:
    #         self.q2.append(self.q1.popleft())
    #     self.q1.append(x)
    #     # Slightly Optimized Solution
    #     self.q1, self.q2 = self.q2, self.q1

    #     # Initial Soluton
    #     # while self.q2:
    #     #     self.q1.append(self.q2.popleft())

    # # Time: O(1)
    # def pop(self) -> int:
    #     return self.q1.popleft()

    # # Time: 0(1)
    # def top(self) -> int:
    #     return self.q1[0]

    # # Time: 0(1)
    # def empty(self) -> bool:
    #     return not self.q1