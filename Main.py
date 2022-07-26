import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        
        if len(self.items) == 0:
            return True

    def is_full(self):
       
        if len(self.items) >= size:
            return True

    def push(self, data):
        if not self.is_full():
            
            self.items.append(data)

    def pop(self):
        if not self.is_empty():
           
            x = self.items.pop()
            return x

    def status(self):
        
        for item in self.items:
            print(item)


size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
