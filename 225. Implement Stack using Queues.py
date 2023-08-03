from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1.append(x)

        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty.")
        return self.q1.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty.")
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
