from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()
        
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        self.stack.pop()
        
    def peek(self):
        return (self.stack[len(self.stack)])
        
    def is_empty(self):
        if len(self.stack) == 0:
            return "Empty: " +  str(True)
        else:
            return "Empty: " + str(False)
        
    def print_stack(self):
        return self.stack

stack = Stack()
print(stack.is_empty())
print(stack.print_stack())
stack.push(4)
print(stack.print_stack())
stack.push(1)
print(stack.print_stack())
stack.push(7)
print(stack.print_stack())
stack.pop()
print(stack.is_empty())
print(stack.print_stack())


