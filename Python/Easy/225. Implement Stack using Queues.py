
class MyStack:
    # Initial Solution
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Time: O(n)
    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    # Time: O(1)
    def pop(self) -> int:
        return self.q1.popleft()

    # Time: 0(1)
    def top(self) -> int:
        return self.q1[0]

    # Time: 0(1)
    def empty(self) -> bool:
        return not self.q1