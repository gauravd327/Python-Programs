from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        self.queue.popleft()
        
    def front(self):
        return (self.queue[len(self.queue) - 1])
        
    def rear(self):
        return (self.queue[0])
        
    def print_queue(self):
        return self.queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.print_queue())
print(queue.front())
print(queue.rear())