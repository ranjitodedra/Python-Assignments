from collections import deque;
stack = deque;

class Stack:
    def __init__(self) :
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isEmpty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.peek());

